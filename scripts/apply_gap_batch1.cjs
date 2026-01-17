const fs = require('fs');
const path = require('path');

const lessonsPath = path.resolve(__dirname, '../frontend/public/data/lessons.json');
const lessons = JSON.parse(fs.readFileSync(lessonsPath, 'utf8'));

const ensureGapIds = (lesson, gapIds) => {
  const existing = Array.isArray(lesson.gap_ids) ? lesson.gap_ids : [];
  lesson.gap_ids = Array.from(new Set([...existing, ...gapIds]));
};

const appendSection = (lesson, marker, block) => {
  if (!lesson.content || lesson.content.includes(marker)) {
    return;
  }
  lesson.content = `${lesson.content.trim()}\n\n${block.trim()}\n`;
};

const setInteractionPlan = (lesson, plan) => {
  lesson.interaction_plan = plan;
};

const updateLesson = (id, updater) => {
  const lesson = lessons[String(id)];
  if (!lesson) {
    throw new Error(`Missing lesson ${id}`);
  }
  updater(lesson);
};

// Forward reference for casting exceptions (approved note)
['12', '149'].forEach((id) => {
  updateLesson(id, (lesson) => {
    appendSection(
      lesson,
      '## Cast failures',
      `## Cast failures
If a cast fails, Python raises a \`ValueError\`. We handle those safely later in **Error Handling**.`
    );
  });
});

// PY-009 Variable Names -> lesson 2
updateLesson(2, (lesson) => {
  appendSection(
    lesson,
    '## Naming pitfalls',
    `## Naming pitfalls
Variable names must start with a letter or underscore. Numbers can appear later, but not first.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'debug_quest',
      title: 'Fix the invalid variable name',
      snippet: '2nd_place = 4\\nscore_total = 20\\nteam = \"Lions\"',
      bugLine: 1,
      options: [
        {
          label: 'Rename to second_place',
          fix: 'second_place = 4',
          correct: true
        },
        {
          label: 'Put the name in quotes',
          fix: '\"2nd_place\" = 4',
          correct: false
        },
        {
          label: 'Use a dash: second-place',
          fix: 'second-place = 4',
          correct: false
        }
      ]
    }
  ]);
  ensureGapIds(lesson, ['PY-009']);
});

// PY-075 Shorthand If -> lesson 30
updateLesson(30, (lesson) => {
  appendSection(
    lesson,
    '## Shorthand if',
    `## Shorthand if
Ternary syntax keeps simple branches compact:

\`\`\`python
label = "pass" if score >= 70 else "retry"
\`\`\``
  );
  setInteractionPlan(lesson, [
    {
      type: 'conditional_path',
      prompt: 'Evaluate the ternary: label = "pass" if score >= 70 else "retry"',
      choices: [
        { label: 'score = 72', outcome: 'true' },
        { label: 'score = 65', outcome: 'false' }
      ],
      trueLabel: 'label = "pass"',
      falseLabel: 'label = "retry"',
      resultVar: 'ternary_result'
    }
  ]);
  ensureGapIds(lesson, ['PY-075']);
});

// PY-076 Nested If -> lesson 29
updateLesson(29, (lesson) => {
  appendSection(
    lesson,
    '## Trace a nested decision',
    `## Trace a nested decision
Nested checks let you apply a second rule only after the first one passes.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'step_executor',
      code: 'age = 20\\nmember = True\\nprice = 12\\n\\nif age < 18:\\n    price = 6\\nelse:\\n    if member:\\n        price = 8',
      steps: [
        { line: 1, description: 'Set age', stateChanges: { age: 20 } },
        { line: 2, description: 'Set member', stateChanges: { member: true } },
        { line: 3, description: 'Set base price', stateChanges: { price: 12 } },
        { line: 5, description: 'age < 18 is false → go to else' },
        { line: 8, description: 'member is true → apply discount', stateChanges: { price: 8 } }
      ]
    },
    {
      type: 'state_inspector',
      title: 'State after each step',
      filter: ['age', 'member', 'price'],
      showTypes: true
    }
  ]);
  ensureGapIds(lesson, ['PY-076']);
});

// PY-010 Assign Multiple Values -> lesson 4
updateLesson(4, (lesson) => {
  appendSection(
    lesson,
    '## Multiple assignment and swap',
    `## Multiple assignment and swap
Python can assign multiple variables at once and swap values without a temp variable.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'memory_machine',
      title: 'Parallel assignment in action',
      slots: ['x', 'y'],
      steps: [
        { label: 'x, y = 3, 7 → x gets 3', slot: 'x', value: 3 },
        { label: 'x, y = 3, 7 → y gets 7', slot: 'y', value: 7 },
        { label: 'x, y = y, x → x becomes 7', slot: 'x', value: 7 },
        { label: 'x, y = y, x → y becomes 3', slot: 'y', value: 3 }
      ]
    }
  ]);
  ensureGapIds(lesson, ['PY-010']);
});

// PY-012 Global Variables -> lesson 39
updateLesson(39, (lesson) => {
  appendSection(
    lesson,
    '## Global vs local',
    `## Global vs local
Local variables live inside a function. Use \`global\` only when you truly intend to modify outer state.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'step_executor',
      code: 'count = 0\\n\\ndef bump_local():\\n    count = 1\\n    return count\\n\\ndef bump_global():\\n    global count\\n    count = count + 1\\n    return count\\n\\nlocal_result = bump_local()\\nglobal_result = bump_global()',
      steps: [
        { line: 1, description: 'Initialize global count', stateChanges: { count: 0 } },
        { line: 12, description: 'Call bump_local (global stays the same)', stateChanges: { local_result: 1 } },
        { line: 13, description: 'Call bump_global (global updates)', stateChanges: { count: 1, global_result: 1 } }
      ]
    },
    {
      type: 'state_inspector',
      title: 'Scope snapshot',
      filter: ['count', 'local_result', 'global_result'],
      showTypes: true
    }
  ]);
  ensureGapIds(lesson, ['PY-012']);
});

// PY-100 String Formatting -> lesson 7
updateLesson(7, (lesson) => {
  appendSection(
    lesson,
    '## Formatting with f-strings',
    `## Formatting with f-strings
Use f-strings to embed variables directly inside text.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'live_code_block',
      initialCode: 'name = \"Ava\"\\nscore = 92\\nprint(f\"{name} {score}\")',
      language: 'python',
      highlightLine: 3,
      variableName: 'format_output'
    },
    {
      type: 'output_diff',
      title: 'Match the formatted output',
      expected: 'Ava scored 92 points',
      actualVar: 'format_output'
    }
  ]);
  ensureGapIds(lesson, ['PY-100']);
});

// PY-079 While Loops -> lesson 19
updateLesson(19, (lesson) => {
  appendSection(
    lesson,
    '## While loop rhythm',
    `## While loop rhythm
Each iteration updates the loop variable until the condition becomes false.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'loop_simulator',
      label: 'Count upward with a while loop',
      iterations: 4,
      startValue: 1,
      stepValue: 1,
      valueVar: 'n',
      stepVar: 'step'
    },
    {
      type: 'state_inspector',
      title: 'Loop state',
      filter: ['n', 'step'],
      showTypes: true
    }
  ]);
  ensureGapIds(lesson, ['PY-079']);
});

// PY-080 For Loops -> lesson 13
updateLesson(13, (lesson) => {
  appendSection(
    lesson,
    '## Trace a for-loop',
    `## Trace a for-loop
Watch how \`i\` and \`total\` change on each iteration.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'step_executor',
      code: 'total = 0\\nfor i in range(1, 4):\\n    total += i',
      steps: [
        { line: 1, description: 'Initialize total', stateChanges: { total: 0 } },
        { line: 2, description: 'First loop value', stateChanges: { i: 1 } },
        { line: 3, description: 'Add i to total', stateChanges: { total: 1 } },
        { line: 2, description: 'Next loop value', stateChanges: { i: 2 } },
        { line: 3, description: 'Add i to total', stateChanges: { total: 3 } },
        { line: 2, description: 'Next loop value', stateChanges: { i: 3 } },
        { line: 3, description: 'Add i to total', stateChanges: { total: 6 } }
      ]
    },
    {
      type: 'state_inspector',
      title: 'Loop variables',
      filter: ['i', 'total'],
      showTypes: true
    }
  ]);
  ensureGapIds(lesson, ['PY-080']);
});

// PY-192 Built-in Functions -> lesson 31
updateLesson(31, (lesson) => {
  appendSection(
    lesson,
    '## Built-ins vs your functions',
    `## Built-ins vs your functions
Built-in functions (like \`len\`) already exist. Your functions are the ones you define with \`def\`.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'step_executor',
      code: 'def square(x):\\n    return x * x\\n\\nnums = [2, 3, 4]\\nlength = len(nums)\\ncustom = square(3)',
      steps: [
        { line: 1, description: 'Define a custom function (no output yet)' },
        { line: 4, description: 'Create a list', stateChanges: { nums: [2, 3, 4] } },
        { line: 5, description: 'Call built-in len()', stateChanges: { length: 3 } },
        { line: 6, description: 'Call your square() function', stateChanges: { custom: 9 } }
      ]
    },
    {
      type: 'state_inspector',
      title: 'Built-in vs custom results',
      filter: ['nums', 'length', 'custom'],
      showTypes: true
    }
  ]);
  ensureGapIds(lesson, ['PY-192']);
});

// SQL-004 DISTINCT -> lesson 1010
updateLesson(1010, (lesson) => {
  appendSection(
    lesson,
    '## DISTINCT for unique values',
    `## DISTINCT for unique values
DISTINCT removes duplicate rows in the result set.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'data_transform',
      title: 'SELECT vs SELECT DISTINCT',
      columns: ['department'],
      beforeRows: [
        { department: 'Sales' },
        { department: 'Sales' },
        { department: 'Support' },
        { department: 'Engineering' },
        { department: 'Support' }
      ],
      filters: [
        {
          id: 'all_rows',
          label: 'SELECT department',
          rows: [
            { department: 'Sales' },
            { department: 'Sales' },
            { department: 'Support' },
            { department: 'Engineering' },
            { department: 'Support' }
          ]
        },
        {
          id: 'distinct_rows',
          label: 'SELECT DISTINCT department',
          rows: [
            { department: 'Sales' },
            { department: 'Support' },
            { department: 'Engineering' }
          ]
        }
      ],
      resultVar: 'dept_rows'
    },
    {
      type: 'output_diff',
      title: 'Match the DISTINCT row count',
      expected: '3',
      actualVar: 'dept_rows'
    }
  ]);
  ensureGapIds(lesson, ['SQL-004']);
});

// SQL-014 SELECT TOP -> lesson 1015
updateLesson(1015, (lesson) => {
  appendSection(
    lesson,
    '## TOP vs LIMIT',
    `## TOP vs LIMIT
Different SQL dialects use \`TOP\` or \`LIMIT\` to keep only the first N rows.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'data_transform',
      title: 'Limit the result set',
      columns: ['order_id', 'total'],
      beforeRows: [
        { order_id: 101, total: 120 },
        { order_id: 102, total: 90 },
        { order_id: 103, total: 210 },
        { order_id: 104, total: 45 },
        { order_id: 105, total: 175 }
      ],
      filters: [
        {
          id: 'no_limit',
          label: 'No LIMIT',
          rows: [
            { order_id: 101, total: 120 },
            { order_id: 102, total: 90 },
            { order_id: 103, total: 210 },
            { order_id: 104, total: 45 },
            { order_id: 105, total: 175 }
          ]
        },
        {
          id: 'limit_three',
          label: 'LIMIT 3',
          rows: [
            { order_id: 101, total: 120 },
            { order_id: 102, total: 90 },
            { order_id: 103, total: 210 }
          ]
        }
      ],
      resultVar: 'limited_rows'
    },
    {
      type: 'output_diff',
      title: 'Match the LIMIT row count',
      expected: '3',
      actualVar: 'limited_rows'
    }
  ]);
  ensureGapIds(lesson, ['SQL-014']);
});

// SQL-037 SELECT INTO / CTAS -> lesson 1134
updateLesson(1134, (lesson) => {
  appendSection(
    lesson,
    '## SELECT INTO / CTAS',
    `## SELECT INTO / CTAS
These patterns create a **new table** from a query result. This changes schema, not just rows.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'data_transform',
      title: 'Schema before and after table creation',
      columns: ['table', 'rows'],
      beforeRows: [
        { table: 'customers', rows: 200 },
        { table: 'orders', rows: 500 }
      ],
      filters: [
        {
          id: 'select_into',
          label: 'After SELECT INTO vip_customers',
          rows: [
            { table: 'customers', rows: 200 },
            { table: 'orders', rows: 500 },
            { table: 'vip_customers', rows: 20 }
          ]
        }
      ],
      resultVar: 'table_count'
    },
    {
      type: 'output_diff',
      title: 'How many tables now exist?',
      expected: '3',
      actualVar: 'table_count'
    }
  ]);
  ensureGapIds(lesson, ['SQL-037']);
});

// SQL-015 Aggregate Functions -> lesson 1034
updateLesson(1034, (lesson) => {
  appendSection(
    lesson,
    '## Other aggregates',
    `## Other aggregates
COUNT, SUM, AVG, MIN, and MAX summarize groups of rows into a single value.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'step_executor',
      code: '-- amounts = [10, 20, 30]\\ncount = 3\\nsum = 60\\navg = 20\\nmin = 10\\nmax = 30',
      steps: [
        { line: 1, description: 'Start with three amounts' },
        { line: 2, description: 'COUNT rows', stateChanges: { count: 3 } },
        { line: 3, description: 'SUM values', stateChanges: { sum: 60 } },
        { line: 4, description: 'AVG values', stateChanges: { avg: 20 } },
        { line: 5, description: 'MIN value', stateChanges: { min: 10 } },
        { line: 6, description: 'MAX value', stateChanges: { max: 30 } }
      ]
    },
    {
      type: 'state_inspector',
      title: 'Aggregate results',
      filter: ['count', 'sum', 'avg', 'min', 'max'],
      showTypes: true
    }
  ]);
  ensureGapIds(lesson, ['SQL-015']);
});

// SQL-029 Full Join -> lesson 1049
updateLesson(1049, (lesson) => {
  appendSection(
    lesson,
    '## Full join intuition',
    `## Full join intuition
FULL OUTER JOIN keeps **all** rows from both sides, matching where it can.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'join_visualizer',
      leftTitle: 'Employees',
      rightTitle: 'Badges',
      leftRows: [
        { emp_id: 1, name: 'Ava' },
        { emp_id: 2, name: 'Kai' },
        { emp_id: 4, name: 'Mina' }
      ],
      rightRows: [
        { badge_id: 'B1', emp_id: 1 },
        { badge_id: 'B2', emp_id: 3 }
      ],
      leftKey: 'emp_id',
      rightKey: 'emp_id',
      joinTypes: ['INNER', 'LEFT', 'FULL'],
      resultVar: 'join_rows'
    }
  ]);
  ensureGapIds(lesson, ['SQL-029']);
});

// SQL-064 ADD CONSTRAINT -> lesson 1237
updateLesson(1237, (lesson) => {
  appendSection(
    lesson,
    '## Add a constraint',
    `## Add a constraint
Constraints reject rows that violate rules (like missing required values).`
  );
  appendSection(
    lesson,
    '## Drop a constraint',
    `## Drop a constraint
Dropping a constraint removes the rule, which can allow previously invalid rows.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'data_transform',
      title: 'NOT NULL constraint on email',
      columns: ['user_id', 'email'],
      beforeRows: [
        { user_id: 1, email: 'ava@example.com' },
        { user_id: 2, email: null },
        { user_id: 3, email: 'kai@example.com' }
      ],
      filters: [
        {
          id: 'no_constraint',
          label: 'No constraint',
          rows: [
            { user_id: 1, email: 'ava@example.com' },
            { user_id: 2, email: null },
            { user_id: 3, email: 'kai@example.com' }
          ]
        },
        {
          id: 'not_null',
          label: 'ADD CONSTRAINT email NOT NULL',
          rows: [
            { user_id: 1, email: 'ava@example.com' },
            { user_id: 3, email: 'kai@example.com' }
          ]
        }
      ],
      resultVar: 'valid_rows'
    },
    {
      type: 'step_executor',
      code: 'ALTER TABLE users DROP CONSTRAINT users_email_key;',
      steps: [
        { line: 1, description: 'Drop the email constraint', stateChanges: { constraints: ['users_pkey'] } }
      ]
    },
    {
      type: 'state_inspector',
      title: 'Constraints on users',
      filter: ['constraints'],
      showTypes: true
    }
  ]);
  ensureGapIds(lesson, ['SQL-064', 'SQL-086']);
});

// SQL-076/079/089 Index operations -> lesson 1238
updateLesson(1238, (lesson) => {
  appendSection(
    lesson,
    '## Create, unique, and drop indexes',
    `## Create, unique, and drop indexes
Indexes speed reads. Unique indexes also enforce uniqueness.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'step_executor',
      code: 'CREATE INDEX idx_orders_date ON orders(order_date);\\nCREATE UNIQUE INDEX idx_orders_code ON orders(order_code);\\nDROP INDEX idx_orders_date;',
      steps: [
        { line: 1, description: 'Create a regular index', stateChanges: { indexes: ['idx_orders_date'] } },
        { line: 2, description: 'Create a unique index', stateChanges: { indexes: ['idx_orders_date', 'idx_orders_code'] } },
        { line: 3, description: 'Drop the first index', stateChanges: { indexes: ['idx_orders_code'] } }
      ]
    },
    {
      type: 'state_inspector',
      title: 'Indexes on orders',
      filter: ['indexes'],
      showTypes: true
    }
  ]);
  ensureGapIds(lesson, ['SQL-076', 'SQL-079', 'SQL-089']);
});

// SQL-077 Create or replace view -> lesson 1144
updateLesson(1144, (lesson) => {
  appendSection(
    lesson,
    '## Replace a view safely',
    `## Replace a view safely
CREATE OR REPLACE VIEW updates a view definition without dropping it first.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'step_executor',
      code: 'CREATE VIEW active_customers AS ...\\nCREATE OR REPLACE VIEW active_customers AS ...',
      steps: [
        { line: 1, description: 'Create the view', stateChanges: { views: ['active_customers:v1'] } },
        { line: 2, description: 'Replace the view definition', stateChanges: { views: ['active_customers:v2'] } }
      ]
    },
    {
      type: 'state_inspector',
      title: 'Views',
      filter: ['views'],
      showTypes: true
    }
  ]);
  ensureGapIds(lesson, ['SQL-077']);
});

fs.writeFileSync(lessonsPath, JSON.stringify(lessons, null, 2));
console.log('Batch 1 applied to lessons.json');
