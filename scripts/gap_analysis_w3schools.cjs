const fs = require('fs');
const path = require('path');

const lessonsPath = path.resolve(__dirname, '../frontend/public/data/lessons.json');
const pythonCoursePath = path.resolve(__dirname, '../frontend/public/data/course-python-basics.json');
const sqlCoursePath = path.resolve(__dirname, '../frontend/public/data/course-sql-fundamentals.json');
const topicsPath = path.resolve(__dirname, './w3schools_topics.json');

const lessons = JSON.parse(fs.readFileSync(lessonsPath, 'utf8'));
const pythonCourse = JSON.parse(fs.readFileSync(pythonCoursePath, 'utf8'));
const sqlCourse = JSON.parse(fs.readFileSync(sqlCoursePath, 'utf8'));
const topics = JSON.parse(fs.readFileSync(topicsPath, 'utf8'));

const STOPWORDS = new Set([
  'python',
  'sql',
  'tutorial',
  'home',
  'intro',
  'introduction',
  'get',
  'started',
  'basics',
  'overview',
  'exercise',
  'exercises',
  'quiz',
  'example',
  'examples',
  'reference',
  'reference',
  'server',
  'compiler',
  'practice',
  'lesson',
  'lessons',
  'to',
  'of',
  'in',
  'on',
  'for',
  'the',
  'a',
  'an',
  'with',
  'using',
  'by'
]);

const normalize = (value) =>
  String(value || '')
    .toLowerCase()
    .replace(/python|sql/g, '')
    .replace(/[^a-z0-9]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();

const SINGULAR_EXCEPTIONS = new Set(['class', 'glass', 'boss', 'pass']);

const tokenize = (value) => {
  const normalized = normalize(value);
  if (!normalized) return [];
  const tokens = [];
  normalized.split(' ').forEach((token) => {
    if (!token || STOPWORDS.has(token)) return;
    tokens.push(token);
    if (
      token.length > 3 &&
      token.endsWith('s') &&
      !token.endsWith('ss') &&
      !SINGULAR_EXCEPTIONS.has(token)
    ) {
      tokens.push(token.slice(0, -1));
    }
  });
  return tokens;
};

const jaccard = (aTokens, bTokens) => {
  if (!aTokens.length || !bTokens.length) return 0;
  const a = new Set(aTokens);
  const b = new Set(bTokens);
  let intersection = 0;
  a.forEach((token) => {
    if (b.has(token)) intersection += 1;
  });
  const union = a.size + b.size - intersection;
  return union === 0 ? 0 : intersection / union;
};

const getChapterLessonIds = (chapter) => {
  const ids = [];
  if (!chapter) return ids;
  if (Array.isArray(chapter.lessons)) {
    chapter.lessons.forEach((lesson) => ids.push(String(lesson.id)));
    return ids;
  }
  (chapter.concepts || []).forEach((concept) => {
    (concept.lessons || []).forEach((lesson) => ids.push(String(lesson.id)));
  });
  return ids;
};

const buildLessonIndex = (course) => {
  const lessonRows = [];
  (course.chapters || []).forEach((chapter) => {
    const chapterId = String(chapter.id);
    const chapterTitle = chapter.title || `Chapter ${chapterId}`;
    const lessonIds = getChapterLessonIds(chapter);
    lessonIds.forEach((lessonId) => {
      const lesson = lessons[String(lessonId)];
      if (!lesson) return;
      const title = lesson.title || '';
      lessonRows.push({
        id: String(lessonId),
        title,
        chapterId,
        chapterTitle,
        normalized: normalize(title),
        tokens: tokenize(title)
      });
    });
  });
  return lessonRows;
};

const pythonLessons = buildLessonIndex(pythonCourse);
const sqlLessons = buildLessonIndex(sqlCourse);

const chapterTokenIndex = (lessonRows) => {
  const map = new Map();
  lessonRows.forEach((row) => {
    const key = `${row.chapterId}:${row.chapterTitle}`;
    if (!map.has(key)) {
      map.set(key, { chapterId: row.chapterId, chapterTitle: row.chapterTitle, tokens: [] });
    }
    map.get(key).tokens.push(...row.tokens);
  });
  const chapters = [];
  map.forEach((value) => {
    const tokenCounts = value.tokens.reduce((acc, token) => {
      acc[token] = (acc[token] || 0) + 1;
      return acc;
    }, {});
    chapters.push({
      chapterId: value.chapterId,
      chapterTitle: value.chapterTitle,
      tokens: Object.keys(tokenCounts)
    });
  });
  return chapters;
};

const pythonChapters = chapterTokenIndex(pythonLessons);
const sqlChapters = chapterTokenIndex(sqlLessons);

const categoryRules = {
  python: [
    { key: 'syntax', match: ['syntax', 'statement', 'indent'] },
    { key: 'output', match: ['output', 'print'] },
    { key: 'comments', match: ['comment'] },
    { key: 'variables', match: ['variable', 'assign', 'names', 'global'] },
    { key: 'types', match: ['type', 'datatype', 'numbers', 'casting', 'bytes', 'bytearray'] },
    { key: 'strings', match: ['string', 'format', 'f-string', 'slice', 'strings'] },
    { key: 'booleans', match: ['boolean', 'bool'] },
    { key: 'operators', match: ['operator', 'arithmetic', 'comparison', 'logical'] },
    { key: 'lists', match: ['list', 'lists', 'array', 'list comprehension'] },
    { key: 'tuples', match: ['tuple'] },
    { key: 'sets', match: ['set'] },
    { key: 'dicts', match: ['dict', 'dictionary', 'dictionaries'] },
    { key: 'conditionals', match: ['if', 'elif', 'else', 'condition'] },
    { key: 'loops', match: ['loop', 'loops', 'while', 'for', 'range', 'break', 'continue'] },
    { key: 'functions', match: ['function', 'functions', 'lambda', 'return', 'scope'] },
    { key: 'oop', match: ['class', 'classes', 'object', 'objects', 'inherit', 'inheritance', 'polymorph', 'init'] },
    { key: 'modules', match: ['module', 'package', 'pip', 'import'] },
    { key: 'files', match: ['file', 'read', 'write', 'open'] },
    { key: 'exceptions', match: ['exception', 'error', 'try', 'except'] },
    { key: 'iterators', match: ['iterator', 'iterators', 'generator', 'generators', 'yield'] },
    { key: 'dates', match: ['date', 'time', 'datetime'] },
    { key: 'math', match: ['math'] },
    { key: 'json', match: ['json'] },
    { key: 'regex', match: ['regex', 'regexp'] },
    { key: 'input', match: ['input', 'user input'] }
  ],
  sql: [
    { key: 'select', match: ['select'] },
    { key: 'where', match: ['where', 'filter', 'and', 'or', 'not', 'between', 'like', 'in'] },
    { key: 'order', match: ['order', 'limit', 'top', 'offset'] },
    { key: 'distinct', match: ['distinct'] },
    { key: 'join', match: ['join', 'inner', 'left', 'right', 'full'] },
    { key: 'group', match: ['group', 'aggregate', 'count', 'sum', 'avg', 'min', 'max'] },
    { key: 'having', match: ['having'] },
    { key: 'insert', match: ['insert'] },
    { key: 'update', match: ['update'] },
    { key: 'delete', match: ['delete'] },
    { key: 'ddl', match: ['create', 'alter', 'drop', 'database', 'table'] },
    { key: 'constraints', match: ['constraint', 'primary key', 'foreign key', 'unique', 'check'] },
    { key: 'indexes', match: ['index'] },
    { key: 'views', match: ['view'] },
    { key: 'subqueries', match: ['subquery'] },
    { key: 'setops', match: ['union', 'intersect', 'except'] },
    { key: 'case', match: ['case', 'when', 'then'] },
    { key: 'transactions', match: ['transaction', 'commit', 'rollback'] },
    { key: 'stored_procedures', match: ['procedure', 'stored'] },
    { key: 'functions', match: ['function'] }
  ]
};

const categoryGuidance = {
  python: {
    syntax: {
      why: 'Syntax rules are a major source of early errors; clarity here reduces confusion later.',
      proposed: 'Add a short “indentation + statement boundaries” callout and a common mistake example.',
      size: 'S',
      risk: 'low',
      impact: 4
    },
    output: {
      why: 'Printing output is the first feedback loop learners rely on.',
      proposed: 'Add a small exercise that prints mixed types and explains newline behavior.',
      size: 'S',
      risk: 'low',
      impact: 4
    },
    comments: {
      why: 'Comments teach reading and maintainability early.',
      proposed: 'Add a brief example showing inline vs block comments and when to use each.',
      size: 'S',
      risk: 'low',
      impact: 2
    },
    variables: {
      why: 'Variables underpin all later work; naming and scope errors are common.',
      proposed: 'Add naming rules, a “rename safely” example, and a scope pitfall note.',
      size: 'M',
      risk: 'low',
      impact: 5
    },
    types: {
      why: 'Type confusion causes subtle bugs and misunderstandings about operations.',
      proposed: 'Add casting examples and a “type mismatch” pitfall exercise.',
      size: 'M',
      risk: 'low',
      impact: 4
    },
    strings: {
      why: 'String operations show indexing and immutability early.',
      proposed: 'Add slicing and formatting examples plus a short transformation exercise.',
      size: 'M',
      risk: 'low',
      impact: 4
    },
    booleans: {
      why: 'Booleans drive conditionals; weak understanding breaks branching.',
      proposed: 'Add a truth-table mini example and a comparison pitfall.',
      size: 'S',
      risk: 'low',
      impact: 3
    },
    operators: {
      why: 'Operator precedence and comparisons are a frequent error source.',
      proposed: 'Add a precedence example and a “parentheses fix” exercise.',
      size: 'M',
      risk: 'low',
      impact: 3
    },
    lists: {
      why: 'Lists are core data structures; mutation and indexing must be clear.',
      proposed: 'Add before/after mutation examples and a small list update exercise.',
      size: 'M',
      risk: 'low',
      impact: 4
    },
    tuples: {
      why: 'Immutable sequences appear in unpacking and function returns.',
      proposed: 'Add unpacking example and a “why tuples” contrast note.',
      size: 'S',
      risk: 'low',
      impact: 3
    },
    sets: {
      why: 'Sets teach uniqueness and membership efficiently.',
      proposed: 'Add membership checks and a “dedupe” example.',
      size: 'S',
      risk: 'low',
      impact: 3
    },
    dicts: {
      why: 'Dictionaries are used everywhere; key errors are common.',
      proposed: 'Add get() vs [] and a missing-key pitfall.',
      size: 'M',
      risk: 'low',
      impact: 4
    },
    conditionals: {
      why: 'Branching is a core reasoning skill for programs.',
      proposed: 'Add a multi-branch example and a “boundary case” exercise.',
      size: 'M',
      risk: 'low',
      impact: 5
    },
    loops: {
      why: 'Loop control and range boundaries are high-friction for beginners.',
      proposed: 'Add an off-by-one example and a small accumulator exercise.',
      size: 'M',
      risk: 'low',
      impact: 5
    },
    functions: {
      why: 'Functions enable reuse; parameter/return confusion is common.',
      proposed: 'Add an input/output tracing example and a “return vs print” exercise.',
      size: 'M',
      risk: 'low',
      impact: 5
    },
    oop: {
      why: 'OOP is conceptually dense; learners often mix up class vs instance state.',
      proposed: 'Add a state diagram example and a “class vs instance” pitfall.',
      size: 'L',
      risk: 'med',
      impact: 4
    },
    modules: {
      why: 'Imports and packages unlock real workflows.',
      proposed: 'Add a tiny “import + call” exercise and clarify pip vs import.',
      size: 'M',
      risk: 'low',
      impact: 4
    },
    files: {
      why: 'File I/O is required for practical scripting.',
      proposed: 'Add a read/write example and a path handling note.',
      size: 'M',
      risk: 'med',
      impact: 4
    },
    exceptions: {
      why: 'Error handling builds resilience and debugging skills.',
      proposed: 'Add try/except structure + common errors exercise.',
      size: 'M',
      risk: 'low',
      impact: 4
    },
    iterators: {
      why: 'Iteration protocol explains for-loops and generators.',
      proposed: 'Add iterator example with iter()/next().',
      size: 'M',
      risk: 'med',
      impact: 3
    },
    dates: {
      why: 'Dates/times are common in real data tasks.',
      proposed: 'Add basic datetime parsing example.',
      size: 'S',
      risk: 'low',
      impact: 3
    },
    math: {
      why: 'Math utilities are used across problem solving.',
      proposed: 'Add a brief import + function example.',
      size: 'S',
      risk: 'low',
      impact: 2
    },
    json: {
      why: 'JSON is the most common data interchange format.',
      proposed: 'Add load/dump example and a nested object exercise.',
      size: 'M',
      risk: 'low',
      impact: 4
    },
    regex: {
      why: 'Pattern matching is powerful but error-prone.',
      proposed: 'Add a simple search vs match contrast.',
      size: 'M',
      risk: 'med',
      impact: 3
    },
    input: {
      why: 'Input enables interactive scripts and reinforces types.',
      proposed: 'Add input() + type casting exercise.',
      size: 'S',
      risk: 'low',
      impact: 3
    },
    default: {
      why: 'This topic appears in W3Schools and should be addressed for completeness.',
      proposed: 'Add a short example and one targeted exercise aligned to the topic.',
      size: 'S',
      risk: 'low',
      impact: 2
    }
  },
  sql: {
    select: {
      why: 'SELECT is the backbone of querying.',
      proposed: 'Add a focused example with column selection and aliasing.',
      size: 'S',
      risk: 'low',
      impact: 5
    },
    where: {
      why: 'Filtering rows correctly is foundational for all analysis.',
      proposed: 'Add a multi-condition example and a “common filter mistakes” note.',
      size: 'M',
      risk: 'low',
      impact: 4
    },
    order: {
      why: 'Sorting and limiting results are common in real queries.',
      proposed: 'Add an ORDER BY + LIMIT example and a stable ordering note.',
      size: 'S',
      risk: 'low',
      impact: 4
    },
    distinct: {
      why: 'DISTINCT prevents accidental double counting.',
      proposed: 'Add a duplicate-removal example and a warning about DISTINCT + aggregates.',
      size: 'S',
      risk: 'low',
      impact: 4
    },
    join: {
      why: 'Joins are the core relational skill; errors are frequent.',
      proposed: 'Add a join diagram explanation and a “missing matches” pitfall.',
      size: 'L',
      risk: 'med',
      impact: 5
    },
    group: {
      why: 'Aggregations are core to analytics queries.',
      proposed: 'Add a simple group/aggregate example and a grouping pitfall.',
      size: 'M',
      risk: 'low',
      impact: 5
    },
    having: {
      why: 'HAVING is often confused with WHERE.',
      proposed: 'Add a side-by-side WHERE vs HAVING example.',
      size: 'S',
      risk: 'low',
      impact: 4
    },
    insert: {
      why: 'DML is essential for data maintenance.',
      proposed: 'Add a multi-row INSERT example.',
      size: 'S',
      risk: 'low',
      impact: 4
    },
    update: {
      why: 'Unsafe updates are a common production mistake.',
      proposed: 'Add a “missing WHERE” caution and a targeted update exercise.',
      size: 'M',
      risk: 'med',
      impact: 4
    },
    delete: {
      why: 'Deletes are dangerous without filters.',
      proposed: 'Add a “confirm rows first” tip and a safe delete exercise.',
      size: 'M',
      risk: 'med',
      impact: 4
    },
    ddl: {
      why: 'DDL defines structure and constraints; it is required for schema work.',
      proposed: 'Add a CREATE TABLE example with constraints and data types.',
      size: 'M',
      risk: 'med',
      impact: 4
    },
    constraints: {
      why: 'Constraints enforce data integrity and prevent bad data.',
      proposed: 'Add PRIMARY KEY and FOREIGN KEY examples with a why note.',
      size: 'M',
      risk: 'med',
      impact: 4
    },
    indexes: {
      why: 'Indexes explain performance tradeoffs.',
      proposed: 'Add a short “when to index” example and caution.',
      size: 'S',
      risk: 'low',
      impact: 3
    },
    views: {
      why: 'Views encapsulate complex queries for reuse.',
      proposed: 'Add a CREATE VIEW example and a simple use case.',
      size: 'S',
      risk: 'low',
      impact: 3
    },
    subqueries: {
      why: 'Subqueries enable powerful filtering and comparisons.',
      proposed: 'Add a SELECT ... WHERE IN (subquery) example.',
      size: 'M',
      risk: 'med',
      impact: 4
    },
    setops: {
      why: 'UNION/INTERSECT/EXCEPT broaden query composition.',
      proposed: 'Add a UNION example and a column compatibility note.',
      size: 'M',
      risk: 'low',
      impact: 3
    },
    case: {
      why: 'CASE adds conditional logic inside SQL.',
      proposed: 'Add a CASE-based categorization example.',
      size: 'S',
      risk: 'low',
      impact: 3
    },
    transactions: {
      why: 'Transactions protect data integrity for multi-step changes.',
      proposed: 'Add BEGIN/COMMIT/ROLLBACK example and safety note.',
      size: 'M',
      risk: 'med',
      impact: 4
    },
    stored_procedures: {
      why: 'Procedures are common in production systems.',
      proposed: 'Add a short explanation and a placeholder example.',
      size: 'M',
      risk: 'high',
      impact: 3
    },
    functions: {
      why: 'Built-in SQL functions are used constantly.',
      proposed: 'Add 2-3 function examples and a quick exercise.',
      size: 'M',
      risk: 'low',
      impact: 3
    },
    default: {
      why: 'This topic appears in W3Schools and should be addressed for completeness.',
      proposed: 'Add a short example and one targeted exercise aligned to the topic.',
      size: 'S',
      risk: 'low',
      impact: 2
    }
  }
};

const detectCategory = (language, title) => {
  const lower = title.toLowerCase();
  const tokens = tokenize(title);
  const rules = categoryRules[language];
  for (const rule of rules) {
    if (
      rule.match.some((token) =>
        token.includes(' ') ? lower.includes(token) : tokens.includes(token)
      )
    ) {
      return rule.key;
    }
  }
  if (language === 'sql') {
    const trimmed = normalize(title);
    if (['and', 'or', 'not', 'between', 'like', 'in'].includes(trimmed)) {
      return 'where';
    }
  }
  return 'default';
};

const pickGuidance = (language, category) =>
  categoryGuidance[language][category] || categoryGuidance[language].default;

const bestChapterForTopic = (topicTokens, chapters) => {
  if (!topicTokens.length && chapters.length) {
    return { ...chapters[0], score: 1 };
  }
  let best = null;
  chapters.forEach((chapter) => {
    const score = jaccard(topicTokens, chapter.tokens);
    if (!best || score > best.score) {
      best = { ...chapter, score };
    }
  });
  if (best && best.score > 0) return best;
  return chapters.length ? { ...chapters[0], score: 0 } : null;
};

const matchTopicToLessons = (topicTitle, lessonRows) => {
  const topicTokens = tokenize(topicTitle);
  const topicNormalized = normalize(topicTitle);
  const candidates = lessonRows.map((lesson) => {
    const score = jaccard(topicTokens, lesson.tokens);
    const exact =
      topicNormalized &&
      (lesson.normalized === topicNormalized ||
        lesson.normalized.includes(topicNormalized) ||
        topicNormalized.includes(lesson.normalized));
    return { ...lesson, score, exact };
  });
  candidates.sort((a, b) => b.score - a.score);
  const top = candidates[0];

  let status = 'Missing';
  if (top && (top.exact || top.score >= 0.75)) {
    status = 'Covered';
  } else if (top && top.score >= 0.35) {
    status = 'Partially Covered';
  }

  return {
    status,
    topicTokens,
    matches: candidates.filter((c) => c.score > 0).slice(0, 3),
    bestContext: top
  };
};

const shouldSkipTopic = (language, title) => {
  const lower = String(title || '').toLowerCase();
  const exclude = [
    'home',
    'compiler',
    'quiz',
    'exercise',
    'exercises',
    'certificate',
    'training',
    'bootcamp',
    'interview',
    'exam',
    'study plan',
    'syllabus',
    'server',
    'hosting',
    'jobs',
    'account',
    'profile',
    'login',
    'signup'
  ];
  if (exclude.some((term) => lower.includes(term))) return true;
  if (language === 'sql' && (lower.includes('keywords') || lower.includes('reference'))) return true;
  return false;
};

const buildGapList = (language, topicsList, lessonRows, chapters) => {
  const results = [];
  const filtered = topicsList
    .filter((topic) => !shouldSkipTopic(language, topic.title))
    .filter((topic, idx, arr) => {
      const normalized = normalize(topic.title);
      return arr.findIndex((item) => normalize(item.title) === normalized) === idx;
    });
  filtered.forEach((topic, index) => {
    const match = matchTopicToLessons(topic.title, lessonRows);
    const category = detectCategory(language, topic.title);
    const guidance = pickGuidance(language, category);
    const gapIdPrefix = language === 'python' ? 'PY' : 'SQL';
    const gapId = `${gapIdPrefix}-${String(index + 1).padStart(3, '0')}`;
    const chapterTarget =
      match.status === 'Missing'
        ? bestChapterForTopic(match.topicTokens, chapters)
        : null;
    results.push({
      gap_id: gapId,
      topic_title: topic.title,
      topic_url: topic.url,
      status: match.status,
      category,
      matches: match.matches,
      best_context: match.bestContext,
      chapter_target: chapterTarget,
      why: guidance.why,
      proposed_changes: guidance.proposed,
      size: guidance.size,
      risk: guidance.risk,
      impact_weight: guidance.impact
    });
  });
  return results;
};

const pythonGaps = buildGapList('python', topics.python || [], pythonLessons, pythonChapters);
const sqlGaps = buildGapList('sql', topics.sql || [], sqlLessons, sqlChapters);

const topicAdjustments = [
  { match: /bytearray|bytes/, delta: -10 },
  { match: /access list|change list|add list|remove list/, delta: -5 },
  { match: /variable names|global variables|assign multiple values/, delta: 5 },
  { match: /join|group by|having|subquery|transaction|index|view|constraint|primary key|foreign key/, delta: 5 },
  { match: /function|lambda/, delta: 4 },
  { match: /loop|while|for/, delta: 4 },
  { match: /condition|if|else/, delta: 3 }
];

const rankUpgrades = (gaps, limit = 20) => {
  const scored = gaps.map((gap) => {
    const statusWeight = gap.status === 'Missing' ? 20 : gap.status === 'Partially Covered' ? 10 : 0;
    let score = gap.impact_weight * 10 + statusWeight;
    const lowerTitle = gap.topic_title.toLowerCase();
    topicAdjustments.forEach((adjustment) => {
      if (adjustment.match.test(lowerTitle)) {
        score += adjustment.delta;
      }
    });
    const targetLessonIds = gap.matches.map((match) => match.id);
    const target =
      targetLessonIds.length > 0
        ? targetLessonIds.join(', ')
        : gap.best_context
          ? `${gap.best_context.id} (${gap.best_context.title})`
          : gap.chapter_target
            ? `${gap.chapter_target.chapterId} (${gap.chapter_target.chapterTitle})`
            : 'TBD';
    return {
      gap_id: gap.gap_id,
      topic_title: gap.topic_title,
      status: gap.status,
      impact_score: score,
      size: gap.size,
      risk: gap.risk,
      target
    };
  });
  scored.sort((a, b) => b.impact_score - a.impact_score);
  return scored.slice(0, limit);
};

const formatGapSection = (title, gaps) => {
  const lines = [`## ${title}`];
  gaps.forEach((gap) => {
    const matchText = gap.matches.length
      ? gap.matches
          .map((match) => `${match.id} (${match.title})`)
          .join(', ')
      : 'None';
    const insertText = gap.chapter_target
      ? `${gap.chapter_target.chapterId} (${gap.chapter_target.chapterTitle})`
      : 'TBD';
    lines.push('');
    lines.push(`- gap_id: ${gap.gap_id}`);
    lines.push(`  topic: ${gap.topic_title}`);
    lines.push(`  status: ${gap.status}`);
    lines.push(`  covered_by: ${matchText}`);
    lines.push(`  insert_target: ${gap.status === 'Missing' ? insertText : 'N/A'}`);
    lines.push(`  why_it_matters: ${gap.why}`);
    lines.push(`  proposed_changes: ${gap.proposed_changes}`);
  });
  return lines.join('\n');
};

const formatUpgradeList = (title, upgrades) => {
  const lines = [`## ${title}`];
  upgrades.forEach((item, idx) => {
    lines.push(
      `${idx + 1}. ${item.gap_id} | ${item.topic_title} | impact=${item.impact_score} | size=${item.size} | risk=${item.risk} | target=${item.target}`
    );
  });
  return lines.join('\n');
};

const reportLines = [
  '# W3Schools Gap Analysis (Reference Benchmark)',
  '',
  'This report maps W3Schools topics to existing lessons. No new chapters or W3Schools-labeled sections are proposed.',
  '',
  'Impact rubric:',
  '- impact_score = (category_weight 1-5) * 10 + status_weight (Missing=20, Partial=10, Covered=0)',
  '- size S/M/L indicates expected effort per lesson update',
  '- risk indicates likelihood of unintended pacing or conceptual regression',
  '',
  'Legend:',
  '- Covered: A strong direct match exists in current lessons.',
  '- Partially Covered: Some overlap exists, but the topic needs reinforcement or a missing sub-concept.',
  '- Missing: No clear lesson covers this topic; suggest insertion point.',
  '',
  formatUpgradeList('Top 20 Highest-Impact Upgrades (Python + SQL)', [
    ...rankUpgrades([...pythonGaps, ...sqlGaps], 20)
  ]),
  '',
  formatGapSection('Python Topic Coverage', pythonGaps),
  '',
  formatGapSection('SQL Topic Coverage', sqlGaps),
  '',
  '## Rules For Applying Upgrades',
  '- Prefer merging into existing lessons before adding new lessons.',
  '- New chapters are allowed only when a topic is completely missing, too large to insert into one chapter, and requires multiple lessons.',
  '- Do not create W3Schools-labeled sections.',
  '- Every change must reference the gap_id it addresses.',
  '- Provide per-lesson diff summaries and a small changelog per batch.'
];

const reportPath = path.resolve(__dirname, '../w3schools_gap_analysis_report.md');
const jsonPath = path.resolve(__dirname, '../w3schools_gap_analysis.json');

fs.writeFileSync(reportPath, reportLines.join('\n'));
fs.writeFileSync(jsonPath, JSON.stringify({ python: pythonGaps, sql: sqlGaps }, null, 2));

console.log(`Wrote ${reportPath} and ${jsonPath}`);
