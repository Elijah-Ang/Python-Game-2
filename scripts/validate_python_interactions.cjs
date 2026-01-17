const fs = require("fs");
const path = require("path");

const lessonsPath = path.resolve(__dirname, "../frontend/public/data/lessons.json");
const coursePath = path.resolve(__dirname, "../frontend/public/data/course-python-basics.json");
const uiSamplePath = path.resolve(__dirname, "../interaction_audit_ui_sample.json");

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

const DECISION_TYPES = new Set([
  "prediction",
  "variable_slider",
  "draggable_value",
  "live_code_block",
  "parsons_puzzle",
  "fill_blanks",
  "token_slot",
  "loop_simulator",
  "conditional_path",
  "data_transform",
  "join_visualizer",
  "debug_quest",
  "graph_manipulator",
  "memory_machine",
  "step_executor"
]);

const CONSEQUENCE_TYPES = new Set([
  "variable_slider",
  "draggable_value",
  "live_code_block",
  "parsons_puzzle",
  "fill_blanks",
  "token_slot",
  "loop_simulator",
  "conditional_path",
  "data_transform",
  "join_visualizer",
  "debug_quest",
  "graph_manipulator",
  "memory_machine",
  "step_executor",
  "output_diff",
  "state_inspector",
  "visual_table"
]);

const hasPredictionInContent = (content) => /<predictioncheck\b/i.test(content || "");

const main = () => {
  const lessons = JSON.parse(fs.readFileSync(lessonsPath, "utf-8"));
  const pythonIds = loadCourseOrder(coursePath);
  const uiSample = JSON.parse(fs.readFileSync(uiSamplePath, "utf-8"))
    .filter((record) => getCurriculum(record.lesson_id) === "python");

  const issues = [];

  const sampleSize = uiSample.length;
  const cap = Math.floor(0.05 * sampleSize);
  const fingerprintCounts = {};
  uiSample.forEach((record) => {
    if (!record.interaction_fingerprint_id) {
      return;
    }
    fingerprintCounts[record.interaction_fingerprint_id] =
      (fingerprintCounts[record.interaction_fingerprint_id] || 0) + 1;
  });
  const overCap = Object.entries(fingerprintCounts)
    .filter(([, count]) => count > cap)
    .map(([id, count]) => `${id} (${count}/${cap})`);
  if (overCap.length > 0) {
    issues.push(`Fingerprint cap exceeded: ${overCap.join(", ")}`);
  }

  let streak = 1;
  for (let i = 1; i < uiSample.length; i += 1) {
    if (uiSample[i].interaction_fingerprint_id &&
        uiSample[i].interaction_fingerprint_id === uiSample[i - 1].interaction_fingerprint_id) {
      streak += 1;
      if (streak > 2) {
        issues.push(`Fingerprint streak > 2 ending at lesson ${uiSample[i].lesson_id}`);
        break;
      }
    } else {
      streak = 1;
    }
  }

  const predictionHits = uiSample.filter((record) => record.prediction_present);
  if (predictionHits.length > 0) {
    issues.push(`Prediction UI present in sample: ${predictionHits.map((r) => r.lesson_id).join(", ")}`);
  }

  const missingPlans = [];
  const missingDecision = [];
  const missingConsequence = [];
  const predictionLessons = [];

  pythonIds.forEach((lessonId) => {
    const lesson = lessons[String(lessonId)];
    if (!lesson) {
      missingPlans.push(`${lessonId} (missing lesson data)`);
      return;
    }
    const plan = Array.isArray(lesson.interaction_plan) ? lesson.interaction_plan : [];
    if (plan.length === 0) {
      missingPlans.push(String(lessonId));
      return;
    }
    const types = plan.map((item) => item.type).filter(Boolean);
    const hasDecision = types.some((type) => DECISION_TYPES.has(type));
    const hasConsequence = types.some((type) => CONSEQUENCE_TYPES.has(type));
    if (!hasDecision) {
      missingDecision.push(String(lessonId));
    }
    if (!hasConsequence) {
      missingConsequence.push(String(lessonId));
    }
    if (types.includes("prediction") || hasPredictionInContent(lesson.content)) {
      const justification = lesson.prediction_justification;
      if (!justification) {
        predictionLessons.push(String(lessonId));
      }
    }
  });

  if (missingPlans.length > 0) {
    issues.push(`Missing interaction_plan: ${missingPlans.join(", ")}`);
  }
  if (missingDecision.length > 0) {
    issues.push(`Missing decision marker: ${missingDecision.join(", ")}`);
  }
  if (missingConsequence.length > 0) {
    issues.push(`Missing consequence marker: ${missingConsequence.join(", ")}`);
  }
  if (predictionLessons.length > 0) {
    issues.push(`Prediction used without justification: ${predictionLessons.join(", ")}`);
  }

  if (issues.length > 0) {
    // eslint-disable-next-line no-console
    console.error("Python interaction validation failed:");
    issues.forEach((issue) => console.error(`- ${issue}`));
    process.exit(1);
  }

  // eslint-disable-next-line no-console
  console.log(`Python interaction validation passed. Sample size: ${sampleSize}, cap: ${cap}`);
};

main();
