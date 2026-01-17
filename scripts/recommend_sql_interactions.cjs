const fs = require("fs");
const path = require("path");

const args = process.argv.slice(2);

const readArg = (name) => {
  const prefix = `--${name}=`;
  const direct = args.find((arg) => arg.startsWith(prefix));
  if (direct) return direct.slice(prefix.length);
  const index = args.indexOf(`--${name}`);
  if (index !== -1 && args[index + 1]) return args[index + 1];
  return null;
};

const format = (readArg("format") || "md").toLowerCase(); // md|tsv|json
const maxRaw = readArg("max");
const max = maxRaw ? Number(maxRaw) : null;
const chapterFilterRaw = readArg("chapter");
const chapterFilter = chapterFilterRaw ? String(chapterFilterRaw) : null;
const noHeader = (readArg("noHeader") || "").toLowerCase() === "1" || args.includes("--noHeader");

const dataDir = path.resolve(__dirname, "../frontend/public/data");
const lessons = require(path.join(dataDir, "lessons.json"));
const course = require(path.join(dataDir, "course-sql-fundamentals.json"));

// Avoid crashing when piping into `head`/`tail`.
process.stdout.on("error", (err) => {
  if (err && err.code === "EPIPE") {
    process.exit(0);
  }
});

const stripHtml = (input) =>
  (input || "")
    .replace(/<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<script[\s\S]*?<\/script>/gi, " ")
    .replace(/<\/?[^>]+>/g, " ")
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/\s+/g, " ")
    .trim();

const extractCodeBlocks = (content) => {
  const text = content || "";
  const blocks = [];
  const fence = /```(?:sql)?\s*([\s\S]*?)```/gi;
  let match;
  while ((match = fence.exec(text))) {
    blocks.push(match[1].trim());
  }
  return blocks;
};

const pickSqlSource = (lesson) => {
  const sources = [];
  if (lesson && typeof lesson.starter_code === "string" && lesson.starter_code.trim()) {
    sources.push(lesson.starter_code);
  }
  if (lesson && typeof lesson.solution_code === "string" && lesson.solution_code.trim()) {
    sources.push(lesson.solution_code);
  }
  extractCodeBlocks(lesson && lesson.content).forEach((b) => sources.push(b));
  const combined = sources.join("\n\n").trim();
  return combined;
};

const stripSqlComments = (sql) =>
  (sql || "")
    // Line comments
    .replace(/--.*$/gm, "")
    // Block comments
    .replace(/\/\*[\s\S]*?\*\//g, "");

const uniq = (arr) => Array.from(new Set(arr));

const extractTables = (sql) => {
  const found = [];
  const normalized = stripSqlComments(sql).replace(/\s+/g, " ");
  const stop = new Set(["the", "a", "an", "your", "this", "that", "these", "those"]);
  const reserved = new Set([
    "select",
    "from",
    "join",
    "where",
    "group",
    "order",
    "limit",
    "having",
    "with",
    "create",
    "insert",
    "update",
    "delete",
    "into",
    "values",
    "on",
    "as"
  ]);
  const tablePattern =
    /\b(from|join|update|into|delete\s+from)\s+(?:the\s+|a\s+|an\s+)?([`"[]?)([a-zA-Z_][\w.]*)([`"\]]?)/gi;
  let match;
  while ((match = tablePattern.exec(normalized))) {
    const table = match[3];
    if (stop.has(table.toLowerCase())) continue;
    if (reserved.has(table.toLowerCase())) continue;
    found.push(table);
  }
  const ddl = normalized.match(/\bcreate\s+table\s+([`"[]?)([a-zA-Z_][\w.]*)([`"\]]?)/i);
  if (ddl && ddl[2]) found.push(ddl[2]);
  return uniq(found);
};

const extractJoinKeys = (sql) => {
  const found = [];
  const normalized = stripSqlComments(sql).replace(/\s+/g, " ");
  const onPattern = /\bon\s+([a-zA-Z_][\w.]*)\s*=\s*([a-zA-Z_][\w.]*)/gi;
  let match;
  while ((match = onPattern.exec(normalized))) {
    found.push(`${match[1]} = ${match[2]}`);
  }
  return uniq(found);
};

const extractGroupByCols = (sql) => {
  const normalized = stripSqlComments(sql).replace(/\s+/g, " ");
  const match = normalized.match(/\bgroup\s+by\s+(.+?)(\border\s+by\b|\bhaving\b|\blimit\b|;|$)/i);
  if (!match) return [];
  const normalizeCol = (raw) => {
    const cleaned = raw.trim().replace(/\s+/g, " ");
    const tokens = cleaned.split(" ").filter(Boolean);
    return tokens.slice(0, 1).join(" ");
  };
  return uniq(
    match[1]
      .split(",")
      .map((s) => normalizeCol(s))
      .filter(Boolean)
      .slice(0, 4)
  );
};

const extractOrderByCols = (sql) => {
  const normalized = stripSqlComments(sql).replace(/\s+/g, " ");
  const match = normalized.match(/\border\s+by\s+(.+?)(\blimit\b|;|$)/i);
  if (!match) return [];
  const normalizeCol = (raw) => {
    const cleaned = raw.trim().replace(/\s+/g, " ");
    const tokens = cleaned.split(" ").filter(Boolean);
    if (!tokens.length) return "";
    const dir = tokens[1] && /^(asc|desc)$/i.test(tokens[1]) ? ` ${tokens[1].toUpperCase()}` : "";
    return `${tokens[0]}${dir}`;
  };
  return uniq(
    match[1]
      .split(",")
      .map((s) => normalizeCol(s))
      .filter(Boolean)
      .slice(0, 4)
  );
};

const has = (sql, re) => re.test(sql || "");

const detectFeatures = (sql, plainTitle, plainContent) => {
  const haystack = `${sql || ""}\n${plainTitle || ""}\n${plainContent || ""}`;
  return {
    ddl:
      has(haystack, /\bcreate\s+table\b/i) ||
      has(haystack, /\balter\s+table\b/i) ||
      has(haystack, /\bcreate\s+view\b/i) ||
      has(haystack, /\bcreate\s+index\b/i),
    dml: has(haystack, /\binsert\s+into\b/i) || has(haystack, /\bupdate\b/i) || has(haystack, /\bdelete\s+from\b/i),
    join: has(haystack, /\b(join|left\s+join|right\s+join|inner\s+join|full\s+outer\s+join|cross\s+join)\b/i),
    crossJoin: has(haystack, /\bcross\s+join\b/i),
    where: has(haystack, /\bwhere\b/i),
    groupBy: has(haystack, /\bgroup\s+by\b/i),
    having: has(haystack, /\bhaving\b/i),
    orderBy: has(haystack, /\border\s+by\b/i),
    limit: has(haystack, /\blimit\b/i) || has(haystack, /\btop\s+\d+\b/i),
    distinct: has(haystack, /\bdistinct\b/i),
    case: has(haystack, /\bcase\b/i),
    cte: has(haystack, /\bwith\s+[a-zA-Z_]\w*\s+as\s*\(/i),
    window: has(haystack, /\bover\s*\(/i) || has(haystack, /\brow_number\s*\(/i) || has(haystack, /\brank\s*\(/i),
    setOps: has(haystack, /\bunion\b/i) || has(haystack, /\bintersect\b/i) || has(haystack, /\bexcept\b/i),
    nulls:
      has(haystack, /\bnull\b/i) ||
      has(haystack, /\bis\s+null\b/i) ||
      has(haystack, /\bis\s+not\s+null\b/i) ||
      has(haystack, /\bcoalesce\s*\(/i),
    subquery: has(haystack, /\(\s*select\b/i) || has(haystack, /\bexists\s*\(/i),
    executionOrder: has(haystack, /\bexecution\s+order\b/i) || has(haystack, /\border\s+of\s+execution\b/i)
  };
};

const chooseArchetype = (features, title) => {
  const lower = (title || "").toLowerCase();
  if (features.executionOrder || lower.includes("execution order")) return "QueryExecutionTimeline";
  if (lower.includes("primary key") || lower.includes("foreign key") || lower.includes("relationships")) return "SchemaGraphBuilder";
  if (features.ddl) return "SchemaBuilder";
  if (features.dml) return "MutationSandbox";
  if (features.window) return "WindowTimeline";
  if (features.setOps) return "SetOpsVenn";
  if (features.crossJoin) return "CrossJoinMatrix";
  if (features.join) return "JoinVisualizer";
  if (features.cte && (lower.includes("cte") || !features.join)) return "CTEStepper";
  if (features.groupBy || features.having) return "AggregationWorkbench";
  if (features.case) return "CaseMapper";
  if (features.orderBy || features.limit) return "SortLimitScrubber";
  if (features.distinct) return "DeduperLens";
  if (features.nulls && features.where) return "NullLogicLab";
  if (features.where) return "FilterAnimator";
  if (features.subquery) return "SubqueryScopeExplorer";
  return "QueryBuilderSlots";
};

const buildDescription = (archetype, ctx) => {
  const tables = ctx.tables.length ? ctx.tables.slice(0, 3) : ["your_table"];
  const joinKeys = ctx.joinKeys.length ? ctx.joinKeys.slice(0, 2) : [];
  const groupCols = ctx.groupCols.length ? ctx.groupCols : [];
  const orderCols = ctx.orderCols.length ? ctx.orderCols : [];

  const tableHint = tables.length ? tables.join(", ") : "tables";
  const joinHint = joinKeys.length ? joinKeys.join(" • ") : "matching keys";
  const groupHint = groupCols.length ? groupCols.join(", ") : "your group columns";
  const orderHint = orderCols.length ? orderCols.join(", ") : "your sort keys";

  switch (archetype) {
    case "QueryExecutionTimeline":
      return `Timeline simulator: step through FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER; intermediate result preview updates (uses ${tableHint}).`;
    case "SchemaGraphBuilder":
      return `Schema graph builder: click-to-connect PK→FK edges between ${tableHint}; cardinality + NULLability badges update; goal is a valid relationship map.`;
    case "SchemaBuilder":
      return `DDL builder: assemble columns/types/constraints for ${tableHint}; invalid constraints highlight; generated CREATE TABLE updates live.`;
    case "MutationSandbox":
      return `Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny ${tableHint} table; row diffs animate; goal matches target final table state.`;
    case "WindowTimeline":
      return `Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.`;
    case "CTEStepper":
      return `CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.`;
    case "SetOpsVenn":
      return `Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.`;
    case "CrossJoinMatrix":
      return `Cross-join matrix: click rows/cols to generate combinations; product grid fills; goal matches expected number of combinations and sample rows.`;
    case "JoinVisualizer":
      return `Join visualizer: connect rows via ${joinHint}; toggle join type; output table updates and unmatched rows highlight (tables: ${tableHint}).`;
    case "AggregationWorkbench":
      return `Aggregation workbench: drag ${groupHint} into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.`;
    case "CaseMapper":
      return `CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.`;
    case "SortLimitScrubber":
      return `Sort/limit scrubber: pick ${orderHint} + direction, then adjust LIMIT slider; preview table reorders instantly; goal matches target first N rows.`;
    case "DeduperLens":
      return `Deduper lens: highlight duplicates and select a “keep rule” (latest/highest/first); removed rows fade; goal matches deduped output.`;
    case "NullLogicLab":
      return `NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.`;
    case "FilterAnimator":
      return `Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.`;
    case "SubqueryScopeExplorer":
      return `Subquery scope explorer: expand/collapse subquery panels; see each subquery result as a mini-table; goal is correct final joined/filtered output.`;
    case "QueryBuilderSlots":
    default:
      return `Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: ${tableHint}).`;
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
          conceptName: "Boss",
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
  // Preserve declared order: chapter order then concept order then lesson.order.
  return items;
};

const recommend = (lessonId, meta) => {
  const lesson = lessons[String(lessonId)];
  const title = (lesson && lesson.title) || meta.title || "";
  const plainContent = stripHtml(lesson && lesson.content);
  const sql = pickSqlSource(lesson);
  const features = detectFeatures(sql, title, plainContent);
  const tables = extractTables(sql);
  const joinKeys = extractJoinKeys(sql);
  const groupCols = extractGroupByCols(sql);
  const orderCols = extractOrderByCols(sql);

  const archetype = chooseArchetype(features, title);
  const description = buildDescription(archetype, { tables, joinKeys, groupCols, orderCols });

  return {
    lesson_id: String(lessonId),
    chapter_id: String(meta.chapterId),
    chapter_title: meta.chapterTitle,
    concept: meta.conceptName,
    title,
    archetype,
    tables,
    description
  };
};

const main = () => {
  const flattened = flattenCourse();
  const output = [];
  for (const item of flattened) {
    const lessonId = item.lessonId;
    const metaTitle = (() => {
      // course file redundantly stores a lesson title; keep as fallback only.
      const chapter = course.chapters.find((c) => String(c.id) === String(item.chapterId));
      const concept = chapter && (chapter.concepts || []).find((cc) => cc.name === item.conceptName);
      const lesson = concept && (concept.lessons || []).find((l) => String(l.id) === lessonId);
      return (lesson && lesson.title) || "";
    })();
    const rec = recommend(lessonId, { ...item, title: metaTitle });
    output.push(rec);
    if (max && output.length >= max) break;
  }

  if (format === "json") {
    process.stdout.write(JSON.stringify(output, null, 2));
    return;
  }

  if (format === "tsv") {
    if (!noHeader) {
      process.stdout.write(
        ["lesson_id", "chapter_id", "chapter_title", "concept", "title", "archetype", "tables", "recommendation"].join("\t") + "\n"
      );
    }
    output.forEach((rec) => {
      const row = [
        rec.lesson_id,
        rec.chapter_id,
        rec.chapter_title,
        rec.concept,
        rec.title,
        rec.archetype,
        rec.tables.join(","),
        rec.description
      ];
      process.stdout.write(row.map((cell) => String(cell || "").replace(/\t/g, " ")).join("\t") + "\n");
    });
    return;
  }

  // md
  const byChapter = new Map();
  output.forEach((rec) => {
    const key = `${rec.chapter_id}:${rec.chapter_title}`;
    if (!byChapter.has(key)) byChapter.set(key, []);
    byChapter.get(key).push(rec);
  });

  const lines = [];
  if (!noHeader) {
    lines.push("# SQL Interactive Element Recommendations");
    lines.push("");
    lines.push(
      "Each row is a per-exercise, concept-aligned interactive system recommendation, tailored using the exercise title/content and starter SQL (tables/joins/groups/clauses)."
    );
    lines.push("");
  }
  for (const [key, recs] of byChapter.entries()) {
    const [chapterId, chapterTitle] = key.split(":");
    lines.push(`## Chapter ${chapterId}: ${chapterTitle}`);
    lines.push("");
    recs.forEach((rec) => {
      lines.push(`- ${rec.lesson_id} — ${rec.title} — **${rec.archetype}**: ${rec.description}`);
    });
    lines.push("");
  }
  process.stdout.write(lines.join("\n").trimEnd() + "\n");
};

main();
