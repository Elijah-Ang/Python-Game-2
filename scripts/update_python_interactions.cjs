const fs = require("fs");
const path = require("path");

const lessonsPath = path.resolve(__dirname, "../frontend/public/data/lessons.json");
const coursePath = path.resolve(__dirname, "../frontend/public/data/course-python-basics.json");

const lessons = JSON.parse(fs.readFileSync(lessonsPath, "utf8"));
const course = JSON.parse(fs.readFileSync(coursePath, "utf8"));

const getLessonIds = () => {
  const ids = [];
  (course.chapters || []).forEach((chapter) => {
    if (Array.isArray(chapter.concepts)) {
      chapter.concepts.forEach((concept) => {
        (concept.lessons || []).forEach((lesson) => {
          if (lesson && lesson.id != null) {
            ids.push(lesson.id);
          }
        });
      });
    } else if (Array.isArray(chapter.lessons)) {
      chapter.lessons.forEach((lesson) => {
        if (lesson && lesson.id != null) {
          ids.push(lesson.id);
        }
      });
    }
  });
  return ids;
};

const parseArrayLiteral = (value) => {
  if (!value) return null;
  const trimmed = value.trim();
  if (!trimmed.startsWith("[") || !trimmed.endsWith("]")) {
    return null;
  }
  try {
    const json = trimmed.replace(/'/g, "\"");
    return JSON.parse(json);
  } catch (err) {
    return null;
  }
};

const parseDictLiteral = (value) => {
  if (!value) return null;
  const trimmed = value.trim();
  if (!trimmed.startsWith("{") || !trimmed.endsWith("}")) {
    return null;
  }
  try {
    const json = trimmed.replace(/'/g, "\"");
    return JSON.parse(json);
  } catch (err) {
    return null;
  }
};

const extractAssignments = (code) => {
  const assignments = [];
  if (!code) return assignments;
  const lines = code.split("\n");
  lines.forEach((line) => {
    if (line.includes("==") || line.includes("!=") || line.includes(">=") || line.includes("<=")) {
      return;
    }
    const match = line.match(/^\s*([A-Za-z_]\w*)\s*=\s*(.+)$/);
    if (!match) return;
    const name = match[1];
    const expr = match[2].trim();
    assignments.push({ name, expr });
  });
  return assignments;
};

const inferValue = (expr, known) => {
  if (!expr) return "value";
  const num = expr.match(/^(-?\d+(\.\d+)?)$/);
  if (num) return Number(num[1]);
  const str = expr.match(/^['"](.+)['"]$/);
  if (str) return str[1];
  const list = parseArrayLiteral(expr);
  if (list) return list;
  const dict = parseDictLiteral(expr);
  if (dict) return dict;
  const plusMatch = expr.match(/^([A-Za-z_]\w*)\s*\+\s*(-?\d+(\.\d+)?)$/);
  if (plusMatch) {
    const base = known[plusMatch[1]];
    const add = Number(plusMatch[2]);
    if (typeof base === "number") return base + add;
  }
  const varMatch = expr.match(/^([A-Za-z_]\w*)$/);
  if (varMatch && known[varMatch[1]] !== undefined) return known[varMatch[1]];
  return expr.length > 40 ? `${expr.slice(0, 37)}...` : expr;
};

const extractListFromCode = (code) => {
  if (!code) return null;
  const match = code.match(/\[[^\]]+\]/);
  if (!match) return null;
  return parseArrayLiteral(match[0]);
};

const extractDictFromCode = (code) => {
  if (!code) return null;
  const match = code.match(/\{[^}]+\}/);
  if (!match) return null;
  return parseDictLiteral(match[0]);
};

const extractDataFrame = (code) => {
  if (!code) return null;
  const match = code.match(/pd\.DataFrame\(\s*\{([\s\S]*?)\}\s*\)/);
  if (!match) return null;
  const body = match[1];
  const cols = [];
  const values = [];
  const entryRegex = /'([^']+)'\s*:\s*(\[[^\]]+\])/g;
  let entry;
  while ((entry = entryRegex.exec(body))) {
    const col = entry[1];
    const arr = parseArrayLiteral(entry[2]) || [];
    cols.push(col);
    values.push(arr);
  }
  if (!cols.length) return null;
  const rowCount = Math.max(...values.map((arr) => arr.length));
  const rows = [];
  for (let i = 0; i < rowCount; i += 1) {
    const row = {};
    cols.forEach((col, idx) => {
      row[col] = values[idx][i] !== undefined ? values[idx][i] : null;
    });
    rows.push(row);
  }
  return { columns: cols, rows };
};

const detectLibrary = (code) => {
  const lower = (code || "").toLowerCase();
  if (lower.includes("pandas") || /\bpd\b/.test(lower)) return "pandas";
  if (lower.includes("numpy") || /\bnp\b/.test(lower)) return "numpy";
  if (lower.includes("matplotlib") || /\bplt\b/.test(lower)) return "matplotlib";
  if (lower.includes("sklearn")) return "sklearn";
  if (lower.includes("open(") || lower.includes("read(") || lower.includes("write(")) return "files";
  if (lower.includes("regex") || lower.includes("str.replace") || /\bre\b/.test(lower)) return "regex";
  return "core";
};

const slugify = (value) => value.toLowerCase().replace(/[^a-z0-9]+/g, "_").replace(/^_|_$/g, "");

const buildMemoryMachine = (lesson) => {
  const assignments = extractAssignments(lesson.starter_code || "");
  const slots = [];
  const steps = [];
  const known = {};
  assignments.slice(0, 4).forEach((item) => {
    if (!slots.includes(item.name)) slots.push(item.name);
    const value = inferValue(item.expr, known);
    known[item.name] = value;
    steps.push({
      label: `Set ${item.name}`,
      slot: item.name,
      value
    });
  });
  if (!slots.length) slots.push("value");
  if (!steps.length) {
    steps.push({ label: "Set value", slot: slots[0], value: 1 });
  }
  return [
    { type: "memory_machine", title: lesson.title, slots, steps },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildStringWorkbench = (lesson) => {
  const code = lesson.starter_code || "";
  const vars = extractAssignments(code).map((a) => a.name);
  const fLine = code.split("\n").find((line) => line.includes("f\"") || line.includes("f'"));
  if (fLine) {
    const blanks = [];
    const template = fLine.replace(/\{([A-Za-z_]\w*)\}/g, (_, name) => {
      if (!blanks.find((b) => b.id === name)) {
        const options = [name].concat(vars.filter((v) => v !== name).slice(0, 2));
        blanks.push({ id: name, options, correct: name });
      }
      return `{{${name}}}`;
    });
    if (blanks.length) {
      return [
        { type: "fill_blanks", template, blanks },
        { type: "reset_state", label: "Reset" }
      ];
    }
  }
  if (vars.length >= 2) {
    return [
      {
        type: "fill_blanks",
        template: "full = {{left}} + {{space}} + {{right}}",
        blanks: [
          { id: "left", options: [vars[0], vars[1]], correct: vars[0] },
          { id: "space", options: ["\" \"", "\"\""], correct: "\" \"" },
          { id: "right", options: [vars[1], vars[0]], correct: vars[1] }
        ]
      },
      { type: "reset_state", label: "Reset" }
    ];
  }
  const single = vars[0] || "text";
  return [
    {
      type: "token_slot",
      template: "print({{value}})",
      slots: [{ id: "value", options: [single, "\"Hello\""], correct: single }]
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildTruthiness = (lesson) => {
  const vars = extractAssignments(lesson.starter_code || "").map((a) => a.name);
  const target = vars[0] || "value";
  return [
    {
      type: "conditional_path",
      prompt: `Is ${target} truthy?`,
      choices: [
        { label: "[] (empty)", outcome: "false" },
        { label: "0", outcome: "false" },
        { label: "\"0\"", outcome: "true" },
        { label: "[1]", outcome: "true" }
      ],
      trueLabel: "Truthy path runs",
      falseLabel: "Falsy path runs",
      resultVar: `${target}_truthy`
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildExpressionTrace = (lesson) => {
  const code = lesson.starter_code || "";
  const exprLine = code.split("\n").find((line) => line.includes(">") || line.includes("<") || line.includes("and") || line.includes("or")) || "result = a > b";
  const expr = exprLine.includes("=") ? exprLine : `result = ${exprLine.trim()}`;
  return [
    {
      type: "step_executor",
      code: expr,
      steps: [
        { line: 1, description: "Evaluate the expression.", stateChanges: { result: "computed" } }
      ]
    }
  ];
};

const buildPathExplorer = (lesson) => {
  const code = lesson.starter_code || "";
  const ifLine = code.split("\n").find((line) => line.trim().startsWith("if ")) || "if score >= 70:";
  const condition = ifLine.replace(/^if\s+/, "").replace(/:\s*$/, "");
  let prompt = `Condition: ${condition}`;
  const match = condition.match(/([A-Za-z_]\w*)\s*([<>]=?|==|!=)\s*(-?\d+(\.\d+)?)/);
  const choices = [];
  if (match) {
    const variable = match[1];
    const op = match[2];
    const threshold = Number(match[3]);
    const trueVal = op.includes(">") ? threshold + 1 : threshold - 1;
    const falseVal = op.includes(">") ? threshold - 1 : threshold + 1;
    choices.push({ label: `${variable} = ${trueVal}`, outcome: "true" });
    choices.push({ label: `${variable} = ${falseVal}`, outcome: "false" });
    prompt = `Set ${variable} to test the branch`;
  } else {
    choices.push({ label: "Condition true", outcome: "true" });
    choices.push({ label: "Condition false", outcome: "false" });
  }
  return [
    {
      type: "conditional_path",
      prompt,
      choices,
      trueLabel: "Condition met",
      falseLabel: "Condition not met"
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildLoopSimulator = (lesson, label = "Loop preview") => {
  const code = lesson.starter_code || "";
  let iterations = 5;
  let startValue = 0;
  let stepValue = 1;
  let valueVar = "i";
  const rangeMatch = code.match(/for\s+([A-Za-z_]\w*)\s+in\s+range\(([^)]+)\)/);
  if (rangeMatch) {
    valueVar = rangeMatch[1];
    const parts = rangeMatch[2].split(",").map((p) => Number(p.trim()));
    if (parts.length === 1) {
      iterations = Math.max(1, parts[0]);
    } else if (parts.length >= 2) {
      startValue = parts[0];
      const stop = parts[1];
      stepValue = parts.length === 3 ? parts[2] : 1;
      iterations = Math.max(1, Math.ceil((stop - startValue) / stepValue));
    }
  }
  return [
    {
      type: "loop_simulator",
      label,
      iterations,
      startValue,
      stepValue,
      valueVar,
      stepVar: "step"
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildControlFlowTimeline = (lesson) => {
  const code = lesson.starter_code || "";
  const snippet = code.split("\n").slice(0, 6).join("\n") || "for n in numbers:\n    if n == target:\n        break";
  return [
    {
      type: "step_executor",
      code: snippet,
      steps: [
        { line: 1, description: "Start loop." },
        { line: 2, description: "Check stop condition." },
        { line: 3, description: "Exit early with break." }
      ]
    }
  ];
};

const buildCallStack = (lesson) => {
  const code = lesson.starter_code || "";
  const snippet = code.split("\n").slice(0, 8).join("\n") || "def greet(name):\n    return f\"Hi {name}\"\n\nresult = greet(\"Ada\")";
  return [
    {
      type: "step_executor",
      code: snippet,
      steps: [
        { line: 1, description: "Define the function." },
        { line: 3, description: "Call the function.", stateChanges: { result: "computed" } }
      ]
    },
    {
      type: "state_inspector",
      title: "Call state",
      showTypes: true
    }
  ];
};

const buildContainerManipulator = (lesson) => {
  const code = lesson.starter_code || "";
  const dict = extractDictFromCode(code);
  if (dict) {
    const data = Object.entries(dict).map(([key, value]) => ({ key, value }));
    const keys = Object.keys(dict);
    return [
      {
        type: "visual_table",
        title: "Key/value view",
        columns: ["key", "value"],
        data,
        allowSort: false,
        allowReorder: false,
        allowRowHighlight: true
      },
      {
        type: "token_slot",
        template: "{{dict}}[{{key}}]",
        slots: [
          { id: "dict", options: ["data", "item", "record"], correct: "data" },
          { id: "key", options: keys.slice(0, 3), correct: keys[0] }
        ]
      },
      { type: "reset_state", label: "Reset" }
    ];
  }
  const list = extractListFromCode(code) || ["a", "b", "c"];
  const data = list.map((value, index) => ({ index, value }));
  return [
    {
      type: "visual_table",
      title: "Container slots",
      columns: ["index", "value"],
      data,
      allowSort: false,
      allowReorder: true,
      allowRowHighlight: true
    },
    {
      type: "token_slot",
      template: "{{list}}.{{op}}({{arg}})",
      slots: [
        { id: "list", options: ["items", "values", "list"], correct: "items" },
        { id: "op", options: ["append", "pop", "insert"], correct: "append" },
        { id: "arg", options: ["\"new\"", "0", "1"], correct: "\"new\"" }
      ]
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildAlgorithmWorkbench = (lesson) => {
  const code = lesson.starter_code || "";
  const snippet = code.split("\n").slice(0, 8).join("\n") || "for n in numbers:\n    total += n";
  return [
    {
      type: "step_executor",
      code: snippet,
      steps: [
        { line: 1, description: "Initialize the scan." },
        { line: 2, description: "Update the running state." }
      ]
    },
    { type: "state_inspector", title: "Algorithm state", showTypes: true }
  ];
};

const buildImportMap = (lesson) => {
  const code = lesson.starter_code || "";
  const fromMatch = code.match(/from\s+([A-Za-z_]\w*)\s+import\s+([A-Za-z_]\w*)/);
  const importMatch = code.match(/import\s+([A-Za-z_]\w*)/);
  const module = fromMatch ? fromMatch[1] : (importMatch ? importMatch[1] : "math");
  const name = fromMatch ? fromMatch[2] : "pi";
  return [
    {
      type: "token_slot",
      template: `from {{module}} import {{name}}`,
      slots: [
        { id: "module", options: [module, "random", "datetime"].slice(0, 3), correct: module },
        { id: "name", options: [name, "sqrt", "choice"].slice(0, 3), correct: name }
      ]
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildRandomnessLab = () => ([
  {
    type: "variable_slider",
    name: "seed",
    min: 1,
    max: 100,
    initial: 42,
    label: "Seed"
  },
  { type: "state_inspector", title: "Seed state", showTypes: true }
]);

const buildTimelineManipulator = () => ([
  {
    type: "variable_slider",
    name: "days",
    min: 0,
    max: 30,
    initial: 7,
    label: "Days"
  },
  { type: "state_inspector", title: "Time delta", showTypes: true }
]);

const buildRegexLab = (lesson) => {
  const code = lesson.starter_code || "";
  const patternMatch = code.match(/r'([^']+)'/);
  const pattern = patternMatch ? `r'${patternMatch[1]}'` : "r'[^0-9]'";
  return [
    {
      type: "token_slot",
      template: "pattern = {{pattern}}",
      slots: [
        { id: "pattern", options: [pattern, "r'\\d'", "r'[^A-Za-z]'"], correct: pattern }
      ]
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildFileSandbox = (lesson) => {
  const code = lesson.starter_code || "";
  const snippet = code.split("\n").slice(0, 8).join("\n") || "with open(\"data.txt\") as f:\n    content = f.read()";
  return [
    {
      type: "step_executor",
      code: snippet,
      steps: [
        { line: 1, description: "Open the file." },
        { line: 2, description: "Read the content.", stateChanges: { content: "loaded" } }
      ]
    },
    { type: "state_inspector", title: "File state", showTypes: true }
  ];
};

const buildDataTransform = (lesson) => {
  const df = extractDataFrame(lesson.starter_code || "");
  const columns = df ? df.columns : ["col", "value"];
  const rows = df ? df.rows : [{ col: "A", value: 1 }, { col: "B", value: 2 }];
  const half = Math.max(1, Math.floor(rows.length / 2));
  return [
    {
      type: "data_transform",
      title: lesson.title,
      columns,
      beforeRows: rows,
      filters: [
        { id: "all", label: "Keep all", rows },
        { id: "filtered", label: "Filtered", rows: rows.slice(0, half) }
      ],
      resultVar: "rows_kept"
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildAggregation = (lesson) => {
  const df = extractDataFrame(lesson.starter_code || "");
  const columns = df ? df.columns : ["group", "value"];
  const rows = df ? df.rows : [{ group: "A", value: 10 }, { group: "B", value: 12 }];
  const groupCol = columns[0];
  const metricCol = columns[1] || columns[0];
  return [
    {
      type: "visual_table",
      title: "Source rows",
      columns,
      data: rows,
      allowSort: false,
      allowFilter: false,
      allowRowHighlight: true
    },
    {
      type: "token_slot",
      template: "df.groupby('{{group}}')['{{metric}}'].{{agg}}()",
      slots: [
        { id: "group", options: [groupCol].concat(columns.slice(1, 3)), correct: groupCol },
        { id: "metric", options: [metricCol].concat(columns.slice(0, 2)), correct: metricCol },
        { id: "agg", options: ["sum", "mean", "count"], correct: "sum" }
      ]
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildJoin = (lesson) => {
  const df = extractDataFrame(lesson.starter_code || "");
  const columns = df ? df.columns : ["id", "value"];
  const key = columns.find((col) => col.includes("id")) || columns[0];
  return [
    {
      type: "join_visualizer",
      leftTitle: "Left table",
      rightTitle: "Right table",
      leftRows: [
        { [key]: 1, name: "A" },
        { [key]: 2, name: "B" }
      ],
      rightRows: [
        { [key]: 1, amount: 10 },
        { [key]: 3, amount: 20 }
      ],
      leftKey: key,
      rightKey: key,
      joinTypes: ["LEFT JOIN", "INNER JOIN"]
    }
  ];
};

const buildDedup = (lesson) => {
  const df = extractDataFrame(lesson.starter_code || "");
  const columns = df ? df.columns : ["item", "value"];
  const rows = df ? df.rows : [{ item: "A", value: 1 }, { item: "A", value: 1 }, { item: "B", value: 2 }];
  const uniqueRows = rows.filter((row, idx, arr) => arr.findIndex((r) => JSON.stringify(r) === JSON.stringify(row)) === idx);
  return [
    {
      type: "data_transform",
      title: lesson.title,
      columns,
      beforeRows: rows,
      filters: [
        { id: "dupes", label: "Original", rows },
        { id: "unique", label: "Drop duplicates", rows: uniqueRows }
      ],
      resultVar: "rows_kept"
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildArrayGrid = (lesson) => {
  const list = extractListFromCode(lesson.starter_code || "") || [1, 2, 3, 4];
  const data = list.map((value, index) => ({ index, value }));
  return [
    {
      type: "visual_table",
      title: "Array view",
      columns: ["index", "value"],
      data,
      allowSort: false,
      allowFilter: false,
      allowRowHighlight: true
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildArrayCondition = (lesson) => {
  const list = extractListFromCode(lesson.starter_code || "") || [10, 20, 30, 40];
  const data = list.map((value, index) => ({ index, value }));
  return [
    {
      type: "visual_table",
      title: "Array values",
      columns: ["index", "value"],
      data,
      allowSort: false,
      allowFilter: false,
      allowRowHighlight: true
    },
    {
      type: "token_slot",
      template: "mask = arr {{op}} {{threshold}}",
      slots: [
        { id: "op", options: [">", "<", ">="], correct: ">" },
        { id: "threshold", options: ["25", "30", "15"], correct: "25" }
      ]
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildBroadcasting = () => ([
  {
    type: "step_executor",
    code: "vector = [1, 2, 3]\nscalar = 10\nresult = vector + scalar",
    steps: [
      { line: 1, description: "Vector shape (3,)" },
      { line: 2, description: "Scalar shape ()" },
      { line: 3, description: "Broadcast and add.", stateChanges: { result: "[11,12,13]" } }
    ]
  }
]);

const buildChartBuilder = (lesson) => {
  const title = (lesson.title || "").toLowerCase();
  let chart = "plot";
  if (title.includes("bar")) chart = "bar";
  if (title.includes("scatter")) chart = "scatter";
  if (title.includes("hist")) chart = "hist";
  if (title.includes("pie")) chart = "pie";
  return [
    {
      type: "token_slot",
      template: `plt.${chart}({{x}}, {{y}})`,
      slots: [
        { id: "x", options: ["x", "labels", "categories"], correct: "x" },
        { id: "y", options: ["y", "values", "scores"], correct: "y" }
      ]
    },
    { type: "reset_state", label: "Reset" }
  ];
};

const buildDistribution = (lesson) => ([
  {
    type: "graph_manipulator",
    title: lesson.title,
    mode: "linear",
    slope: 1,
    intercept: 0,
    xMin: -5,
    xMax: 5,
    initialX: 1
  },
  { type: "reset_state", label: "Reset" }
]);

const buildPipeline = () => ([
  {
    type: "step_executor",
    code: "scale -> model -> score",
    steps: [
      { line: 1, description: "Scale features." },
      { line: 1, description: "Train model." },
      { line: 1, description: "Score pipeline." }
    ]
  }
]);

const buildDecisionTree = () => ([
  {
    type: "conditional_path",
    prompt: "Follow the tree rule",
    choices: [
      { label: "feature >= threshold", outcome: "true" },
      { label: "feature < threshold", outcome: "false" }
    ],
    trueLabel: "Go right",
    falseLabel: "Go left"
  }
]);

const buildConfusionMatrix = () => ([
  {
    type: "visual_table",
    title: "Confusion matrix",
    columns: ["", "Pred +", "Pred -"],
    data: [
      { "": "Actual +", "Pred +": 42, "Pred -": 8 },
      { "": "Actual -", "Pred +": 5, "Pred -": 45 }
    ],
    allowSort: false,
    allowFilter: false
  },
  {
    type: "variable_slider",
    name: "threshold",
    min: 0,
    max: 1,
    initial: 0.5,
    label: "Threshold"
  }
]);

const buildThresholdTradeoff = () => ([
  {
    type: "variable_slider",
    name: "threshold",
    min: 0,
    max: 1,
    initial: 0.5,
    label: "Threshold"
  },
  { type: "state_inspector", title: "Metrics", showTypes: true }
]);

const buildMultiStage = (lesson) => ([
  ...buildMemoryMachine(lesson),
  ...buildLoopSimulator(lesson, "Checkpoint loop"),
  ...buildPathExplorer(lesson)
]);

const selectArchetype = (lesson) => {
  const title = lesson.title || "";
  const t = title.toLowerCase();
  const code = lesson.starter_code || "";
  const lib = detectLibrary(code);
  const tags = lesson.concept_tags || [];

  if (lib === "pandas") {
    if (t.includes("merge") || t.includes("join")) return "join";
    if (t.includes("group") || t.includes("pivot")) return "aggregate";
    if (t.includes("missing") || t.includes("fill") || t.includes("imputation")) return "missing";
    if (t.includes("duplicate") || t.includes("dedup")) return "dedup";
    if (t.includes("string") || t.includes("regex")) return "regex";
    return "transform";
  }
  if (lib === "numpy") {
    if (t.includes("where")) return "array_condition";
    if (t.includes("broadcast")) return "broadcast";
    if (t.includes("mean") || t.includes("median") || t.includes("variance") || t.includes("std") || t.includes("percentile") || t.includes("correlation") || t.includes("covariance") || t.includes("z-score")) {
      return "distribution";
    }
    return "array_grid";
  }
  if (lib === "matplotlib") return "chart";
  if (lib === "sklearn") {
    if (t.includes("decision tree")) return "decision_tree";
    if (t.includes("confusion")) return "confusion";
    if (t.includes("precision") || t.includes("recall")) return "threshold";
    return "pipeline";
  }
  if (lib === "files") return "file";
  if (lib === "regex") return "regex";

  if (t.includes("boss") || t.includes("challenge")) return "multi";
  if (tags.includes("strings") || t.includes("string") || t.includes("format")) return "string";
  if (tags.includes("booleans") || t.includes("truthy") || t.includes("falsy")) return "truthy";
  if (tags.includes("conditionals") || t.includes("if") || t.includes("decision") || t.includes("grade") || t.includes("categories")) return "path";
  if (t.includes("comparison") || t.includes("logical") || t.includes("ternary") || t.includes("operator")) return "expression";
  if (t.includes("range")) return "range";
  if (tags.includes("loops") || t.includes("loop") || t.includes("countdown") || t.includes("accumul")) return "loop";
  if (t.includes("break") || t.includes("continue")) return "control_flow";
  if (tags.includes("functions") || t.includes("function") || t.includes("lambda") || t.includes("scope") || t.includes("recursive")) return "callstack";
  if (tags.includes("lists") || tags.includes("dictionaries") || tags.includes("sets") || tags.includes("tuples") || t.includes("list") || t.includes("dict") || t.includes("tuple") || t.includes("set") || t.includes("slice")) return "container";
  if (t.includes("search") || t.includes("sort") || t.includes("two sum") || t.includes("fibonacci")) return "algorithm";
  if (t.includes("random")) return "random";
  if (t.includes("datetime") || t.includes("time")) return "timeline";
  if (t.includes("import") || t.includes("module") || t.includes("itertools") || t.includes("functools") || t.includes("os path")) return "import";
  return "memory";
};

const buildPlan = (lesson) => {
  const archetype = selectArchetype(lesson);
  switch (archetype) {
    case "string": return { recipe: "py_string_workbench", plan: buildStringWorkbench(lesson) };
    case "truthy": return { recipe: "py_truthiness", plan: buildTruthiness(lesson) };
    case "expression": return { recipe: "py_expression_trace", plan: buildExpressionTrace(lesson) };
    case "path": return { recipe: "py_path_explorer", plan: buildPathExplorer(lesson) };
    case "range": return { recipe: "py_range", plan: buildLoopSimulator(lesson, "range preview") };
    case "loop": return { recipe: "py_loop_sim", plan: buildLoopSimulator(lesson, lesson.title) };
    case "control_flow": return { recipe: "py_control_flow", plan: buildControlFlowTimeline(lesson) };
    case "callstack": return { recipe: "py_call_stack", plan: buildCallStack(lesson) };
    case "container": return { recipe: "py_container", plan: buildContainerManipulator(lesson) };
    case "algorithm": return { recipe: "py_algorithm", plan: buildAlgorithmWorkbench(lesson) };
    case "import": return { recipe: "py_import", plan: buildImportMap(lesson) };
    case "random": return { recipe: "py_random", plan: buildRandomnessLab(lesson) };
    case "timeline": return { recipe: "py_timeline", plan: buildTimelineManipulator(lesson) };
    case "regex": return { recipe: "py_regex", plan: buildRegexLab(lesson) };
    case "file": return { recipe: "py_file", plan: buildFileSandbox(lesson) };
    case "transform": return { recipe: "py_transform", plan: buildDataTransform(lesson) };
    case "aggregate": return { recipe: "py_aggregate", plan: buildAggregation(lesson) };
    case "join": return { recipe: "py_join", plan: buildJoin(lesson) };
    case "missing": return { recipe: "py_missing", plan: buildDataTransform(lesson) };
    case "dedup": return { recipe: "py_dedup", plan: buildDedup(lesson) };
    case "array_grid": return { recipe: "py_array", plan: buildArrayGrid(lesson) };
    case "array_condition": return { recipe: "py_array_condition", plan: buildArrayCondition(lesson) };
    case "broadcast": return { recipe: "py_broadcast", plan: buildBroadcasting(lesson) };
    case "chart": return { recipe: "py_chart", plan: buildChartBuilder(lesson) };
    case "distribution": return { recipe: "py_distribution", plan: buildDistribution(lesson) };
    case "pipeline": return { recipe: "py_pipeline", plan: buildPipeline(lesson) };
    case "decision_tree": return { recipe: "py_tree", plan: buildDecisionTree(lesson) };
    case "confusion": return { recipe: "py_confusion", plan: buildConfusionMatrix(lesson) };
    case "threshold": return { recipe: "py_threshold", plan: buildThresholdTradeoff(lesson) };
    case "multi": return { recipe: "py_multi_stage", plan: buildMultiStage(lesson) };
    case "memory":
    default:
      return { recipe: "py_memory", plan: buildMemoryMachine(lesson) };
  }
};

const pythonIds = getLessonIds();
const updated = [];

pythonIds.forEach((id) => {
  const lesson = lessons[String(id)];
  if (!lesson) return;
  const { recipe, plan } = buildPlan(lesson);
  lesson.interaction_recipe_id = recipe;
  lesson.interaction_plan = plan;
  lesson.interaction_required = true;
  if (lesson.send_to_editor_template) {
    delete lesson.send_to_editor_template;
  }
  updated.push(id);
});

fs.writeFileSync(lessonsPath, JSON.stringify(lessons, null, 2));
// eslint-disable-next-line no-console
console.log(`Updated Python lessons: ${updated.length}`);
