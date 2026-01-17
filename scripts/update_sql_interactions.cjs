const fs = require('fs');
const path = require('path');

const lessonsPath = path.resolve(__dirname, '../frontend/public/data/lessons.json');
const coursePath = path.resolve(__dirname, '../frontend/public/data/course-sql-fundamentals.json');
const recommendationsPath = path.resolve(__dirname, '../sql_interaction_recommendations.md');

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

const getSqlLessonIds = () => {
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

const stripSqlComments = (sql) =>
  (sql || '')
    .replace(/--.*$/gm, '')
    .replace(/\/\*[\s\S]*?\*\//g, '');

const pickSqlSource = (lesson) => {
  const sources = [];
  if (lesson && typeof lesson.starter_code === 'string' && lesson.starter_code.trim()) {
    sources.push(lesson.starter_code);
  }
  if (lesson && typeof lesson.solution_code === 'string' && lesson.solution_code.trim()) {
    sources.push(lesson.solution_code);
  }
  const content = lesson && lesson.content ? lesson.content : '';
  const fence = /```(?:sql)?\\s*([\\s\\S]*?)```/gi;
  let match;
  while ((match = fence.exec(content))) {
    if (match[1] && match[1].trim()) sources.push(match[1].trim());
  }
  return sources.join('\\n\\n').trim();
};

const extractTables = (sql) => {
  const normalized = stripSqlComments(sql).replace(/\\s+/g, ' ');
  const stop = new Set(['the', 'a', 'an', 'your', 'this', 'that', 'these', 'those']);
  const reserved = new Set([
    'select', 'from', 'join', 'where', 'group', 'order', 'limit', 'having', 'with',
    'create', 'insert', 'update', 'delete', 'into', 'values', 'on', 'as'
  ]);
  const tablePattern =
    /\\b(from|join|update|into|delete\\s+from)\\s+(?:the\\s+|a\\s+|an\\s+)?([`\"\\[]?)([a-zA-Z_][\\w.]*)([`\"\\]]?)/gi;
  const found = [];
  let match;
  while ((match = tablePattern.exec(normalized))) {
    const table = match[3];
    if (stop.has(table.toLowerCase())) continue;
    if (reserved.has(table.toLowerCase())) continue;
    found.push(table);
  }
  const ddl = normalized.match(/\\bcreate\\s+table\\s+([`\"\\[]?)([a-zA-Z_][\\w.]*)([`\"\\]]?)/i);
  if (ddl && ddl[2]) found.push(ddl[2]);
  return Array.from(new Set(found));
};

const extractJoinKeys = (sql) => {
  const normalized = stripSqlComments(sql).replace(/\\s+/g, ' ');
  const onPattern = /\\bon\\s+([a-zA-Z_][\\w.]*)\\s*=\\s*([a-zA-Z_][\\w.]*)/gi;
  const found = [];
  let match;
  while ((match = onPattern.exec(normalized))) {
    found.push({ left: match[1], right: match[2] });
  }
  return found;
};

const extractSelectColumns = (sql) => {
  const normalized = stripSqlComments(sql);
  const match = normalized.match(/\\bselect\\s+([\\s\\S]+?)\\s+from\\b/i);
  if (!match) return [];
  let columns = match[1].trim();
  columns = columns.replace(/^distinct\\s+/i, '');
  if (columns.includes('*')) return [];
  return columns
    .split(',')
    .map((col) => col.trim())
    .filter(Boolean)
    .map((col) => col.split(' ').slice(0, 1)[0])
    .map((col) => col.includes('.') ? col.split('.').pop() : col);
};

const extractWhereClause = (sql) => {
  const normalized = stripSqlComments(sql).replace(/\\s+/g, ' ');
  const match = normalized.match(/\\bwhere\\s+(.+?)(\\bgroup\\s+by\\b|\\border\\s+by\\b|\\bhaving\\b|\\blimit\\b|;|$)/i);
  if (!match) return null;
  const clause = match[1].trim();
  const simple = clause.match(/^([a-zA-Z_][\\w.]*)\\s*(=|!=|<>|>=|<=|>|<|like|in)\\s*(.+)$/i);
  if (!simple) return { raw: clause };
  return {
    raw: clause,
    column: simple[1].includes('.') ? simple[1].split('.').pop() : simple[1],
    operator: simple[2].toUpperCase(),
    value: simple[3].trim()
  };
};

const extractGroupByColumns = (sql) => {
  const normalized = stripSqlComments(sql).replace(/\\s+/g, ' ');
  const match = normalized.match(/\\bgroup\\s+by\\s+(.+?)(\\border\\s+by\\b|\\bhaving\\b|\\blimit\\b|;|$)/i);
  if (!match) return [];
  return match[1]
    .split(',')
    .map((col) => col.trim().split(' ')[0])
    .filter(Boolean)
    .map((col) => (col.includes('.') ? col.split('.').pop() : col));
};

const extractOrderByColumns = (sql) => {
  const normalized = stripSqlComments(sql).replace(/\\s+/g, ' ');
  const match = normalized.match(/\\border\\s+by\\s+(.+?)(\\blimit\\b|;|$)/i);
  if (!match) return [];
  return match[1]
    .split(',')
    .map((col) => col.trim())
    .filter(Boolean)
    .map((col) => col.split(' ')[0])
    .map((col) => (col.includes('.') ? col.split('.').pop() : col));
};

const extractCreateTable = (sql) => {
  const normalized = stripSqlComments(sql);
  const match = normalized.match(/\\bcreate\\s+table\\s+([a-zA-Z_][\\w.]*)\\s*\\((([\\s\\S]*?))\\)/i);
  if (!match) return null;
  const table = match[1];
  const body = match[2];
  const columns = body
    .split(',')
    .map((entry) => entry.trim())
    .filter(Boolean)
    .map((entry) => entry.split(' ')[0])
    .filter((col) => /^[a-zA-Z_]/.test(col));
  return { table, columns: Array.from(new Set(columns)) };
};

const parseValueLiteral = (raw) => {
  if (!raw) return null;
  const trimmed = raw.trim();
  const quoted = trimmed.match(/^['\"](.+?)['\"]$/);
  if (quoted) return quoted[1];
  const num = trimmed.match(/^-?\\d+(\\.\\d+)?$/);
  if (num) return Number(num[0]);
  return trimmed;
};

const inferTablesFromTitle = (title) => {
  const lower = String(title || '').toLowerCase();
  const tables = [];
  if (lower.includes('order')) tables.push('orders');
  if (lower.includes('customer')) tables.push('customers');
  if (lower.includes('user')) tables.push('users');
  if (lower.includes('product')) tables.push('products');
  if (lower.includes('employee')) tables.push('employees');
  if (lower.includes('event')) tables.push('events');
  if (lower.includes('session')) tables.push('sessions');
  if (lower.includes('date') || lower.includes('time')) tables.push('order_dates');
  if (lower.includes('payment')) tables.push('payments');
  if (lower.includes('inventory')) tables.push('inventory');
  if (lower.includes('transaction')) tables.push('transactions');
  return Array.from(new Set(tables));
};

const inferColumnsFromTitle = (title) => {
  const lower = String(title || '').toLowerCase();
  const columns = [];
  if (lower.includes('date') || lower.includes('time') || lower.includes('cohort')) columns.push('order_date');
  if (lower.includes('month')) columns.push('month');
  if (lower.includes('year')) columns.push('year');
  if (lower.includes('customer')) columns.push('customer_id');
  if (lower.includes('user')) columns.push('user_id');
  if (lower.includes('order')) columns.push('order_id');
  if (lower.includes('status')) columns.push('status');
  if (lower.includes('category')) columns.push('category');
  if (lower.includes('region')) columns.push('region');
  if (lower.includes('amount') || lower.includes('price') || lower.includes('cost') || lower.includes('salary')) {
    columns.push('amount');
  }
  if (lower.includes('count') || lower.includes('total')) columns.push('total');
  if (lower.includes('ratio') || lower.includes('percent') || lower.includes('rate')) columns.push('rate');
  if (lower.includes('join')) columns.push('id');
  if (!columns.length) columns.push('id', 'value');
  return Array.from(new Set(columns));
};

const sampleValueForColumn = (column, index, targetValue) => {
  const lower = column.toLowerCase();
  if (targetValue !== undefined && targetValue !== null) {
    if (index === 0) return targetValue;
  }
  if (lower.includes('id')) return index + 1;
  if (lower.includes('date')) return `2024-0${index + 1}-0${index + 2}`;
  if (lower.includes('time')) return `2024-01-0${index + 1} 0${index + 1}:00`;
  if (lower.includes('amount') || lower.includes('price') || lower.includes('salary') || lower.includes('cost')) {
    return 10 * (index + 1);
  }
  if (lower.includes('count') || lower.includes('total')) return (index + 1) * 3;
  if (lower.includes('status')) {
    return ['shipped', 'processing', 'cancelled', 'pending'][index % 4];
  }
  if (lower.includes('name')) {
    return ['Avery', 'Blake', 'Casey', 'Drew'][index % 4];
  }
  if (lower.includes('category')) {
    return ['alpha', 'beta', 'gamma', 'delta'][index % 4];
  }
  return `value_${index + 1}`;
};

const sanitizeColumn = (value, fallback) => {
  if (!value) return fallback;
  const trimmed = String(value).trim();
  if (!trimmed) return fallback;
  if (trimmed === '*') return fallback;
  if (/^\d+$/.test(trimmed)) return fallback;
  return trimmed;
};

const toForeignKey = (table) => {
  const base = String(table || 'item').split('.').pop();
  if (base.endsWith('s') && base.length > 1) {
    return `${base.slice(0, -1)}_id`;
  }
  return `${base}_id`;
};

const buildRows = (columns, options = {}) => {
  const cols = columns.length ? columns : ['id', 'value'];
  const rowCount = options.rowCount || 4;
  const rows = [];
  for (let i = 0; i < rowCount; i += 1) {
    const row = {};
    cols.forEach((col) => {
      if (options.overrides && options.overrides[col] && options.overrides[col][i] !== undefined) {
        row[col] = options.overrides[col][i];
      } else {
        row[col] = sampleValueForColumn(col, i, options.targetColumn === col ? options.targetValue : undefined);
      }
    });
    rows.push(row);
  }
  return rows;
};

const filterRows = (rows, predicate) => rows.filter((row) => predicate(row));

const parseCondition = (where) => {
  if (!where || !where.column || !where.operator) return null;
  const value = parseValueLiteral(where.value);
  return { column: where.column, operator: where.operator, value };
};

const evalCondition = (row, condition) => {
  if (!condition) return false;
  const cell = row[condition.column];
  const value = condition.value;
  switch (condition.operator) {
    case '=':
      return cell === value;
    case '!=':
    case '<>':
      return cell !== value;
    case '>':
      return cell > value;
    case '<':
      return cell < value;
    case '>=':
      return cell >= value;
    case '<=':
      return cell <= value;
    case 'LIKE': {
      if (typeof cell !== 'string' || typeof value !== 'string') return false;
      const needle = value.replace(/%/g, '');
      return cell.includes(needle);
    }
    case 'IN': {
      if (typeof value !== 'string') return false;
      const list = value.replace(/[()]/g, '').split(',').map((v) => parseValueLiteral(v.trim()));
      return list.includes(cell);
    }
    default:
      return false;
  }
};

const buildTokenSlot = (template, slots) => ([
  { type: 'token_slot', template, slots },
  { type: 'reset_state', label: 'Reset' }
]);

const buildStepExecutor = (code, steps) => ([
  { type: 'step_executor', code, steps },
  { type: 'reset_state', label: 'Reset' }
]);

const buildDataTransform = (title, columns, beforeRows, filters, resultVar) => ([
  { type: 'data_transform', title, columns, beforeRows, filters, resultVar },
  { type: 'reset_state', label: 'Reset' }
]);

const buildJoinVisualizerPlan = (title, leftTitle, rightTitle, leftRows, rightRows, leftKey, rightKey) => ([
  {
    type: 'join_visualizer',
    leftTitle: leftTitle || 'Left table',
    rightTitle: rightTitle || 'Right table',
    leftRows,
    rightRows,
    leftKey,
    rightKey,
    joinTypes: ['INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN'],
    resultVar: 'join_rows',
    joinVar: 'join_type',
    title
  },
  { type: 'reset_state', label: 'Reset' }
]);

const buildConditionalPath = (prompt, choices, trueLabel, falseLabel) => ([
  { type: 'conditional_path', prompt, choices, trueLabel, falseLabel, resultVar: 'case_result' },
  { type: 'reset_state', label: 'Reset' }
]);

const buildQueryBuilderSlots = (lesson, context) => {
  const table = context.tables[0] || 'table_name';
  const selectCols = context.selectCols.length ? context.selectCols : ['*'];
  const where = context.where;
  const columnSlot = selectCols.length > 1 ? selectCols.join(', ') : selectCols[0];
  const slotId = 'select_cols';
  const options = [
    columnSlot,
    selectCols.slice(0, 1).join(', '),
    '*'
  ].filter((v, idx, arr) => v && arr.indexOf(v) === idx);
  let template = `SELECT {{${slotId}}} FROM ${table}`;
  const slots = [{ id: slotId, label: 'Columns', options, correct: columnSlot }];
  if (where && where.raw) {
    const whereSlotId = 'where_clause';
    const raw = where.raw;
    const wrong = where.column ? `${where.column} != ${where.value}` : `1=1`;
    template += ` WHERE {{${whereSlotId}}}`;
    slots.push({
      id: whereSlotId,
      label: 'Filter',
      options: [raw, wrong].filter((v, idx, arr) => v && arr.indexOf(v) === idx),
      correct: raw
    });
  }
  template += ';';
  return buildTokenSlot(template, slots);
};

const buildSchemaGraphBuilder = (lesson, context) => {
  const leftTable = context.tables[0] || 'customers';
  const rightTable = context.tables[1] || `${leftTable}_orders`;
  const joinKey = context.joinKeys[0];
  const leftKey = joinKey ? joinKey.left.split('.').pop() : 'id';
  const rightKey = joinKey ? joinKey.right.split('.').pop() : toForeignKey(leftTable);
  const leftRows = buildRows([leftKey, 'name'], { rowCount: 3 });
  const rightRows = buildRows([rightKey, 'status'], {
    rowCount: 4,
    overrides: {
      [rightKey]: [1, 2, 2, 4],
      status: ['open', 'closed', 'open', 'pending']
    }
  });
  return buildJoinVisualizerPlan('Schema relationship map', leftTable, rightTable, leftRows, rightRows, leftKey, rightKey);
};

const buildWindowTimeline = (lesson, context) => {
  const table = context.tables[0] || 'orders';
  const partition = context.groupCols[0] || 'customer_id';
  const orderCol = context.orderCols[0] || 'order_date';
  const valueCol = context.selectCols.find((c) => c !== partition) || 'amount';
  const code = [
    `SELECT ${partition}, ${valueCol},`,
    `  SUM(${valueCol}) OVER (PARTITION BY ${partition} ORDER BY ${orderCol}) AS running_total`,
    `FROM ${table};`
  ].join('\\n');
  const steps = [
    { line: 1, description: `Partition rows by ${partition}.` },
    { line: 2, description: `Order rows by ${orderCol} within each partition.` },
    { line: 2, description: `Compute running SUM for ${valueCol}.`, stateChanges: { running_total: 1 } }
  ];
  return buildStepExecutor(code, steps);
};

const buildJoinVisualizer = (lesson, context) => {
  const leftTable = context.tables[0] || 'customers';
  const rightTable = context.tables[1] || 'orders';
  const joinKey = context.joinKeys[0];
  const leftKey = joinKey ? joinKey.left.split('.').pop() : 'id';
  const rightKey = joinKey ? joinKey.right.split('.').pop() : toForeignKey(leftTable);
  const leftRows = buildRows([leftKey, 'name'], { rowCount: 3 });
  const rightRows = buildRows([rightKey, 'total'], {
    rowCount: 4,
    overrides: {
      [rightKey]: [1, 1, 2, 4],
      total: [50, 120, 75, 200]
    }
  });
  return buildJoinVisualizerPlan('Join outcome preview', leftTable, rightTable, leftRows, rightRows, leftKey, rightKey);
};

const buildFilterAnimator = (lesson, context) => {
  const columns = context.selectCols.length ? context.selectCols : ['id', 'status', 'amount'];
  const condition = parseCondition(context.where);
  let beforeRows = buildRows(columns, { rowCount: 5 });
  if (condition) {
    beforeRows = buildRows(columns, {
      rowCount: 5,
      targetColumn: condition.column,
      targetValue: condition.value,
      overrides: {
        [condition.column]: [condition.value, condition.value, sampleValueForColumn(condition.column, 2), sampleValueForColumn(condition.column, 3)]
      }
    });
  }
  const matchRows = condition ? filterRows(beforeRows, (row) => evalCondition(row, condition)) : beforeRows.slice(0, 2);
  const nonMatchRows = condition ? filterRows(beforeRows, (row) => !evalCondition(row, condition)) : beforeRows.slice(2);
  const filters = [
    {
      id: 'match',
      label: condition ? `WHERE ${condition.column} ${condition.operator} ${condition.value}` : 'Apply filter',
      rows: matchRows.length ? matchRows : beforeRows.slice(0, 2)
    },
    {
      id: 'nonmatch',
      label: condition ? `WHERE ${condition.column} != ${condition.value}` : 'No filter',
      rows: nonMatchRows.length ? nonMatchRows : beforeRows.slice(2)
    }
  ];
  return buildDataTransform('Filter the rows', columns, beforeRows, filters, 'rows_kept');
};

const buildSortLimitScrubber = (lesson, context) => {
  const columns = context.selectCols.length ? context.selectCols : ['id', 'amount'];
  const orderCol = sanitizeColumn(context.orderCols[0], columns.find((c) => c !== 'id') || 'amount');
  const beforeRows = buildRows(columns, {
    rowCount: 5,
    overrides: {
      [orderCol]: [12, 45, 7, 30, 22]
    }
  });
  const descRows = [...beforeRows].sort((a, b) => b[orderCol] - a[orderCol]).slice(0, 3);
  const ascRows = [...beforeRows].sort((a, b) => a[orderCol] - b[orderCol]).slice(0, 3);
  const filters = [
    { id: 'top', label: `Top 3 by ${orderCol} DESC`, rows: descRows },
    { id: 'bottom', label: `Bottom 3 by ${orderCol} ASC`, rows: ascRows }
  ];
  return buildDataTransform('Sort + limit preview', columns, beforeRows, filters, 'limit_rows');
};

const buildCTEStepper = (lesson, context) => {
  const table = context.tables[0] || 'orders';
  const cteName = 'base_data';
  const code = [
    `WITH ${cteName} AS (`,
    `  SELECT * FROM ${table}`,
    `)`,
    `SELECT * FROM ${cteName};`
  ].join('\\n');
  const steps = [
    { line: 1, description: `Define CTE ${cteName}.` },
    { line: 2, description: `Populate ${cteName} from ${table}.` },
    { line: 4, description: `Query the CTE result set.` }
  ];
  return buildStepExecutor(code, steps);
};

const buildNullLogicLab = (lesson, context) => {
  const columns = context.selectCols.length ? context.selectCols : ['id', 'value'];
  const targetCol = sanitizeColumn(columns.find((c) => c !== 'id') || columns[0], 'value');
  const beforeRows = buildRows(columns, {
    rowCount: 4,
    overrides: {
      [targetCol]: [null, sampleValueForColumn(targetCol, 1), null, sampleValueForColumn(targetCol, 3)]
    }
  });
  const nullRows = beforeRows.filter((row) => row[targetCol] == null);
  const notNullRows = beforeRows.filter((row) => row[targetCol] != null);
  const filters = [
    { id: 'is_null', label: `${targetCol} IS NULL`, rows: nullRows },
    { id: 'is_not_null', label: `${targetCol} IS NOT NULL`, rows: notNullRows }
  ];
  return buildDataTransform('NULL logic lab', columns, beforeRows, filters, 'null_rows');
};

const buildQueryExecutionTimeline = (lesson, context) => {
  const table = context.tables[0] || 'orders';
  const code = [
    `FROM ${table}`,
    `WHERE status = 'shipped'`,
    `GROUP BY customer_id`,
    `SELECT customer_id, COUNT(*) AS orders`,
    `ORDER BY orders DESC`
  ].join('\\n');
  const steps = [
    { line: 1, description: `Load rows from ${table}.` },
    { line: 2, description: `Filter rows with WHERE.` },
    { line: 3, description: `Group rows for aggregation.` },
    { line: 4, description: `Select aggregated output.` },
    { line: 5, description: `Order final result.` }
  ];
  return buildStepExecutor(code, steps);
};

const buildSetOpsVenn = (lesson, context) => {
  const columns = ['set', 'value'];
  const beforeRows = [
    { set: 'A', value: 'alpha' },
    { set: 'A', value: 'beta' },
    { set: 'B', value: 'beta' },
    { set: 'B', value: 'gamma' }
  ];
  const unionRows = [
    { set: 'union', value: 'alpha' },
    { set: 'union', value: 'beta' },
    { set: 'union', value: 'gamma' }
  ];
  const intersectRows = [
    { set: 'intersect', value: 'beta' }
  ];
  const filters = [
    { id: 'union', label: 'UNION', rows: unionRows },
    { id: 'intersect', label: 'INTERSECT', rows: intersectRows }
  ];
  return buildDataTransform('Set operations', columns, beforeRows, filters, 'set_rows');
};

const buildSchemaBuilder = (lesson, context) => {
  const ddl = extractCreateTable(context.sql) || { table: context.tables[0] || 'new_table', columns: [] };
  const table = ddl.table || context.tables[0] || 'new_table';
  const columns = ddl.columns.length ? ddl.columns.slice(0, 3) : ['id', 'name'];
  const slots = [];
  const columnDefs = columns.map((col, idx) => {
    const slotId = `type_${idx}`;
    const options = col.toLowerCase().includes('id')
      ? ['INT', 'UUID', 'TEXT']
      : col.toLowerCase().includes('date')
        ? ['DATE', 'TIMESTAMP', 'TEXT']
        : ['TEXT', 'INT', 'BOOLEAN'];
    slots.push({ id: slotId, label: `${col} type`, options, correct: options[0] });
    return `${col} {{${slotId}}}`;
  });
  const template = `CREATE TABLE ${table} ( ${columnDefs.join(', ')} );`;
  return buildTokenSlot(template, slots);
};

const buildMutationSandbox = (lesson, context) => {
  const table = context.tables[0] || 'items';
  const columns = context.selectCols.length ? context.selectCols : ['id', 'status'];
  const beforeRows = buildRows(columns, { rowCount: 3 });
  const insertRow = { ...beforeRows[0], id: 4, status: 'new' };
  const updateRows = beforeRows.map((row, idx) => idx === 0 ? { ...row, status: 'updated' } : row);
  const deleteRows = beforeRows.slice(1);
  const filters = [
    { id: 'insert', label: `INSERT into ${table}`, rows: [...beforeRows, insertRow] },
    { id: 'update', label: `UPDATE ${table}`, rows: updateRows },
    { id: 'delete', label: `DELETE from ${table}`, rows: deleteRows }
  ];
  return buildDataTransform('Mutation sandbox', columns, beforeRows, filters, 'mutations_applied');
};

const buildCrossJoinMatrix = (lesson, context) => {
  const columns = ['color', 'size'];
  const beforeRows = [
    { color: 'red', size: null },
    { color: 'blue', size: null }
  ];
  const crossRows = [
    { color: 'red', size: 'S' },
    { color: 'red', size: 'M' },
    { color: 'blue', size: 'S' },
    { color: 'blue', size: 'M' }
  ];
  const innerRows = [
    { color: 'red', size: 'S' }
  ];
  const filters = [
    { id: 'cross', label: 'CROSS JOIN', rows: crossRows },
    { id: 'inner', label: 'INNER JOIN', rows: innerRows }
  ];
  return buildDataTransform('Cross join matrix', columns, beforeRows, filters, 'cross_rows');
};

const buildAggregationWorkbench = (lesson, context) => {
  const table = context.tables[0] || 'orders';
  const groupCol = sanitizeColumn(context.groupCols[0], context.selectCols[0] || 'status');
  const valueCol = context.selectCols.find((c) => c !== groupCol) || 'amount';
  const slots = [
    {
      id: 'group_col',
      label: 'Group by',
      options: [groupCol, 'region', 'category'].filter((v, idx, arr) => arr.indexOf(v) === idx),
      correct: groupCol
    },
    {
      id: 'agg_fn',
      label: 'Aggregate',
      options: ['COUNT', 'SUM', 'AVG'],
      correct: 'COUNT'
    }
  ];
  const template = `SELECT {{group_col}}, {{agg_fn}}(${valueCol}) FROM ${table} GROUP BY {{group_col}};`;
  return buildTokenSlot(template, slots);
};

const buildCaseMapper = (lesson, context) => {
  const condition = parseCondition(context.where);
  const column = (condition && condition.column) || context.selectCols[0] || 'status';
  const value = (condition && condition.value) || 'vip';
  const prompt = `Which rows map to the TRUE branch of CASE WHEN ${column} = ${value}?`;
  const choices = [
    { label: `${column} = ${value}`, outcome: 'true' },
    { label: `${column} != ${value}`, outcome: 'false' }
  ];
  return buildConditionalPath(prompt, choices, `Label = ${value}`, 'Label = other');
};

const buildDeduperLens = (lesson, context) => {
  const columns = context.selectCols.length ? context.selectCols : ['customer_id', 'email'];
  const targetCol = columns[0];
  const beforeRows = buildRows(columns, {
    rowCount: 4,
    overrides: {
      [targetCol]: ['A1', 'A1', 'B2', 'C3']
    }
  });
  const keepFirst = [beforeRows[0], beforeRows[2], beforeRows[3]];
  const keepLatest = [beforeRows[1], beforeRows[2], beforeRows[3]];
  const filters = [
    { id: 'keep_first', label: 'Keep first occurrence', rows: keepFirst },
    { id: 'keep_latest', label: 'Keep latest occurrence', rows: keepLatest }
  ];
  return buildDataTransform('Deduplicate rows', columns, beforeRows, filters, 'dedupe_rows');
};

const buildSubqueryScopeExplorer = (lesson, context) => {
  const table = context.tables[0] || 'orders';
  const code = [
    `SELECT * FROM ${table}`,
    `WHERE amount > (SELECT AVG(amount) FROM ${table});`
  ].join('\\n');
  const steps = [
    { line: 2, description: 'Run subquery to compute AVG(amount).' },
    { line: 1, description: `Filter ${table} rows using subquery result.` }
  ];
  return buildStepExecutor(code, steps);
};

const buildPlanForArchetype = (archetype, lesson, context) => {
  switch (archetype) {
    case 'SchemaGraphBuilder':
      return buildSchemaGraphBuilder(lesson, context);
    case 'WindowTimeline':
      return buildWindowTimeline(lesson, context);
    case 'JoinVisualizer':
      return buildJoinVisualizer(lesson, context);
    case 'FilterAnimator':
      return buildFilterAnimator(lesson, context);
    case 'SortLimitScrubber':
      return buildSortLimitScrubber(lesson, context);
    case 'CTEStepper':
      return buildCTEStepper(lesson, context);
    case 'NullLogicLab':
      return buildNullLogicLab(lesson, context);
    case 'QueryExecutionTimeline':
      return buildQueryExecutionTimeline(lesson, context);
    case 'SetOpsVenn':
      return buildSetOpsVenn(lesson, context);
    case 'SchemaBuilder':
      return buildSchemaBuilder(lesson, context);
    case 'MutationSandbox':
      return buildMutationSandbox(lesson, context);
    case 'CrossJoinMatrix':
      return buildCrossJoinMatrix(lesson, context);
    case 'AggregationWorkbench':
      return buildAggregationWorkbench(lesson, context);
    case 'CaseMapper':
      return buildCaseMapper(lesson, context);
    case 'DeduperLens':
      return buildDeduperLens(lesson, context);
    case 'SubqueryScopeExplorer':
      return buildSubqueryScopeExplorer(lesson, context);
    case 'QueryBuilderSlots':
    default:
      return buildQueryBuilderSlots(lesson, context);
  }
};

const recommendations = parseRecommendations(recommendationsText);
const sqlLessonIds = getSqlLessonIds();

let updated = 0;
const missing = [];

sqlLessonIds.forEach((lessonId) => {
  const lesson = lessons[lessonId];
  if (!lesson) {
    missing.push(lessonId);
    return;
  }
  const archetype = recommendations.get(lessonId) || 'QueryBuilderSlots';
  const sql = pickSqlSource(lesson);
  let tables = extractTables(sql);
  if (!tables.length) {
    tables = inferTablesFromTitle(lesson.title);
  }
  let selectCols = extractSelectColumns(sql);
  if (!selectCols.length) {
    selectCols = inferColumnsFromTitle(lesson.title);
  }
  const context = {
    sql,
    tables,
    joinKeys: extractJoinKeys(sql),
    selectCols,
    where: extractWhereClause(sql),
    groupCols: extractGroupByColumns(sql),
    orderCols: extractOrderByColumns(sql)
  };
  const plan = buildPlanForArchetype(archetype, lesson, context);
  lesson.interaction_plan = plan;
  lesson.interaction_recipe_id = `sql_${slugify(archetype)}`;
  lesson.interaction_required = true;
  if (lesson.send_to_editor_template) {
    delete lesson.send_to_editor_template;
  }
  updated += 1;
});

fs.writeFileSync(lessonsPath, JSON.stringify(lessons, null, 2));

const summary = {
  updated,
  totalSqlLessons: sqlLessonIds.length,
  missingLessons: missing
};

fs.writeFileSync(
  path.resolve(__dirname, '../scripts/sql_interaction_update_report.json'),
  JSON.stringify(summary, null, 2)
);

console.log(`Updated ${updated}/${sqlLessonIds.length} SQL lessons.`);
if (missing.length) {
  console.log(`Missing lessons: ${missing.join(', ')}`);
}
