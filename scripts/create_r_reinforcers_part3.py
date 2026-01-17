"""
Create Missing R Reinforcers - Part 3
Concepts: 2041, 2042, 2051
"""

import json

with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

def create_reinforcer(concept_id, role_num, title, content):
    reinf_id = concept_id * 10 + role_num
    concept = lessons.get(str(concept_id), {})
    return {
        "id": reinf_id,
        "title": title,
        "content": content,
        "starter_code": "",
        "solution_code": "",
        "expected_output": "",
        "chapter_id": concept.get("chapter_id", 5),
        "chapter_title": concept.get("chapter_title", ""),
        "gap_ids": ["R-REINF"],
        "batch_id": "R-3"
    }

# ===== 2041: Lengthening Data =====
lessons["20411"] = create_reinforcer(2041, 1, "Analogy: Unpacking a Wide Suitcase",
"""# 📦 Wide to Long

## What You'll Learn
How `pivot_longer()` converts wide data into tidy (long) format.

## Why This Matters
Wide data has values spread across columns. Long data has one row per observation. ggplot and dplyr prefer long format.

> 💡 The `%>%` takes your data and passes it to `pivot_longer()`.

## Example

```r
table4a %>%
  pivot_longer(
    cols = c(`1999`, `2000`),
    names_to = "year",
    values_to = "cases"
  )
```

## 🎯 Your Task

1. Identify which columns need to become rows
2. `names_to` = what to call the new column from headers
3. `values_to` = what to call the column of values

**Expected Output:**
A longer table with year and cases columns

## ⚠️ Common Mistake

**Wrong:**
```r
cols = c(1999, 2000)  # Numbers need backticks
```

**Fixed:**
```r
cols = c(`1999`, `2000`)
```

---

✅ **No Hidden Prerequisites**: Uses `pivot_longer()` from this lesson.
""")

lessons["20412"] = create_reinforcer(2041, 2, "Variation: Column Selection",
"""# 🎯 Selecting Columns to Pivot

## What You'll Learn
Different ways to select which columns to pivot.

## Why This Matters
You don't have to list every column. Use helpers like `starts_with()`, `ends_with()`, or ranges.

## Example

```r
# By name
cols = c(col1, col2, col3)

# By helper
cols = starts_with("year_")

# By position
cols = 2:5
```

## 🎯 Your Task

1. Try `starts_with()` to select columns
2. All matching columns will be pivoted
3. This is cleaner than listing each one

**Expected Output:**
Same pivot result, cleaner code

## ⚠️ Common Mistake

**Wrong:**
Forgetting to quote the prefix in `starts_with()`.

**Fixed:**
```r
starts_with("year_")  # Quoted prefix
```

---

✅ **No Hidden Prerequisites**: Column selection helpers.
""")

lessons["20413"] = create_reinforcer(2041, 3, "Fix the Code: Missing Quotes",
"""# 🔧 Fix: names_to and values_to

## What You'll Learn
Why `names_to` and `values_to` need quoted strings.

## Why This Matters
These are NEW column names you're creating. They must be in quotes because they don't exist yet.

## Example

```r
# Wrong
pivot_longer(cols, names_to = year, values_to = cases)

# Fixed
pivot_longer(cols, names_to = "year", values_to = "cases")
```

## 🎯 Your Task

1. Add quotes around the new column names
2. These are strings, not existing variables
3. Verify the pivot works

**Expected Output:**
A properly pivoted table

## ⚠️ Common Mistake

**Wrong:**
```r
names_to = year
```

**Fixed:**
```r
names_to = "year"
```

---

✅ **No Hidden Prerequisites**: Pivot argument syntax.
""")

lessons["20414"] = create_reinforcer(2041, 4, "Challenge: Pivot Your Data",
"""# 🦸 Challenge: Tidy the Data

## What You'll Learn
Apply pivoting to create analysis-ready data.

## Why This Matters
Most data arrives messy. Tidying is step one of every analysis.

> 💡 The `%>%` takes untidy data and makes it tidy.

## Example

Pattern:
```r
data %>%
  pivot_longer(cols = ..., names_to = "...", values_to = "...")
```

## 🎯 Your Task

Given `table4a` with columns `country`, `1999`, `2000`:
1. Pivot the year columns into rows
2. Name the new columns "year" and "cases"
3. Result should have 6 rows (3 countries × 2 years)

**Expected Output:**
A table with country, year, cases columns (6 rows)

## ⚠️ Common Mistake

**Wrong:**
Pivoting the country column too.

**Fixed:**
Only pivot the year columns, keep country as identifier.

---

✅ **No Hidden Prerequisites**: Complete pivot workflow.
""")

# ===== 2042: Widening Data =====
lessons["20421"] = create_reinforcer(2042, 1, "Analogy: Spreading Out",
"""# 📊 Long to Wide

## What You'll Learn
How `pivot_wider()` spreads values across multiple columns.

## Why This Matters
Sometimes you need data wide for presentation, comparison tables, or specific functions. `pivot_wider()` is the reverse of `pivot_longer()`.

> 💡 The `%>%` takes long data and makes it wide.

## Example

```r
fish_encounters %>%
  pivot_wider(names_from = station, values_from = seen)
```

## 🎯 Your Task

1. `names_from` = which column's values become headers
2. `values_from` = which column provides the cell values
3. Missing combinations become NA

**Expected Output:**
A wider table with one column per station

## ⚠️ Common Mistake

**Wrong:**
Confusing `names_from` and `values_from`.

**Fixed:**
`names_from` = headers, `values_from` = cell contents.

---

✅ **No Hidden Prerequisites**: Uses `pivot_wider()` from this lesson.
""")

lessons["20422"] = create_reinforcer(2042, 2, "Variation: Fill Missing Values",
"""# 🕳️ Handling NA in Wide Data

## What You'll Learn
Use `values_fill` to replace NAs with a default.

## Why This Matters
When widening, missing combinations create NAs. Sometimes 0 or another value makes more sense.

## Example

```r
pivot_wider(
  names_from = station,
  values_from = seen,
  values_fill = 0
)
```

## 🎯 Your Task

1. Add `values_fill = 0` to replace NAs
2. Verify missing values show 0 instead
3. Good for counts where missing = zero

**Expected Output:**
Wide table with 0s instead of NAs

## ⚠️ Common Mistake

**Wrong:**
```r
values_fill = "0"  # String, not number
```

**Fixed:**
```r
values_fill = 0  # Numeric
```

---

✅ **No Hidden Prerequisites**: Pivot_wider argument.
""")

lessons["20423"] = create_reinforcer(2042, 3, "Fix the Code: Argument Order",
"""# 🔧 Fix: Pivot Arguments

## What You'll Learn
The correct argument names for `pivot_wider()`.

## Why This Matters
`names_from` and `values_from` are required. Typos or wrong names cause errors.

## Example

```r
# Wrong
pivot_wider(names = col1, values = col2)

# Fixed
pivot_wider(names_from = col1, values_from = col2)
```

## 🎯 Your Task

1. The argument names are incomplete
2. Add `_from` to both arguments
3. Verify the pivot works

**Expected Output:**
A properly widened table

## ⚠️ Common Mistake

**Wrong:**
```r
names_from(column)  # Wrong syntax
```

**Fixed:**
```r
names_from = column
```

---

✅ **No Hidden Prerequisites**: Argument naming.
""")

lessons["20424"] = create_reinforcer(2042, 4, "Challenge: Comparison Table",
"""# 🦸 Challenge: Create a Comparison

## What You'll Learn
Use widening to create side-by-side comparisons.

## Why This Matters
Wide format is great for comparison tables and crosstabs.

> 💡 The `%>%` transforms your data shape.

## Example

Pattern:
```r
data %>%
  pivot_wider(names_from = category, values_from = value)
```

## 🎯 Your Task

Create a table comparing penguin body mass by species and island:
1. Start with a grouped summary
2. Pivot to put islands as columns
3. Species as rows, islands as columns

**Expected Output:**
A comparison table (species × island)

## ⚠️ Common Mistake

Need to summarize BEFORE pivoting — can't pivot raw data directly.

---

✅ **No Hidden Prerequisites**: Combines grouping with pivoting.
""")

# ===== 2051: Projects & Paths =====
lessons["20511"] = create_reinforcer(2051, 1, "Analogy: Your Office Desk",
"""# 🏢 RStudio Projects

## What You'll Learn
Why projects organize your work and simplify file paths.

## Why This Matters
Projects set a "home base" directory. All paths become relative. Moving the folder doesn't break your code.

## Example

```r
# Without project: full path needed
read_csv("/Users/me/Documents/work/data/file.csv")

# With project: relative path
read_csv("data/file.csv")
```

## 🎯 Your Task

1. Create a new project in RStudio
2. Notice the .Rproj file created
3. All file paths are now relative to this folder

**Expected Output:**
Understanding why relative paths are better

## ⚠️ Common Mistake

**Wrong:**
Using full absolute paths like `/Users/...`

**Fixed:**
Use relative paths within a project.

---

✅ **No Hidden Prerequisites**: Conceptual lesson about projects.
""")

lessons["20512"] = create_reinforcer(2051, 2, "Variation: Working Directory",
"""# 📂 Check Your Location

## What You'll Learn
How to check and understand your working directory.

## Why This Matters
If `read_csv("data.csv")` can't find the file, your working directory is wrong.

## Example

```r
# Where am I?
getwd()

# What's here?
list.files()
```

## 🎯 Your Task

1. Run `getwd()` to see current directory
2. Run `list.files()` to see what's there
3. If in a project, you're in the project folder

**Expected Output:**
The path to your current working directory

## ⚠️ Common Mistake

**Wrong:**
```r
setwd("/some/path")  # Fragile, avoid
```

**Fixed:**
Use projects instead of `setwd()`.

---

✅ **No Hidden Prerequisites**: Uses base R functions.
""")

lessons["20513"] = create_reinforcer(2051, 3, "Fix the Code: File Not Found",
"""# 🔧 Fix: Path Problems

## What You'll Learn
How to debug "file not found" errors.

## Why This Matters
Most path errors are typos or wrong directory.

## Example

```r
# Error: cannot open file 'dataa.csv'
read_csv("dataa.csv")  # Typo!

# Fixed
read_csv("data.csv")
```

## 🎯 Your Task

1. Check spelling of filename
2. Use `list.files()` to see actual files
3. Check if file is in a subfolder

**Expected Output:**
File loads successfully

## ⚠️ Common Mistake

**Wrong:**
```r
read_csv("Data.csv")  # Case matters on some systems
```

**Fixed:**
```r
read_csv("data.csv")  # Match exact case
```

---

✅ **No Hidden Prerequisites**: Debugging file paths.
""")

lessons["20514"] = create_reinforcer(2051, 4, "Challenge: Organize a Project",
"""# 🦸 Challenge: Project Structure

## What You'll Learn
Apply project organization best practices.

## Why This Matters
A tidy project is a reproducible project.

## Example

Recommended structure:
```
my_project/
├── data/          # Raw data
├── scripts/       # R code
├── output/        # Results
└── my_project.Rproj
```

## 🎯 Your Task

1. Create folders: data, scripts, output
2. Put data files in data/
3. Put analysis scripts in scripts/
4. Save outputs to output/

**Expected Output:**
An organized project folder

## ⚠️ Common Mistake

Mixing raw data with processed data — keep them separate!

---

✅ **No Hidden Prerequisites**: Folder organization concepts.
""")

# Save
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Part 3 complete: Created reinforcers for 2041, 2042, 2051 (12 reinforcers)")
