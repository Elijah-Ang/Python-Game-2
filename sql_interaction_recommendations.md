# SQL Interactive Element Recommendations

Generated from lesson content (`frontend/public/data/lessons.json`) and SQL course ordering (`frontend/public/data/course-sql-fundamentals.json`).

Each bullet is a per-exercise, concept-aligned interactive system recommendation, tailored using the exercise title/content and starter SQL (tables/joins/groups/clauses).

## Chapter 200: Setup & Mental Model

- 1001 — What is a Database? — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: your_table).
- 1002 — Tables, Rows, and Columns — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: employees).
- 1003 — Primary Keys — **SchemaGraphBuilder**: Schema graph builder: click-to-connect PK→FK edges between customers; cardinality + NULLability badges update; goal is a valid relationship map.
- 1162 — Quiz: Window Functions I — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1163 — Quiz: Window Functions II — **JoinVisualizer**: Join visualizer: connect rows via c.id = o.customer_id; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders).
- 1004 — Foreign Keys & Relationships — **SchemaGraphBuilder**: Schema graph builder: click-to-connect PK→FK edges between orders; cardinality + NULLability badges update; goal is a valid relationship map.
- 1005 — SQL is Declarative — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1006 — Result Sets — **SortLimitScrubber**: Sort/limit scrubber: pick your sort keys + direction, then adjust LIMIT slider; preview table reorders instantly; goal matches target first N rows.
- 1164 — Quiz: Window Functions III — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1165 — Quiz: CTEs I — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.
- 1007 — NULL Basics — **NullLogicLab**: NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.
- 1008 — Schema Organization — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: sales, sales.orders, employees).
- 1009 — Query Execution Order — **QueryExecutionTimeline**: Timeline simulator: step through FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER; intermediate result preview updates (uses employees).
- 1166 — Quiz: CTEs II — **JoinVisualizer**: Join visualizer: connect rows via matching keys; toggle join type; output table updates and unmatched rows highlight (tables: employees).
- 1167 — Quiz: CTEs III — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.

## Chapter 201: SELECT Basics

- 1010 — Your First SELECT — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: users, table_name).
- 1011 — Selecting Multiple Columns — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: employees, customers).
- 1012 — SELECT All Columns — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: products, employees).
- 1168 — Quiz: Set Operations I — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1169 — Quiz: Set Operations II — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1013 — Column Aliases with AS — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: employees, users, products).
- 1014 — Table Aliases — **JoinVisualizer**: Join visualizer: connect rows via e.dept_id = d.id • a.manager_id = b.id; toggle join type; output table updates and unmatched rows highlight (tables: employees, departments).
- 1015 — LIMIT Clause — **SortLimitScrubber**: Sort/limit scrubber: pick salary DESC + direction, then adjust LIMIT slider; preview table reorders instantly; goal matches target first N rows.
- 1170 — Quiz: Set Operations III — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1171 — Quiz: Date/Time I — **SortLimitScrubber**: Sort/limit scrubber: pick id + direction, then adjust LIMIT slider; preview table reorders instantly; goal matches target first N rows.
- 1016 — WHERE Basics — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1017 — Comparison Operators — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1018 — IN Operator — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1172 — Quiz: Date/Time II — **CaseMapper**: CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.
- 1173 — Quiz: Date/Time III — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1019 — BETWEEN Operator — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1020 — LIKE Pattern Matching — **CaseMapper**: CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.
- 1021 — ORDER BY Sorting — **SortLimitScrubber**: Sort/limit scrubber: pick salary DESC + direction, then adjust LIMIT slider; preview table reorders instantly; goal matches target first N rows.
- 1174 — Quiz: Analytics I — **AggregationWorkbench**: Aggregation workbench: drag your group columns into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1175 — Quiz: Analytics II — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.

## Chapter 202: Data Types, NULLs & Calculations

- 1022 — Integer Types — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1023 — Numeric and Decimal Types — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for products; invalid constraints highlight; generated CREATE TABLE updates live.
- 1176 — Quiz: Analytics III — **JoinVisualizer**: Join visualizer: connect rows via matching keys; toggle join type; output table updates and unmatched rows highlight (tables: products).
- 1177 — Rounding Methods — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: orders).
- 1178 — Integer Division — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: projects).
- 1024 — Text Types — **CaseMapper**: CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.
- 1025 — Date and Timestamp Types — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for orders, events; invalid constraints highlight; generated CREATE TABLE updates live.
- 1026 — Boolean Type — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny users table; row diffs animate; goal matches target final table state.
- 1179 — String Functions — **CaseMapper**: CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.
- 1180 — Date Formatting — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: orders).
- 1027 — Understanding NULL — **NullLogicLab**: NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.
- 1028 — IS NULL and IS NOT NULL — **NullLogicLab**: NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.
- 1029 — Three-Valued Logic — **NullLogicLab**: NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.
- 1030 — COALESCE Function — **NullLogicLab**: NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.
- 1181 — NULL Coalescing Chain — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: contacts, users).
- 1031 — NULLIF Function — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: stats, customers).
- 1032 — CAST and Type Conversion — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: products).
- 1033 — Safe Division with NULLIF — **CaseMapper**: CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.
- 1182 — Type Casting — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: raw_orders).
- 1183 — Safe Conversions — **CaseMapper**: CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.

## Chapter 203: Aggregations & Grouping

- 1034 — COUNT Function — **NullLogicLab**: NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.
- 1035 — COUNT DISTINCT — **DeduperLens**: Deduper lens: highlight duplicates and select a “keep rule” (latest/highest/first); removed rows fade; goal matches deduped output.
- 1036 — SUM Function — **NullLogicLab**: NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.
- 1184 — Conditional COUNT — **CaseMapper**: CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.
- 1185 — NULL-aware SUM — **AggregationWorkbench**: Aggregation workbench: drag region into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1037 — AVG Function — **NullLogicLab**: NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.
- 1038 — MIN and MAX — **SortLimitScrubber**: Sort/limit scrubber: pick price DESC + direction, then adjust LIMIT slider; preview table reorders instantly; goal matches target first N rows.
- 1186 — Range Calculation — **AggregationWorkbench**: Aggregation workbench: drag department into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1187 — Percentage Share — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1188 — Running Average — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1039 — GROUP BY Basics — **AggregationWorkbench**: Aggregation workbench: drag status into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1040 — GROUP BY Multiple Columns — **AggregationWorkbench**: Aggregation workbench: drag category, year into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1041 — HAVING Clause — **AggregationWorkbench**: Aggregation workbench: drag category into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1042 — WHERE vs HAVING — **AggregationWorkbench**: Aggregation workbench: drag customer_id into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1189 — Multi-level Grouping — **AggregationWorkbench**: Aggregation workbench: drag country, city into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.

## Chapter 204: Joins Like a Pro

- 1043 — Why We Need Joins — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders, customers, Customers table; row diffs animate; goal matches target final table state.
- 1044 — INNER JOIN Basics — **JoinVisualizer**: Join visualizer: connect rows via p.category_id = c.id • TableA.key = TableB.key; toggle join type; output table updates and unmatched rows highlight (tables: products, categories, TableA).
- 1045 — INNER JOIN Multiple Tables — **QueryExecutionTimeline**: Timeline simulator: step through FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER; intermediate result preview updates (uses orders, customers, products).
- 1190 — Three-Table Join — **JoinVisualizer**: Join visualizer: connect rows via u.id = s.user_id • s.id = p.session_id; toggle join type; output table updates and unmatched rows highlight (tables: users, sessions, pageviews).
- 1191 — Self-Referential — **JoinVisualizer**: Join visualizer: connect rows via e.manager_id = m.id • a.department = b.department; toggle join type; output table updates and unmatched rows highlight (tables: employees).
- 1046 — LEFT JOIN Basics — **JoinVisualizer**: Join visualizer: connect rows via c.id = o.customer_id; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders).
- 1047 — LEFT JOIN for Missing Data — **JoinVisualizer**: Join visualizer: connect rows via c.id = o.customer_id • LeftTable.key = RightTable.key; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders, LeftTable).
- 1048 — RIGHT JOIN — **JoinVisualizer**: Join visualizer: connect rows via e.department_id = d.id • TableA.key = TableB.key; toggle join type; output table updates and unmatched rows highlight (tables: employees, departments, TableA).
- 1049 — FULL OUTER JOIN — **JoinVisualizer**: Join visualizer: connect rows via c.id = o.customer_id • TableA.key = TableB.key; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders, TableA).
- 1192 — Cross Join — **CrossJoinMatrix**: Cross-join matrix: click rows/cols to generate combinations; product grid fills; goal matches expected number of combinations and sample rows.
- 1050 — CROSS JOIN — **CrossJoinMatrix**: Cross-join matrix: click rows/cols to generate combinations; product grid fills; goal matches expected number of combinations and sample rows.
- 1051 — Join Cardinality — **JoinVisualizer**: Join visualizer: connect rows via matching keys; toggle join type; output table updates and unmatched rows highlight (tables: orders).
- 1052 — Duplicate Rows in Joins — **JoinVisualizer**: Join visualizer: connect rows via c.id = o.customer_id • A.ID = B.ID; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders).
- 1053 — Self Joins — **JoinVisualizer**: Join visualizer: connect rows via e.manager_id = m.id • e.ManagerID = m.ID; toggle join type; output table updates and unmatched rows highlight (tables: employees, Employees).
- 1054 — Join Best Practices — **JoinVisualizer**: Join visualizer: connect rows via o.customer_id = c.id; toggle join type; output table updates and unmatched rows highlight (tables: orders, customers, order_items).

## Chapter 250: Query Architect Boss

- 1055 — 🏛️ Query Architect Challenge — **JoinVisualizer**: Join visualizer: connect rows via c.id = o.customer_id; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders).

## Chapter 205: Subqueries & Set Operations

- 1056 — Subquery in WHERE — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1057 — IN with Subquery — **NullLogicLab**: NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.
- 1193 — Outer Join Uses — **JoinVisualizer**: Join visualizer: connect rows via c.customer_id = o.customer_id • c.id = o.customer_id; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders, products).
- 1194 — Multi-value IN — **JoinVisualizer**: Join visualizer: connect rows via c.id = o.customer_id; toggle join type; output table updates and unmatched rows highlight (tables: products, order_items, orders).
- 1195 — Scalar Comparison — **CaseMapper**: CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.
- 1058 — EXISTS Operator — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1059 — NOT EXISTS — **JoinVisualizer**: Join visualizer: connect rows via c.ID = o.CustomerID; toggle join type; output table updates and unmatched rows highlight (tables: products, order_items, Customers).
- 1196 — Double EXISTS — **JoinVisualizer**: Join visualizer: connect rows via o.product_id = p.product_id • o.id = oi.order_id; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders, products).
- 1197 — NOT EXISTS Pattern — **JoinVisualizer**: Join visualizer: connect rows via o.customer_id = c.id; toggle join type; output table updates and unmatched rows highlight (tables: products, order_items, table_a).
- 1198 — Correlated EXISTS — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1060 — Scalar Subqueries — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1061 — Correlated Subqueries — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1199 — Inline Views — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1200 — SELECT Subqueries — **JoinVisualizer**: Join visualizer: connect rows via c.id = o.customer_id; toggle join type; output table updates and unmatched rows highlight (tables: orders, customers, order_items).
- 1201 — Recursive Logic — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1062 — UNION Operator — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1063 — UNION ALL — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1064 — INTERSECT and EXCEPT — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1202 — Union Dedup — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1203 — Intersection Find — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.

## Chapter 206: CTEs (WITH Clause)

- 1065 — Introduction to CTEs — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.
- 1066 — Basic CTE Syntax — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.
- 1067 — CTEs vs Subqueries — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.
- 1204 — Problem Decomposition — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.
- 1205 — Readable CTEs — **JoinVisualizer**: Join visualizer: connect rows via c.customer_id = o.customer_id • o.customer_id = c.id; toggle join type; output table updates and unmatched rows highlight (tables: customers, active_customers, orders).
- 1068 — Multiple CTEs — **JoinVisualizer**: Join visualizer: connect rows via s.ID = r.OrderID; toggle join type; output table updates and unmatched rows highlight (tables: employees, sales_dept, high_salary).
- 1069 — Chained CTEs — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.
- 1206 — CTE Pipeline — **JoinVisualizer**: Join visualizer: connect rows via o.customer_id = c.id • e.user_id = u.id; toggle join type; output table updates and unmatched rows highlight (tables: orders, recent_orders, completed_orders).
- 1207 — Parallel CTEs — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.
- 1208 — CTE Reuse — **JoinVisualizer**: Join visualizer: connect rows via current.month = previous.month • t1.month = t2.month; toggle join type; output table updates and unmatched rows highlight (tables: orders, monthly_metrics, totals).
- 1070 — CTEs for Readability — **JoinVisualizer**: Join visualizer: connect rows via c.id = ot.customer_id • c.id = h.customer_id; toggle join type; output table updates and unmatched rows highlight (tables: products, active_products, category_counts).
- 1071 — Reusing CTEs — **JoinVisualizer**: Join visualizer: connect rows via ThisMonth.UserID = LastMonth.UserID; toggle join type; output table updates and unmatched rows highlight (tables: employees, Logins, ActiveUsers).
- 1072 — Recursive CTEs Intro — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1073 — CTE Best Practices — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.
- 1209 — Debug with CTEs — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.

## Chapter 207: Window Functions

- 1074 — What are Window Functions? — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1075 — OVER Clause Basics — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1076 — PARTITION BY — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1077 — ORDER BY in Windows — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1210 — Window vs GROUP BY — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1078 — ROW_NUMBER — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1079 — RANK and DENSE_RANK — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1211 — Top N per Group — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1212 — Percentile Rank — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1213 — Dense vs Regular — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1080 — Running Totals with SUM — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1081 — Moving Averages — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1214 — Cumulative Sum — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1215 — Rolling Window — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1216 — YTD Calculations — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1082 — LAG Function — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1083 — LEAD Function — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1084 — FIRST_VALUE and LAST_VALUE — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1085 — NTILE for Bucketing — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1217 — Period Comparison — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.

## Chapter 208: Time-Series SQL

- 1086 — Date Truncation — **AggregationWorkbench**: Aggregation workbench: drag 1 into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1087 — DATE_TRUNC Function — **AggregationWorkbench**: Aggregation workbench: drag 1 into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1088 — Grouping by Time Periods — **AggregationWorkbench**: Aggregation workbench: drag 1 into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1218 — Period Grouping — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1219 — Date Range — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1089 — Date Arithmetic — **NullLogicLab**: NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.
- 1090 — EXTRACT Function — **AggregationWorkbench**: Aggregation workbench: drag 1, 2 into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1220 — Age Calculation — **AggregationWorkbench**: Aggregation workbench: drag 1 into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1221 — Business Days — **JoinVisualizer**: Join visualizer: connect rows via d.date = h.holiday_date; toggle join type; output table updates and unmatched rows highlight (tables: order_date, orders, date_series).
- 1222 — Date Intervals — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1091 — Cohort Analysis Basics — **AggregationWorkbench**: Aggregation workbench: drag 1 into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1092 — Retention Tables — **JoinVisualizer**: Join visualizer: connect rows via u.user_id = e.user_id • c.UserID = a.UserID; toggle join type; output table updates and unmatched rows highlight (tables: users, events, Cohorts).
- 1093 — Session Analysis — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1223 — First-Time Users — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1224 — Return Visitors — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1094 — Conversion Funnels — **CaseMapper**: CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.
- 1095 — Gap Analysis — **JoinVisualizer**: Join visualizer: connect rows via matching keys; toggle join type; output table updates and unmatched rows highlight (tables: sales, table).
- 1096 — Calendar Tables — **JoinVisualizer**: Join visualizer: connect rows via c.date = o.order_date • c.Date = o.OrderDate; toggle join type; output table updates and unmatched rows highlight (tables: calendar, orders, Calendar).
- 1097 — Year-over-Year Comparisons — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1225 — Funnel Metrics — **JoinVisualizer**: Join visualizer: connect rows via e1.user_id = e2.user_id; toggle join type; output table updates and unmatched rows highlight (tables: events, funnel).

## Chapter 251: Analytics Wizard Boss

- 1098 — 🧙 Analytics Wizard Challenge — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.

## Chapter 209: Data Cleaning & Metrics

- 1099 — Identifying Duplicates — **AggregationWorkbench**: Aggregation workbench: drag name into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1100 — Deduplication with ROW_NUMBER — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders, ranked, Users table; row diffs animate; goal matches target final table state.
- 1101 — Keeping First/Last Record — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders, StatusHistory table; row diffs animate; goal matches target final table state.
- 1226 — Fuzzy Duplicates — **JoinVisualizer**: Join visualizer: connect rows via matching keys; toggle join type; output table updates and unmatched rows highlight (tables: customers).
- 1227 — Keep Latest — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1102 — Detecting Outliers — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1103 — Percentile Calculations — **SortLimitScrubber**: Sort/limit scrubber: pick amount) + direction, then adjust LIMIT slider; preview table reorders instantly; goal matches target first N rows.
- 1104 — Handling Outliers — **SortLimitScrubber**: Sort/limit scrubber: pick your sort keys + direction, then adjust LIMIT slider; preview table reorders instantly; goal matches target first N rows.
- 1228 — IQR Method — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.
- 1229 — Z-Score Filter — **JoinVisualizer**: Join visualizer: connect rows via p.category = g.category; toggle join type; output table updates and unmatched rows highlight (tables: orders, products, group_stats).
- 1105 — Metric Definitions Matter — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1106 — Active User Definitions — **AggregationWorkbench**: Aggregation workbench: drag DATE(event_time) into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1107 — Avoiding Double Counting — **JoinVisualizer**: Join visualizer: connect rows via u.id = o.user_id • u.id = uo.user_id; toggle join type; output table updates and unmatched rows highlight (tables: orders, users, user_orders).
- 1230 — Standard Deviation — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.
- 1231 — Cohort Retention — **JoinVisualizer**: Join visualizer: connect rows via o.customer_id = c.user_id • ma.cohort_month = cs.cohort_month; toggle join type; output table updates and unmatched rows highlight (tables: orders, cohorts, monthly_activity).
- 1108 — Data Quality Checks — **NullLogicLab**: NULL logic lab: toggle NULL values and filter operators (=, <, IS NULL); rows survive/fail with three-valued logic explanations.
- 1109 — Assertion Queries — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1110 — Metric Validation — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1232 — Completeness Check — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1233 — Consistency Check — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.

## Chapter 210: Database Design Essentials

- 1111 — Why Tables Split — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders table; row diffs animate; goal matches target final table state.
- 1112 — Normalization Basics — **DeduperLens**: Deduper lens: highlight duplicates and select a “keep rule” (latest/highest/first); removed rows fade; goal matches deduped output.
- 1113 — First Normal Form — **JoinVisualizer**: Join visualizer: connect rows via u.id = p.user_id; toggle join type; output table updates and unmatched rows highlight (tables: users, user_phones).
- 1114 — Second and Third Normal Form — **JoinVisualizer**: Join visualizer: connect rows via e.department_id = d.id; toggle join type; output table updates and unmatched rows highlight (tables: employees, departments).
- 1234 — Dependency Analysis — **JoinVisualizer**: Join visualizer: connect rows via c.customer_id = o.customer_id • c.customer_id = r.customer_id; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders, reviews).
- 1115 — Fact Tables — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: orders).
- 1116 — Dimension Tables — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1117 — Star Schema — **JoinVisualizer**: Join visualizer: connect rows via o.customer_id = c.id • o.product_id = p.id; toggle join type; output table updates and unmatched rows highlight (tables: orders, customers, products).
- 1235 — Dimension Building — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for date, generate_series, orders; invalid constraints highlight; generated CREATE TABLE updates live.
- 1236 — Fact Table Design — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for fact_orders; invalid constraints highlight; generated CREATE TABLE updates live.
- 1118 — Primary Key Constraints — **SchemaGraphBuilder**: Schema graph builder: click-to-connect PK→FK edges between users, Users; cardinality + NULLability badges update; goal is a valid relationship map.
- 1119 — Foreign Key Constraints — **SchemaGraphBuilder**: Schema graph builder: click-to-connect PK→FK edges between orders, customers, Orders; cardinality + NULLability badges update; goal is a valid relationship map.
- 1120 — Unique Constraints — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for users, Users; invalid constraints highlight; generated CREATE TABLE updates live.
- 1237 — Constraint Testing — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1238 — Index Creation — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for pg_indexes; invalid constraints highlight; generated CREATE TABLE updates live.
- 1121 — When to Denormalize — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders table; row diffs animate; goal matches target final table state.
- 1122 — Analytics Schema Design — **AggregationWorkbench**: Aggregation workbench: drag DATE_TRUNC('month', order_date) into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1239 — Table Design — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for orders; invalid constraints highlight; generated CREATE TABLE updates live.
- 1240 — SCD Implementation — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for customers_scd2, customers; invalid constraints highlight; generated CREATE TABLE updates live.
- 1241 — Audit Columns — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for orders; invalid constraints highlight; generated CREATE TABLE updates live.

## Chapter 211: Performance & Query Plans

- 1123 — Why Performance Matters — **JoinVisualizer**: Join visualizer: connect rows via matching keys; toggle join type; output table updates and unmatched rows highlight (tables: users).
- 1124 — Introduction to Indexes — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for users; invalid constraints highlight; generated CREATE TABLE updates live.
- 1125 — How Indexes Work — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1126 — Index Trade-offs — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1242 — Query Logging — **SortLimitScrubber**: Sort/limit scrubber: pick total_time DESC + direction, then adjust LIMIT slider; preview table reorders instantly; goal matches target first N rows.
- 1127 — Reading EXPLAIN Output — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1128 — Sequential vs Index Scan — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1243 — Cost Analysis — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for orders; invalid constraints highlight; generated CREATE TABLE updates live.
- 1244 — Join Order — **JoinVisualizer**: Join visualizer: connect rows via c.customer_id = o.customer_id • o.order_id = oi.order_id; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders, order_items).
- 1245 — Scan Types — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for orders; invalid constraints highlight; generated CREATE TABLE updates live.
- 1129 — Filter Early Principle — **JoinVisualizer**: Join visualizer: connect rows via o.customer_id = c.id; toggle join type; output table updates and unmatched rows highlight (tables: orders, customers).
- 1130 — Reducing Rows Before Joins — **JoinVisualizer**: Join visualizer: connect rows via c.id = ot.customer_id • s.UserID = u.ID; toggle join type; output table updates and unmatched rows highlight (tables: orders, customers, order_totals).
- 1131 — Avoiding SELECT * — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: customers).
- 1246 — Query Rewrite — **SetOpsVenn**: Set-ops Venn: toggle UNION/INTERSECT/EXCEPT and DISTINCT/ALL; Venn + resulting rows update; goal matches target row set.
- 1247 — Sargable Queries — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for orders, products, users; invalid constraints highlight; generated CREATE TABLE updates live.

## Chapter 212: Mutations & Transactions

- 1132 — INSERT Basics — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny products, key_value_store, Users table; row diffs animate; goal matches target final table state.
- 1133 — INSERT Multiple Rows — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny users, Users table; row diffs animate; goal matches target final table state.
- 1134 — INSERT from SELECT — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny vip_orders, orders, ArchivedOrders table; row diffs animate; goal matches target final table state.
- 1248 — Upsert Pattern — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny products, SET, name table; row diffs animate; goal matches target final table state.
- 1249 — Default Values — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for tasks, orders; invalid constraints highlight; generated CREATE TABLE updates live.
- 1135 — UPDATE Basics — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny products, Users, Products table; row diffs animate; goal matches target final table state.
- 1136 — UPDATE with Conditions — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders, Posts, Employees table; row diffs animate; goal matches target final table state.
- 1137 — DELETE Basics — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders, Users, Queue table; row diffs animate; goal matches target final table state.
- 1250 — Conditional Update — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny customers, orders, products table; row diffs animate; goal matches target final table state.
- 1251 — Batch Update — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders, batch, large_table table; row diffs animate; goal matches target final table state.
- 1138 — DELETE with Conditions — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders, Logs, Users table; row diffs animate; goal matches target final table state.
- 1139 — Transaction Basics — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1140 — BEGIN, COMMIT, ROLLBACK — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny accounts, Account table; row diffs animate; goal matches target final table state.
- 1141 — Savepoints — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders, B table; row diffs animate; goal matches target final table state.
- 1142 — Isolation Levels Intro — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: your_table).
- 1143 — Safe Update Patterns — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny products, Tickets table; row diffs animate; goal matches target final table state.
- 1144 — View Basics — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for orders, Users, ActiveUsers; invalid constraints highlight; generated CREATE TABLE updates live.
- 1145 — Updatable Views — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders, ActiveUsers table; row diffs animate; goal matches target final table state.
- 1146 — Materialized Views — **JoinVisualizer**: Join visualizer: connect rows via c.id = o.customer_id; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders).

## Chapter 213: Analytics Engineering

- 1252 — Regular Views Intro — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for orders, customers, high_value_orders; invalid constraints highlight; generated CREATE TABLE updates live.
- 1147 — Materialized Views — **AggregationWorkbench**: Aggregation workbench: drag DATE_TRUNC('month', order_date) into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1253 — When to Use Each View Type — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for orders, daily_sales_summary; invalid constraints highlight; generated CREATE TABLE updates live.
- 1254 — Refreshing Materialized Views — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny orders, regular_view_orders, mat_view_orders table; row diffs animate; goal matches target final table state.
- 1255 — View Performance Challenge — **JoinVisualizer**: Join visualizer: connect rows via r.id = s.region_id • s.id = o.store_id; toggle join type; output table updates and unmatched rows highlight (tables: regions, stores, orders).
- 1150 — Staging Models — **JoinVisualizer**: Join visualizer: connect rows via matching keys; toggle join type; output table updates and unmatched rows highlight (tables: raw.orders, raw.customers).
- 1151 — Intermediate Models — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1152 — Marts Layer — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
- 1256 — Model Dependencies — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for raw_orders_v1, stg_orders, raw; invalid constraints highlight; generated CREATE TABLE updates live.
- 1257 — Build Analytics Pipeline — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for raw_events, stg_page_views, users; invalid constraints highlight; generated CREATE TABLE updates live.
- 1148 — Naming Conventions — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for tbl_c, o_data, dim_customers; invalid constraints highlight; generated CREATE TABLE updates live.
- 1149 — SQL Style Guide — **JoinVisualizer**: Join visualizer: connect rows via c.id = o.cust_id • c.customer_id = o.customer_id; toggle join type; output table updates and unmatched rows highlight (tables: customers, orders, ORDERS).
- 1258 — Documenting Your Models — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for core_metrics; invalid constraints highlight; generated CREATE TABLE updates live.
- 1259 — Testing Data Quality — **JoinVisualizer**: Join visualizer: connect rows via o.customer_id = c.id; toggle join type; output table updates and unmatched rows highlight (tables: orders, customers).
- 1260 — Code Review Challenge — **JoinVisualizer**: Join visualizer: connect rows via p.cat_id = c.id • u.id = o.user_id; toggle join type; output table updates and unmatched rows highlight (tables: products, categories, users).

## Chapter 214: Cloud Warehouse Features

- 1153 — Cloud vs Traditional DB — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1261 — Compute vs Storage Separation — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: massive_log_table).
- 1262 — Auto-Scaling & Elasticity — **CaseMapper**: CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.
- 1263 — Cloud Warehouse Comparison — **CaseMapper**: CASE mapper: arrange condition→label branches; sample rows route through branches; goal matches expected labels for all shown rows.
- 1264 — Choose the Right Warehouse — **QueryBuilderSlots**: Query builder slots: fill SELECT/FROM/WHERE/ORDER slots with constrained choices; result preview updates instantly (tables: your_table).
- 1156 — Table Partitioning — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for raw.events, analytics.events, orders; invalid constraints highlight; generated CREATE TABLE updates live.
- 1157 — Clustering Keys — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for raw.orders, analytics.orders, raw_orders; invalid constraints highlight; generated CREATE TABLE updates live.
- 1154 — QUALIFY Clause — **QueryExecutionTimeline**: Timeline simulator: step through FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER; intermediate result preview updates (uses employees, orders, raw_events).
- 1155 — QUALIFY with ROW_NUMBER — **MutationSandbox**: Mutation sandbox: run INSERT/UPDATE/DELETE against a tiny raw_orders, raw_users, events table; row diffs animate; goal matches target final table state.
- 1265 — Partition Design Challenge — **SchemaBuilder**: DDL builder: assemble columns/types/constraints for app_logs; invalid constraints highlight; generated CREATE TABLE updates live.
- 1158 — Cost-Based Thinking — **FilterAnimator**: Filter animator: adjust WHERE chips (column/operator/value); rows animate in/out; goal is correct remaining row count and preview rows.
- 1159 — Scanning Fewer Columns — **CTEStepper**: CTE stepper: reveal each WITH clause as a stage; intermediate tables materialize; goal is to get final result set correct.
- 1160 — Scanning Fewer Rows — **AggregationWorkbench**: Aggregation workbench: drag customer_id into GROUP slot; choose aggregates; groups/bars update + result table highlights changed cells.
- 1161 — Query Optimization Tips — **JoinVisualizer**: Join visualizer: connect rows via a.id = b.id; toggle join type; output table updates and unmatched rows highlight (tables: customer_orders, order_date, orders).
- 1266 — Cost Reduction Challenge — **SortLimitScrubber**: Sort/limit scrubber: pick cost DESC + direction, then adjust LIMIT slider; preview table reorders instantly; goal matches target first N rows.

## Chapter 13: Final Boss

- 1267 — The Data Warehouse Migration — **WindowTimeline**: Window timeline: choose PARTITION/ORDER/frame chips; per-row running values update; goal matches expected row-by-row output.
