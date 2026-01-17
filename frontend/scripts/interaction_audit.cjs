const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const lessonsPath = path.resolve(__dirname, "../public/data/lessons.json");
const outputPath = path.resolve(__dirname, "../../interaction_audit.json");
const reportPath = path.resolve(__dirname, "../../interaction_audit_report.md");
const screenshotDir = path.resolve(__dirname, "../../screenshots");
const rawBaseUrl = process.env.BASE_URL || "http://127.0.0.1:5173/Python-Game-2/";
const baseUrl = rawBaseUrl.endsWith("/") ? rawBaseUrl : `${rawBaseUrl}/`;
const lessonTimeoutMs = Number(process.env.LESSON_TIMEOUT_MS || 10000);

const args = process.argv.slice(2);

const readArg = (name) => {
  const prefix = `--${name}=`;
  const direct = args.find((arg) => arg.startsWith(prefix));
  if (direct) {
    return direct.slice(prefix.length);
  }
  const index = args.indexOf(`--${name}`);
  if (index !== -1 && args[index + 1]) {
    return args[index + 1];
  }
  return null;
};

const mode = (readArg("mode") || "meta").toLowerCase();
const sampleRaw = readArg("sample");
const sampleSize = sampleRaw ? Number(sampleRaw) : null;
const inputPath = readArg("input") || outputPath;

if (!["meta", "shots"].includes(mode)) {
  throw new Error(`Unknown mode "${mode}". Use --mode=meta or --mode=shots.`);
}

const ensureDir = (dir) => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
};

const formatDuration = (ms) => {
  if (!Number.isFinite(ms)) {
    return "0s";
  }
  const totalSeconds = Math.max(0, Math.round(ms / 1000));
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  if (hours > 0) {
    return `${hours}h ${minutes}m`;
  }
  if (minutes > 0) {
    return `${minutes}m ${seconds}s`;
  }
  return `${seconds}s`;
};

const getCurriculum = (lessonId) => {
  if (lessonId >= 2000) {
    return "r";
  }
  if (lessonId >= 1001) {
    return "sql";
  }
  return "python";
};

const extractVariables = (starterCode) => {
  const matches = [];
  (starterCode || "").split("\n").forEach((line) => {
    const match = line.match(/^\s*([a-zA-Z_]\w*)\s*=/);
    if (match) {
      matches.push(match[1]);
    }
  });
  return matches.length ? matches : ["value"];
};

const proposeIdea = (lesson) => {
  const tag = (lesson.concept_tags || [])[0] || "general";
  const vars = extractVariables(lesson.starter_code);
  const title = lesson.title || "this lesson";
  switch (tag) {
    case "variables":
      return `Memory machine: assign ${vars[0]} and watch state update for "${title}".`;
    case "strings":
      return `Token slots: build a message with ${vars[0]} and preview the output.`;
    case "numbers":
      return `Graph manipulator: drag x and see numeric output change for "${title}".`;
    case "loops":
      return `Loop simulator: animate iterations and show running total for "${title}".`;
    case "conditionals":
      return `Conditional path visualizer: pick a branch and see the output.`;
    case "join":
      return `Join visualizer: animate matching keys and show the joined rows.`;
    case "group_by":
      return `Aggregate playground: pick an agg and see grouped output.`;
    case "visualization":
      return `Plot toggle: swap geoms and watch the visualization respond.`;
    default:
      return `Debug quest: fix a single-line bug tied to "${title}".`;
  }
};

const summarizeRecipes = (records) => {
  const counts = {};
  records.forEach((record) => {
    counts[record.interaction_recipe_id] = (counts[record.interaction_recipe_id] || 0) + 1;
  });
  return Object.entries(counts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
    .map(([id, count]) => `- ${id}: ${count}`)
    .join("\n");
};

const computeEntropy = (counts, total) => {
  if (!total) {
    return 0;
  }
  let entropy = 0;
  Object.values(counts).forEach((count) => {
    const p = count / total;
    if (p > 0) {
      entropy -= p * Math.log2(p);
    }
  });
  return entropy;
};

const computeStreaks = (records) => {
  const streaks = [];
  let current = null;
  records.forEach((record) => {
    if (!current || record.interaction_recipe_id !== current.recipeId) {
      if (current) {
        streaks.push(current);
      }
      current = {
        recipeId: record.interaction_recipe_id,
        startLesson: record.lesson_id,
        endLesson: record.lesson_id,
        length: 1
      };
      return;
    }
    current.endLesson = record.lesson_id;
    current.length += 1;
  });
  if (current) {
    streaks.push(current);
  }
  return streaks;
};

const summarizePredictionRates = (records) => {
  const byCurriculum = {};
  const byChapter = {};
  records.forEach((record) => {
    const curriculum = record.curriculum || "unknown";
    byCurriculum[curriculum] = byCurriculum[curriculum] || { total: 0, prediction: 0 };
    byCurriculum[curriculum].total += 1;
    if (record.prediction_present) {
      byCurriculum[curriculum].prediction += 1;
    }

    const chapterKey = `${curriculum}:${record.chapter_id || "unknown"}`;
    byChapter[chapterKey] = byChapter[chapterKey] || { total: 0, prediction: 0 };
    byChapter[chapterKey].total += 1;
    if (record.prediction_present) {
      byChapter[chapterKey].prediction += 1;
    }
  });
  return { byCurriculum, byChapter };
};

const formatRate = (count, total) => {
  if (!total) {
    return "0/0 (0%)";
  }
  const pct = Math.round((count / total) * 100);
  return `${count}/${total} (${pct}%)`;
};

const applySample = (targets) => {
  if (!sampleSize || !Number.isFinite(sampleSize) || sampleSize <= 0) {
    return targets;
  }
  return targets.slice(0, sampleSize);
};

const waitForAuditReady = async (page, lessonId) => {
  await page.waitForFunction(
    (targetId) => {
      const ready = window.__AUDIT_READY__;
      return ready && ready.lessonId === targetId;
    },
    lessonId,
    { timeout: lessonTimeoutMs }
  );
  return page.evaluate(() => window.__AUDIT_READY__);
};

const captureLessonShot = async (page, lessonId) => {
  const root = await page.$("[data-lesson-id]");
  if (!root) {
    return { ok: false, error: "lesson_root_missing" };
  }
  const box = await root.boundingBox();
  if (!box) {
    return { ok: false, error: "lesson_root_not_visible" };
  }
  const clip = {
    x: Math.max(0, box.x),
    y: Math.max(0, box.y),
    width: Math.max(1, box.width),
    height: Math.max(1, box.height)
  };
  const screenshotPath = path.join(screenshotDir, `lesson-${lessonId}.png`);
  await page.screenshot({ path: screenshotPath, clip });
  return { ok: true, path: screenshotPath };
};

const logProgress = (label, index, total, startTime) => {
  const elapsed = Date.now() - startTime;
  const avg = elapsed / Math.max(1, index);
  const eta = avg * Math.max(0, total - index);
  const percent = total ? Math.round((index / total) * 100) : 100;
  // eslint-disable-next-line no-console
  console.log(`${label} ${index}/${total} (${percent}%) avg ${formatDuration(avg)} ETA ${formatDuration(eta)}`);
};

const runMetaAudit = async () => {
  const lessons = JSON.parse(fs.readFileSync(lessonsPath, "utf-8"));
  const lessonIds = Object.keys(lessons).map((id) => Number(id)).sort((a, b) => a - b);
  const targets = applySample(lessonIds);

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  const records = [];

  await page.goto(baseUrl, { waitUntil: "domcontentloaded" });

  let lastRecipe = null;
  let consecutiveCount = 0;
  let predictionCount = 0;
  const startTime = Date.now();

  for (let index = 0; index < targets.length; index += 1) {
    const lessonId = targets[index];
    const lesson = lessons[String(lessonId)];
    const hashRoute = `#/lesson/${lessonId}?audit=1`;
    // eslint-disable-next-line no-console
    console.log(`Auditing lesson ${lessonId}...`);
    try {
      await page.evaluate((nextHash) => {
        window.location.hash = nextHash;
      }, hashRoute);

      const auditData = await waitForAuditReady(page, lessonId);
      const recipeId = auditData && auditData.recipeId ? auditData.recipeId : lesson.interaction_recipe_id || "";
      const componentTypes = (auditData && Array.isArray(auditData.components)) ? auditData.components : [];
      const hasPrediction = Boolean(auditData && auditData.hasPrediction);
      const predictionJustified = Boolean(lesson.prediction_justification);
      if (hasPrediction) {
        predictionCount += 1;
      }

      if (recipeId === lastRecipe) {
        consecutiveCount += 1;
      } else {
        consecutiveCount = 1;
        lastRecipe = recipeId;
      }
      const repeatFlag = consecutiveCount > 2;

      const issues = [];
      if (hasPrediction && !predictionJustified) {
        issues.push("prediction_unjustified");
      }
      if (repeatFlag) {
        issues.push("recipe_repeated_3x");
      }
      if (!componentTypes.length) {
        issues.push("no_interactive_components");
      }

      const qualityScore = Math.min(5, componentTypes.length + (repeatFlag ? -1 : 0));

      records.push({
        lesson_id: lessonId,
        title: lesson.title,
        route: `#/lesson/${lessonId}`,
        interaction_recipe_id: recipeId,
        components_used: componentTypes,
        consecutive_recipe_count: consecutiveCount,
        prediction_present: hasPrediction,
        prediction_justified: predictionJustified,
        issues,
        quality_score: qualityScore,
        proposed_interaction: proposeIdea(lesson),
        curriculum: getCurriculum(lessonId),
        chapter_id: lesson.chapter_id || null
      });
    } catch (error) {
      const errorMessage = error && error.message ? error.message : String(error);
      let bodyText = "";
      try {
        bodyText = await page.evaluate(() => document.body.innerText.slice(0, 2000));
      } catch (readError) {
        bodyText = "";
      }

      records.push({
        lesson_id: lessonId,
        title: lesson ? lesson.title : "",
        route: `#/lesson/${lessonId}`,
        interaction_recipe_id: lesson ? lesson.interaction_recipe_id || "" : "",
        components_used: [],
        consecutive_recipe_count: 0,
        prediction_present: false,
        prediction_justified: false,
        issues: ["load_failed"],
        quality_score: 0,
        proposed_interaction: lesson ? proposeIdea(lesson) : "",
        error: errorMessage,
        body_text: bodyText,
        curriculum: getCurriculum(lessonId),
        chapter_id: lesson ? lesson.chapter_id || null : null
      });
      lastRecipe = null;
      consecutiveCount = 0;
    }

    logProgress("Progress", index + 1, targets.length, startTime);
  }

  await browser.close();

  fs.writeFileSync(outputPath, JSON.stringify(records, null, 2));

  const recipeCounts = {};
  records.forEach((record) => {
    recipeCounts[record.interaction_recipe_id] = (recipeCounts[record.interaction_recipe_id] || 0) + 1;
  });
  const uniqueRecipes = Object.keys(recipeCounts).filter((id) => id).length;
  const entropy = computeEntropy(recipeCounts, records.length).toFixed(2);
  const streaks = computeStreaks(records).sort((a, b) => b.length - a.length).slice(0, 20);
  const repetitionFlagged = records.filter((record) => record.issues.includes("recipe_repeated_3x"));
  const { byCurriculum, byChapter } = summarizePredictionRates(records);

  const report = [
    "# Interaction Audit Summary",
    `Mode: meta`,
    `Total lessons: ${records.length}`,
    `Flagged lessons: ${records.filter((r) => r.issues.length > 0).length}`,
    `Prediction present: ${predictionCount}`,
    `Recipes repeating 3+ times: ${records.filter((r) => r.issues.includes("recipe_repeated_3x")).length}`,
    "",
    "## Longest recipe streaks",
    ...streaks.map((streak) => `- ${streak.recipeId || "none"} x${streak.length} (lessons ${streak.startLesson}-${streak.endLesson})`),
    "",
    "## Recipe distribution",
    `Unique recipes: ${uniqueRecipes}`,
    `Entropy: ${entropy}`,
    "",
    "## Top recipes",
    summarizeRecipes(records),
    "",
    "## Prediction usage rate",
    `Overall: ${formatRate(predictionCount, records.length)}`,
    "",
    "By curriculum:",
    ...Object.entries(byCurriculum)
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([curriculum, counts]) => `- ${curriculum}: ${formatRate(counts.prediction, counts.total)}`),
    "",
    "By chapter:",
    ...Object.entries(byChapter)
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([chapterKey, counts]) => `- ${chapterKey}: ${formatRate(counts.prediction, counts.total)}`),
    "",
    "## Lessons flagged for repetition > 2 in a row",
    ...repetitionFlagged.map((record) => `- ${record.lesson_id} (${record.interaction_recipe_id || "none"})`),
    "",
    "## Notes",
    "Each lesson entry includes components used, repetition flags, and a proposed replacement idea."
  ].join("\n");
  fs.writeFileSync(reportPath, report);

  // eslint-disable-next-line no-console
  console.log(`Audit complete. Records: ${records.length}`);
};

const runShots = async () => {
  if (!fs.existsSync(inputPath)) {
    throw new Error(`Missing audit metadata at ${inputPath}. Run --mode=meta first.`);
  }
  const records = JSON.parse(fs.readFileSync(inputPath, "utf-8"));
  const flagged = records.filter((record) => Array.isArray(record.issues) && record.issues.length > 0);
  const targets = applySample(flagged);

  if (!targets.length) {
    // eslint-disable-next-line no-console
    console.log("No flagged lessons to capture.");
    return;
  }

  ensureDir(screenshotDir);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto(baseUrl, { waitUntil: "domcontentloaded" });

  const startTime = Date.now();
  let captured = 0;

  for (let index = 0; index < targets.length; index += 1) {
    const record = targets[index];
    const lessonId = record.lesson_id;
    const hashRoute = `#/lesson/${lessonId}?audit=1`;
    // eslint-disable-next-line no-console
    console.log(`Capturing lesson ${lessonId}...`);
    try {
      await page.evaluate((nextHash) => {
        window.location.hash = nextHash;
      }, hashRoute);
      await waitForAuditReady(page, lessonId);
      const shot = await captureLessonShot(page, lessonId);
      if (shot.ok) {
        captured += 1;
      } else {
        // eslint-disable-next-line no-console
        console.warn(`Screenshot skipped for ${lessonId}: ${shot.error}`);
      }
    } catch (error) {
      // eslint-disable-next-line no-console
      console.warn(`Screenshot failed for ${lessonId}:`, error && error.message ? error.message : String(error));
    }
    logProgress("Shots", index + 1, targets.length, startTime);
  }

  await browser.close();

  // eslint-disable-next-line no-console
  console.log(`Screenshots captured: ${captured}/${targets.length}`);
};

const runAudit = async () => {
  if (mode === "shots") {
    await runShots();
    return;
  }
  await runMetaAudit();
};

runAudit().catch((error) => {
  // eslint-disable-next-line no-console
  console.error(error);
  process.exit(1);
});
