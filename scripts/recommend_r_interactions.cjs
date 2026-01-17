const path = require('path');

const args = process.argv.slice(2);

const readArg = (name) => {
  const prefix = `--${name}=`;
  const direct = args.find((arg) => arg.startsWith(prefix));
  if (direct) return direct.slice(prefix.length);
  const index = args.indexOf(`--${name}`);
  if (index !== -1 && args[index + 1]) return args[index + 1];
  return null;
};

const format = (readArg('format') || 'md').toLowerCase(); // md|tsv|json
const maxRaw = readArg('max');
const max = maxRaw ? Number(maxRaw) : null;
const chapterFilterRaw = readArg('chapter');
const chapterFilter = chapterFilterRaw ? String(chapterFilterRaw) : null;
const noHeader = (readArg('noHeader') || '').toLowerCase() === '1' || args.includes('--noHeader');

const dataDir = path.resolve(__dirname, '../frontend/public/data');
const lessons = require(path.join(dataDir, 'lessons.json'));
const course = require(path.join(dataDir, 'course-r-fundamentals.json'));

// Avoid crashing when piping into `head`/`tail`.
process.stdout.on('error', (err) => {
  if (err && err.code === 'EPIPE') process.exit(0);
});

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
  while ((match = fence.exec(text))) {
    blocks.push(match[1].trim());
  }
  return blocks;
};

const pickRSource = (lesson) => {
  const sources = [];
  if (lesson && typeof lesson.starter_code === 'string' && lesson.starter_code.trim()) sources.push(lesson.starter_code);
  if (lesson && typeof lesson.solution_code === 'string' && lesson.solution_code.trim()) sources.push(lesson.solution_code);
  extractCodeBlocks(lesson && lesson.content).forEach((b) => sources.push(b));
  return sources.join('\n\n').trim();
};

const uniq = (arr) => Array.from(new Set(arr));

const extractDatasets = (code) => {
  const sql = code || '';
  const found = [];
  const ggplot = /ggplot\s*\(\s*(?:data\s*=\s*)?([a-zA-Z_]\w*)/gi;
  let m;
  while ((m = ggplot.exec(sql))) found.push(m[1]);
  const pipeStart = /^\s*([a-zA-Z_]\w*)\s*(?:%>%|\|>)/gm;
  while ((m = pipeStart.exec(sql))) found.push(m[1]);
  const bare = /^\s*([a-zA-Z_]\w*)\s*$/gm;
  while ((m = bare.exec(sql))) {
    const name = m[1];
    if (!['library', 'ggplot', 'filter', 'select', 'mutate', 'summarise', 'summarize'].includes(name)) {
      found.push(name);
    }
  }
  return uniq(found).slice(0, 4);
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
  const x = pick('x');
  const y = pick('y');
  const color = pick('color');
  const fill = pick('fill');
  const shape = pick('shape');
  return { x, y, color, fill, shape };
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

const detect = (code, title, plainContent, tags, ops) => {
  const codeHay = String(code || '');
  const textHay = `${title || ''}\n${plainContent || ''}`;
  const tagSet = new Set((tags || []).map((t) => String(t).toLowerCase()));
  const hasTag = (t) => tagSet.has(String(t).toLowerCase());
  const codeRe = (r) => r.test(codeHay);
  const textRe = (r) => r.test(textHay);
  const hasOp = (op) => (ops || []).includes(op);
  return {
    ggplot: codeRe(/\bggplot\s*\(/i) || codeRe(/\bgeom_/i) || codeRe(/\baes\s*\(/i),
    dplyr:
      codeRe(/\b(filter|select|mutate|summarise|summarize|group_by|arrange|count|distinct)\s*\(/i) ||
      (tags || []).some((t) => String(t).toLowerCase().startsWith('dplyr_')),
    joins: codeRe(/\b(left_join|inner_join|right_join|full_join)\s*\(/i) || hasTag('join'),
    pivots: codeRe(/\b(pivot_longer|pivot_wider)\s*\(/i),
    pipe: codeRe(/%>%|\|>/),
    vectors: codeRe(/\bc\s*\(/i) || codeRe(/\bseq\s*\(/i) || codeRe(/\brep\s*\(/i) || codeRe(/\b:\s*\d/),
    indexing: codeRe(/\b[a-zA-Z_]\w*\s*\[[^\]]+\]/),
    functionDef: codeRe(/\bfunction\s*\(/i) || hasTag('functions'),
    ifElse: codeRe(/\bif\s*\(|\bifelse\s*\(/i) || codeRe(/\bcase_when\s*\(/i) || hasTag('conditionals'),
    loops: codeRe(/\bfor\s*\(|\bwhile\s*\(/i),
    factors: codeRe(/\bfactor\s*\(|\blevels\s*\(/i) || codeRe(/\brelevel\s*\(/i) || hasTag('factors'),
    dates: codeRe(/\bas\.date\s*\(|\bymd\s*\(|\bfloor_date\s*\(/i) || textRe(/\bdate\b/i) || hasTag('dates'),
    strings: codeRe(/\bstr_\w+\s*\(/i) || codeRe(/\bpaste\s*\(/i) || codeRe(/\bsprintf\s*\(/i) || hasTag('strings'),
    stats:
      codeRe(/\blm\s*\(|\bglm\s*\(|\bt\.test\s*\(|\bcor\s*\(/i) ||
      codeRe(/\b(mean|median|sd|var)\s*\(/i) ||
      hasTag('statistics'),
    debug: textRe(/\bfix the code\b/i) || textRe(/\berror\b/i) || textRe(/\bbroken\b/i),
    filterOp: hasOp('filter'),
    mutateOp: hasOp('mutate'),
    groupByOp: hasOp('group_by') || hasOp('summarise') || hasOp('summarize'),
    caseWhenOp: codeRe(/\bcase_when\s*\(/i),
    arrangeOp: hasOp('arrange')
  };
};

const chooseArchetype = (features, title) => {
  const lower = String(title || '').toLowerCase();
  if (lower.includes('fix the code') || features.debug) return 'DebugQuestR';
  if (lower.includes('quarto') || lower.includes('yaml') || lower.includes('qmd')) return 'StringWorkbench';
  if (features.functionDef || lower.includes('function')) return 'FunctionScopeStepper';
  if (features.joins) return 'JoinVisualizer';
  if (features.pivots) return 'PivotAnimator';
  if (features.ggplot) return 'AesMappingBuilder';
  if (features.dplyr && features.stats && features.pipe) return 'PipelineStepper';
  if (features.dplyr && features.pipe && (features.ifElse || features.caseWhenOp || lower.includes('case'))) return 'CaseBranchMapper';
  if (features.dplyr && features.pipe && (features.groupByOp || lower.includes('group'))) return 'GroupSummarizeWorkbench';
  if (features.dplyr && features.pipe && features.mutateOp) return 'MutateFactory';
  if (features.dplyr && (features.filterOp || lower.includes('filter') || lower.includes('rows'))) return 'FilterAnimator';
  if (features.stats) return 'StatWhatIfLab';
  if (features.ifElse) return 'ConditionalPath';
  if (features.loops) return 'LoopSimulator';
  if (features.functionDef) return 'FunctionScopeStepper';
  if (features.vectors || features.indexing) return 'VectorIndexPlayground';
  if (features.factors) return 'FactorLevelsRack';
  if (features.dates) return 'TimeBucketingWorkbench';
  if (features.strings) return 'StringWorkbench';
  return 'DatasetExplorer';
};

const describe = (archetype, ctx) => {
  const dataset = ctx.datasets[0] || 'your_dataset';
  const aesBits = [];
  if (ctx.aes.x) aesBits.push(`x=${ctx.aes.x}`);
  if (ctx.aes.y) aesBits.push(`y=${ctx.aes.y}`);
  if (ctx.aes.color) aesBits.push(`color=${ctx.aes.color}`);
  if (ctx.aes.fill) aesBits.push(`fill=${ctx.aes.fill}`);

  const dplyrOps = ctx.ops.length ? ctx.ops.slice(0, 4).join(' → ') : null;

  switch (archetype) {
    case 'DatasetExplorer':
      return `Visual table explorer: preview ${dataset}, toggle column highlights, and click rows to see how “observations vs variables” behave.`;
    case 'AesMappingBuilder':
      return `Aesthetic mapping puzzle: fill the {{x}}, {{y}}, and {{color/fill}} slots for ggplot(${dataset}, aes(...)); the plot preview updates as you swap mappings (${aesBits.join(', ') || 'x/y/color'}).`;
    case 'FilterAnimator':
      return `Filter animator: toggle filter chips (predicate on ${dataset}) and watch rows animate in/out; success = correct remaining rows for the prompt.`;
    case 'MutateFactory':
      return `Mutate factory: choose an expression for a new column; “before/after” table updates and highlights the changed cells for ${dataset}.`;
    case 'GroupSummarizeWorkbench':
      return `Group+summarise workbench: drag a grouping column into the GROUP slot and choose an aggregate; groups and summary table update for ${dataset}.`;
    case 'JoinVisualizer':
      return `Join visualizer: connect matching keys between two tables and toggle join type; result table updates and unmatched rows highlight.`;
    case 'PivotAnimator':
      return `Pivot animator: pick key/value columns to pivot_longer/wider; table morphs between wide↔long with highlighted moved cells.`;
    case 'PipelineStepper':
      return `Pipeline stepper: step through each |> stage (${dplyrOps || 'transformations'}) and watch the intermediate table after each operation.`;
    case 'CaseBranchMapper':
      return `CASE/ifelse branch mapper: choose which condition routes rows to each branch; rows flow into TRUE/FALSE bins with immediate labeling feedback.`;
    case 'TimeBucketingWorkbench':
      return `Time bucketing workbench: select a date floor/round granularity; grouped counts update (day/week/month) and the table preview re-buckets.`;
    case 'StatWhatIfLab':
      return `Stats what-if lab: use a slider to change sample size/parameter; summary stats update live (mean/SD/CI), with a simple visualization reacting immediately.`;
    case 'VectorIndexPlayground':
      return `Vector index playground: click indices (1-based) and see the selected elements + resulting vector update; goal checks exact slice/replacement.`;
    case 'FactorLevelsRack':
      return `Factor levels rack: reorder/select levels and watch counts (or color mapping) update; success = correct reference level/order.`;
    case 'StringWorkbench':
      return `String workbench: slot the correct string function/regex token and see transformed outputs update immediately for sample inputs.`;
    case 'FunctionScopeStepper':
      return `Function scope stepper: step through a function call; show argument binding + local variables changing at each line (state inspector updates).`;
    case 'LoopSimulator':
      return `Loop simulator: animate iterations and show accumulator state at each step; success = reach the target final value without off-by-one.`;
    case 'ConditionalPath':
      return `Conditional path: choose inputs/conditions and watch which branch lights up; success = route specific cases to the correct branch.`;
    case 'DebugQuestR':
      return `Debug quest: pick the correct fix for a broken R snippet; the “run” result and error message update instantly until it passes.`;
    default:
      return `Interactive exercise: constrained manipulations update a live preview and enforce a clear success state.`;
  }
};

const flattenCourse = () => {
  const items = [];
  course.chapters.forEach((chapter) => {
    if (chapterFilter && String(chapter.id) !== chapterFilter) return;
    if (Array.isArray(chapter.lessons)) {
      chapter.lessons.forEach((lesson) => {
        items.push({
          chapterId: chapter.id,
          chapterTitle: chapter.title,
          conceptName: 'Boss',
          lessonId: String(lesson.id),
          order: lesson.order
        });
      });
      return;
    }
    (chapter.concepts || []).forEach((concept) => {
      (concept.lessons || []).forEach((lesson) => {
        items.push({
          chapterId: chapter.id,
          chapterTitle: chapter.title,
          conceptName: concept.name,
          lessonId: String(lesson.id),
          order: lesson.order
        });
      });
    });
  });
  return items;
};

const recommend = (lessonId, meta) => {
  const lesson = lessons[String(lessonId)];
  const title = (lesson && lesson.title) || meta.title || '';
  const plainContent = stripHtml(lesson && lesson.content);
  const code = pickRSource(lesson);
  const datasets = extractDatasets(code).length ? extractDatasets(code) : extractDatasets(plainContent);
  const aes = extractAes(code);
  const ops = extractDplyrOps(code);
  const tags = (lesson && lesson.concept_tags) || [];
  const features = detect(code, title, plainContent, tags, ops);
  const archetype = chooseArchetype(features, title);
  const description = describe(archetype, { datasets, aes, ops });

  return {
    lesson_id: String(lessonId),
    chapter_id: String(meta.chapterId),
    chapter_title: meta.chapterTitle,
    concept: meta.conceptName,
    title,
    archetype,
    datasets,
    recommendation: description
  };
};

const main = () => {
  const flattened = flattenCourse();
  const out = [];
  for (const item of flattened) {
    const lessonId = item.lessonId;
    const fallbackTitle = (() => {
      const chapter = course.chapters.find((c) => String(c.id) === String(item.chapterId));
      const concept = chapter && (chapter.concepts || []).find((cc) => cc.name === item.conceptName);
      const lesson = concept && (concept.lessons || []).find((l) => String(l.id) === lessonId);
      return (lesson && lesson.title) || '';
    })();
    out.push(recommend(lessonId, { ...item, title: fallbackTitle }));
    if (max && out.length >= max) break;
  }

  if (format === 'json') {
    process.stdout.write(JSON.stringify(out, null, 2));
    return;
  }

  if (format === 'tsv') {
    if (!noHeader) {
      process.stdout.write(['lesson_id', 'chapter_id', 'chapter_title', 'concept', 'title', 'archetype', 'datasets', 'recommendation'].join('\t') + '\n');
    }
    out.forEach((rec) => {
      const row = [
        rec.lesson_id,
        rec.chapter_id,
        rec.chapter_title,
        rec.concept,
        rec.title,
        rec.archetype,
        rec.datasets.join(','),
        rec.recommendation
      ];
      process.stdout.write(row.map((cell) => String(cell || '').replace(/\t/g, ' ')).join('\t') + '\n');
    });
    return;
  }

  // md
  const byChapter = new Map();
  out.forEach((rec) => {
    const key = `${rec.chapter_id}\u0000${rec.chapter_title}`;
    if (!byChapter.has(key)) byChapter.set(key, []);
    byChapter.get(key).push(rec);
  });

  const lines = [];
  if (!noHeader) {
    lines.push('# R Interactive Element Recommendations');
    lines.push('');
    lines.push('Generated from lesson content (`frontend/public/data/lessons.json`) and R course ordering (`frontend/public/data/course-r-fundamentals.json`).');
    lines.push('');
    lines.push('Each bullet is a per-exercise, concept-aligned interactive system recommendation, tailored using the exercise title/content and starter R code (datasets/pipelines/aesthetics).');
    lines.push('');
  }

  for (const [key, recs] of byChapter.entries()) {
    const [chapterId, chapterTitle] = key.split('\u0000');
    lines.push(`## Chapter ${chapterId}: ${chapterTitle}`);
    lines.push('');
    recs.forEach((rec) => {
      lines.push(`- ${rec.lesson_id} — ${rec.title} — **${rec.archetype}**: ${rec.recommendation}`);
    });
    lines.push('');
  }

  process.stdout.write(lines.join('\n').trimEnd() + '\n');
};

main();
