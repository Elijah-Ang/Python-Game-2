const fs = require("fs");
const path = require("path");

const inputPath = path.resolve(__dirname, "../interaction_audit_ui_sample.json");
const lessonsPath = path.resolve(__dirname, "../frontend/public/data/lessons.json");

const scaffolding = new Set([
  "InteractionPlanRenderer",
  "HintLadder",
  "ResetStateButton",
  "SendToEditor",
  "StateInspector",
  "OutputDiff"
]);

const primaryShape = (components) => {
  const filtered = (components || []).filter((comp) => comp && !scaffolding.has(comp));
  return filtered[0] || "base";
};

const main = () => {
  if (!fs.existsSync(inputPath)) {
    console.error(`Missing UI sample audit at ${inputPath}`);
    process.exit(1);
  }
  const records = JSON.parse(fs.readFileSync(inputPath, "utf-8"));
  const lessons = JSON.parse(fs.readFileSync(lessonsPath, "utf-8"));

  const fingerprintCounts = {};
  records.forEach((record) => {
    if (!record.interaction_fingerprint_id) return;
    fingerprintCounts[record.interaction_fingerprint_id] = (fingerprintCounts[record.interaction_fingerprint_id] || 0) + 1;
  });

  const maxAllowed = Math.max(1, Math.floor(records.length * 0.05));
  const fingerprintViolations = Object.entries(fingerprintCounts)
    .filter(([, count]) => count > maxAllowed)
    .map(([fingerprintId, count]) => ({ fingerprintId, count }));

  const streakViolations = [];
  let streak = [];
  records.forEach((record) => {
    if (!record.interaction_fingerprint_id) {
      streak = [];
      return;
    }
    if (!streak.length || streak[0].interaction_fingerprint_id === record.interaction_fingerprint_id) {
      streak.push(record);
    } else {
      if (streak.length > 2) {
        streakViolations.push([...streak]);
      }
      streak = [record];
    }
  });
  if (streak.length > 2) {
    streakViolations.push([...streak]);
  }

  const chapterTotals = {};
  const chapterShapeCounts = {};
  records.forEach((record) => {
    const lesson = lessons[String(record.lesson_id)];
    const chapterId = lesson && lesson.chapter_id ? String(lesson.chapter_id) : "unknown";
    const shape = primaryShape(record.components || []);
    chapterTotals[chapterId] = (chapterTotals[chapterId] || 0) + 1;
    chapterShapeCounts[chapterId] = chapterShapeCounts[chapterId] || {};
    chapterShapeCounts[chapterId][shape] = (chapterShapeCounts[chapterId][shape] || 0) + 1;
  });

  const chapterViolations = [];
  Object.entries(chapterShapeCounts).forEach(([chapterId, shapes]) => {
    const total = chapterTotals[chapterId] || 0;
    Object.entries(shapes).forEach(([shape, count]) => {
      if (total > 0 && count / total > 0.25) {
        chapterViolations.push({ chapterId, shape, count, total });
      }
    });
  });

  const errors = [];
  if (fingerprintViolations.length) {
    errors.push(`Fingerprint frequency violations: ${fingerprintViolations.map((v) => `${v.fingerprintId} (${v.count}/${records.length})`).join(", ")}`);
  }
  if (streakViolations.length) {
    errors.push(`Fingerprint streaks >2 found: ${streakViolations.length}`);
  }
  if (chapterViolations.length) {
    errors.push(`Chapter shape dominance violations: ${chapterViolations.length}`);
  }

  if (errors.length) {
    console.error(errors.join("\n"));
    process.exit(1);
  }

  console.log("UI fingerprint validation passed.");
};

main();
