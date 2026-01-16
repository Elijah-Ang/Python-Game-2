const fs = require("fs");
const path = require("path");

const lessonsPath = path.resolve("frontend/public/data/lessons.json");

const decisionTypes = new Set([
  "prediction",
  "variable_slider",
  "draggable_value",
  "fill_blanks",
  "parsons_puzzle",
  "live_code_block",
  "step_executor",
  "visual_table"
]);

const consequenceTypes = new Set([
  "memory_box",
  "visual_table",
  "state_inspector",
  "output_diff",
  "step_executor",
  "prediction",
  "fill_blanks",
  "live_code_block"
]);

const lessons = JSON.parse(fs.readFileSync(lessonsPath, "utf-8"));

let missingPlan = 0;
let missingTags = 0;
let missingInteraction = 0;
let missingDecision = 0;
let missingConsequence = 0;
let missingTemplate = 0;

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
}

const summary = {
  totalLessons: Object.keys(lessons).length,
  missingPlan,
  missingTags,
  missingInteraction,
  missingDecision,
  missingConsequence,
  missingTemplate
};

console.log("Interaction plan validation:");
console.log(JSON.stringify(summary, null, 2));

const hasErrors = Object.entries(summary).some(([key, value]) => key !== "totalLessons" && value > 0);
process.exit(hasErrors ? 1 : 0);
