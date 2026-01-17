const fs = require("fs");
const path = require("path");

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

const sampleRaw = readArg("sample");
const sampleSize = sampleRaw ? Number(sampleRaw) : 60;
const curriculumRaw = readArg("curriculum") || "all";
const curriculum = curriculumRaw.toLowerCase();

const rawBaseUrl = process.env.BASE_URL || "http://127.0.0.1:5173/Python-Game-2/";
const baseUrl = rawBaseUrl.endsWith("/") ? rawBaseUrl : `${rawBaseUrl}/`;
const lessonTimeoutMs = Number(process.env.LESSON_TIMEOUT_MS || 2000);

const lessonsPath = path.resolve(__dirname, "../frontend/public/data/lessons.json");
const coursePaths = {
  python: path.resolve(__dirname, "../frontend/public/data/course-python-basics.json"),
  sql: path.resolve(__dirname, "../frontend/public/data/course-sql-fundamentals.json"),
  r: path.resolve(__dirname, "../frontend/public/data/course-r-fundamentals.json")
};

const outputPath = path.resolve(__dirname, "../interaction_audit_ui_sample.json");
const reportPath = path.resolve(__dirname, "../interaction_audit_ui_sample_report.md");
const screenshotDir = path.resolve(__dirname, "../ui_sample_screenshots");

const ensureDir = (dir) => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
};

const resolvePlaywright = () => {
  try {
    return require("playwright");
  } catch (error) {
    const fallback = path.resolve(__dirname, "../frontend");
    return require(require.resolve("playwright", { paths: [fallback] }));
  }
};

const formatDuration = (ms) => {
  if (!Number.isFinite(ms)) {
    return "0s";
  }
  const totalSeconds = Math.max(0, Math.round(ms / 1000));
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  if (minutes > 0) {
    return `${minutes}m ${seconds}s`;
  }
  return `${seconds}s`;
};

const logProgress = (index, total, startTime) => {
  const elapsed = Date.now() - startTime;
  const avg = elapsed / Math.max(1, index);
  const eta = avg * Math.max(0, total - index);
  const percent = total ? Math.round((index / total) * 100) : 100;
  // eslint-disable-next-line no-console
  console.log(`Sample ${index}/${total} (${percent}%) avg ${formatDuration(avg)} ETA ${formatDuration(eta)}`);
};

const loadCourseOrder = (filePath) => {
  const data = JSON.parse(fs.readFileSync(filePath, "utf-8"));
  const ids = [];
  (data.chapters || []).forEach((chapter) => {
    let lessons = [];
    if (Array.isArray(chapter.concepts)) {
      chapter.concepts.forEach((concept) => {
        if (Array.isArray(concept.lessons)) {
          lessons = lessons.concat(concept.lessons);
        }
      });
    } else if (Array.isArray(chapter.lessons)) {
      lessons = chapter.lessons;
    }
    lessons.forEach((lesson) => {
      if (lesson && lesson.id != null) {
        ids.push(lesson.id);
      }
    });
  });
  return ids;
};

const buildSampleIds = (allIds, count) => {
  if (!count || count >= allIds.length) {
    return allIds.slice();
  }
  const step = allIds.length / count;
  const sample = [];
  for (let i = 0; i < count; i += 1) {
    const index = Math.floor(i * step);
    sample.push(allIds[index]);
  }
  return sample;
};

const hashFingerprint = (payload) => {
  const crypto = require("crypto");
  return crypto.createHash("md5").update(payload).digest("hex").slice(0, 10);
};

const detectPredictionText = (text) => /predict|prediction|guess the output/i.test(text || "");

const getCurriculum = (lessonId) => {
  if (lessonId >= 2000) {
    return "r";
  }
  if (lessonId >= 1001) {
    return "sql";
  }
  return "python";
};

const assertCurriculum = () => {
  const allowed = ["all", "python", "sql", "r"];
  if (!allowed.includes(curriculum)) {
    throw new Error(`Invalid curriculum "${curriculumRaw}". Use one of: ${allowed.join(", ")}`);
  }
};

const run = async () => {
  assertCurriculum();
  const lessons = JSON.parse(fs.readFileSync(lessonsPath, "utf-8"));
  const courseOrder = curriculum === "all"
    ? [
      ...loadCourseOrder(coursePaths.python),
      ...loadCourseOrder(coursePaths.sql),
      ...loadCourseOrder(coursePaths.r)
    ]
    : loadCourseOrder(coursePaths[curriculum]);
  const seen = new Set();
  const orderedIds = courseOrder.filter((id) => {
    if (seen.has(id)) {
      return false;
    }
    if (curriculum !== "all" && getCurriculum(id) !== curriculum) {
      return false;
    }
    seen.add(id);
    return true;
  });
  const remainingIds = Object.keys(lessons)
    .map((id) => Number(id))
    .filter((id) => !seen.has(id))
    .filter((id) => (curriculum === "all" ? true : getCurriculum(id) === curriculum))
    .sort((a, b) => a - b);
  const allIds = orderedIds.concat(remainingIds);
  const sampleIds = buildSampleIds(allIds, sampleSize);

  const { chromium } = resolvePlaywright();
  ensureDir(screenshotDir);
  const browser = await chromium.launch();

  const records = [];
  const startTime = Date.now();

  for (let index = 0; index < sampleIds.length; index += 1) {
    const lessonId = sampleIds[index];
    const lesson = lessons[String(lessonId)];
    const hashRoute = `#/lesson/${lessonId}?ui_audit=1`;
    // eslint-disable-next-line no-console
    console.log(`Auditing lesson ${lessonId}...`);
    const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
    let domInfo = null;
    let predictionText = false;
    let predictionPresent = false;
    let fingerprintPayload = "";
    let fingerprintId = "";
    let screenshotPath = "";
    let errorMessage = "";

    try {
      await page.goto(`${baseUrl}${hashRoute}`, { waitUntil: "domcontentloaded" });
      await page.waitForFunction(
        (targetId) => {
          const node = document.querySelector("[data-lesson-id]");
          return node && node.getAttribute("data-lesson-id") === String(targetId);
        },
        lessonId,
        { timeout: lessonTimeoutMs }
      );
    } catch (error) {
      errorMessage = error && error.message ? error.message : String(error);
    }

    if (!errorMessage) {
      await page.waitForTimeout(75);
      domInfo = await page.evaluate(() => {
        const uniq = (items) => Array.from(new Set(items.filter(Boolean)));
        const components = uniq(Array.from(document.querySelectorAll("[data-component]")).map((node) => node.getAttribute("data-component")));
        const layout = uniq(Array.from(document.querySelectorAll("[data-layout]")).map((node) => node.getAttribute("data-layout")));
        const ctas = uniq(Array.from(document.querySelectorAll("[data-cta]")).map((node) => node.getAttribute("data-cta")));
        const predictionSelector = Boolean(
          document.querySelector('[data-component="PredictionCheck"]') ||
          document.querySelector('[data-interaction-type="prediction"]')
        );
        const componentText = Array.from(document.querySelectorAll("[data-component], [data-interaction-type]"))
          .map((node) => (node.textContent || "").trim())
          .join(" ");
        return { components, layout, ctas, predictionSelector, componentText };
      });

      predictionText = detectPredictionText(domInfo.componentText);
      predictionPresent = domInfo.predictionSelector || predictionText;

      fingerprintPayload = JSON.stringify({
        components: domInfo.components.slice().sort(),
        layout: domInfo.layout.slice().sort(),
        ctas: domInfo.ctas.slice().sort()
      });
      fingerprintId = hashFingerprint(fingerprintPayload);
    }

    screenshotPath = path.join(screenshotDir, `lesson-${lessonId}.png`);
    await page.screenshot({ path: screenshotPath, fullPage: false });
    await page.close();

    records.push({
      lesson_id: lessonId,
      title: lesson ? lesson.title : "",
      route: `#/lesson/${lessonId}`,
      components: domInfo ? domInfo.components : [],
      layout_sections: domInfo ? domInfo.layout : [],
      ctas: domInfo ? domInfo.ctas : [],
      prediction_present: predictionPresent,
      prediction_text_match: predictionText,
      prediction_selector_match: domInfo ? domInfo.predictionSelector : false,
      interaction_fingerprint: fingerprintPayload,
      interaction_fingerprint_id: fingerprintId,
      screenshot: path.relative(path.resolve(__dirname, ".."), screenshotPath),
      issues: errorMessage ? ["load_failed"] : [],
      error: errorMessage || undefined
    });

    logProgress(index + 1, sampleIds.length, startTime);
  }

  await browser.close();

  const fingerprintCounts = {};
  records.forEach((record) => {
    if (!record.interaction_fingerprint_id) {
      return;
    }
    fingerprintCounts[record.interaction_fingerprint_id] = (fingerprintCounts[record.interaction_fingerprint_id] || 0) + 1;
  });
  const threshold = Math.max(1, Math.ceil(records.length * 0.25));
  records.forEach((record, idx) => {
    if (record.prediction_present) {
      record.issues.push("prediction_present");
    }
    const prev1 = records[idx - 1];
    const prev2 = records[idx - 2];
    if (record.interaction_fingerprint_id &&
        prev2 &&
        prev1 &&
        record.interaction_fingerprint_id === prev1.interaction_fingerprint_id &&
        record.interaction_fingerprint_id === prev2.interaction_fingerprint_id) {
      record.issues.push("fingerprint_repeated_3x");
    }
    if (record.interaction_fingerprint_id && fingerprintCounts[record.interaction_fingerprint_id] > threshold) {
      record.issues.push("fingerprint_overused");
    }
  });

  const topFingerprints = Object.entries(fingerprintCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
    .map(([fingerprintId, count]) => {
      const example = records.find((r) => r.interaction_fingerprint_id === fingerprintId);
      const parts = example
        ? `${example.components.join(", ") || "none"} | ${example.layout_sections.join(", ") || "none"} | ${example.ctas.join(", ") || "none"}`
        : "";
      return { fingerprintId, count, example: parts };
    });

  const predictionHits = records.filter((record) => record.prediction_present);
  const repetitionHits = records.filter((record) => record.issues.includes("fingerprint_repeated_3x"));
  const overusedHits = records.filter((record) => record.issues.includes("fingerprint_overused"));
  const loadFailedHits = records.filter((record) => record.issues.includes("load_failed"));

  const longestStreak = (() => {
    let best = { start: 0, end: 0, length: 0, fingerprintId: "" };
    let current = { start: 0, end: 0, length: 0, fingerprintId: "" };
    records.forEach((record, idx) => {
      if (current.fingerprintId !== record.interaction_fingerprint_id) {
        current = { start: idx, end: idx, length: 1, fingerprintId: record.interaction_fingerprint_id };
      } else {
        current.end = idx;
        current.length += 1;
      }
      if (current.length > best.length) {
        best = { ...current };
      }
    });
    return best;
  })();

  const representative = new Set();
  if (longestStreak.length > 0) {
    for (let i = longestStreak.start; i <= longestStreak.end && representative.size < 12; i += 1) {
      representative.add(records[i].lesson_id);
    }
  }
  const step = Math.max(1, Math.floor(records.length / 12));
  for (let i = 0; i < records.length && representative.size < 12; i += step) {
    representative.add(records[i].lesson_id);
  }
  const representativeList = Array.from(representative)
    .slice(0, 12)
    .map((lessonId) => {
      const record = records.find((r) => r.lesson_id === lessonId);
      return record ? record.screenshot : `ui_sample_screenshots/lesson-${lessonId}.png`;
    });

  fs.writeFileSync(outputPath, JSON.stringify(records, null, 2));

  const report = [
    "# UI Sample Audit Summary",
    `Curriculum: ${curriculum}`,
    `Sample size: ${records.length}`,
    `Prediction UI present: ${predictionHits.length}`,
    `Repeated fingerprint streaks (3+): ${repetitionHits.length}`,
    `Overused fingerprints (>25%): ${overusedHits.length}`,
    `Load failures: ${loadFailedHits.length}`,
    "",
    "## Top repeated fingerprints",
    ...topFingerprints.map((entry) => `- ${entry.fingerprintId}: ${entry.count} (${entry.example})`),
    "",
    "## Prediction occurrences",
    ...(predictionHits.length
      ? predictionHits.map((record) => `- ${record.lesson_id}: ${record.title}`)
      : ["- none"]),
    "",
    "## Repetition > 2 in a row",
    ...(repetitionHits.length
      ? repetitionHits.map((record) => `- ${record.lesson_id}: ${record.interaction_fingerprint_id}`)
      : ["- none"]),
    "",
    "## Representative screenshots (12)",
    ...representativeList.map((shot) => `- ${shot}`)
  ].join("\n");

  fs.writeFileSync(reportPath, report);
  // eslint-disable-next-line no-console
  console.log(`UI sample audit complete. Records: ${records.length}`);
};

run().catch((error) => {
  // eslint-disable-next-line no-console
  console.error(error);
  process.exit(1);
});
