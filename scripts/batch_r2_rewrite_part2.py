"""
Batch R-2 Rewrite Script - Part 2
Concepts: 2270 (Joins), 2310 (Databases), 2320 (Arrow)
"""

import json

with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

def add_metadata(lesson):
    if 'gap_ids' not in lesson:
        lesson['gap_ids'] = []
    if 'R-REINF' not in lesson['gap_ids']:
        lesson['gap_ids'].append('R-REINF')
    lesson['batch_id'] = 'R-2'
    return lesson

# ===== CONCEPT 2270: Mutating Joins =====

lessons["22701"] = add_metadata({
    **lessons["22701"],
    "title": "Analogy: ID Badge",
    "content": """# 🪪 The ID Badge Match

## What You'll Learn
How joins connect two tables by matching a common column.

## Why This Matters
Data often lives in multiple tables. Customers in one, orders in another. Joins let you combine them: "For each order, find the customer info." The "ID badge" (key column) links matching rows.

> 💡 The `%>%` takes `orders` and passes it to `left_join()` — think "take orders, then add customer info."

## Example

```r
orders %>% left_join(customers, by = "customer_id")
```

This adds customer columns to each order row.

## 🎯 Your Task

1. Understand: `left_join(A, B, by = "key")` keeps all rows from A
2. Matching rows from B are added as new columns
3. Non-matches get NA in the B columns

**Expected Output:**
A combined table with columns from both datasets

## ⚠️ Common Mistake

**Wrong:**
```r
left_join(orders, customers)
```
No `by` argument — R guesses (risky!).

**Fixed:**
```r
left_join(orders, customers, by = "customer_id")
```
Always specify the key explicitly.

---

✅ **No Hidden Prerequisites**: Uses `left_join()` from dplyr.
"""
})

lessons["22702"] = add_metadata({
    **lessons["22702"],
    "title": "Variation: Right & Inner",
    "content": """# 🔄 Different Join Types

## What You'll Learn
How `right_join()` and `inner_join()` differ from `left_join()`.

## Why This Matters
- `left_join`: keep all LEFT rows
- `right_join`: keep all RIGHT rows
- `inner_join`: keep only MATCHES

Choose based on what you need to preserve.

> 💡 The `%>%` takes your data and passes it to the join function.

## Example

```r
# Keep only matching rows
band_members %>% inner_join(band_instruments, by = "name")
```

## 🎯 Your Task

1. `left_join()` keeps all left rows
2. `inner_join()` keeps only rows that match in BOTH tables
3. Try `inner_join()` to see fewer rows returned

**Expected Output:**
Only rows where the key exists in both tables

## ⚠️ Common Mistake

**Wrong:**
Using `left_join` when you only want complete matches.

**Fixed:**
Use `inner_join` to drop non-matching rows.

---

✅ **No Hidden Prerequisites**: Uses `inner_join()` from dplyr.
"""
})

lessons["22703"] = add_metadata({
    **lessons["22703"],
    "title": "Fix the Code: by Argument",
    "content": """# 🔧 Fix: Join Key

## What You'll Learn
How to fix common join key errors.

## Why This Matters
Joins fail silently if the key column doesn't match. Typos, case differences, or wrong column names cause empty results or wrong matches.

## Example

```r
# Tables have different key names
# Table A has "id", Table B has "ID"

left_join(A, B, by = c("id" = "ID"))
```

## 🎯 Your Task

1. The code below fails because column names don't match
2. Table X has `student_id`, Table Y has `StudentID`
3. Fix using `by = c("student_id" = "StudentID")`

**Broken:**
```r
left_join(X, Y, by = "student_id")
```

**Expected Output:**
A properly joined table

## ⚠️ Common Mistake

**Wrong:**
```r
by = "student_id"
```
Only works if BOTH tables have that exact name.

**Fixed:**
```r
by = c("student_id" = "StudentID")
```
Map names explicitly.

---

✅ **No Hidden Prerequisites**: Uses `left_join()` with named vectors.
"""
})

lessons["22704"] = add_metadata({
    **lessons["22704"],
    "title": "Challenge: Match Tables",
    "content": """# 🦸 Challenge: Join Two Tables

## What You'll Learn
Apply joins to combine related datasets.

## Why This Matters
Almost every real analysis requires combining data. This is your core join skill test.

> 💡 The `%>%` takes your primary table and passes it to the join function.

## Example

```r
primary_table %>%
  left_join(lookup_table, by = "key_column")
```

## 🎯 Your Task

Using the built-in `band_members` and `band_instruments` tables:
1. Join them by the `name` column
2. Use `inner_join()` to keep only musicians with instruments
3. How many rows remain?

**Expected Output:**
A table with only the matched musicians

## ⚠️ Common Mistake

**Wrong:**
```r
inner_join(band_members, band_instruments)
```
Omitting `by` works here but is fragile.

**Fixed:**
```r
inner_join(band_members, band_instruments, by = "name")
```
Always specify the key.

---

✅ **No Hidden Prerequisites**: Uses `inner_join()` and built-in datasets.
"""
})

# ===== CONCEPT 2310: Databases & dbplyr =====

lessons["23101"] = add_metadata({
    **lessons["23101"],
    "title": "Analogy: Remote Control",
    "content": """# 🎮 The Remote Control

## What You'll Learn
How dbplyr lets you write dplyr code that runs on a database.

## Why This Matters
Too much data to fit in memory? Leave it in the database. dbplyr translates your R code to SQL and runs it there. You write R, the database does the work.

## Example

```r
library(DBI)
library(dbplyr)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")
dbWriteTable(con, "mtcars", mtcars)

tbl(con, "mtcars") %>% filter(mpg > 20)
```

This runs on the database, not in R!

## 🎯 Your Task

1. Understand: `tbl(connection, "table_name")` creates a database reference
2. You can use `filter()`, `select()`, `mutate()` — same syntax
3. The database executes the query

**Expected Output:**
A query result from the database

## ⚠️ Common Mistake

**Wrong:**
Trying to use R-only functions (like `str_sub()`) in database queries.

**Fixed:**
Stick to functions that have SQL equivalents.

---

✅ **No Hidden Prerequisites**: Uses DBI and dbplyr packages.
"""
})

lessons["23102"] = add_metadata({
    **lessons["23102"],
    "title": "Variation: See the SQL",
    "content": """# 👀 Peek at the SQL

## What You'll Learn
How to see what SQL query dbplyr generates.

## Why This Matters
Understanding the SQL helps debug slow queries and learn SQL syntax. `show_query()` reveals what's happening behind the scenes.

## Example

```r
tbl(con, "mtcars") %>%
  filter(mpg > 20) %>%
  show_query()
```

Shows:
```sql
SELECT * FROM mtcars WHERE mpg > 20
```

## 🎯 Your Task

1. Create a query with `tbl()` and `filter()`
2. Add `show_query()` at the end
3. Read the generated SQL

**Expected Output:**
A SQL SELECT statement

## ⚠️ Common Mistake

**Wrong:**
Assuming R code runs in R — with dbplyr, it becomes SQL!

**Fixed:**
Use `show_query()` to verify what's happening.

---

✅ **No Hidden Prerequisites**: Uses `show_query()` from dbplyr.
"""
})

lessons["23103"] = add_metadata({
    **lessons["23103"],
    "title": "Fix the Code: collect()",
    "content": """# 🔧 Fix: Bring Data to R

## What You'll Learn
Why you need `collect()` to actually download database results.

## Why This Matters
By default, dbplyr is "lazy" — it doesn't run until needed. `collect()` triggers execution and brings results into R memory.

## Example

```r
# This is just a query plan
query <- tbl(con, "mtcars") %>% filter(mpg > 20)

# This actually runs it
result <- query %>% collect()
```

## 🎯 Your Task

1. The code builds a query but never runs it
2. Add `collect()` to bring results into R
3. Now you can use R functions on the result

**Broken:**
```r
tbl(con, "mtcars") %>% filter(mpg > 20)
```
(Query not executed!)

**Expected Output:**
An actual R data frame

## ⚠️ Common Mistake

**Wrong:**
Forgetting `collect()` then wondering why calculations fail.

**Fixed:**
```r
tbl(con, "mtcars") %>% filter(mpg > 20) %>% collect()
```
Now it's in R memory.

---

✅ **No Hidden Prerequisites**: Uses `collect()` from dbplyr.
"""
})

lessons["23104"] = add_metadata({
    **lessons["23104"],
    "title": "Challenge: Query Database",
    "content": """# 🦸 Challenge: Database Query

## What You'll Learn
Build a complete database query workflow.

## Why This Matters
Real-world data lives in databases. This exercise practices the full workflow.

## Example

```r
con <- DBI::dbConnect(...)
result <- tbl(con, "table") %>%
  filter(condition) %>%
  select(columns) %>%
  collect()
```

## 🎯 Your Task

1. Connect to a database
2. Reference a table with `tbl()`
3. Filter and select some columns
4. Use `collect()` to get results

**Expected Output:**
A filtered subset of the database table

## ⚠️ Common Mistake

**Wrong:**
```r
tbl(con, "table") %>% filter(x > 10)
```
Forgot to `collect()`!

**Fixed:**
```r
tbl(con, "table") %>% filter(x > 10) %>% collect()
```
Always `collect()` when done.

---

✅ **No Hidden Prerequisites**: Uses DBI, dbplyr, and `collect()`.
"""
})

# ===== CONCEPT 2320: Arrow & Parquet =====

lessons["23201"] = add_metadata({
    **lessons["23201"],
    "title": "Analogy: Express Lane",
    "content": """# 🚀 The Express Lane

## What You'll Learn
How Arrow and Parquet files handle big data faster than CSV.

## Why This Matters
CSV files are slow: they're text, require parsing, and don't store types. Parquet is a binary format that's 10-100x faster. Arrow lets R work with Parquet seamlessly.

## Example

```r
library(arrow)

# Read parquet (much faster than CSV)
data <- read_parquet("data.parquet")

# Write parquet
write_parquet(penguins, "penguins.parquet")
```

## 🎯 Your Task

1. Understand: Parquet stores data in a compressed, typed binary format
2. Arrow is the R package that reads/writes Parquet
3. The syntax mirrors `read_csv()` / `write_csv()`

**Expected Output:**
A tibble from the parquet file

## ⚠️ Common Mistake

**Wrong:**
Using `read.csv()` on huge files (slow!).

**Fixed:**
Save as parquet once, then use `read_parquet()` forever.

---

✅ **No Hidden Prerequisites**: Uses `arrow` package.
"""
})

lessons["23202"] = add_metadata({
    **lessons["23202"],
    "title": "Variation: Write Parquet",
    "content": """# 💾 Save as Parquet

## What You'll Learn
How to convert your data to Parquet for faster future reads.

## Why This Matters
If you work with the same data repeatedly, saving it as Parquet once saves time every future read. Parquet also compresses the file!

## Example

```r
library(arrow)

# Convert CSV to Parquet
data <- read_csv("big_data.csv")
write_parquet(data, "big_data.parquet")

# Future reads are instant!
data2 <- read_parquet("big_data.parquet")
```

## 🎯 Your Task

1. Use `write_parquet()` to save the penguins dataset
2. Then use `read_parquet()` to load it back
3. Compare: same data, faster format

**Expected Output:**
A .parquet file on disk

## ⚠️ Common Mistake

**Wrong:**
```r
write.parquet(data, "file.parquet")
```
Wrong function name! It's `write_parquet`.

**Fixed:**
```r
write_parquet(data, "file.parquet")
```
Arrow functions use underscores.

---

✅ **No Hidden Prerequisites**: Uses `write_parquet()` from arrow.
"""
})

lessons["23203"] = add_metadata({
    **lessons["23203"],
    "title": "Fix the Code: Package",
    "content": """# 🔧 Fix: Load Arrow

## What You'll Learn
The most common Arrow error: forgetting to load the package.

## Why This Matters
`read_parquet()` doesn't exist until you load `library(arrow)`. This is true for all non-base packages!

## Example

```r
# This fails
read_parquet("data.parquet")
# Error: could not find function "read_parquet"

# Fix: load the package first
library(arrow)
read_parquet("data.parquet")
```

## 🎯 Your Task

1. The error says "could not find function"
2. This always means: package not loaded
3. Add `library(arrow)` before the function call

**Broken:**
```r
read_parquet("data.parquet")
```

**Expected Output:**
The data loads successfully

## ⚠️ Common Mistake

**Wrong:**
Forgetting `library(arrow)`.

**Fixed:**
```r
library(arrow)
read_parquet("data.parquet")
```

---

✅ **No Hidden Prerequisites**: Uses `library()` and arrow package.
"""
})

lessons["23204"] = add_metadata({
    **lessons["23204"],
    "title": "Challenge: Convert File",
    "content": """# 🦸 Challenge: CSV to Parquet

## What You'll Learn
Apply the full workflow to convert a file.

## Why This Matters
This is a real-world task: take slow CSV, convert to fast Parquet.

## Example

```r
library(arrow)
data <- read_csv("input.csv")
write_parquet(data, "output.parquet")
```

## 🎯 Your Task

1. Load the arrow package
2. Read any CSV file with `read_csv()`
3. Save it as Parquet with `write_parquet()`
4. Verify by reading it back with `read_parquet()`

**Expected Output:**
Data loaded from the new Parquet file

## ⚠️ Common Mistake

**Wrong:**
```r
write_parquet(data, "output.csv")
```
Wrong extension — use `.parquet`!

**Fixed:**
```r
write_parquet(data, "output.parquet")
```

---

✅ **No Hidden Prerequisites**: Uses arrow, read_csv, write_parquet.
"""
})

with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Batch R-2 Part 2 complete: 2270, 2310, 2320 (12 reinforcers)")
