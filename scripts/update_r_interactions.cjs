const fs = require('fs');
const path = require('path');

const lessonsPath = path.resolve(__dirname, '../frontend/public/data/lessons.json');
const coursePath = path.resolve(__dirname, '../frontend/public/data/course-r-fundamentals.json');
const recommendationsPath = path.resolve(__dirname, '../r_interaction_recommendations.md');

const lessons = JSON.parse(fs.readFileSync(lessonsPath, 'utf8'));
const course = JSON.parse(fs.readFileSync(coursePath, 'utf8'));
const recommendationsText = fs.readFileSync(recommendationsPath, 'utf8');

const slugify = (value) =>
  String(value || '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '');

const parseRecommendations = (text) => {
  const map = new Map();
  text.split('\n').forEach((line) => {
    const trimmed = line.trim();
    if (!trimmed.startsWith('- ')) return;
    const afterDash = trimmed.slice(2);
    const id = afterDash.split(' ')[0];
    if (!/^\d+$/.test(id)) return;
    const boldStart = afterDash.indexOf('**');
    if (boldStart === -1) return;
    const boldEnd = afterDash.indexOf('**', boldStart + 2);
    if (boldEnd === -1) return;
    const archetype = afterDash.slice(boldStart + 2, boldEnd).trim();
    if (!archetype) return;
    map.set(id, archetype);
  });
  return map;
};

const getRLessonIds = () => {
  const ids = [];
  (course.chapters || []).forEach((chapter) => {
    if (Array.isArray(chapter.lessons)) {
      chapter.lessons.forEach((lesson) => {
        if (lesson && lesson.id != null) ids.push(String(lesson.id));
      });
      return;
    }
    (chapter.concepts || []).forEach((concept) => {
      (concept.lessons || []).forEach((lesson) => {
        if (lesson && lesson.id != null) ids.push(String(lesson.id));
      });
    });
  });
  return ids;
};

const stripHtml = (input) =>
  String(input || '')
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<\/?[^>]+>/g, ' ')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/\s+/g, ' ')
    .trim();

const extractCodeBlocks = (content) => {
  const text = content || '';
  const blocks = [];
  const fence = /```(?:r)?\s*([\s\S]*?)```/gi;
  let match;
  while ((match = fence.exec(text))) blocks.push(match[1].trim());
  return blocks;
};

const pickRSource = (lesson) => {
  const sources = [];
  if (lesson && typeof lesson.starter_code === 'string' && lesson.starter_code.trim()) sources.push(lesson.starter_code);
  if (lesson && typeof lesson.solution_code === 'string' && lesson.solution_code.trim()) sources.push(lesson.solution_code);
  extractCodeBlocks(lesson && lesson.content).forEach((b) => sources.push(b));
  return sources.join('\n\n').trim();
};

const normalizeDataset = (name) => {
  if (!name) return null;
  const base = String(name).trim();
  const cleaned = base.includes('::') ? base.split('::').pop() : base;
  return cleaned.replace(/[()]/g, '');
};

const extractDatasets = (code) => {
  const src = code || '';
  const found = [];
  const stop = new Set(['data', 'df', 'dataset', 'table', 'aes']);
  const ggplot = /ggplot\s*\(\s*(?:data\s*=\s*)?([a-zA-Z_]\w*(?:::\w+)?)\b/gi;
  let m;
  while ((m = ggplot.exec(src))) {
    const name = normalizeDataset(m[1]);
    if (name && !stop.has(name.toLowerCase())) found.push(name);
  }
  const pipeStart = /^\s*([a-zA-Z_]\w*(?:::\w+)?)\s*(?:%>%|\|>)/gm;
  while ((m = pipeStart.exec(src))) {
    const name = normalizeDataset(m[1]);
    if (name && !stop.has(name.toLowerCase())) found.push(name);
  }
  const bare = /^\s*([a-zA-Z_]\w*(?:::\w+)?)\s*$/gm;
  while ((m = bare.exec(src))) {
    const name = normalizeDataset(m[1]);
    if (!['library', 'ggplot', 'filter', 'select', 'mutate', 'summarise', 'summarize'].includes(name)) {
      if (name && !stop.has(name.toLowerCase())) {
      found.push(name);
      }
    }
  }
  return Array.from(new Set(found)).filter(Boolean).slice(0, 3);
};

const extractAes = (code) => {
  const src = code || '';
  const match = src.match(/aes\s*\(([\s\S]*?)\)/i);
  if (!match) return {};
  const inside = match[1];
  const pick = (key) => {
    const m = inside.match(new RegExp(`\\b${key}\\s*=\\s*([^,\\)]+)`, 'i'));
    if (!m) return null;
    return m[1].trim().replace(/\)$/, '');
  };
  return {
    x: pick('x'),
    y: pick('y'),
    color: pick('color'),
    fill: pick('fill'),
    shape: pick('shape')
  };
};

const extractDplyrOps = (code) => {
  const lower = String(code || '').toLowerCase();
  const ops = [];
  [
    'filter',
    'select',
    'arrange',
    'mutate',
    'summarise',
    'summarize',
    'group_by',
    'count',
    'distinct',
    'left_join',
    'inner_join',
    'right_join',
    'full_join',
    'pivot_longer',
    'pivot_wider'
  ].forEach((op) => {
    const re = new RegExp(`\\b${op}\\s*\\(`, 'i');
    if (re.test(lower)) ops.push(op);
  });
  return ops;
};

const extractFilterCondition = (code) => {
  const match = code.match(/\bfilter\s*\(([\s\S]*?)\)/i);
  if (!match) return null;
  const inside = match[1];
  const simple = inside.match(/([a-zA-Z_]\w*)\s*(==|!=|>=|<=|>|<|%in%)\s*([^\s,\)]+)/);
  if (!simple) return { raw: inside.trim() };
  return {
    raw: inside.trim(),
    column: simple[1],
    operator: simple[2],
    value: simple[3]
  };
};

const extractMutate = (code) => {
  const match = code.match(/\bmutate\s*\(([\s\S]*?)\)/i);
  if (!match) return null;
  const inside = match[1];
  const assign = inside.match(/([a-zA-Z_]\w*)\s*=\s*([^,\)]+)/);
  if (!assign) return null;
  return { column: assign[1], expr: assign[2].trim() };
};

const extractGroupBy = (code) => {
  const match = code.match(/\bgroup_by\s*\(([\s\S]*?)\)/i);
  if (!match) return [];
  return match[1]
    .split(',')
    .map((c) => c.trim())
    .filter(Boolean)
    .map((c) => c.split(' ')[0]);
};

const extractJoin = (code) => {
  const match = code.match(/\b(left_join|inner_join|right_join|full_join)\s*\(\s*([a-zA-Z_]\w*)\s*,\s*([a-zA-Z_]\w*)/i);
  if (!match) return null;
  const byMatch = code.match(/\bby\s*=\s*["']([\w\.]+)["']/i);
  return {
    left: match[2],
    right: match[3],
    by: byMatch ? byMatch[1] : 'id'
  };
};

const extractPivot = (code) => {
  const isLong = /\bpivot_longer\s*\(/i.test(code);
  const isWide = /\bpivot_wider\s*\(/i.test(code);
  if (!isLong && !isWide) return null;
  return { mode: isLong ? 'longer' : 'wider' };
};

const extractColumnsFromCode = (code) => {
  const cols = new Set();
  const add = (value) => {
    if (!value) return;
    const clean = value.replace(/[`"'(){}]/g, '').replace(/\.\.\./g, '').trim();
    if (!clean) return;
    if (/^\d+$/.test(clean)) return;
    if (clean.includes('..')) return;
    if (['c', 'mean', 'sum', 'median', 'sd', 'var', 'min', 'max', 'n'].includes(clean)) return;
    cols.add(clean);
  };
  const useRegex = (re) => {
    let m;
    while ((m = re.exec(code))) add(m[1]);
  };
  useRegex(/select\s*\(([\s\S]*?)\)/gi);
  useRegex(/arrange\s*\(([\s\S]*?)\)/gi);
  useRegex(/group_by\s*\(([\s\S]*?)\)/gi);
  const filterMatch = code.match(/\bfilter\s*\(([\s\S]*?)\)/i);
  if (filterMatch) {
    const filterCols = filterMatch[1].match(/([a-zA-Z_]\w*)\s*(==|!=|>=|<=|>|<|%in%)/g);
    if (filterCols) {
      filterCols.forEach((col) => add(col.split(/\s+/)[0]));
    }
  }
  const aes = extractAes(code);
  [aes.x, aes.y, aes.color, aes.fill, aes.shape].forEach(add);
  return Array.from(cols).filter(Boolean);
};

const DATASET_SPECS = {
  penguins: {
    numeric: ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'],
    categorical: ['species', 'island', 'sex']
  },
  mpg: {
    numeric: ['displ', 'hwy', 'cty', 'cyl'],
    categorical: ['class', 'drv', 'manufacturer', 'model']
  },
  diamonds: {
    numeric: ['carat', 'depth', 'table', 'price', 'x', 'y', 'z'],
    categorical: ['cut', 'color', 'clarity']
  },
  flights: {
    numeric: ['month', 'day', 'dep_time', 'arr_time', 'distance', 'air_time'],
    categorical: ['carrier', 'origin', 'dest']
  },
  iris: {
    numeric: ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width'],
    categorical: ['Species']
  },
  mtcars: {
    numeric: ['mpg', 'disp', 'hp', 'wt', 'qsec'],
    categorical: ['cyl', 'gear', 'am']
  },
  diamonds_small: {
    numeric: ['carat', 'price'],
    categorical: ['cut', 'color']
  }
};

const sampleValue = (column, idx) => {
  const lower = column.toLowerCase();
  if (lower.includes('id')) return idx + 1;
  if (lower.includes('date')) return `2023-0${idx + 1}-0${idx + 2}`;
  if (lower.includes('time')) return `08:0${idx}`;
  if (lower.includes('species')) return ['Adelie', 'Chinstrap', 'Gentoo'][idx % 3];
  if (lower.includes('island')) return ['Torgersen', 'Dream', 'Biscoe'][idx % 3];
  if (lower.includes('sex')) return ['male', 'female'][idx % 2];
  if (lower.includes('class')) return ['compact', 'suv', 'pickup'][idx % 3];
  if (lower.includes('cut')) return ['Ideal', 'Premium', 'Good'][idx % 3];
  if (lower.includes('color')) return ['D', 'E', 'F'][idx % 3];
  if (lower.includes('clarity')) return ['VS1', 'SI1', 'VVS2'][idx % 3];
  if (lower.includes('month')) return idx + 1;
  if (lower.includes('day')) return idx + 5;
  if (lower.includes('price') || lower.includes('weight') || lower.includes('length') || lower.includes('depth')) {
    return 10 * (idx + 1);
  }
  if (lower.includes('mass')) return 3000 + idx * 100;
  if (lower.includes('count') || lower.includes('total') || lower.includes('n_')) return idx + 10;
  if (lower.includes('rate') || lower.includes('ratio')) return Number((0.1 * (idx + 1)).toFixed(2));
  if (lower.includes('name')) return ['Ava', 'Ben', 'Cam', 'Dee'][idx % 4];
  return idx + 1;
};

const buildRows = (columns, rowCount = 4, overrides = {}) => {
  const rows = [];
  for (let i = 0; i < rowCount; i += 1) {
    const row = {};
    columns.forEach((col) => {
      if (overrides[col] && overrides[col][i] !== undefined) {
        row[col] = overrides[col][i];
      } else {
        row[col] = sampleValue(col, i);
      }
    });
    rows.push(row);
  }
  return rows;
};

const getDatasetSpec = (dataset, columnsFromCode) => {
  const name = normalizeDataset(dataset) || 'dataset';
  const spec = DATASET_SPECS[name];
  if (spec) {
    return {
      name,
      numeric: spec.numeric,
      categorical: spec.categorical,
      columns: [...spec.numeric, ...spec.categorical]
    };
  }
  const fallbackColumns = columnsFromCode && columnsFromCode.length ? columnsFromCode : ['value', 'group'];
  return {
    name,
    numeric: fallbackColumns.slice(0, 2),
    categorical: fallbackColumns.slice(2),
    columns: fallbackColumns
  };
};

const buildDatasetExplorer = (context) => {
  const columns = context.columns.slice(0, 6);
  return [
    {
      type: 'visual_table',
      title: `${context.dataset} preview`,
      columns,
      data: buildRows(columns, 5),
      allowSort: true,
      allowFilter: true,
      allowRowHighlight: true,
      highlightColumn: columns[0]
    },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildAesMappingBuilder = (context) => {
  const columns = context.columns.slice(0, 6);
  const xChoices = context.numeric.length ? context.numeric : columns;
  const yChoices = context.numeric.length > 1 ? context.numeric : columns;
  const colorChoices = context.categorical.length ? context.categorical : columns;
  const xCorrect = context.aes.x && columns.includes(context.aes.x) ? context.aes.x : xChoices[0];
  const yCorrect = context.aes.y && columns.includes(context.aes.y) ? context.aes.y : yChoices[1] || yChoices[0];
  const colorCorrect = context.aes.color && columns.includes(context.aes.color)
    ? context.aes.color
    : colorChoices[0];

  const slots = [
    { id: 'x', label: 'x', options: xChoices, correct: xCorrect },
    { id: 'y', label: 'y', options: yChoices, correct: yCorrect }
  ];
  if (colorChoices.length) {
    slots.push({ id: 'color', label: 'color', options: colorChoices, correct: colorCorrect });
  }
  const template = `ggplot(${context.dataset}, aes(x = {{x}}, y = {{y}}${colorChoices.length ? ', color = {{color}}' : ''})) + geom_point()`;

  return [
    {
      type: 'visual_table',
      title: `${context.dataset} sample`,
      columns,
      data: buildRows(columns, 5),
      allowSort: true,
      allowFilter: false,
      allowRowHighlight: true
    },
    { type: 'token_slot', template, slots },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildDebugQuestR = (lesson) => {
  const snippet = (lesson.starter_code || '').trim() || 'x <- 1';
  const solution = (lesson.solution_code || '').trim() || snippet;
  const lines = snippet.split('\n');
  let bugLine = 1;
  if (lesson.solution_code) {
    const solLines = solution.split('\n');
    for (let i = 0; i < Math.max(lines.length, solLines.length); i += 1) {
      if ((lines[i] || '') !== (solLines[i] || '')) {
        bugLine = i + 1;
        break;
      }
    }
  }
  const wrongOption = snippet.includes('<-') ? snippet.replace('<-', '=') : `${snippet} # typo`;
  const options = [
    { label: 'Apply the fix', fix: solution, correct: true },
    { label: 'Keep the original', fix: snippet, correct: false },
    { label: 'Try a quick tweak', fix: wrongOption, correct: false }
  ];
  return [
    {
      type: 'debug_quest',
      title: lesson.title || 'Fix the code',
      snippet,
      bugLine,
      options
    },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildFilterAnimator = (context, filterCondition) => {
  const columns = context.columns.slice(0, 5);
  const beforeRows = buildRows(columns, 5);
  let matchRows = beforeRows.slice(0, 2);
  let nonMatchRows = beforeRows.slice(2);
  let label = 'Apply filter';
  let labelAlt = 'Remove filter';
  if (filterCondition && filterCondition.column && filterCondition.operator) {
    label = `${filterCondition.column} ${filterCondition.operator} ${filterCondition.value}`;
    labelAlt = `${filterCondition.column} != ${filterCondition.value}`;
    matchRows = beforeRows.filter((row) => String(row[filterCondition.column]) === filterCondition.value.replace(/['"]/g, ''));
    if (!matchRows.length) matchRows = beforeRows.slice(0, 2);
    nonMatchRows = beforeRows.filter((row) => !matchRows.includes(row));
  }
  const filters = [
    { id: 'match', label, rows: matchRows },
    { id: 'nonmatch', label: labelAlt, rows: nonMatchRows }
  ];
  return [
    {
      type: 'data_transform',
      title: `Filter ${context.dataset}`,
      columns,
      beforeRows,
      filters,
      resultVar: 'rows_kept'
    },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildMutateFactory = (context, mutateInfo) => {
  const columns = context.columns.slice(0, 4);
  const newCol = mutateInfo && mutateInfo.column ? mutateInfo.column : 'new_var';
  const beforeRows = buildRows(columns, 4);
  const afterRows = beforeRows.map((row, idx) => ({
    ...row,
    [newCol]: typeof row[columns[0]] === 'number' ? row[columns[0]] * 2 : idx + 10
  }));
  const filters = [
    { id: 'apply', label: `Add ${newCol}`, rows: afterRows },
    { id: 'skip', label: 'Keep original', rows: beforeRows }
  ];
  return [
    {
      type: 'data_transform',
      title: `Mutate ${context.dataset}`,
      columns: [...columns, newCol],
      beforeRows,
      filters,
      resultVar: 'mutate_rows'
    },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildGroupSummarizeWorkbench = (context, groupCols) => {
  const groupCol = groupCols[0] || context.categorical[0] || context.columns[0];
  const valueCol = context.numeric[0] || context.columns[1] || context.columns[0];
  const template = `summarise(${context.dataset}, ${valueCol}_avg = mean(${valueCol}), .by = {{group}})`;
  const slots = [
    {
      id: 'group',
      label: 'Group by',
      options: [groupCol, ...(context.categorical.filter((c) => c !== groupCol).slice(0, 2))],
      correct: groupCol
    }
  ];
  return [
    { type: 'token_slot', template, slots },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildJoinVisualizerPlan = (context, joinInfo) => {
  const leftName = joinInfo ? joinInfo.left : context.datasets[0] || 'table_a';
  const rightName = joinInfo ? joinInfo.right : context.datasets[1] || 'table_b';
  const key = joinInfo ? joinInfo.by : 'id';
  const leftRows = buildRows([key, 'value'], 3);
  const rightRows = buildRows([key, 'detail'], 4, { [key]: [1, 2, 2, 4] });
  return [
    {
      type: 'join_visualizer',
      leftTitle: leftName,
      rightTitle: rightName,
      leftRows,
      rightRows,
      leftKey: key,
      rightKey: key,
      joinTypes: ['INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN'],
      resultVar: 'join_rows',
      joinVar: 'join_type'
    },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildPivotAnimator = (context) => {
  const columns = ['id', 'metric_a', 'metric_b'];
  const beforeRows = [
    { id: 1, metric_a: 10, metric_b: 5 },
    { id: 2, metric_a: 8, metric_b: 7 }
  ];
  const afterRows = [
    { id: 1, key: 'metric_a', value: 10 },
    { id: 1, key: 'metric_b', value: 5 },
    { id: 2, key: 'metric_a', value: 8 },
    { id: 2, key: 'metric_b', value: 7 }
  ];
  const filters = [
    { id: 'long', label: 'Pivot longer', rows: afterRows },
    { id: 'wide', label: 'Keep wide', rows: beforeRows }
  ];
  return [
    {
      type: 'data_transform',
      title: 'Pivot the table',
      columns: ['id', 'key', 'value'],
      beforeRows,
      filters,
      resultVar: 'pivot_rows'
    },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildPipelineStepper = (code, ops) => {
  const steps = (ops.length ? ops : ['select', 'filter', 'summarise']).map((op, idx) => ({
    line: idx + 1,
    description: `Apply ${op} step`
  }));
  const scaffold = (ops.length ? ops : ['select()', 'filter()', 'summarise()']).map((op) => `${op}`).join('\n');
  return [
    { type: 'step_executor', code: scaffold, steps },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildCaseBranchMapper = (context) => {
  const column = context.categorical[0] || context.columns[0];
  const prompt = `Which rows should go to the TRUE branch when ${column} matches the condition?`;
  return [
    {
      type: 'conditional_path',
      prompt,
      choices: [
        { label: `${column} matches`, outcome: 'true' },
        { label: `${column} does not match`, outcome: 'false' }
      ],
      trueLabel: 'TRUE branch',
      falseLabel: 'FALSE branch',
      resultVar: 'case_branch'
    },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildTimeBucketingWorkbench = (context) => {
  const columns = ['date', 'count'];
  const beforeRows = [
    { date: '2023-01-02', count: 10 },
    { date: '2023-01-03', count: 12 },
    { date: '2023-02-01', count: 14 }
  ];
  const monthRows = [
    { date: '2023-01', count: 22 },
    { date: '2023-02', count: 14 }
  ];
  const filters = [
    { id: 'day', label: 'Daily', rows: beforeRows },
    { id: 'month', label: 'Monthly', rows: monthRows }
  ];
  return [
    {
      type: 'data_transform',
      title: 'Bucket dates',
      columns,
      beforeRows,
      filters,
      resultVar: 'bucket_rows'
    },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildStatWhatIfLab = (context) => {
  return [
    {
      type: 'graph_manipulator',
      title: 'Change the parameter',
      mode: 'linear',
      slope: 1,
      intercept: 0,
      xMin: 0,
      xMax: 10,
      initialX: 3,
      xVar: 'stat_param',
      yVar: 'stat_value'
    },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildVectorIndexPlayground = (context) => {
  const template = 'x[c({{i1}}, {{i2}})]';
  const slots = [
    { id: 'i1', label: 'Index 1', options: ['1', '2', '3', '4'], correct: '1' },
    { id: 'i2', label: 'Index 2', options: ['2', '3', '4'], correct: '3' }
  ];
  return [
    {
      type: 'visual_table',
      title: 'Vector x',
      columns: ['index', 'value'],
      data: [
        { index: 1, value: 10 },
        { index: 2, value: 14 },
        { index: 3, value: 22 },
        { index: 4, value: 5 }
      ],
      allowSort: false,
      allowFilter: false,
      allowRowHighlight: true
    },
    { type: 'token_slot', template, slots },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildFactorLevelsRack = (context) => {
  const columns = ['level', 'count'];
  const beforeRows = [
    { level: 'A', count: 4 },
    { level: 'B', count: 3 },
    { level: 'C', count: 5 }
  ];
  const reordered = [
    { level: 'B', count: 3 },
    { level: 'A', count: 4 },
    { level: 'C', count: 5 }
  ];
  const filters = [
    { id: 'original', label: 'Original order', rows: beforeRows },
    { id: 'reorder', label: 'Reorder levels', rows: reordered }
  ];
  return [
    {
      type: 'data_transform',
      title: 'Factor levels',
      columns,
      beforeRows,
      filters,
      resultVar: 'factor_levels'
    },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildStringWorkbench = (lesson, context) => {
  const title = String(lesson.title || '').toLowerCase();
  const content = String(lesson.content || '').toLowerCase();
  if (title.includes('yaml') || title.includes('quarto') || content.includes('yaml')) {
    const template = [
      '---',
      'title: {{title}}',
      'format: {{format}}',
      '---'
    ].join('\n');
    const slots = [
      { id: 'title', label: 'Title', options: ['"My Report"', '"Project Notes"', '"Analysis"'], correct: '"My Report"' },
      { id: 'format', label: 'Format', options: ['html', 'pdf', 'revealjs'], correct: 'html' }
    ];
    return [
      { type: 'token_slot', template, slots },
      { type: 'reset_state', label: 'Reset' }
    ];
  }

  const template = 'str_to_upper({{text}})';
  const slots = [
    { id: 'text', label: 'Column', options: [context.columns[0] || 'name', 'city', 'status'], correct: context.columns[0] || 'name' }
  ];
  return [
    { type: 'token_slot', template, slots },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildFunctionScopeStepper = (lesson, code) => {
  const source = (lesson.starter_code || code || '').toString();
  const lines = source.split('\n').filter((line) => line.trim());
  const snippet = lines.length ? lines.slice(0, 8).join('\n') : [
    'add_tax <- function(price) {',
    '  total <- price * 1.08',
    '  return(total)',
    '}',
    'add_tax(100)'
  ].join('\n');
  const snippetLines = snippet.split('\n');
  const steps = snippetLines.map((line, idx) => {
    const lower = line.toLowerCase();
    let description = `Execute line ${idx + 1}.`;
    if (lower.includes('function')) description = 'Define the function.';
    else if (lower.includes('return')) description = 'Return value from the function.';
    else if (lower.includes('<-')) description = 'Assign a local variable.';
    else if (lower.includes('|>') || lower.includes('%>%')) description = 'Pipe data to the next step.';
    else if (lower.includes('(') && lower.includes(')')) description = 'Call the function.';
    return { line: idx + 1, description };
  });
  return [
    { type: 'step_executor', code: snippet, steps },
    { type: 'reset_state', label: 'Reset' }
  ];
};

const buildLoopSimulatorPlan = () => ([
  {
    type: 'loop_simulator',
    label: 'Loop total',
    iterations: 5,
    startValue: 0,
    stepValue: 2,
    valueVar: 'total',
    stepVar: 'i'
  },
  { type: 'reset_state', label: 'Reset' }
]);

const buildConditionalPath = () => ([
  {
    type: 'conditional_path',
    prompt: 'Which condition is TRUE?',
    choices: [
      { label: 'value > 10', outcome: 'true' },
      { label: 'value <= 10', outcome: 'false' }
    ],
    trueLabel: 'TRUE branch',
    falseLabel: 'FALSE branch',
    resultVar: 'condition_result'
  },
  { type: 'reset_state', label: 'Reset' }
]);

const buildPlanForArchetype = (archetype, lesson, context, helpers) => {
  switch (archetype) {
    case 'DatasetExplorer':
      return buildDatasetExplorer(context);
    case 'AesMappingBuilder':
      return buildAesMappingBuilder(context);
    case 'DebugQuestR':
      return buildDebugQuestR(lesson);
    case 'FilterAnimator':
      return buildFilterAnimator(context, helpers.filterCondition);
    case 'MutateFactory':
      return buildMutateFactory(context, helpers.mutateInfo);
    case 'GroupSummarizeWorkbench':
      return buildGroupSummarizeWorkbench(context, helpers.groupCols);
    case 'JoinVisualizer':
      return buildJoinVisualizerPlan(context, helpers.joinInfo);
    case 'PivotAnimator':
      return buildPivotAnimator(context);
    case 'PipelineStepper':
      return buildPipelineStepper(helpers.code, helpers.ops);
    case 'CaseBranchMapper':
      return buildCaseBranchMapper(context);
    case 'TimeBucketingWorkbench':
      return buildTimeBucketingWorkbench(context);
    case 'StatWhatIfLab':
      return buildStatWhatIfLab(context);
    case 'VectorIndexPlayground':
      return buildVectorIndexPlayground(context);
    case 'FactorLevelsRack':
      return buildFactorLevelsRack(context);
    case 'StringWorkbench':
      return buildStringWorkbench(lesson, context);
    case 'FunctionScopeStepper':
      return buildFunctionScopeStepper(lesson, helpers.code);
    case 'LoopSimulator':
      return buildLoopSimulatorPlan();
    case 'ConditionalPath':
      return buildConditionalPath();
    default:
      return buildDatasetExplorer(context);
  }
};

const recommendations = parseRecommendations(recommendationsText);
const rLessonIds = getRLessonIds();

let updated = 0;
const missing = [];

rLessonIds.forEach((lessonId) => {
  const lesson = lessons[lessonId];
  if (!lesson) {
    missing.push(lessonId);
    return;
  }
  const archetype = recommendations.get(lessonId) || 'DatasetExplorer';
  const code = pickRSource(lesson);
  const datasets = extractDatasets(code);
  const columnsFromCode = extractColumnsFromCode(code);
  const datasetSpec = getDatasetSpec(datasets[0], columnsFromCode);
  const context = {
    dataset: datasetSpec.name,
    datasets,
    columns: datasetSpec.columns,
    numeric: datasetSpec.numeric,
    categorical: datasetSpec.categorical,
    aes: extractAes(code)
  };
  const helpers = {
    code,
    ops: extractDplyrOps(code),
    filterCondition: extractFilterCondition(code),
    mutateInfo: extractMutate(code),
    groupCols: extractGroupBy(code),
    joinInfo: extractJoin(code),
    pivot: extractPivot(code)
  };

  const plan = buildPlanForArchetype(archetype, lesson, context, helpers);
  lesson.interaction_plan = plan;
  lesson.interaction_recipe_id = `r_${slugify(archetype)}`;
  lesson.interaction_required = true;
  if (lesson.send_to_editor_template) {
    delete lesson.send_to_editor_template;
  }
  updated += 1;
});

fs.writeFileSync(lessonsPath, JSON.stringify(lessons, null, 2));

const summary = {
  updated,
  totalRLessons: rLessonIds.length,
  missingLessons: missing
};

fs.writeFileSync(path.resolve(__dirname, '../scripts/r_interaction_update_report.json'), JSON.stringify(summary, null, 2));

console.log(`Updated ${updated}/${rLessonIds.length} R lessons.`);
if (missing.length) console.log(`Missing lessons: ${missing.join(', ')}`);
