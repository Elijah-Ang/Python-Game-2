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

const BATCH_ID = 'B2-FP';

// Lesson 3: Reassigning Variables
updateLesson(3, (lesson) => {
  appendSection(
    lesson,
    '## Watch reassignment happen',
    `## Watch reassignment happen
Reassigning updates the **same** memory slot with a new value.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'memory_machine',
      title: 'Reassign the same variable',
      slots: ['score'],
      steps: [
        { label: 'score = 0', slot: 'score', value: 0 },
        { label: 'score = 100', slot: 'score', value: 100 }
      ]
    },
    {
      type: 'output_diff',
      title: 'Final score after reassignment',
      expected: '100',
      actualVar: 'score'
    }
  ]);
  ensureGapIds(lesson, [BATCH_ID]);
});

// Lesson 11: Compound Assignment
updateLesson(11, (lesson) => {
  appendSection(
    lesson,
    '## In-place updates',
    `## In-place updates
\`score = score + 1\` and \`score += 1\` both update the **same memory cell**.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'memory_machine',
      title: 'Compound assignment updates in place',
      slots: ['score'],
      steps: [
        { label: 'score = 5', slot: 'score', value: 5 },
        { label: 'score = score + 1', slot: 'score', value: 6 },
        { label: 'score += 1', slot: 'score', value: 7 }
      ]
    },
    {
      type: 'output_diff',
      title: 'Final score after two updates',
      expected: '7',
      actualVar: 'score'
    }
  ]);
  ensureGapIds(lesson, [BATCH_ID]);
});

// Lesson 16: Using range()
updateLesson(16, (lesson) => {
  appendSection(
    lesson,
    '## Start, stop, step',
    `## Start, stop, step
\`range(start, stop, step)\` generates a sequence that **stops before** the stop value.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'step_executor',
      code: 'for i in range(2, 7, 2):\\n    print(i)',
      steps: [
        { line: 1, description: 'First value from range', stateChanges: { i: 2 } },
        { line: 2, description: 'Print 2' },
        { line: 1, description: 'Next value', stateChanges: { i: 4 } },
        { line: 2, description: 'Print 4' },
        { line: 1, description: 'Next value', stateChanges: { i: 6 } },
        { line: 2, description: 'Print 6' }
      ]
    },
    {
      type: 'state_inspector',
      title: 'Current i',
      filter: ['i'],
      showTypes: true
    },
    {
      type: 'output_diff',
      title: 'Last value produced by range(2, 7, 2)',
      expected: '6',
      actualVar: 'i'
    }
  ]);
  ensureGapIds(lesson, [BATCH_ID]);
});

// Lesson 22: If Statements
updateLesson(22, (lesson) => {
  appendSection(
    lesson,
    '## Choose the true path',
    `## Choose the true path
Pick the input that makes the condition evaluate to **True**.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'conditional_path',
      prompt: 'Condition: age >= 21',
      choices: [
        { label: 'age = 25', outcome: 'true' },
        { label: 'age = 17', outcome: 'false' }
      ],
      trueLabel: 'Welcome!',
      falseLabel: 'Access denied',
      resultVar: 'if_result'
    },
    {
      type: 'output_diff',
      title: 'Did you choose a True case?',
      expected: 'true',
      actualVar: 'if_result'
    }
  ]);
  ensureGapIds(lesson, [BATCH_ID]);
});

// Lesson 32: Function Parameters
updateLesson(32, (lesson) => {
  appendSection(
    lesson,
    '## Parameters in action',
    `## Parameters in action
Arguments flow into parameters, then the function returns a result.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'step_executor',
      code: 'def add(a, b):\\n    total = a + b\\n    return total\\n\\nresult = add(2, 5)',
      steps: [
        { line: 1, description: 'Define add(a, b)' },
        { line: 5, description: 'Call add(2, 5)', stateChanges: { a: 2, b: 5 } },
        { line: 2, description: 'Compute total', stateChanges: { total: 7 } },
        { line: 3, description: 'Return total', stateChanges: { result: 7 } }
      ]
    },
    {
      type: 'state_inspector',
      title: 'Parameters and result',
      filter: ['a', 'b', 'total', 'result'],
      showTypes: true
    },
    {
      type: 'output_diff',
      title: 'Result of add(2, 5)',
      expected: '7',
      actualVar: 'result'
    }
  ]);
  ensureGapIds(lesson, [BATCH_ID]);
});

// Lesson 175: Nested Lookup
updateLesson(175, (lesson) => {
  appendSection(
    lesson,
    '## Trace the lookup',
    `## Trace the lookup
Access each layer one step at a time to avoid mistakes.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'step_executor',
      code: 'user = {\"profile\": {\"settings\": {\"theme\": \"dark\"}}}\\nprofile = user[\"profile\"]\\nsettings = profile[\"settings\"]\\ntheme = settings[\"theme\"]',
      steps: [
        { line: 1, description: 'Create nested data', stateChanges: { user: { profile: { settings: { theme: 'dark' } } } } },
        { line: 2, description: 'Grab profile', stateChanges: { profile: { settings: { theme: 'dark' } } } },
        { line: 3, description: 'Grab settings', stateChanges: { settings: { theme: 'dark' } } },
        { line: 4, description: 'Read theme', stateChanges: { theme: 'dark' } }
      ]
    },
    {
      type: 'state_inspector',
      title: 'Lookup trail',
      filter: ['profile', 'settings', 'theme'],
      showTypes: true
    },
    {
      type: 'output_diff',
      title: 'Final theme value',
      expected: 'dark',
      actualVar: 'theme'
    }
  ]);
  ensureGapIds(lesson, [BATCH_ID]);
});

// Lesson 98: Range (statistics)
updateLesson(98, (lesson) => {
  appendSection(
    lesson,
    '## Outliers change the range',
    `## Outliers change the range
Pick the dataset with the **larger** range (the one with the outlier).`
  );
  setInteractionPlan(lesson, [
    {
      type: 'data_transform',
      title: 'Range with and without an outlier',
      columns: ['value'],
      beforeRows: [
        { value: 10 },
        { value: 15 },
        { value: 20 },
        { value: 25 },
        { value: 30 }
      ],
      filters: [
        {
          id: 'base',
          label: 'Base data',
          rows: [
            { value: 10 },
            { value: 15 },
            { value: 20 },
            { value: 25 },
            { value: 30 }
          ]
        },
        {
          id: 'outlier',
          label: 'With outlier',
          rows: [
            { value: 10 },
            { value: 15 },
            { value: 20 },
            { value: 25 },
            { value: 30 },
            { value: 100 }
          ]
        }
      ],
      resultVar: 'range_rows'
    },
    {
      type: 'output_diff',
      title: 'Select the larger-range dataset (row count)',
      expected: '6',
      actualVar: 'range_rows'
    }
  ]);
  ensureGapIds(lesson, [BATCH_ID]);
});

// Lesson 140: Duplicates in Specific Columns
updateLesson(140, (lesson) => {
  appendSection(
    lesson,
    '## Dedupe by subset',
    `## Dedupe by subset
When you dedupe on \`email\`, rows with the same email collapse into one.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'data_transform',
      title: 'Duplicates by email',
      columns: ['email', 'city'],
      beforeRows: [
        { email: 'ava@site.com', city: 'Boston' },
        { email: 'ava@site.com', city: 'Austin' },
        { email: 'kai@site.com', city: 'Denver' },
        { email: 'min@site.com', city: 'Denver' },
        { email: 'kai@site.com', city: 'Boulder' }
      ],
      filters: [
        {
          id: 'all_rows',
          label: 'All rows',
          rows: [
            { email: 'ava@site.com', city: 'Boston' },
            { email: 'ava@site.com', city: 'Austin' },
            { email: 'kai@site.com', city: 'Denver' },
            { email: 'min@site.com', city: 'Denver' },
            { email: 'kai@site.com', city: 'Boulder' }
          ]
        },
        {
          id: 'by_email',
          label: 'Deduped by email',
          rows: [
            { email: 'ava@site.com', city: 'Boston' },
            { email: 'kai@site.com', city: 'Denver' },
            { email: 'min@site.com', city: 'Denver' }
          ]
        }
      ],
      resultVar: 'unique_rows'
    },
    {
      type: 'output_diff',
      title: 'Unique customers after dedupe',
      expected: '3',
      actualVar: 'unique_rows'
    }
  ]);
  ensureGapIds(lesson, [BATCH_ID]);
});

// Lesson 194: Conditional Replace
updateLesson(194, (lesson) => {
  appendSection(
    lesson,
    '## See what changes',
    `## See what changes
Focus on the values that actually change when the condition matches.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'data_transform',
      title: 'Values replaced by np.where',
      columns: ['value'],
      beforeRows: [
        { value: 1 },
        { value: -2 },
        { value: 3 },
        { value: -4 },
        { value: 5 }
      ],
      filters: [
        {
          id: 'original',
          label: 'Original values',
          rows: [
            { value: 1 },
            { value: -2 },
            { value: 3 },
            { value: -4 },
            { value: 5 }
          ]
        },
        {
          id: 'replaced_only',
          label: 'Replaced values only',
          rows: [
            { value: 0 },
            { value: 0 }
          ]
        }
      ],
      resultVar: 'replaced_count'
    },
    {
      type: 'output_diff',
      title: 'How many values were replaced?',
      expected: '2',
      actualVar: 'replaced_count'
    }
  ]);
  ensureGapIds(lesson, [BATCH_ID]);
});

// Lesson 204: Data Reshaping
updateLesson(204, (lesson) => {
  appendSection(
    lesson,
    '## Wide vs long shape',
    `## Wide vs long shape
The long format has **more rows** because each subject becomes its own row.`
  );
  setInteractionPlan(lesson, [
    {
      type: 'data_transform',
      title: 'Wide to long reshape',
      columns: ['student', 'subject', 'score'],
      beforeRows: [
        { student: 'Alice', subject: 'Math', score: 90 },
        { student: 'Alice', subject: 'Science', score: 85 },
        { student: 'Alice', subject: 'English', score: 92 },
        { student: 'Bob', subject: 'Math', score: 78 },
        { student: 'Bob', subject: 'Science', score: 82 },
        { student: 'Bob', subject: 'English', score: 88 }
      ],
      filters: [
        {
          id: 'wide',
          label: 'Wide format (2 rows)',
          rows: [
            { student: 'Alice', subject: 'Math, Science, English', score: '90, 85, 92' },
            { student: 'Bob', subject: 'Math, Science, English', score: '78, 82, 88' }
          ]
        },
        {
          id: 'long',
          label: 'Long format (6 rows)',
          rows: [
            { student: 'Alice', subject: 'Math', score: 90 },
            { student: 'Alice', subject: 'Science', score: 85 },
            { student: 'Alice', subject: 'English', score: 92 },
            { student: 'Bob', subject: 'Math', score: 78 },
            { student: 'Bob', subject: 'Science', score: 82 },
            { student: 'Bob', subject: 'English', score: 88 }
          ]
        }
      ],
      resultVar: 'shape_rows'
    },
    {
      type: 'output_diff',
      title: 'Select the long format (row count)',
      expected: '6',
      actualVar: 'shape_rows'
    }
  ]);
  ensureGapIds(lesson, [BATCH_ID]);
});

fs.writeFileSync(lessonsPath, JSON.stringify(lessons, null, 2));
console.log('Batch 2 applied to lessons.json');
