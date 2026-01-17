const fs = require('fs');
const path = require('path');

const lessonsPath = path.resolve(__dirname, '../frontend/public/data/lessons.json');
const lessons = JSON.parse(fs.readFileSync(lessonsPath, 'utf8'));

const ensureGapIds = (lesson, gapIds) => {
  const existing = Array.isArray(lesson.gap_ids) ? lesson.gap_ids : [];
  const merged = Array.from(new Set([...existing, ...gapIds]));
  lesson.gap_ids = merged;
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

updateLesson(1, (lesson) => {
  appendSection(
    lesson,
    '## Syntax essentials (micro)',
    `## Syntax essentials (micro)
Python uses **indentation** to show code blocks. A line ending with \`:\` opens a block, and the next line must be indented by **4 spaces**.

## Output essentials (micro)
\`print()\` shows output. Each call ends with a newline, so separate print calls appear on separate lines.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'token_slot',
      template: 'if score > 90{{colon}}\\n{{indent}}print(\"A\")',
      slots: [
        {
          id: 'colon',
          label: 'block opener',
          options: [':', ';'],
          correct: ':'
        },
        {
          id: 'indent',
          label: 'indentation',
          options: ['▸▸▸▸', '▸▸'],
          correct: '▸▸▸▸'
        }
      ]
    },
    {
      type: 'live_code_block',
      initialCode: 'score = 4\\nprint(\"Score:\", score)\\nprint(\"Done\")',
      language: 'python',
      highlightLine: 1,
      variableName: 'print_output'
    },
    {
      type: 'output_diff',
      title: 'Match the output (set score to 7)',
      expected: 'Score: 7\\nDone',
      actualVar: 'print_output'
    }
  ]);
  ensureGapIds(lesson, ['PY-003', 'PY-005']);
});

updateLesson(2, (lesson) => {
  appendSection(
    lesson,
    '## Quick comments',
    `## Quick comments
Use \`#\` for single-line comments. Comments explain **why** something exists, without changing how the code runs.

\`\`\`python
# Explain intent, not the obvious
age = 25  # customer age in years
\`\`\``
  );
  setInteractionPlan(lesson, [
    {
      type: 'token_slot',
      template: '{{comment}} This line explains the variable purpose\\nage = 25',
      slots: [
        {
          id: 'comment',
          label: 'comment marker',
          options: ['#', '//', '--'],
          correct: '#'
        }
      ]
    }
  ]);
  ensureGapIds(lesson, ['PY-007']);
});

updateLesson(9, (lesson) => {
  appendSection(
    lesson,
    '## Print numbers clearly',
    `## Print numbers clearly
Integers and floats print **without quotes**. Use \`print()\` to show numeric values directly or mix them with labels.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'fill_blanks',
      template: 'print({{int_value}})\\nprint({{float_value}})',
      blanks: [
        {
          id: 'int_value',
          options: ['5', '5.0', '\"5\"'],
          correct: '5'
        },
        {
          id: 'float_value',
          options: ['5.0', '5', '\"5\"'],
          correct: '5.0'
        }
      ]
    }
  ]);
  ensureGapIds(lesson, ['PY-006']);
});

updateLesson(10, (lesson) => {
  appendSection(
    lesson,
    '## Operator precedence',
    `## Operator precedence
Multiplication and division happen **before** addition and subtraction. Use parentheses to control the order.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'fill_blanks',
      template: 'result = {{expr}}\\nprint(result)',
      blanks: [
        {
          id: 'expr',
          options: ['3 + 2 * 4', '(3 + 2) * 4'],
          correct: '(3 + 2) * 4'
        }
      ]
    }
  ]);
  ensureGapIds(lesson, ['PY-036']);
});

updateLesson(12, (lesson) => {
  appendSection(
    lesson,
    '## Casting basics',
    `## Casting basics
Use \`int()\`, \`float()\`, and \`str()\` to convert values safely when types do not match.

\`\`\`python
age_text = "42"
age = int(age_text)
price = float("3.5")
label = str(100)
\`\`\`
`
  );
  setInteractionPlan(lesson, [
    {
      type: 'token_slot',
      template: 'age_text = \"42\"\\nage = {{cast1}}(age_text)\\nprice_text = \"3.5\"\\nprice = {{cast2}}(price_text)',
      slots: [
        {
          id: 'cast1',
          label: 'convert to int',
          options: ['int', 'float', 'str'],
          correct: 'int'
        },
        {
          id: 'cast2',
          label: 'convert to float',
          options: ['float', 'int', 'str'],
          correct: 'float'
        }
      ]
    }
  ]);
  ensureGapIds(lesson, ['PY-019']);
});

updateLesson(227, (lesson) => {
  appendSection(
    lesson,
    '## Exception safety',
    `## Exception safety
Catch the **specific** error you expect, and set a safe fallback value so the pipeline keeps moving.

\`\`\`python
try:
    value = int(raw_value)
except ValueError:
    value = 0
\`\`\``
  );
  setInteractionPlan(lesson, [
    {
      type: 'debug_quest',
      title: 'Fix the conversion crash',
      snippet: 'value = \"17a\"\\nnum = int(value)\\nprint(num)',
      bugLine: 2,
      options: [
        {
          label: 'Wrap the conversion in try/except ValueError and fall back to 0',
          fix: 'try:\\n    num = int(value)\\nexcept ValueError:\\n    num = 0',
          correct: true
        },
        {
          label: 'Convert with float() to avoid errors',
          fix: 'num = float(value)',
          correct: false
        },
        {
          label: 'Comment out the conversion line',
          fix: '# num = int(value)',
          correct: false
        }
      ]
    }
  ]);
  ensureGapIds(lesson, ['PY-099', 'PY-195']);
});

updateLesson(1016, (lesson) => {
  appendSection(
    lesson,
    '## OR conditions',
    `## OR conditions
Use \`OR\` to keep rows that match **either** condition.

\`\`\`sql
SELECT *
FROM orders
WHERE status = 'Open' OR priority = 'High';
\`\`\``
  );
  setInteractionPlan(lesson, [
    {
      type: 'data_transform',
      title: 'Compare AND vs OR filters',
      columns: ['order_id', 'status', 'priority'],
      beforeRows: [
        { order_id: 101, status: 'Open', priority: 'Low' },
        { order_id: 102, status: 'Closed', priority: 'High' },
        { order_id: 103, status: 'Open', priority: 'High' },
        { order_id: 104, status: 'Pending', priority: 'Low' },
        { order_id: 105, status: 'Closed', priority: 'Low' },
        { order_id: 106, status: 'Pending', priority: 'High' }
      ],
      filters: [
        {
          id: 'open_only',
          label: "status = 'Open'",
          rows: [
            { order_id: 101, status: 'Open', priority: 'Low' },
            { order_id: 103, status: 'Open', priority: 'High' }
          ]
        },
        {
          id: 'open_or_high',
          label: "status = 'Open' OR priority = 'High'",
          rows: [
            { order_id: 101, status: 'Open', priority: 'Low' },
            { order_id: 102, status: 'Closed', priority: 'High' },
            { order_id: 103, status: 'Open', priority: 'High' },
            { order_id: 106, status: 'Pending', priority: 'High' }
          ]
        }
      ],
      resultVar: 'rows_kept'
    },
    {
      type: 'output_diff',
      title: 'Match the OR result count',
      expected: '4',
      actualVar: 'rows_kept'
    }
  ]);
  ensureGapIds(lesson, ['SQL-008']);
});

updateLesson(1018, (lesson) => {
  appendSection(
    lesson,
    '## IN for multiple values',
    `## IN for multiple values
Use \`IN\` to match **any** value in a list, instead of chaining many \`OR\` checks.

\`\`\`sql
SELECT *
FROM customers
WHERE state IN ('CA', 'NY', 'TX');
\`\`\``
  );
  setInteractionPlan(lesson, [
    {
      type: 'token_slot',
      template: "SELECT *\\nFROM customers\\nWHERE state {{op}} ('CA', 'NY', 'TX');",
      slots: [
        {
          id: 'op',
          label: 'list match',
          options: ['IN', '=', 'LIKE'],
          correct: 'IN'
        }
      ]
    }
  ]);
  ensureGapIds(lesson, ['SQL-022']);
});

updateLesson(1020, (lesson) => {
  appendSection(
    lesson,
    '## Wildcards: % and _',
    `## Wildcards: % and _
\`%\` matches **any length** of text, and \`_\` matches **one character**.

\`\`\`sql
-- starts with "Al"
name LIKE 'Al%'
\`\`\``
  );
  setInteractionPlan(lesson, [
    {
      type: 'fill_blanks',
      template: "name LIKE 'Al{{wild1}}'\\nname LIKE '{{wild2}}y'",
      blanks: [
        {
          id: 'wild1',
          options: ['%', '_'],
          correct: '%'
        },
        {
          id: 'wild2',
          options: ['____', '%'],
          correct: '____'
        }
      ]
    }
  ]);
  ensureGapIds(lesson, ['SQL-021']);
});

fs.writeFileSync(lessonsPath, JSON.stringify(lessons, null, 2));
console.log('Batch 0 applied to lessons.json');
