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

const inputPath = readArg("input") || path.resolve(__dirname, "../interaction_audit_ui_sample.json");
const lessonsPath = path.resolve(__dirname, "../frontend/public/data/lessons.json");
const fingerprintListArg = readArg("fingerprints");
const fingerprintList = fingerprintListArg
  ? fingerprintListArg.split(",").map((value) => value.trim()).filter(Boolean)
  : ["7eb386507c", "9c0e087fd1", "7ed1a92787", "1aa321456d"];

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

const pickWords = (title) => {
  const words = (title || "").split(/\s+/).map((word) => word.replace(/[^a-zA-Z0-9]/g, "")).filter(Boolean);
  return [words[0] || "Option A", words[1] || "Option B"];
};

const buildLoopSimulator = (lesson) => {
  const vars = extractVariables(lesson.starter_code);
  const valueVar = vars[0] || "total";
  const iterations = 4 + (lesson.id % 3);
  const stepValue = (lesson.id % 4) + 1;
  const startValue = lesson.id % 3;
  return {
    recipeId: "regen_loop_sim",
    plan: [
      {
        type: "loop_simulator",
        label: `${lesson.title}: loop through ${valueVar}`,
        iterations,
        startValue,
        stepValue,
        valueVar,
        stepVar: `${valueVar}_step`
      }
    ]
  };
};

const buildConditionalPath = (lesson) => {
  const [wordA, wordB] = pickWords(lesson.title);
  return {
    recipeId: "regen_conditional_path",
    plan: [
      {
        type: "conditional_path",
        prompt: `Choose the branch for ${lesson.title}`,
        choices: [
          { label: `${wordA} passes`, outcome: "true" },
          { label: `${wordB} fails`, outcome: "false" }
        ],
        trueLabel: `${wordA} path runs`,
        falseLabel: `${wordB} path runs`,
        resultVar: "branch_result"
      }
    ]
  };
};

const buildGraphManipulator = (lesson) => {
  const slope = ((lesson.id % 5) + 1) * 0.5;
  return {
    recipeId: "regen_graph_manipulator",
    plan: [
      {
        type: "graph_manipulator",
        title: `${lesson.title}: adjust the input`,
        mode: lesson.id % 2 === 0 ? "linear" : "quadratic",
        slope,
        intercept: lesson.id % 10,
        xMin: -5,
        xMax: 5,
        initialX: 2,
        xVar: "input_x",
        yVar: "output_y"
      }
    ]
  };
};

const buildMemoryMachine = (lesson) => {
  const vars = extractVariables(lesson.starter_code).slice(0, 3);
  const slots = vars.length ? vars : ["value", "result"];
  const steps = slots.map((slot, idx) => ({
    label: `Set ${slot}`,
    slot,
    value: typeof slot === "string" && slot.includes("name") ? `item_${idx + 1}` : (idx + 1) * (lesson.id % 5 + 1)
  }));
  return {
    recipeId: "regen_memory_machine",
    plan: [
      {
        type: "memory_machine",
        title: `Track values for ${lesson.title}`,
        slots,
        steps
      }
    ]
  };
};

const buildFillBlanks = (lesson) => {
  const vars = extractVariables(lesson.starter_code);
  const targetVar = vars[0] || "value";
  return {
    recipeId: "regen_fill_blanks",
    plan: [
      {
        type: "fill_blanks",
        template: `Set {{variable}} to {{value}} then print it for ${lesson.title}.`,
        blanks: [
          { id: "variable", options: [targetVar, "result", "temp"], correct: targetVar },
          { id: "value", options: ["5", "10", "15"], correct: "10" }
        ]
      }
    ]
  };
};

const buildDataTransform = (lesson) => {
  const columns = ["id", "status", "score"];
  const beforeRows = [
    { id: 1, status: "active", score: 12 },
    { id: 2, status: "inactive", score: 4 },
    { id: 3, status: "active", score: 18 }
  ];
  return {
    recipeId: "regen_data_transform",
    plan: [
      {
        type: "data_transform",
        title: `${lesson.title}: filter the rows`,
        columns,
        beforeRows,
        filters: [
          { id: "active", label: "status = active", rows: beforeRows.filter((row) => row.status === "active") },
          { id: "high", label: "score >= 10", rows: beforeRows.filter((row) => row.score >= 10) }
        ],
        resultVar: "rows_kept"
      }
    ]
  };
};

const buildJoinVisualizer = (lesson) => {
  const leftRows = [
    { id: 1, name: "Avery" },
    { id: 2, name: "Blake" }
  ];
  const rightRows = [
    { id: 1, dept: "Sales" },
    { id: 3, dept: "Design" }
  ];
  return {
    recipeId: "regen_join_visualizer",
    plan: [
      {
        type: "join_visualizer",
        leftTitle: "Employees",
        rightTitle: "Departments",
        leftRows,
        rightRows,
        leftKey: "id",
        rightKey: "id",
        joinTypes: ["LEFT JOIN", "INNER JOIN", "RIGHT JOIN"],
        resultVar: "join_rows",
        joinVar: "join_type"
      }
    ]
  };
};

const buildDebugQuest = (lesson) => {
  const snippet = `total = 0\nfor i in range(3)\n    total += i\nprint(total)`;
  return {
    recipeId: "regen_debug_quest",
    plan: [
      {
        type: "debug_quest",
        title: `${lesson.title}: fix the bug`,
        snippet,
        bugLine: 2,
        options: [
          { label: "Add missing colon to the loop line", fix: "for i in range(3):", correct: true },
          { label: "Remove the print line", fix: "remove print", correct: false },
          { label: "Change total to total()", fix: "total()", correct: false }
        ],
        solvedVar: "debug_solved"
      }
    ]
  };
};

const buildStepExecutor = (lesson) => {
  const code = `sum = 0\nfor n in [1, 2, 3]:\n    sum += n\nprint(sum)`;
  return {
    recipeId: "regen_step_executor",
    plan: [
      {
        type: "step_executor",
        code,
        steps: [
          { line: 1, description: "Initialize sum", stateChanges: { sum: 0 } },
          { line: 2, description: "Start loop", stateChanges: { n: 1 } },
          { line: 3, description: "Add n", stateChanges: { sum: 1 } }
        ]
      }
    ]
  };
};

const builderByTag = {
  loops: [buildLoopSimulator, buildStepExecutor],
  conditionals: [buildConditionalPath],
  join: [buildJoinVisualizer, buildDataTransform],
  group_by: [buildDataTransform],
  visualization: [buildGraphManipulator],
  variables: [buildMemoryMachine, buildFillBlanks],
  strings: [buildFillBlanks, buildDebugQuest],
  general: [buildDebugQuest, buildGraphManipulator, buildMemoryMachine]
};

const main = () => {
  if (!fs.existsSync(inputPath)) {
    throw new Error(`Missing UI sample audit at ${inputPath}`);
  }
  const uiSample = JSON.parse(fs.readFileSync(inputPath, "utf-8"));
  const lessons = JSON.parse(fs.readFileSync(lessonsPath, "utf-8"));

  const fingerprintCounts = uiSample.reduce((acc, record) => {
    if (record.interaction_fingerprint_id) {
      acc[record.interaction_fingerprint_id] = (acc[record.interaction_fingerprint_id] || 0) + 1;
    }
    return acc;
  }, {});
  const maxAllowed = Math.max(1, Math.floor(uiSample.length * 0.05));
  const overused = Object.keys(fingerprintCounts).filter((id) => fingerprintCounts[id] > maxAllowed);

  const streakIds = new Set();
  let current = [];
  uiSample.forEach((record) => {
    if (!record.interaction_fingerprint_id) {
      current = [];
      return;
    }
    if (!current.length || current[0].interaction_fingerprint_id === record.interaction_fingerprint_id) {
      current.push(record);
    } else {
      if (current.length > 2) {
        current.forEach((item) => streakIds.add(item.lesson_id));
      }
      current = [record];
    }
    if (current.length > 2) {
      current.forEach((item) => streakIds.add(item.lesson_id));
    }
  });

  const flaggedIds = new Set();
  uiSample.forEach((record) => {
    if (fingerprintList.includes(record.interaction_fingerprint_id)) {
      flaggedIds.add(record.lesson_id);
    }
    if (overused.includes(record.interaction_fingerprint_id)) {
      flaggedIds.add(record.lesson_id);
    }
  });
  streakIds.forEach((id) => flaggedIds.add(id));

  const builderUsage = new Map();
  const updated = [];

  Array.from(flaggedIds).forEach((lessonId) => {
    const lesson = lessons[String(lessonId)];
    if (!lesson) return;
    const tags = lesson.concept_tags || ["general"];
    const primaryTag = tags[0] || "general";
    const builders = builderByTag[primaryTag] || builderByTag.general;
    let selectedBuilder = builders[0];
    let minCount = Infinity;
    builders.forEach((builder) => {
      const key = builder.name;
      const count = builderUsage.get(key) || 0;
      if (count < minCount) {
        minCount = count;
        selectedBuilder = builder;
      }
    });
    const built = selectedBuilder(lesson);
    builderUsage.set(selectedBuilder.name, (builderUsage.get(selectedBuilder.name) || 0) + 1);

    const addReset = lessonId % 2 === 0;
    lesson.interaction_plan = addReset
      ? [...built.plan, { type: "reset_state", label: "Reset interaction" }]
      : built.plan;
    lesson.interaction_recipe_id = built.recipeId;
    lesson.send_to_editor_template = "";

    updated.push(lessonId);
  });

  fs.writeFileSync(lessonsPath, JSON.stringify(lessons, null, 2));
  // eslint-disable-next-line no-console
  console.log(`Regenerated ${updated.length} lessons: ${updated.slice(0, 20).join(", ")}${updated.length > 20 ? "..." : ""}`);
};

main();
