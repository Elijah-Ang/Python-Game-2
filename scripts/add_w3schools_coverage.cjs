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

const normalize = (value) =>
  String(value || '')
    .toLowerCase()
    .replace(/python|sql/g, '')
    .replace(/[^a-z0-9]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();

const getLessonIds = (course) => {
  const ids = [];
  (course.chapters || []).forEach((chapter) => {
    if (Array.isArray(chapter.lessons)) {
      chapter.lessons.forEach((lesson) => ids.push(String(lesson.id)));
      return;
    }
    (chapter.concepts || []).forEach((concept) => {
      (concept.lessons || []).forEach((lesson) => ids.push(String(lesson.id)));
    });
  });
  return ids;
};

const existingPythonTitles = new Set(
  getLessonIds(pythonCourse)
    .map((id) => lessons[id]?.title)
    .filter(Boolean)
    .map(normalize)
);

const existingSqlTitles = new Set(
  getLessonIds(sqlCourse)
    .map((id) => lessons[id]?.title)
    .filter(Boolean)
    .map(normalize)
);

const PYTHON_EXCLUDE = [
  'examples',
  'exercises',
  'quiz',
  'compiler',
  'server',
  'bootcamp',
  'certificate',
  'training',
  'study plan',
  'syllabus',
  'interview',
  'exam'
];

const SQL_EXCLUDE = [
  'examples',
  'quiz',
  'hosting'
];

const filterPython = (title) => {
  const lower = String(title || '').toLowerCase();
  if (PYTHON_EXCLUDE.some((term) => lower.includes(term))) return false;
  return true;
};

const filterSql = (title) => {
  const lower = String(title || '').toLowerCase();
  if (SQL_EXCLUDE.some((term) => lower.includes(term))) return false;
  return true;
};

const pythonConceptTags = (title) => {
  const lower = title.toLowerCase();
  if (lower.includes('string')) return ['strings'];
  if (lower.includes('list')) return ['lists'];
  if (lower.includes('tuple')) return ['tuples'];
  if (lower.includes('set')) return ['sets'];
  if (lower.includes('dict')) return ['dictionaries'];
  if (lower.includes('if') || lower.includes('else') || lower.includes('elif')) return ['conditionals'];
  if (lower.includes('loop') || lower.includes('while') || lower.includes('for')) return ['loops'];
  if (lower.includes('function') || lower.includes('lambda')) return ['functions'];
  if (lower.includes('class') || lower.includes('object') || lower.includes('inherit')) return ['classes'];
  if (lower.includes('file')) return ['files'];
  if (lower.includes('module') || lower.includes('package') || lower.includes('pip')) return ['modules'];
  if (lower.includes('json')) return ['json'];
  if (lower.includes('regex')) return ['regex'];
  if (lower.includes('exception') || lower.includes('try')) return ['errors'];
  if (lower.includes('date') || lower.includes('time')) return ['datetime'];
  if (lower.includes('math')) return ['math'];
  if (lower.includes('operator')) return ['operators'];
  if (lower.includes('boolean')) return ['booleans'];
  return ['basics'];
};

const sqlConceptTags = (title) => {
  const lower = title.toLowerCase();
  if (lower.includes('select')) return ['select'];
  if (lower.includes('where')) return ['where'];
  if (lower.includes('join')) return ['join'];
  if (lower.includes('group')) return ['group_by'];
  if (lower.includes('having')) return ['having'];
  if (lower.includes('insert')) return ['insert'];
  if (lower.includes('update')) return ['update'];
  if (lower.includes('delete')) return ['delete'];
  if (lower.includes('create') || lower.includes('alter') || lower.includes('drop')) return ['schema'];
  if (lower.includes('constraint')) return ['constraints'];
  if (lower.includes('index')) return ['index'];
  if (lower.includes('view')) return ['view'];
  if (lower.includes('null')) return ['nulls'];
  if (lower.includes('case')) return ['case'];
  if (lower.includes('union') || lower.includes('intersect') || lower.includes('except')) return ['set_ops'];
  if (lower.includes('aggregate') || lower.includes('sum') || lower.includes('avg') || lower.includes('count')) return ['aggregates'];
  if (lower.includes('operator')) return ['operators'];
  return ['sql_basics'];
};

const pythonTemplate = (title) => {
  const lower = title.toLowerCase();
  let content = `# ${title}\n\n## Overview\nThis lesson mirrors the W3Schools topic **${title}** with a concise example and a short practice task.\n`;
  let starter = '# TODO: follow the prompt below\n';
  let solution = '';

  if (lower.includes('string')) {
    content += '\n## Example\n```python\ntext = \"hello\"\nprint(text.upper())\n```\n';
    starter += 'text = \"python\"\n# Print the uppercase version\n';
    solution = 'text = \"python\"\\nprint(text.upper())';
  } else if (lower.includes('list')) {
    content += '\n## Example\n```python\nitems = [1, 2, 3]\nitems.append(4)\nprint(items)\n```\n';
    starter += 'items = [1, 2, 3]\n# Append 4 and print\n';
    solution = 'items = [1, 2, 3]\\nitems.append(4)\\nprint(items)';
  } else if (lower.includes('tuple')) {
    content += '\n## Example\n```python\ncoords = (3, 4)\nprint(coords[0])\n```\n';
    starter += 'coords = (10, 20)\n# Print the first value\n';
    solution = 'coords = (10, 20)\\nprint(coords[0])';
  } else if (lower.includes('set')) {
    content += '\n## Example\n```python\nvalues = {1, 2, 2, 3}\nprint(values)\n```\n';
    starter += 'values = {\"a\", \"b\", \"b\"}\n# Print the set\n';
    solution = 'values = {\"a\", \"b\", \"b\"}\\nprint(values)';
  } else if (lower.includes('dict')) {
    content += '\n## Example\n```python\nperson = {\"name\": \"Ava\", \"age\": 30}\nprint(person[\"name\"])\n```\n';
    starter += 'person = {\"name\": \"Ava\", \"age\": 30}\n# Print the name\n';
    solution = 'person = {\"name\": \"Ava\", \"age\": 30}\\nprint(person[\"name\"])';
  } else if (lower.includes('if') || lower.includes('else')) {
    content += '\n## Example\n```python\nscore = 72\nif score >= 70:\n    print(\"pass\")\nelse:\n    print(\"retry\")\n```\n';
    starter += 'score = 55\n# Print \"pass\" if score >= 60 else \"retry\"\n';
    solution = 'score = 55\\nif score >= 60:\\n    print(\"pass\")\\nelse:\\n    print(\"retry\")';
  } else if (lower.includes('loop') || lower.includes('while') || lower.includes('for')) {
    content += '\n## Example\n```python\nfor i in range(3):\n    print(i)\n```\n';
    starter += '# Print numbers 1 through 3\n';
    solution = 'for i in range(1, 4):\\n    print(i)';
  } else if (lower.includes('function') || lower.includes('lambda')) {
    content += '\n## Example\n```python\ndef add(a, b):\n    return a + b\nprint(add(2, 3))\n```\n';
    starter += '# Write a function multiply(a, b) that returns a*b\n';
    solution = 'def multiply(a, b):\\n    return a * b\\nprint(multiply(3, 4))';
  } else if (lower.includes('class') || lower.includes('object')) {
    content += '\n## Example\n```python\nclass Pet:\n    def __init__(self, name):\n        self.name = name\n\np = Pet(\"Milo\")\nprint(p.name)\n```\n';
    starter += 'class Pet:\\n    def __init__(self, name):\\n        self.name = name\\n\\n# Create a Pet named \"Luna\" and print the name\n';
    solution = 'class Pet:\\n    def __init__(self, name):\\n        self.name = name\\n\\np = Pet(\"Luna\")\\nprint(p.name)';
  } else if (lower.includes('file')) {
    content += '\n## Example\n```python\nwith open(\"notes.txt\", \"w\") as f:\n    f.write(\"hello\")\n```\n';
    starter += '# Open a file named \"log.txt\" in write mode and write \"ok\"\\n';
    solution = 'with open(\"log.txt\", \"w\") as f:\\n    f.write(\"ok\")';
  } else if (lower.includes('json')) {
    content += '\n## Example\n```python\nimport json\npayload = \"{\\\"x\\\": 1}\"\nprint(json.loads(payload)[\"x\"])\n```\n';
    starter += 'import json\\n# Parse the JSON string and print the value for \"x\"\\njson_text = \"{\\\"x\\\": 5}\"\\n';
    solution = 'import json\\njson_text = \"{\\\"x\\\": 5}\"\\nprint(json.loads(json_text)[\"x\"])';
  } else if (lower.includes('regex')) {
    content += '\n## Example\n```python\nimport re\nprint(bool(re.search(\"cat\", \"catnap\")))\n```\n';
    starter += 'import re\\n# Check if the word \"dog\" appears in the text\\ntext = \"hotdog\"\\n';
    solution = 'import re\\ntext = \"hotdog\"\\nprint(bool(re.search(\"dog\", text)))';
  } else if (lower.includes('exception') || lower.includes('try')) {
    content += '\n## Example\n```python\ntry:\n    1 / 0\nexcept ZeroDivisionError:\n    print(\"Cannot divide\")\n```\n';
    starter += '# Wrap the division in try/except and print \"bad\" on ZeroDivisionError\\n';
    solution = 'try:\\n    1 / 0\\nexcept ZeroDivisionError:\\n    print(\"bad\")';
  } else if (lower.includes('date') || lower.includes('time')) {
    content += '\n## Example\n```python\nfrom datetime import date\nprint(date.today())\n```\n';
    starter += 'from datetime import date\\n# Print today\\n';
    solution = 'from datetime import date\\nprint(date.today())';
  } else if (lower.includes('math')) {
    content += '\n## Example\n```python\nimport math\nprint(math.sqrt(25))\n```\n';
    starter += 'import math\\n# Print the square root of 81\\n';
    solution = 'import math\\nprint(math.sqrt(81))';
  } else if (lower.includes('operator')) {
    content += '\n## Example\n```python\nx = 4\nprint(x == 4)\n```\n';
    starter += 'x = 7\\n# Print whether x is greater than 5\\n';
    solution = 'x = 7\\nprint(x > 5)';
  } else {
    content += '\n## Example\n```python\nprint(\"Hello, Python\")\n```\n';
    starter += '# Print a greeting\\n';
    solution = 'print(\"Hello, Python\")';
  }

  return { content, starter, solution };
};

const sqlTemplate = (title) => {
  const lower = title.toLowerCase();
  let content = `# ${title}\\n\\n## Overview\\nThis lesson mirrors the W3Schools topic **${title}** with a short example and a practice query.\\n`;
  let starter = '-- TODO: write the query below\\n';
  let solution = '';

  if (lower.includes('select')) {
    content += '\\n## Example\\n```sql\\nSELECT name FROM customers;\\n```\\n';
    starter += 'SELECT ... FROM customers;\\n';
    solution = 'SELECT name FROM customers;';
  } else if (lower.includes('where')) {
    content += '\\n## Example\\n```sql\\nSELECT * FROM orders WHERE status = \"shipped\";\\n```\\n';
    starter += 'SELECT * FROM orders WHERE status = ...;\\n';
    solution = 'SELECT * FROM orders WHERE status = \"shipped\";';
  } else if (lower.includes('join')) {
    content += '\\n## Example\\n```sql\\nSELECT c.name, o.id\\nFROM customers c\\nJOIN orders o ON c.id = o.customer_id;\\n```\\n';
    starter += 'SELECT c.name, o.id\\nFROM customers c\\nJOIN orders o ON c.id = o.customer_id;\\n';
    solution = 'SELECT c.name, o.id\\nFROM customers c\\nJOIN orders o ON c.id = o.customer_id;';
  } else if (lower.includes('group by')) {
    content += '\\n## Example\\n```sql\\nSELECT status, COUNT(*)\\nFROM orders\\nGROUP BY status;\\n```\\n';
    starter += 'SELECT status, COUNT(*) FROM orders GROUP BY status;\\n';
    solution = 'SELECT status, COUNT(*) FROM orders GROUP BY status;';
  } else if (lower.includes('having')) {
    content += '\\n## Example\\n```sql\\nSELECT customer_id, COUNT(*)\\nFROM orders\\nGROUP BY customer_id\\nHAVING COUNT(*) > 5;\\n```\\n';
    starter += 'SELECT customer_id, COUNT(*)\\nFROM orders\\nGROUP BY customer_id\\nHAVING COUNT(*) > ...;\\n';
    solution = 'SELECT customer_id, COUNT(*)\\nFROM orders\\nGROUP BY customer_id\\nHAVING COUNT(*) > 5;';
  } else if (lower.includes('insert')) {
    content += '\\n## Example\\n```sql\\nINSERT INTO products (name, price) VALUES (\"Widget\", 25.00);\\n```\\n';
    starter += 'INSERT INTO products (name, price) VALUES (..., ...);\\n';
    solution = 'INSERT INTO products (name, price) VALUES (\"Widget\", 25.00);';
  } else if (lower.includes('update')) {
    content += '\\n## Example\\n```sql\\nUPDATE products SET price = 30 WHERE id = 1;\\n```\\n';
    starter += 'UPDATE products SET price = ... WHERE id = 1;\\n';
    solution = 'UPDATE products SET price = 30 WHERE id = 1;';
  } else if (lower.includes('delete')) {
    content += '\\n## Example\\n```sql\\nDELETE FROM orders WHERE status = \"cancelled\";\\n```\\n';
    starter += 'DELETE FROM orders WHERE status = ...;\\n';
    solution = 'DELETE FROM orders WHERE status = \"cancelled\";';
  } else if (lower.includes('create table')) {
    content += '\\n## Example\\n```sql\\nCREATE TABLE customers (id INT, name TEXT);\\n```\\n';
    starter += 'CREATE TABLE customers (id INT, name TEXT);\\n';
    solution = 'CREATE TABLE customers (id INT, name TEXT);';
  } else if (lower.includes('alter table')) {
    content += '\\n## Example\\n```sql\\nALTER TABLE customers ADD COLUMN city TEXT;\\n```\\n';
    starter += 'ALTER TABLE customers ADD COLUMN city TEXT;\\n';
    solution = 'ALTER TABLE customers ADD COLUMN city TEXT;';
  } else if (lower.includes('drop table')) {
    content += '\\n## Example\\n```sql\\nDROP TABLE old_data;\\n```\\n';
    starter += 'DROP TABLE old_data;\\n';
    solution = 'DROP TABLE old_data;';
  } else if (lower.includes('case')) {
    content += '\\n## Example\\n```sql\\nSELECT amount, CASE WHEN amount > 100 THEN \"high\" ELSE \"low\" END AS bucket\\nFROM payments;\\n```\\n';
    starter += 'SELECT amount, CASE WHEN amount > ... THEN \"high\" ELSE \"low\" END AS bucket\\nFROM payments;\\n';
    solution = 'SELECT amount, CASE WHEN amount > 100 THEN \"high\" ELSE \"low\" END AS bucket\\nFROM payments;';
  } else if (lower.includes('null')) {
    content += '\\n## Example\\n```sql\\nSELECT * FROM users WHERE email IS NULL;\\n```\\n';
    starter += 'SELECT * FROM users WHERE email IS NULL;\\n';
    solution = 'SELECT * FROM users WHERE email IS NULL;';
  } else if (lower.includes('union')) {
    content += '\\n## Example\\n```sql\\nSELECT name FROM customers\\nUNION\\nSELECT name FROM leads;\\n```\\n';
    starter += 'SELECT name FROM customers UNION SELECT name FROM leads;\\n';
    solution = 'SELECT name FROM customers UNION SELECT name FROM leads;';
  } else if (lower.includes('view')) {
    content += '\\n## Example\\n```sql\\nCREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;\\n```\\n';
    starter += 'CREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;\\n';
    solution = 'CREATE VIEW active_users AS SELECT * FROM users WHERE active = 1;';
  } else if (lower.includes('index')) {
    content += '\\n## Example\\n```sql\\nCREATE INDEX idx_users_email ON users(email);\\n```\\n';
    starter += 'CREATE INDEX idx_users_email ON users(email);\\n';
    solution = 'CREATE INDEX idx_users_email ON users(email);';
  } else if (lower.includes('data types')) {
    content += '\\n## Example\\n```sql\\nCREATE TABLE items (id INT, name TEXT, price DECIMAL(10,2));\\n```\\n';
    starter += 'CREATE TABLE items (id INT, name TEXT, price DECIMAL(10,2));\\n';
    solution = 'CREATE TABLE items (id INT, name TEXT, price DECIMAL(10,2));';
  } else {
    content += '\\n## Example\\n```sql\\n-- Example placeholder\\n```\\n';
    starter += '-- Write a SQL example for this topic\\n';
    solution = '-- Example placeholder';
  }

  return { content, starter, solution };
};

const addLesson = (id, title, content, starter, solution, chapterId, chapterTitle, tags) => {
  lessons[String(id)] = {
    id,
    title,
    content,
    starter_code: starter,
    solution_code: solution,
    chapter_id: chapterId,
    chapter_title: chapterTitle,
    concept_tags: tags,
    interaction_confidence: 1,
    manual_review: false
  };
};

const addChapterIfMissing = (course, chapterId, title) => {
  const exists = (course.chapters || []).some((ch) => String(ch.id) === String(chapterId));
  if (exists) return;
  course.chapters.push({
    id: chapterId,
    title,
    icon: '📚',
    is_boss: false,
    concepts: [
      {
        name: 'W3Schools Coverage',
        icon: '📘',
        lessons: []
      }
    ]
  });
};

const appendLessonToChapter = (course, chapterId, lessonId, title) => {
  const chapter = course.chapters.find((ch) => String(ch.id) === String(chapterId));
  if (!chapter) return;
  const concept = chapter.concepts[0];
  const order = concept.lessons.length + 1;
  concept.lessons.push({ id: Number(lessonId), title, order });
};

const addPythonCoverage = () => {
  const chapterId = 150;
  const chapterTitle = 'W3Schools Coverage: Python';
  addChapterIfMissing(pythonCourse, chapterId, chapterTitle);

  const startId = 26000;
  let nextId = startId;
  let added = 0;

  topics.python.forEach((topic) => {
    if (!filterPython(topic.title)) return;
    const key = normalize(topic.title);
    if (!key) return;
    if (existingPythonTitles.has(key)) return;
    const template = pythonTemplate(topic.title);
    addLesson(nextId, topic.title, template.content, template.starter, template.solution, chapterId, chapterTitle, pythonConceptTags(topic.title));
    appendLessonToChapter(pythonCourse, chapterId, nextId, topic.title);
    existingPythonTitles.add(key);
    nextId += 1;
    added += 1;
  });

  return added;
};

const addSqlCoverage = () => {
  const chapterId = 215;
  const chapterTitle = 'W3Schools Coverage: SQL';
  addChapterIfMissing(sqlCourse, chapterId, chapterTitle);

  const startId = 27000;
  let nextId = startId;
  let added = 0;

  topics.sql.forEach((topic) => {
    if (!filterSql(topic.title)) return;
    const key = normalize(topic.title);
    if (!key) return;
    if (existingSqlTitles.has(key)) return;
    const template = sqlTemplate(topic.title);
    addLesson(nextId, topic.title, template.content, template.starter, template.solution, chapterId, chapterTitle, sqlConceptTags(topic.title));
    appendLessonToChapter(sqlCourse, chapterId, nextId, topic.title);
    existingSqlTitles.add(key);
    nextId += 1;
    added += 1;
  });

  return added;
};

const pythonAdded = addPythonCoverage();
const sqlAdded = addSqlCoverage();

fs.writeFileSync(lessonsPath, JSON.stringify(lessons, null, 2));
fs.writeFileSync(pythonCoursePath, JSON.stringify(pythonCourse, null, 2));
fs.writeFileSync(sqlCoursePath, JSON.stringify(sqlCourse, null, 2));

const report = {
  python_added: pythonAdded,
  sql_added: sqlAdded
};

fs.writeFileSync(path.resolve(__dirname, './w3schools_coverage_report.json'), JSON.stringify(report, null, 2));
console.log(`Added ${pythonAdded} Python lessons and ${sqlAdded} SQL lessons from W3Schools coverage.`);
