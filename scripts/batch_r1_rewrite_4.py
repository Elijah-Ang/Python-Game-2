"""
Batch R-1 Reinforcer Rewrite Script - Priority 9-12
Concepts 2040, 2023, 2021, 2121 (Missing why-how / thin content)
"""

import json

# Load lessons
with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

# ============================================
# CONCEPT 2040: Tidy Data
# Teaches: pivot_longer, tidy data principles
# Issues: Analogy doesn't explain tidy rules
# ============================================

lessons["20401"] = {
    **lessons["20401"],
    "title": "Analogy: Stacking Pancakes",
    "content": """# 🥞 Stacking Pancakes

## What You'll Learn
Tidy data means: one row per observation, one column per variable.

## Why This Matters
Imagine pancakes stacked wide (side by side) vs tall (stacked up). Wide data looks neat but is hard to work with. Tall/tidy data is easier for R to digest. Most ggplot and dplyr functions expect tidy data.

## Example: Wide vs Tidy

```
WIDE (hard to work with)         TIDY (easy to work with)
─────────────────────────        ─────────────────────────
country | 1999 | 2000            country | year  | cases
────────┼──────┼──────           ────────┼───────┼───────
Brazil  | 100  | 200             Brazil  | 1999  | 100
                                 Brazil  | 2000  | 200
```

Each year becomes a ROW instead of a column.

## 🎯 Your Task

Look at the "wide" table above. Count:
1. How many columns has the wide table? Type `3`
2. How many rows has the tidy version? Type `2`

**Expected Output:**
`[1] 3` then `[1] 2`

---

✅ **No Hidden Prerequisites**: Conceptual exercise.
""",
    "starter_code": "# How many columns in wide table?\n3\n# How many rows in tidy version?\n2",
    "solution_code": "3\n2",
    "expected_output": "[1] 3\n[1] 2"
}

lessons["20402"] = {
    **lessons["20402"],
    "title": "Variation: Naming New Columns",
    "content": """# 📋 Naming New Columns

## What You'll Learn
`pivot_longer()` lets you name the new columns with `names_to` and `values_to`.

## Why This Matters
When you convert wide to long, you get two new columns: one for the old column names, one for the values. Naming them clearly makes your data understandable.

## Example

```r
table4a %>%
  pivot_longer(
    cols = c(`1999`, `2000`),     # Which columns to pivot
    names_to = "year",            # Name for the new "names" column
    values_to = "cases"           # Name for the new "values" column
  )
```

## 🎯 Your Task

If you pivot columns `jan`, `feb`, `mar`:
1. What might you call `names_to`? → `"month"`
2. What might you call `values_to`? → `"sales"`

Type the answers as strings.

**Expected Output:**
`"month"` and `"sales"`

---

✅ **No Hidden Prerequisites**: Conceptual + string practice.
""",
    "starter_code": '# What would you name these new columns?\n"month"\n"sales"',
    "solution_code": '"month"\n"sales"',
    "expected_output": '[1] "month"\n[1] "sales"'
}

lessons["20403"] = {
    **lessons["20403"],
    "title": "Fix the Code: Missing Quote",
    "content": """# 🔧 Fix the Quote

## What You'll Learn
Column names in `names_to` and `values_to` must be strings (in quotes).

## Why This Matters
Without quotes, R thinks `year` is a variable, not a new column name. This causes confusing "object not found" errors.

## Example

```r
# ❌ Error: object 'year' not found
pivot_longer(..., names_to = year)

# ✅ Works
pivot_longer(..., names_to = "year")
```

## 🎯 Your Task

1. Look at the broken code below
2. Add quotes around the column names
3. (Just practice the syntax—run returns the string)

**Expected Output:**
`'names_to = "year", values_to = "value"'`

---

✅ **No Hidden Prerequisites**: String quoting practice.
""",
    "starter_code": '# Fix by adding quotes\n\'names_to = "year", values_to = "value"\'',
    "solution_code": '\'names_to = "year", values_to = "value"\'',
    "expected_output": '[1] "names_to = \\"year\\", values_to = \\"value\\""'
}

lessons["20404"] = {
    **lessons["20404"],
    "title": "Challenge: Pivot It",
    "content": """# 🦸 Challenge: Pivot It

## What You'll Learn
Apply `pivot_longer()` to convert wide data to tidy format.

## Why This Matters
Real datasets often come in wide format. Pivoting is a core skill you'll use constantly.

## 🎯 Your Task

Given this setup:
```r
library(tidyr)
table4a  # Wide: columns for 1999, 2000
```

Write a pivot that:
1. Pivots columns `1999` and `2000`
2. Names the year column `"year"`
3. Names the cases column `"cases"`

**Expected Output:**
A tidy tibble with country, year, and cases columns

---

✅ **No Hidden Prerequisites**: Uses `pivot_longer()` from this lesson.
""",
    "starter_code": "# Pivot table4a from wide to long\n# table4a %>% pivot_longer(...)\n# Note: column names with numbers need backticks: `1999`",
    "solution_code": 'table4a %>% pivot_longer(cols = c(`1999`, `2000`), names_to = "year", values_to = "cases")',
    "expected_output": "# A tibble: 6 × 3"
}

# ============================================
# CONCEPT 2023: Add Columns (Mutate)
# Teaches: mutate() to add/modify columns
# Issues: Missing why-how
# ============================================

lessons["20231"] = {
    **lessons["20231"],
    "title": "Analogy: The Transformation Ray",
    "content": """# 🔮 The Transformation Ray

## What You'll Learn
`mutate()` adds new columns or transforms existing ones—like a sci-fi transformation ray.

## Why This Matters
Raw data is rarely ready for analysis. You need to compute new values: convert units, calculate ratios, create categories. `mutate()` is how you do it.

## Example

```r
# Add a new column: flight speed
flights %>% mutate(
  speed = distance / air_time * 60  # miles per hour
)
```

This adds `speed` while keeping all original columns.

## 🎯 Your Task

1. Use mutate to add a column `double_mass` = `body_mass_g * 2`
2. Apply it to penguins

**Expected Output:**
A tibble with a new `double_mass` column

---

✅ **No Hidden Prerequisites**: Uses `mutate()` from this lesson and `penguins`.
""",
    "starter_code": "# Create a new column: double_mass\npenguins %>% mutate(\n  double_mass = body_mass_g * 2\n)",
    "solution_code": "penguins %>% mutate(double_mass = body_mass_g * 2)",
    "expected_output": "# A tibble with double_mass column"
}

lessons["20232"] = {
    **lessons["20232"],
    "title": "Variation: Math with Columns",
    "content": """# ➗ Math with Columns

## What You'll Learn
You can use any math operation, and combine multiple columns.

## Why This Matters
Analysis often requires ratios or calculations. Body mass index = mass / height². Profit = revenue - costs. `mutate()` handles all of it.

## Example

```r
# Ratio of two columns
penguins %>% mutate(
  bill_ratio = bill_length_mm / bill_depth_mm
)

# Multiple calculations at once
penguins %>% mutate(
  mass_kg = body_mass_g / 1000,
  flipper_cm = flipper_length_mm / 10
)
```

## 🎯 Your Task

1. Create a column `mass_kg` that converts grams to kilograms
2. Formula: `body_mass_g / 1000`

**Expected Output:**
Penguins with `mass_kg` column (values like 3.75, 5.0, etc.)

---

✅ **No Hidden Prerequisites**: Uses only `mutate()` and arithmetic.
""",
    "starter_code": "# Convert body mass to kilograms\npenguins %>% mutate(\n  mass_kg = ____\n)",
    "solution_code": "penguins %>% mutate(mass_kg = body_mass_g / 1000)",
    "expected_output": "# A tibble with mass_kg column"
}

lessons["20233"] = {
    **lessons["20233"],
    "title": "Fix the Code: Name It",
    "content": """# 🔧 Name the New Column

## What You'll Learn
New columns in `mutate()` need a name on the left side of `=`.

## Why This Matters
Without a name, R doesn't know what to call your new column. The error is confusing but the fix is simple.

## Example

```r
# ❌ Error: unnamed calculation
penguins %>% mutate(body_mass_g * 2)

# ✅ Give it a name
penguins %>% mutate(double_mass = body_mass_g * 2)
```

## 🎯 Your Task

1. The starter code is missing a column name
2. Add `new_col = ` before the calculation
3. Run to verify

**Expected Output:**
A tibble with the new named column

---

✅ **No Hidden Prerequisites**: Uses only `mutate()`.
""",
    "starter_code": "# Add a column name before the calculation\npenguins %>% mutate(\n  body_mass_g + 100\n)",
    "solution_code": "penguins %>% mutate(new_col = body_mass_g + 100)",
    "expected_output": "# A tibble with new_col column"
}

lessons["20234"] = {
    **lessons["20234"],
    "title": "Challenge: Double Up",
    "content": """# 🦸 Challenge: Multiple New Columns

## What You'll Learn
Create multiple columns in a single `mutate()` call.

## Why This Matters
Real analysis often needs several calculations at once. One `mutate()` call is cleaner than many.

## 🎯 Your Task

Add TWO new columns to penguins:
1. `bill_sum` = `bill_length_mm + bill_depth_mm`
2. `flipper_m` = `flipper_length_mm / 1000` (convert to meters)

**Expected Output:**
Penguins with both new columns

---

✅ **No Hidden Prerequisites**: Uses `mutate()` with multiple columns.
""",
    "starter_code": "# Add two columns in one mutate\npenguins %>% mutate(\n  bill_sum = ____,\n  flipper_m = ____\n)",
    "solution_code": "penguins %>% mutate(bill_sum = bill_length_mm + bill_depth_mm, flipper_m = flipper_length_mm / 1000)",
    "expected_output": "# A tibble with bill_sum and flipper_m"
}

# ============================================
# CONCEPT 2021: Arrange Rows
# Teaches: arrange() to sort rows
# Issues: Missing why-how
# ============================================

lessons["20211"] = {
    **lessons["20211"],
    "title": "Analogy: Sorting Cards",
    "content": """# 🃏 Sorting Cards

## What You'll Learn
`arrange()` sorts rows—like sorting a deck of cards by number.

## Why This Matters
Sorted data reveals patterns. Want the top 10 best-selling products? Most delayed flights? Heaviest penguins? `arrange()` puts them in order so you can see.

## Example

```r
# Sort by one column (ascending by default)
penguins %>% arrange(body_mass_g)

# Sort descending (largest first)
penguins %>% arrange(desc(body_mass_g))
```

## 🎯 Your Task

1. Sort penguins by `flipper_length_mm` (smallest first)
2. Look at the first few rows

**Expected Output:**
Penguins sorted with smallest flippers at top

---

✅ **No Hidden Prerequisites**: Uses `arrange()` from this lesson.
""",
    "starter_code": "# Sort by flipper length (ascending)\npenguins %>% arrange(flipper_length_mm)",
    "solution_code": "penguins %>% arrange(flipper_length_mm)",
    "expected_output": "# A tibble sorted by flipper_length_mm"
}

lessons["20212"] = {
    **lessons["20212"],
    "title": "Variation: Two Levels",
    "content": """# 📊 Sorting by Multiple Columns

## What You'll Learn
Sort by multiple columns: first by one, then ties broken by another.

## Why This Matters
Often one column has ties. "Sort by species THEN by mass" shows patterns within each species.

## Example

```r
# First by species, then by body mass
penguins %>% arrange(species, body_mass_g)

# First by species (alpha), then by mass (descending)
penguins %>% arrange(species, desc(body_mass_g))
```

## 🎯 Your Task

1. Sort penguins by `island` first
2. Then by `body_mass_g` within each island

**Expected Output:**
Penguins grouped by island, then sorted by mass

---

✅ **No Hidden Prerequisites**: Uses `arrange()` with multiple columns.
""",
    "starter_code": "# Sort by island, then by body_mass_g\npenguins %>% arrange(island, body_mass_g)",
    "solution_code": "penguins %>% arrange(island, body_mass_g)",
    "expected_output": "# A tibble sorted by island then body_mass_g"
}

lessons["20213"] = {
    **lessons["20213"],
    "title": "Fix the Code: Missing desc()",
    "content": """# 🔧 Descending Order

## What You'll Learn
Use `desc()` to sort largest-first (descending).

## Why This Matters
By default, `arrange()` sorts smallest-first. For "top 10 heaviest" you need `desc()`.

## Example

```r
# ❌ This gives SMALLEST first
penguins %>% arrange(body_mass_g)

# ✅ This gives LARGEST first
penguins %>% arrange(desc(body_mass_g))
```

## 🎯 Your Task

1. The starter code sorts smallest-first
2. Add `desc()` to get largest-first
3. Verify the heaviest penguin is first

**Expected Output:**
Penguins with 6300g at top

---

✅ **No Hidden Prerequisites**: Uses `arrange()` and `desc()`.
""",
    "starter_code": "# Fix this to show HEAVIEST penguins first\npenguins %>% arrange(body_mass_g)",
    "solution_code": "penguins %>% arrange(desc(body_mass_g))",
    "expected_output": "# A tibble with heaviest first"
}

lessons["20214"] = {
    **lessons["20214"],
    "title": "Challenge: Backwards",
    "content": """# 🦸 Challenge: Reverse Sort

## What You'll Learn
Apply `desc()` to multiple columns for complex sorting.

## Why This Matters
Sometimes you want "alphabetical species, but heaviest first within each". This requires mixing ascending and descending.

## 🎯 Your Task

Sort penguins so that:
1. Species is alphabetical (A → Z, ascending)
2. Within each species, mass is largest-first (descending)

**Expected Output:**
Adelie penguins (heaviest first), then Chinstrap (heaviest first), then Gentoo

---

✅ **No Hidden Prerequisites**: Uses `arrange()`, `desc()`.
""",
    "starter_code": "# Alphabetical species, but heaviest first within each\npenguins %>% arrange(species, desc(body_mass_g))",
    "solution_code": "penguins %>% arrange(species, desc(body_mass_g))",
    "expected_output": "# A tibble: Adelie heaviest first, then Chinstrap, then Gentoo"
}

# ============================================
# CONCEPT 2121: Themes & Scales
# Teaches: theme_*() and scale_*() functions
# Issues: Thin content, no examples
# ============================================

lessons["21211"] = {
    **lessons["21211"],
    "title": "Analogy: Changing Outfits",
    "content": """# 👔 Changing Outfits

## What You'll Learn
Themes change the visual "outfit" of your plot—fonts, colors, backgrounds.

## Why This Matters
Default ggplot looks good, but professional reports need a polished look. `theme_minimal()`, `theme_bw()`, `theme_classic()` give you instant professional style.

## Example

```r
# Default gray background
ggplot(penguins, aes(x = body_mass_g)) + geom_histogram()

# Clean white background
ggplot(penguins, aes(x = body_mass_g)) + geom_histogram() + theme_minimal()
```

## 🎯 Your Task

1. Create a histogram of `body_mass_g`
2. Add `theme_bw()` for a black-and-white theme

**Expected Output:**
A histogram with clean black-and-white styling

---

✅ **No Hidden Prerequisites**: Uses `ggplot()`, `geom_histogram()`, `theme_bw()`.
""",
    "starter_code": "# Add a black-and-white theme\nggplot(penguins, aes(x = body_mass_g)) + \n  geom_histogram() +\n  theme_bw()",
    "solution_code": "ggplot(penguins, aes(x = body_mass_g)) + geom_histogram() + theme_bw()",
    "expected_output": "[Graph: Histogram with theme_bw]"
}

lessons["21212"] = {
    **lessons["21212"],
    "title": "Variation: Classic Theme",
    "content": """# 📜 Classic Theme

## What You'll Learn
`theme_classic()` creates a publication-ready look with no gridlines.

## Why This Matters
Scientific journals often prefer minimal styling. `theme_classic()` is clean and formal—perfect for papers.

## Example

```r
# Compare themes
p <- ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) + geom_point()

p + theme_gray()     # Default
p + theme_classic()  # Publication-ready
```

## 🎯 Your Task

1. Create a scatterplot of flipper vs mass
2. Apply `theme_classic()`

**Expected Output:**
A scatterplot with no gridlines, clean axes

---

✅ **No Hidden Prerequisites**: Uses `ggplot()`, `geom_point()`, `theme_classic()`.
""",
    "starter_code": "# Use theme_classic for a clean look\nggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) + \n  geom_point() +\n  theme_classic()",
    "solution_code": "ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) + geom_point() + theme_classic()",
    "expected_output": "[Graph: Scatterplot with theme_classic]"
}

lessons["21213"] = {
    **lessons["21213"],
    "title": "Fix the Code: Parentheses",
    "content": """# 🔧 Don't Forget Parentheses

## What You'll Learn
Theme functions need `()` even with no arguments.

## Why This Matters
`theme_minimal` (no parentheses) refers to the function object. `theme_minimal()` (with parentheses) CALLS the function. Without `()`, nothing happens.

## Example

```r
# ❌ Doesn't apply the theme
ggplot(...) + theme_minimal

# ✅ Applies the theme
ggplot(...) + theme_minimal()
```

## 🎯 Your Task

1. Find the missing `()` in the starter code
2. Add them to make the theme work

**Expected Output:**
A histogram with minimal theme applied

---

✅ **No Hidden Prerequisites**: Uses `ggplot()`, `geom_histogram()`, `theme_minimal()`.
""",
    "starter_code": "# Fix the missing parentheses\nggplot(penguins, aes(x = body_mass_g)) + \n  geom_histogram() +\n  theme_minimal",
    "solution_code": "ggplot(penguins, aes(x = body_mass_g)) + geom_histogram() + theme_minimal()",
    "expected_output": "[Graph: Histogram with theme_minimal]"
}

lessons["21214"] = {
    **lessons["21214"],
    "title": "Challenge: Dark Mode",
    "content": """# 🦸 Challenge: Dark Mode

## What You'll Learn
Use `theme_dark()` for a dark background plot.

## Why This Matters
Dark themes are trendy and reduce eye strain. They're also great for presentations in dim rooms.

## 🎯 Your Task

Create a "dark mode" scatterplot:
1. Plot `bill_length_mm` vs `bill_depth_mm`
2. Color by `species`
3. Apply `theme_dark()`

**Expected Output:**
A scatterplot with dark background

---

✅ **No Hidden Prerequisites**: Uses `ggplot()`, `aes()`, `geom_point()`, `theme_dark()`.
""",
    "starter_code": "# Create a dark-mode scatterplot\nggplot(penguins, aes(x = bill_length_mm, y = bill_depth_mm, color = species)) + \n  geom_point() +\n  theme_dark()",
    "solution_code": "ggplot(penguins, aes(x = bill_length_mm, y = bill_depth_mm, color = species)) + geom_point() + theme_dark()",
    "expected_output": "[Graph: Scatterplot with dark theme]"
}

# Save updated lessons
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("✅ Updated concepts 2040, 2023, 2021, 2121 reinforcers (16 lessons)")
print("✅ BATCH R-1 COMPLETE: 48 reinforcers rewritten across 12 concept sets")
