"""
Batch R-2 Rewrite Script - Part 4 (Final)
Concept: 2420 (Base R)
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

# ===== CONCEPT 2420: A Field Guide to Base R =====

lessons["24201"] = add_metadata({
    **lessons["24201"],
    "title": "Analogy: The Original Tools",
    "content": """# 🔧 The Original Toolbox

## What You'll Learn
When and why to use base R instead of tidyverse.

## Why This Matters
Base R was here first. Many packages, error messages, and legacy code use base R syntax. Knowing both makes you a more capable R programmer.

## Example

```r
# Tidyverse way
penguins %>% filter(species == "Adelie")

# Base R way
penguins[penguins$species == "Adelie", ]
```

Both get the same result!

## 🎯 Your Task

1. Base R uses `$` for columns and `[ , ]` for subsetting
2. `df[rows, columns]` — rows on left, columns on right
3. Try: `penguins[1:5, c("species", "island")]`

**Expected Output:**
First 5 rows, 2 columns

## ⚠️ Common Mistake

**Wrong:**
```r
penguins[species == "Adelie"]
```
Missing the comma and data frame reference!

**Fixed:**
```r
penguins[penguins$species == "Adelie", ]
```

---

✅ **No Hidden Prerequisites**: Uses base R `[ ]` and `$` syntax.
"""
})

lessons["24202"] = add_metadata({
    **lessons["24202"],
    "title": "Variation: Brackets",
    "content": """# 🔲 Single vs Double Brackets

## What You'll Learn
The difference between `[` and `[[` in R.

## Why This Matters
`[` returns a subset (same type), `[[` extracts a single element. For data frames, `df["col"]` returns a data frame, `df[["col"]]` returns a vector.

## Example

```r
# Returns a data frame with one column
penguins["species"]

# Returns the species vector itself
penguins[["species"]]

# Same as [[ for columns
penguins$species
```

## 🎯 Your Task

1. Use `[["column_name"]]` when you want the raw vector
2. Use `["column_name"]` when you want a mini data frame
3. Compare outputs of both on `penguins`

**Expected Output:**
Single brackets → tibble; double brackets → vector

## ⚠️ Common Mistake

**Wrong:**
Using `[` when you need a vector for a function.

**Fixed:**
Use `[[` or `$` to extract vectors.

---

✅ **No Hidden Prerequisites**: Base R subsetting.
"""
})

lessons["24203"] = add_metadata({
    **lessons["24203"],
    "title": "Fix the Code: Comma",
    "content": """# 🔧 Fix: Row-Column Comma

## What You'll Learn
The most common base R subsetting error: forgetting the comma.

## Why This Matters
`df[rows, cols]` must have a comma! `df[rows]` means columns (lists), which is confusing. For data frames, always use both positions.

## Example

```r
# Wrong: selects columns
penguins[1:5]

# Right: selects rows 1-5, all columns
penguins[1:5, ]
```

The trailing comma says "all columns".

## 🎯 Your Task

1. The code is missing a comma
2. Add `, ]` to say "all columns"
3. Now it correctly selects rows

**Broken:**
```r
penguins[1:10]
```

**Expected Output:**
First 10 rows of penguins

## ⚠️ Common Mistake

**Wrong:**
```r
df[1:10]
```
Selects columns, not rows!

**Fixed:**
```r
df[1:10, ]
```
Comma makes it rows.

---

✅ **No Hidden Prerequisites**: Base R `[ , ]` syntax.
"""
})

lessons["24204"] = add_metadata({
    **lessons["24204"],
    "title": "Challenge: Base R Filter",
    "content": """# 🦸 Challenge: Filter Without Tidyverse

## What You'll Learn
Apply base R to filter data.

## Why This Matters
Sometimes you can't use tidyverse (legacy code, package conflicts). This tests your base R skills.

## Example

```r
# Pattern for filtering in base R
df[df$column == value, ]
```

## 🎯 Your Task

Using ONLY base R (no pipes, no dplyr):
1. Filter penguins where `island == "Biscoe"`
2. Use the `df[condition, ]` pattern
3. Count how many rows (should be 168)

**Expected Output:**
168 rows of Biscoe penguins

## ⚠️ Common Mistake

**Wrong:**
```r
penguins[island == "Biscoe"]
```
Multiple errors: no `$`, wrong comma position.

**Fixed:**
```r
penguins[penguins$island == "Biscoe", ]
```

---

✅ **No Hidden Prerequisites**: Base R only - `[ ]`, `$`, `==`.
"""
})

with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Batch R-2 Part 4 complete: 2420 (4 reinforcers)")
print("\\nBatch R-2 TOTAL: 40 reinforcers across 10 concepts")
