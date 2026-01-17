const fs = require("fs");
const path = require("path");

const lessonsPath = path.resolve("frontend/public/data/lessons.json");
const coursePaths = {
  python: path.resolve("frontend/public/data/course-python-basics.json"),
  sql: path.resolve("frontend/public/data/course-sql-fundamentals.json"),
  r: path.resolve("frontend/public/data/course-r-fundamentals.json")
};

const decisionTypes = new Set([
  "variable_slider",
  "draggable_value",
  "fill_blanks",
  "parsons_puzzle",
  "live_code_block",
  "step_executor",
  "visual_table",
  "token_slot",
  "loop_simulator",
  "conditional_path",
  "data_transform",
  "join_visualizer",
  "debug_quest",
  "graph_manipulator",
  "memory_machine"
]);

const consequenceTypes = new Set([
  "memory_box",
  "visual_table",
  "state_inspector",
  "output_diff",
  "step_executor",
  "fill_blanks",
  "live_code_block",
  "token_slot",
  "loop_simulator",
  "conditional_path",
  "data_transform",
  "join_visualizer",
  "debug_quest",
  "graph_manipulator",
  "memory_machine"
]);

const lessons = JSON.parse(fs.readFileSync(lessonsPath, "utf-8"));

let missingPlan = 0;
let missingTags = 0;
let missingInteraction = 0;
let missingDecision = 0;
let missingConsequence = 0;
let missingTemplate = 0;
let missingRecipe = 0;
let predictionWithoutJustification = 0;
let consecutiveRecipeViolations = 0;
let chapterRecipeViolations = 0;

const loadCourseOrder = (coursePath) => {
  if (!fs.existsSync(coursePath)) {
    return [];
  }
  const data = JSON.parse(fs.readFileSync(coursePath, "utf-8"));
  const order = [];
  for (const chapter of data.chapters || []) {
    if (chapter.concepts) {
      for (const concept of chapter.concepts) {
        for (const lesson of concept.lessons || []) {
          order.push(lesson.id);
        }
      }
    } else {
      for (const lesson of chapter.lessons || []) {
        order.push(lesson.id);
      }
    }
  }
  return order;
};

for (const [id, lesson] of Object.entries(lessons)) {
  const tags = lesson.concept_tags || [];
  const plan = lesson.interaction_plan || [];
  const required = lesson.interaction_required === true;

  if (!required) {
    missingInteraction += 1;
  }
  if (!tags.length) {
    missingTags += 1;
  }
  if (!plan.length) {
    missingPlan += 1;
  }

  const hasDecision = plan.some((item) => decisionTypes.has(item.type));
  const hasConsequence = plan.some((item) => consequenceTypes.has(item.type));
  if (!hasDecision) {
    missingDecision += 1;
  }
  if (!hasConsequence) {
    missingConsequence += 1;
  }

  const hasSend = plan.some((item) => item.type === "send_to_editor");
  if (hasSend && !lesson.send_to_editor_template) {
    missingTemplate += 1;
  }

  if (!lesson.interaction_recipe_id) {
    missingRecipe += 1;
  }

  const usesPrediction = plan.some((item) => item.type === "prediction");
  if (usesPrediction && !lesson.prediction_justification) {
    predictionWithoutJustification += 1;
  }
}

for (const [curriculum, coursePath] of Object.entries(coursePaths)) {
  const order = loadCourseOrder(coursePath);
  const recent = [];
  const chapterTotals = {};
  const chapterRecipeCounts = {};

  for (const lessonId of order) {
    const lesson = lessons[String(lessonId)];
    if (!lesson) {
      continue;
    }
    const recipeId = lesson.interaction_recipe_id || "";
    const chapterId = lesson.chapter_id || 0;
    chapterTotals[chapterId] = (chapterTotals[chapterId] || 0) + 1;
    chapterRecipeCounts[chapterId] = chapterRecipeCounts[chapterId] || {};
    chapterRecipeCounts[chapterId][recipeId] = (chapterRecipeCounts[chapterId][recipeId] || 0) + 1;

    recent.push(recipeId);
    if (recent.length > 3) {
      recent.shift();
    }
    if (recent.length === 3 && recent[0] === recent[1] && recent[1] === recent[2]) {
      consecutiveRecipeViolations += 1;
    }
  }

  for (const [chapterId, recipes] of Object.entries(chapterRecipeCounts)) {
    const total = chapterTotals[chapterId] || 1;
    if (total < 4) {
      continue;
    }
    for (const count of Object.values(recipes)) {
      if (count / total > 0.25) {
        chapterRecipeViolations += 1;
        break;
      }
    }
  }
}

const summary = {
  totalLessons: Object.keys(lessons).length,
  missingPlan,
  missingTags,
  missingInteraction,
  missingDecision,
  missingConsequence,
  missingTemplate,
  missingRecipe,
  predictionWithoutJustification,
  consecutiveRecipeViolations,
  chapterRecipeViolations
};

console.log("Interaction plan validation:");
console.log(JSON.stringify(summary, null, 2));

const hasErrors = Object.entries(summary).some(([key, value]) => key !== "totalLessons" && value > 0);
process.exit(hasErrors ? 1 : 0);
