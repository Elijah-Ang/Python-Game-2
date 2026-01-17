"""
Create Missing R Reinforcers - Part 2
Concepts: 2012, 2024, 2031
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
        "chapter_id": concept.get("chapter_id", 1),
        "chapter_title": concept.get("chapter_title", ""),
        "gap_ids": ["R-REINF"],
        "batch_id": "R-3"
    }

# ===== 2012: Calling Functions =====
lessons["20121"] = create_reinforcer(2012, 1, "Analogy: Recipes",
"""# 📋 Functions Are Recipes

## What You'll Learn
How functions take inputs and produce outputs, like following a recipe.

## Why This Matters
Functions do work for you. Give them ingredients (arguments), get back a result. `mean(x)` gives you the average of x.

## Example

```r
mean(c(1, 2, 3, 4, 5))
# Returns: 3
```

## 🎯 Your Task

1. Call `mean()` with the numbers 10, 20, 30
2. Use `c()` to combine the numbers
3. Observe the returned average

**Expected Output:**
`20` (the mean of 10, 20, 30)

## ⚠️ Common Mistake

**Wrong:**
```r
mean(10, 20, 30)  # Multiple arguments
```

**Fixed:**
```r
mean(c(10, 20, 30))  # One vector argument
```

---

✅ **No Hidden Prerequisites**: Uses `mean()` and `c()` from this lesson.
""")

lessons["20122"] = create_reinforcer(2012, 2, "Variation: Named Arguments",
"""# 🏷️ Named Arguments

## What You'll Learn
How to use named arguments for clarity and control.

## Why This Matters
`na.rm = TRUE` is clearer than just `TRUE`. Named arguments document your intent.

## Example

```r
# With NA values
x <- c(1, 2, NA, 4)
mean(x)                 # Returns NA
mean(x, na.rm = TRUE)   # Returns 2.33
```

## 🎯 Your Task

1. Try `mean(c(5, 10, NA))` — you get NA
2. Add `na.rm = TRUE` to ignore the NA
3. Verify you get 7.5

**Expected Output:**
`7.5`

## ⚠️ Common Mistake

**Wrong:**
```r
mean(x, TRUE)  # Unclear what TRUE means
```

**Fixed:**
```r
mean(x, na.rm = TRUE)  # Self-documenting
```

---

✅ **No Hidden Prerequisites**: Uses named arguments from this lesson.
""")

lessons["20123"] = create_reinforcer(2012, 3, "Fix the Code: Missing Parentheses",
"""# 🔧 Fix: Function Call Syntax

## What You'll Learn
Functions need parentheses, even with no arguments.

## Why This Matters
Without `()`, R returns the function itself, not its result.

## Example

```r
# Wrong — returns function object
nrow

# Fixed — actually calls the function
nrow(penguins)
```

## 🎯 Your Task

1. The code is missing parentheses
2. Add `()` with the data frame inside
3. Verify you get the row count

**Expected Output:**
`344` (number of rows in penguins)

## ⚠️ Common Mistake

**Wrong:**
```r
nrow
```

**Fixed:**
```r
nrow(penguins)
```

---

✅ **No Hidden Prerequisites**: Basic function calling syntax.
""")

lessons["20124"] = create_reinforcer(2012, 4, "Challenge: Chain Functions",
"""# 🦸 Challenge: Nested Calls

## What You'll Learn
Use function outputs as inputs to other functions.

## Why This Matters
Real analysis chains functions: round the mean, get the length of unique values, etc.

## Example

```r
round(mean(c(1.5, 2.5, 3.5)), digits = 1)
```

## 🎯 Your Task

Find the rounded average body mass of penguins:
1. Get `penguins$body_mass_g`
2. Calculate `mean(..., na.rm = TRUE)`
3. Wrap with `round(..., digits = 0)`

**Expected Output:**
`4202` (rounded mean body mass)

## ⚠️ Common Mistake

**Wrong:**
Forgetting `na.rm = TRUE` when there are NAs.

**Fixed:**
Always check if your data has NA values.

---

✅ **No Hidden Prerequisites**: Combines `round()`, `mean()`, `$` access.
""")

# ===== 2024: Groups & Summaries =====
lessons["20241"] = create_reinforcer(2024, 1, "Analogy: Sorting into Bins",
"""# 📊 Group, Then Summarize

## What You'll Learn
How `group_by()` + `summarize()` calculates statistics per group.

## Why This Matters
"What's the average mass PER species?" requires grouping first, then calculating. This is the core of data analysis.

> 💡 The `%>%` takes data and passes it to the next function.

## Example

```r
penguins %>%
  group_by(species) %>%
  summarize(avg_mass = mean(body_mass_g, na.rm = TRUE))
```

## 🎯 Your Task

1. Group penguins by species
2. Summarize to get the mean body mass per species
3. You should see 3 rows (one per species)

**Expected Output:**
A table with species and avg_mass columns (3 rows)

## ⚠️ Common Mistake

**Wrong:**
```r
summarize(avg = mean(body_mass_g))  # Forgot to group!
```

**Fixed:**
```r
group_by(species) %>% summarize(...)
```

---

✅ **No Hidden Prerequisites**: Uses `group_by()` and `summarize()` from this lesson.
""")

lessons["20242"] = create_reinforcer(2024, 2, "Variation: Multiple Summaries",
"""# 📈 Multiple Stats at Once

## What You'll Learn
Calculate multiple summary statistics in one `summarize()` call.

## Why This Matters
One pass through the data gives you mean, median, min, max — all at once.

> 💡 The `%>%` passes grouped data to summarize.

## Example

```r
penguins %>%
  group_by(species) %>%
  summarize(
    avg_mass = mean(body_mass_g, na.rm = TRUE),
    max_mass = max(body_mass_g, na.rm = TRUE),
    count = n()
  )
```

## 🎯 Your Task

1. Group by species
2. Calculate BOTH mean AND count
3. Use `n()` for count (no arguments needed)

**Expected Output:**
Table with species, avg_mass, and count columns

## ⚠️ Common Mistake

**Wrong:**
```r
summarize(mean, max)  # Function names only
```

**Fixed:**
```r
summarize(avg = mean(col), max = max(col))
```

---

✅ **No Hidden Prerequisites**: Uses `n()` and multiple summaries.
""")

lessons["20243"] = create_reinforcer(2024, 3, "Fix the Code: Forgot na.rm",
"""# 🔧 Fix: NA in Summary

## What You'll Learn
Why summaries return NA when data contains missing values.

## Why This Matters
One NA poisons the whole calculation. Always use `na.rm = TRUE` with real data.

## Example

```r
# Wrong — returns NA
mean(c(1, 2, NA))

# Fixed
mean(c(1, 2, NA), na.rm = TRUE)
```

## 🎯 Your Task

1. The summary is returning NA
2. Add `na.rm = TRUE` to the mean/sum function
3. Verify you get a number

**Expected Output:**
Actual numeric values, not NA

## ⚠️ Common Mistake

**Wrong:**
```r
summarize(avg = mean(body_mass_g))
```

**Fixed:**
```r
summarize(avg = mean(body_mass_g, na.rm = TRUE))
```

---

✅ **No Hidden Prerequisites**: NA handling in summaries.
""")

lessons["20244"] = create_reinforcer(2024, 4, "Challenge: Group by Two",
"""# 🦸 Challenge: Multiple Groups

## What You'll Learn
Group by multiple columns for finer breakdowns.

## Why This Matters
"Average mass per species AND sex" gives you 6 groups instead of 3.

> 💡 The `%>%` chains the operations together.

## Example

```r
group_by(col1, col2)
```

## 🎯 Your Task

Get average mass grouped by BOTH species AND island:
1. Use `group_by(species, island)`
2. Summarize with mean body mass
3. How many rows do you get?

**Expected Output:**
5 rows (not all species live on all islands)

## ⚠️ Common Mistake

**Wrong:**
```r
group_by(species) %>% group_by(island)  # Replaces!
```

**Fixed:**
```r
group_by(species, island)  # Both at once
```

---

✅ **No Hidden Prerequisites**: Multiple grouping columns.
""")

# ===== 2031: Pipes & Formatting =====
lessons["20311"] = create_reinforcer(2031, 1, "Analogy: Assembly Line",
"""# 🏭 The Pipe Assembly Line

## What You'll Learn
How `%>%` chains operations for readable code.

## Why This Matters
Without pipes: `f(g(h(x)))` — inside out, hard to read.
With pipes: `x %>% h() %>% g() %>% f()` — left to right, step by step.

## Example

```r
# Without pipe (hard to read)
round(mean(na.omit(penguins$body_mass_g)), 1)

# With pipe (clear steps)
penguins$body_mass_g %>%
  na.omit() %>%
  mean() %>%
  round(1)
```

## 🎯 Your Task

1. Read the piped version left-to-right
2. Each `%>%` passes the result to the next function
3. Understand: data flows through the pipe

**Expected Output:**
Understanding that pipes improve readability

## ⚠️ Common Mistake

**Wrong:**
```r
x %>% mean  # Missing parentheses
```

**Fixed:**
```r
x %>% mean()
```

---

✅ **No Hidden Prerequisites**: Introduces `%>%` pipe concept.
""")

lessons["20312"] = create_reinforcer(2031, 2, "Variation: Native Pipe",
"""# |> vs %>%

## What You'll Learn
R 4.1+ has a built-in pipe `|>` (native) vs tidyverse `%>%` (magrittr).

## Why This Matters
Both work. `|>` is built-in (no package needed). `%>%` has extra features. Most code works with either.

## Example

```r
# Tidyverse pipe
penguins %>% filter(species == "Adelie")

# Native pipe (R 4.1+)
penguins |> filter(species == "Adelie")
```

## 🎯 Your Task

1. Try replacing `%>%` with `|>` in existing code
2. Both should give the same result
3. Pick one style and be consistent

**Expected Output:**
Same result with either pipe

## ⚠️ Common Mistake

Don't mix `|>` and `%>%` in the same pipeline — pick one.

---

✅ **No Hidden Prerequisites**: Pipe variants.
""")

lessons["20313"] = create_reinforcer(2031, 3, "Fix the Code: Pipe Placement",
"""# 🔧 Fix: Pipe Syntax

## What You'll Learn
Common pipe syntax errors and how to fix them.

## Why This Matters
Pipes at wrong positions cause errors.

## Example

```r
# Wrong — pipe at start of line (after newline)
penguins
%>% filter(species == "Adelie")

# Fixed — pipe at end of previous line
penguins %>%
  filter(species == "Adelie")
```

## 🎯 Your Task

1. The pipe is in the wrong position
2. Move it to the end of the previous line
3. Verify the code runs

**Expected Output:**
Filtered data (no error)

## ⚠️ Common Mistake

**Wrong:**
```r
penguins
  %>% filter(...)
```

**Fixed:**
```r
penguins %>%
  filter(...)
```

---

✅ **No Hidden Prerequisites**: Pipe syntax rules.
""")

lessons["20314"] = create_reinforcer(2031, 4, "Challenge: Build a Pipeline",
"""# 🦸 Challenge: Multi-Step Pipeline

## What You'll Learn
Build a complete data analysis pipeline.

## Why This Matters
Real workflows chain many steps: filter, mutate, group, summarize.

> 💡 Each `%>%` passes the result to the next step.

## Example

```r
data %>%
  step1() %>%
  step2() %>%
  step3()
```

## 🎯 Your Task

Create a pipeline that:
1. Starts with `penguins`
2. Filters to Adelie species only
3. Groups by island
4. Summarizes mean body mass

**Expected Output:**
A table with island and mean mass for Adelie penguins

## ⚠️ Common Mistake

**Wrong:**
Forgetting `%>%` between steps.

**Fixed:**
Every step needs `%>%` to connect to the next.

---

✅ **No Hidden Prerequisites**: Combines filter, group_by, summarize.
""")

# Save
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Part 2 complete: Created reinforcers for 2012, 2024, 2031 (12 reinforcers)")
