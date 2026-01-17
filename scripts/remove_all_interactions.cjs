const fs = require('fs');
const path = require('path');

const lessonsPath = path.resolve(__dirname, '../frontend/public/data/lessons.json');
const lessons = JSON.parse(fs.readFileSync(lessonsPath, 'utf8'));

let updated = 0;

Object.values(lessons).forEach((lesson) => {
  if (!lesson || typeof lesson !== 'object') return;
  let changed = false;
  if (lesson.interaction_plan) {
    delete lesson.interaction_plan;
    changed = true;
  }
  if (lesson.interaction_recipe_id) {
    delete lesson.interaction_recipe_id;
    changed = true;
  }
  if (lesson.interaction_required !== undefined) {
    delete lesson.interaction_required;
    changed = true;
  }
  if (lesson.send_to_editor_template) {
    delete lesson.send_to_editor_template;
    changed = true;
  }
  if (lesson.expected_output) {
    delete lesson.expected_output;
    changed = true;
  }
  if (lesson.expected_result) {
    delete lesson.expected_result;
    changed = true;
  }
  if (changed) updated += 1;
});

fs.writeFileSync(lessonsPath, JSON.stringify(lessons, null, 2));
console.log(`Removed interactions from ${updated} lessons.`);
