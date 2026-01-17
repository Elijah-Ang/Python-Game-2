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

const curriculumRaw = readArg("curriculum") || "all";
const curriculum = curriculumRaw.toLowerCase();
const allowedCurricula = ["all", "python", "sql", "r"];
if (!allowedCurricula.includes(curriculum)) {
  throw new Error(`Invalid curriculum "${curriculumRaw}". Use one of: ${allowedCurricula.join(", ")}`);
}

const lessonsPath = path.resolve(__dirname, "../frontend/public/data/lessons.json");
const coursePaths = {
  python: path.resolve(__dirname, "../frontend/public/data/course-python-basics.json"),
  sql: path.resolve(__dirname, "../frontend/public/data/course-sql-fundamentals.json"),
  r: path.resolve(__dirname, "../frontend/public/data/course-r-fundamentals.json")
};

const outputPath = path.resolve(__dirname, "../interaction_audit.json");
const reportPath = path.resolve(__dirname, "../interaction_audit_report.md");

const CONTENT_COMPONENT_MAP = {
  VariableSlider: "variable_slider",
  VisualMemoryBox: "memory_box",
  DraggableValueBox: "draggable_value",
  ValueChip: "value_chip",
  LiveCodeBlock: "live_code_block",
  VisualTable: "visual_table",
  ParsonsPuzzle: "parsons_puzzle",
  PredictionCheck: "prediction",
  HintLadder: "hint_ladder",
  StateInspector: "state_inspector",
  ResetStateButton: "reset_state",
  OutputDiff: "output_diff",
  StepExecutor: "step_executor",
  FillBlanks: "fill_blanks",
  TokenSlotPuzzle: "token_slot",
  LoopSimulator: "loop_simulator",
  ConditionalPath: "conditional_path",
  DataTransformAnimator: "data_transform",
  JoinVisualizer: "join_visualizer",
  DebugQuest: "debug_quest",
  GraphManipulator: "graph_manipulator",
  MemoryMachine: "memory_machine"
};

const extractContentComponents = (content) => {
  if (!content) {
    return [];
  }
  const found = new Set();
  Object.entries(CONTENT_COMPONENT_MAP).forEach(([tag, type]) => {
    const regex = new RegExp(`<${tag}\\b`, "i");
    if (regex.test(content)) {
      found.add(type);
    }
  });
  return Array.from(found);
};

const extractPlanComponents = (lesson) => {
  if (!lesson) {
    return [];
  }
  const found = new Set();
  (lesson.interaction_plan || []).forEach((item) => {
    if (item && item.type) {
      found.add(item.type);
    }
  });
  if (lesson.send_to_editor_template) {
    found.add("send_to_editor");
  }
  return Array.from(found);
};

const buildComponents = (lesson) => {
  const plan = extractPlanComponents(lesson);
  const content = extractContentComponents(lesson.content);
  return Array.from(new Set([...plan, ...content]));
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

const getCurriculum = (lessonId) => {
  if (lessonId >= 2000) {
    return "r";
  }
  if (lessonId >= 1001) {
    return "sql";
  }
  return "python";
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

const formatRate = (count, total) => {
  if (!total) {
    return "0/0 (0%)";
  }
  const pct = Math.round((count / total) * 100);
  return `${count}/${total} (${pct}%)`;
};

const computeStreaks = (orderIds, lessons, curriculum) => {
  const streaks = [];
  let current = null;
  orderIds.forEach((lessonId, index) => {
    const lesson = lessons[String(lessonId)];
    if (!lesson) {
      return;
    }
    const recipeId = lesson.interaction_recipe_id || "";
    if (!current || current.recipeId !== recipeId) {
      if (current) {
        streaks.push(current);
      }
      current = {
        curriculum,
        recipeId,
        startLesson: lessonId,
        endLesson: lessonId,
        startIndex: index + 1,
        endIndex: index + 1,
        length: 1
      };
      return;
    }
    current.endLesson = lessonId;
    current.endIndex = index + 1;
    current.length += 1;
  });
  if (current) {
    streaks.push(current);
  }
  return streaks;
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

const buildRecord = (lessonId, lesson, consecutiveCount) => {
  const components = buildComponents(lesson);
  const hasPrediction = components.includes("prediction");
  const predictionJustified = Boolean(lesson.prediction_justification);
  const repeatFlag = consecutiveCount > 2;
  const issues = [];
  if (hasPrediction && !predictionJustified) {
    issues.push("prediction_unjustified");
  }
  if (repeatFlag) {
    issues.push("recipe_repeated_3x");
  }
  if (!components.length) {
    issues.push("no_interactive_components");
  }
  const qualityScore = Math.min(5, components.length + (repeatFlag ? -1 : 0));
  return {
    lesson_id: lessonId,
    title: lesson.title,
    route: `#/lesson/${lessonId}`,
    interaction_recipe_id: lesson.interaction_recipe_id || "",
    components_used: components,
    consecutive_recipe_count: consecutiveCount,
    prediction_present: hasPrediction,
    prediction_justified: predictionJustified,
    issues,
    quality_score: qualityScore,
    proposed_interaction: proposeIdea(lesson),
    curriculum: getCurriculum(lessonId),
    chapter_id: lesson.chapter_id || null
  };
};

const main = () => {
  const lessons = JSON.parse(fs.readFileSync(lessonsPath, "utf-8"));
  const courseOrder = {
    python: loadCourseOrder(coursePaths.python),
    sql: loadCourseOrder(coursePaths.sql),
    r: loadCourseOrder(coursePaths.r)
  };
  const selectedOrder = curriculum === "all"
    ? courseOrder
    : { [curriculum]: courseOrder[curriculum] };

  const records = [];
  const seen = new Set();
  const streaks = [];

  Object.entries(selectedOrder).forEach(([curriculumKey, orderIds]) => {
    let lastRecipe = null;
    let consecutiveCount = 0;
    orderIds.forEach((lessonId) => {
      const lesson = lessons[String(lessonId)];
      if (!lesson) {
        return;
      }
      const recipeId = lesson.interaction_recipe_id || "";
      if (recipeId === lastRecipe) {
        consecutiveCount += 1;
      } else {
        consecutiveCount = 1;
        lastRecipe = recipeId;
      }
      records.push(buildRecord(lessonId, lesson, consecutiveCount));
      seen.add(lessonId);
    });
    streaks.push(...computeStreaks(orderIds, lessons, curriculumKey));
  });

  const remainingIds = Object.keys(lessons)
    .map((id) => Number(id))
    .filter((id) => !seen.has(id))
    .filter((id) => (curriculum === "all" ? true : getCurriculum(id) === curriculum))
    .sort((a, b) => a - b);
  remainingIds.forEach((lessonId) => {
    const lesson = lessons[String(lessonId)];
    if (!lesson) {
      return;
    }
    records.push(buildRecord(lessonId, lesson, 1));
  });

  fs.writeFileSync(outputPath, JSON.stringify(records, null, 2));

  const recipeCounts = {};
  records.forEach((record) => {
    recipeCounts[record.interaction_recipe_id] = (recipeCounts[record.interaction_recipe_id] || 0) + 1;
  });
  const uniqueRecipes = Object.keys(recipeCounts).filter((id) => id).length;
  const entropy = computeEntropy(recipeCounts, records.length).toFixed(2);

  const predictionTotals = { overall: { total: 0, prediction: 0 } };
  const predictionByCurriculum = {};
  const predictionByChapter = {};
  records.forEach((record) => {
    const curriculum = record.curriculum || "unknown";
    const chapterKey = `${curriculum}:${record.chapter_id || "unknown"}`;
    predictionTotals.overall.total += 1;
    if (record.prediction_present) {
      predictionTotals.overall.prediction += 1;
    }
    predictionByCurriculum[curriculum] = predictionByCurriculum[curriculum] || { total: 0, prediction: 0 };
    predictionByCurriculum[curriculum].total += 1;
    if (record.prediction_present) {
      predictionByCurriculum[curriculum].prediction += 1;
    }
    predictionByChapter[chapterKey] = predictionByChapter[chapterKey] || { total: 0, prediction: 0 };
    predictionByChapter[chapterKey].total += 1;
    if (record.prediction_present) {
      predictionByChapter[chapterKey].prediction += 1;
    }
  });

  const longestStreaks = streaks
    .sort((a, b) => b.length - a.length)
    .slice(0, 20)
    .map((streak) =>
      `- ${streak.curriculum}: ${streak.recipeId || "none"} x${streak.length} (pos ${streak.startIndex}-${streak.endIndex}, lessons ${streak.startLesson}→${streak.endLesson})`
    );

  const repetitionFlagged = records.filter((record) => record.issues.includes("recipe_repeated_3x"));

  const report = [
    "# Interaction Audit Summary",
    `Curriculum: ${curriculum}`,
    `Total lessons: ${records.length}`,
    `Flagged lessons: ${records.filter((r) => r.issues.length > 0).length}`,
    `Prediction present: ${predictionTotals.overall.prediction}`,
    `Recipes repeating 3+ times: ${records.filter((r) => r.issues.includes("recipe_repeated_3x")).length}`,
    "",
    "## Longest recipe streaks",
    ...longestStreaks,
    "",
    "## Recipe distribution",
    `Unique recipes: ${uniqueRecipes}`,
    `Entropy: ${entropy}`,
    "",
    "## Top recipes",
    summarizeRecipes(records),
    "",
    "## Prediction usage rate",
    `Overall: ${formatRate(predictionTotals.overall.prediction, predictionTotals.overall.total)}`,
    "",
    "By curriculum:",
    ...Object.entries(predictionByCurriculum)
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([curriculum, counts]) => `- ${curriculum}: ${formatRate(counts.prediction, counts.total)}`),
    "",
    "By chapter:",
    ...Object.entries(predictionByChapter)
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([chapterKey, counts]) => `- ${chapterKey}: ${formatRate(counts.prediction, counts.total)}`),
    "",
    "## Lessons flagged for repetition > 2 in a row",
    ...(repetitionFlagged.length
      ? repetitionFlagged.map((record) => `- ${record.lesson_id} (${record.interaction_recipe_id || "none"})`)
      : ["- none"]),
    "",
    "## Notes",
    "Each lesson entry includes components used, repetition flags, and a proposed replacement idea."
  ].join("\n");

  fs.writeFileSync(reportPath, report);
  // eslint-disable-next-line no-console
  console.log(`Audit complete. Records: ${records.length}`);
};

main();
