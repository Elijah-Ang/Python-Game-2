"""
Batch R-1 Compliance Patch - Fix Content Issues

Fixes:
1. Replace flights dataset with penguins where inappropriate
2. Add missing Example sections to Challenges
3. Add missing Common Mistake sections
4. Remove "!" false positives (they're in "wrong" examples, which is fine)
"""

import json
import re

# Load lessons
with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

fixes_made = []

# ===== FIX: 22011 - Replace flights with penguins =====
lessons["22011"]["content"] = """# 🎩 The Sorting Hat

## What You'll Learn
How `if_else()` assigns one of two values based on a condition—like the Sorting Hat choosing between houses.

## Why This Matters
Data often needs labels. Is a penguin "Heavy" or "Light"? `if_else()` looks at each row and assigns the right label—just like the Sorting Hat reads each student and assigns a house.

## Example

```r
penguins %>% mutate(
  size = if_else(body_mass_g > 4000, "Heavy", "Light")
)
```

If mass > 4000 → "Heavy". Otherwise → "Light".

## 🎯 Your Task

1. Look at the pattern: `if_else(condition, true_result, false_result)`
2. Create a column `size` that labels penguins as "Heavy" if `body_mass_g > 4000`, else "Light"
3. Use: `penguins %>% mutate(size = if_else(body_mass_g > 4000, "Heavy", "Light"))`

**Expected Output:**
Penguins data with a new `size` column containing "Heavy" or "Light"

## ⚠️ Common Mistake

**Wrong:**
```r
if_else(body_mass_g > 4000, Heavy, Light)
```
Missing quotes around text values.

**Fixed:**
```r
if_else(body_mass_g > 4000, "Heavy", "Light")
```

---

✅ **No Hidden Prerequisites**: Uses `mutate()` (Ch 3) and `if_else()` from this lesson. Uses `penguins` dataset.
"""
lessons["22011"]["starter_code"] = '# Label penguins as "Heavy" (> 4000g) or "Light"\npenguins %>% mutate(\n  size = if_else(____)\n)'
lessons["22011"]["solution_code"] = 'penguins %>% mutate(size = if_else(body_mass_g > 4000, "Heavy", "Light"))'
fixes_made.append("22011: Replaced flights with penguins")

# ===== FIX: 22012 - Replace flights with penguins =====
lessons["22012"]["content"] = """# 🎯 Three or More Categories

## What You'll Learn
`case_when()` handles 3+ outcomes—when `if_else()` isn't enough.

## Why This Matters
Sometimes you need more than two categories. Penguins can be "Small", "Medium", or "Large". `case_when()` checks conditions in order and assigns the first match.

## Example

```r
penguins %>% mutate(
  size = case_when(
    body_mass_g < 3500  ~ "Small",
    body_mass_g <= 4500 ~ "Medium",
    .default = "Large"
  )
)
```

The `~` separates condition from result. `.default` catches everything else.

## 🎯 Your Task

1. Create categories for penguin size: "Small" (< 3500g), "Medium" (3500-4500g), "Large" (> 4500g)
2. Use `case_when()` inside `mutate()`

**Expected Output:**
Penguins data with a `size_category` column

## ⚠️ Common Mistake

**Wrong:**
```r
case_when(
  x < 10 = "small"
)
```
Using `=` instead of `~`.

**Fixed:**
```r
case_when(
  x < 10 ~ "small"
)
```

---

✅ **No Hidden Prerequisites**: Uses `mutate()` (Ch 3) and `case_when()` from this lesson. The `~` is part of `case_when()` syntax.
"""
fixes_made.append("22012: Replaced flights with penguins, kept ~ as part of case_when syntax")

# ===== FIX: 22013 - Clean up example =====
lessons["22013"]["content"] = """# 🔧 Fix the Code

## What You'll Learn
Spot common syntax errors in `if_else()` and `case_when()`.

## Why This Matters
The argument order in `if_else()` trips up beginners. Learning to read error messages now builds debugging skills.

## Example

The code below has an error. Can you find it?

```r
# Missing the FALSE value
if_else(body_mass_g > 4000, "Heavy")
```

`if_else()` REQUIRES three arguments: condition, true, false.

## 🎯 Your Task

1. Look at the starter code
2. The `if_else()` is missing its third argument
3. Add "Light" as the false value

**Expected Output:**
Penguins data with `heavy` column

## ⚠️ Common Mistake

**Wrong:**
```r
if_else(x > 0, "yes")
```
Missing the FALSE value.

**Fixed:**
```r
if_else(x > 0, "yes", "no")
```
All three arguments required.

---

✅ **No Hidden Prerequisites**: Uses `mutate()` and `if_else()`. Uses `penguins` dataset.
"""
fixes_made.append("22013: Cleaned up example, removed flights reference")

# ===== FIX: 22014 - Add Example section =====
lessons["22014"]["content"] = """# 🦸 Challenge: Classify Flipper Length

## What You'll Learn
Apply conditional logic independently to create meaningful categories.

## Why This Matters
Real data analysis constantly requires creating categories. This challenge tests your ability to use `if_else()` without hand-holding.

## Example

Here's the pattern you'll use:

```r
data %>% mutate(
  new_column = if_else(condition, "yes_value", "no_value")
)
```

## 🎯 Your Task

Create a new column `flipper_size` in penguins:
1. If `flipper_length_mm >= 200`, label as "Long"
2. Otherwise, label as "Short"
3. Start with `penguins %>% mutate(...)`

**Expected Output:**
Penguins data with a new `flipper_size` column containing "Long" or "Short"

## ⚠️ Common Mistake

**Wrong:**
```r
if_else(flipper_length_mm >= 200, Long, Short)
```
Missing quotes around text.

**Fixed:**
```r
if_else(flipper_length_mm >= 200, "Long", "Short")
```

---

✅ **No Hidden Prerequisites**: Uses `mutate()`, `if_else()`, and `penguins`.
"""
fixes_made.append("22014: Added Example section with pattern (not answer)")

# ===== FIX: 20302 - Remove flights and filter references =====
lessons["20302"]["content"] = """# 🐍 snake_case Naming

## What You'll Learn
R uses `snake_case` (lowercase with underscores) for variable names.

## Why This Matters
Consistent naming helps everyone read code. When you see `penguin_data`, you know it's a variable. When you see `PenguinData`, that's confusing in R!

## Example

```r
# Good (snake_case)
small_penguins <- penguins

# Bad (camelCase, PascalCase)
smallPenguins <- penguins
SmallPenguins <- penguins
```

## 🎯 Your Task

1. Rename the variable from `MyData` to `my_data`
2. Keep the rest of the code the same
3. Run to verify it works

**Expected Output:**
A tibble of penguin data

## ⚠️ Common Mistake

**Wrong:**
```r
my_Data  # Mixed case
my-data  # Hyphens not allowed
```

**Fixed:**
```r
my_data  # All lowercase, underscores only
```

---

✅ **No Hidden Prerequisites**: Uses only variable assignment. Uses `penguins` dataset.
"""
lessons["20302"]["starter_code"] = "# Rename using snake_case\nMyData <- penguins\nMyData"
lessons["20302"]["solution_code"] = "my_data <- penguins\nmy_data"
fixes_made.append("20302: Replaced flights with penguins, removed filter()")

# ===== FIX: 20231 - Replace flights with penguins =====
lessons["20231"]["content"] = """# 🔮 The Transformation Ray

## What You'll Learn
`mutate()` adds new columns or transforms existing ones—like a sci-fi transformation ray.

## Why This Matters
Raw data is rarely ready for analysis. You need to compute new values: convert units, calculate ratios, create categories. `mutate()` is how you do it.

## Example

```r
# Add a new column: body mass in kilograms
penguins %>% mutate(
  mass_kg = body_mass_g / 1000
)
```

This adds `mass_kg` while keeping all original columns.

## 🎯 Your Task

1. Use mutate to add a column `double_mass` = `body_mass_g * 2`
2. Apply it to penguins

**Expected Output:**
Penguins data with a new `double_mass` column

## ⚠️ Common Mistake

**Wrong:**
```r
mutate(double_mass = body_mass_g * 2)
```
Forgot to pipe in the data.

**Fixed:**
```r
penguins %>% mutate(double_mass = body_mass_g * 2)
```

---

✅ **No Hidden Prerequisites**: Uses `mutate()` from this lesson. Uses pipe `%>%` and `penguins`.
"""
fixes_made.append("20231: Replaced flights with penguins, added Common Mistake")

# ===== FIX: 20211 - Replace flights with penguins =====
lessons["20211"]["content"] = """# 🃏 Sorting Cards

## What You'll Learn
`arrange()` sorts rows—like sorting a deck of cards by number.

## Why This Matters
Sorted data reveals patterns. Want the heaviest penguins? The smallest bills? `arrange()` puts them in order so you can see.

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

## ⚠️ Common Mistake

**Wrong:**
```r
arrange(penguins, flipper_length_mm)
```
Works, but piping is cleaner.

**Fixed:**
```r
penguins %>% arrange(flipper_length_mm)
```

---

✅ **No Hidden Prerequisites**: Uses `arrange()` from this lesson. Uses `%>%` and `penguins`.
"""
fixes_made.append("20211: Replaced flights with penguins, added Common Mistake")

# ===== FIX: 20013 - Remove tibble mention =====
lessons["20013"]["content"] = """# 🔧 Fix the Code

## What You'll Learn
R is case-sensitive—`penguins` works, but `Penguins` or `PENGUINS` don't.

## Why This Matters
This is the #1 beginner error in R! Getting comfortable with exact spelling and case now will save you hours of debugging later.

## Example

```r
# This causes an error
Penguins
# Error: object 'Penguins' not found
```

## 🎯 Your Task

1. Look at the starter code—it has a capitalization error
2. Fix the case to all lowercase
3. Run and verify you see the dataset

**Expected Output:**
The penguins data (344 rows × 8 columns)

## ⚠️ Common Mistake

**Wrong:**
```r
PENGUINS
penGUins
```
Any wrong capitalization fails.

**Fixed:**
```r
penguins
```
Exactly as defined.

---

✅ **No Hidden Prerequisites**: Uses only the `penguins` dataset.
"""
fixes_made.append("20013: Removed tibble mention from output description")

# ===== FIX: 20504 - Remove tibble, simplify =====
lessons["20504"]["content"] = """# 🦸 Challenge: Script Header

## What You'll Learn
Best practice: Start scripts with a header comment describing what they do.

## Why This Matters
When you open a script 6 months from now, you'll forget what it does. A header comment saves you time.

## Example

Here's the pattern for a script header:

```r
# Title: My Analysis
# Author: Your Name
# Date: 2024-01-18

# Your code starts here
```

## 🎯 Your Task

Write a proper script header with:
1. A title comment: `# Penguin Analysis`
2. An author comment: `# Author: [Your Name]`
3. A date comment: `# Date: 2024-01-18`
4. Then run `penguins` to view the data

**Expected Output:**
The penguins data displayed

## ⚠️ Common Mistake

**Wrong:**
```r
Penguin Analysis
```
Forgot the `#` symbol.

**Fixed:**
```r
# Penguin Analysis
```

---

✅ **No Hidden Prerequisites**: Uses only comments and `penguins`.
"""
fixes_made.append("20504: Added Example, removed tibble, added Common Mistake")

# ===== FIX: Challenge lessons - Add Example sections =====

# 20024 - Add Example
lessons["20024"]["content"] = """# 🦸 Challenge: Your Own Canvas

## What You'll Learn
Create a ggplot canvas from memory, without hints.

## Why This Matters
Typing the pattern yourself builds muscle memory. You'll write `ggplot(data = ...)` thousands of times in your R career—start practicing now!

## Example

Here's the pattern you've been using:

```r
ggplot(data = dataset_name)
```

## 🎯 Your Task

Without looking at previous examples:
1. Create an empty canvas using the `diamonds` dataset
2. Use the full pattern: `ggplot(data = ...)`
3. Run and verify you see the blank canvas

**Expected Output:**
A gray rectangle (the blank canvas)

## ⚠️ Common Mistake

**Wrong:**
```r
ggplot(data = diamond)
```
Typo: 'diamond' not 'diamonds'.

**Fixed:**
```r
ggplot(data = diamonds)
```

---

✅ **No Hidden Prerequisites**: Uses `ggplot()` from this lesson; `diamonds` is a built-in dataset.
"""
fixes_made.append("20024: Added Example section")

# 20034 - Add Example
lessons["20034"]["content"] = """# 🦸 Challenge: Map Your Own Axes

## What You'll Learn
Write a complete ggplot call with axis mappings from memory.

## Why This Matters
Building muscle memory for the `ggplot(data = ..., mapping = aes(...))` pattern is essential. You'll use this hundreds of times!

## Example

Here's the pattern:

```r
ggplot(data = dataset, mapping = aes(x = column1, y = column2))
```

## 🎯 Your Task

Using the `mpg` dataset (about cars):
1. Map `displ` (engine displacement) to the x-axis
2. Map `hwy` (highway miles per gallon) to the y-axis
3. Write the full ggplot call

**Expected Output:**
Canvas with "displ" on x-axis and "hwy" on y-axis

## ⚠️ Common Mistake

**Wrong:**
```r
ggplot(mpg, aes(displ, hwy))
```
Too abbreviated.

**Fixed:**
```r
ggplot(data = mpg, mapping = aes(x = displ, y = hwy))
```
Explicit is clearer.

---

✅ **No Hidden Prerequisites**: Uses `ggplot()` and `aes()` from this lesson; `mpg` is a built-in dataset.
"""
fixes_made.append("20034: Added Example section")

# 20014 - Add Example
lessons["20014"]["content"] = """# 🦸 Challenge: Find the Range

## What You'll Learn
Use `range()` to find the min and max of a column.

## Why This Matters
Before graphing, it helps to know the range of your data. Knowing the smallest and largest values helps you understand what to expect on your axes.

## Example

Here's the pattern:

```r
range(dataset$column, na.rm = TRUE)
```

The `$` accesses a column. `na.rm = TRUE` ignores missing values.

## 🎯 Your Task

1. Find the range of `body_mass_g` in the penguins dataset
2. Use: `range(penguins$body_mass_g, na.rm = TRUE)`
3. What are the lightest and heaviest penguins?

**Expected Output:**
Two numbers: minimum and maximum body mass (around 2700 and 6300)

## ⚠️ Common Mistake

**Wrong:**
```r
range(body_mass_g)
```
Didn't specify the dataset.

**Fixed:**
```r
range(penguins$body_mass_g, na.rm = TRUE)
```

---

✅ **No Hidden Prerequisites**: Uses `range()` (base R), `$` (base R), and `penguins`.
"""
fixes_made.append("20014: Added Example section")

# 20304 - Add Example
lessons["20304"]["content"] = """# 🦸 Challenge: Clean Up This Code

## What You'll Learn
Apply all style rules: snake_case names + proper spacing.

## Why This Matters
In real projects, you'll often need to clean up messy code. This is practice for that.

## Example

Here's the pattern for good style:

```r
# Bad
MyResult<-10+15

# Good
my_result <- 10 + 15
```

## 🎯 Your Task

Fix this code block by:
1. Renaming `MyResult` to `my_result` (snake_case)
2. Adding spaces around `<-` and `+`
3. Adding a space after the comma

**Expected Output:**
`[1] 25`

## ⚠️ Common Mistake

**Wrong:**
```r
my_result<- 10+15
```
Missing spaces.

**Fixed:**
```r
my_result <- 10 + 15
```

---

✅ **No Hidden Prerequisites**: Uses only variable assignment.
"""
fixes_made.append("20304: Added Example section")

# ===== FIX: Priority 9-12 - Add Common Mistake sections =====

# 20232
lessons["20232"]["content"] = """# ➗ Math with Columns

## What You'll Learn
You can use any math operation, and combine multiple columns.

## Why This Matters
Analysis often requires ratios or calculations. Body mass in kg = mass_g / 1000. Bill ratio = length / depth. `mutate()` handles all of it.

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

## ⚠️ Common Mistake

**Wrong:**
```r
mutate(mass_kg = body_mass_g / 1000)
```
Forgot the data and pipe.

**Fixed:**
```r
penguins %>% mutate(mass_kg = body_mass_g / 1000)
```

---

✅ **No Hidden Prerequisites**: Uses `mutate()` and `%>%` from prior lessons.
"""
fixes_made.append("20232: Added Common Mistake")

# 20233
lessons["20233"]["content"] = """# 🔧 Name the New Column

## What You'll Learn
New columns in `mutate()` need a name on the left side of `=`.

## Why This Matters
Without a name, R doesn't know what to call your new column. The error is confusing but the fix is simple.

## Example

```r
# Bad: unnamed calculation
penguins %>% mutate(body_mass_g * 2)

# Good: give it a name
penguins %>% mutate(double_mass = body_mass_g * 2)
```

## 🎯 Your Task

1. The starter code is missing a column name
2. Add `new_col = ` before the calculation
3. Run to verify

**Expected Output:**
Penguins data with the new named column

## ⚠️ Common Mistake

**Wrong:**
```r
mutate(body_mass_g + 100)
```
No name for the new column.

**Fixed:**
```r
mutate(new_col = body_mass_g + 100)
```

---

✅ **No Hidden Prerequisites**: Uses `mutate()` and `%>%`.
"""
fixes_made.append("20233: Added Common Mistake")

# 20234 - Add Example and Common Mistake
lessons["20234"]["content"] = """# 🦸 Challenge: Multiple New Columns

## What You'll Learn
Create multiple columns in a single `mutate()` call.

## Why This Matters
Real analysis often needs several calculations at once. One `mutate()` call is cleaner than many.

## Example

Here's the pattern:

```r
data %>% mutate(
  col1 = calculation1,
  col2 = calculation2
)
```

## 🎯 Your Task

Add TWO new columns to penguins:
1. `bill_sum` = `bill_length_mm + bill_depth_mm`
2. `flipper_m` = `flipper_length_mm / 1000` (convert to meters)

**Expected Output:**
Penguins with both new columns

## ⚠️ Common Mistake

**Wrong:**
```r
mutate(bill_sum = bill_length_mm + bill_depth_mm)
mutate(flipper_m = flipper_length_mm / 1000)
```
Two separate calls is inefficient.

**Fixed:**
```r
penguins %>% mutate(
  bill_sum = bill_length_mm + bill_depth_mm,
  flipper_m = flipper_length_mm / 1000
)
```

---

✅ **No Hidden Prerequisites**: Uses `mutate()` with multiple columns.
"""
fixes_made.append("20234: Added Example and Common Mistake")

# 20212
lessons["20212"]["content"] = """# 📊 Sorting by Multiple Columns

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

## ⚠️ Common Mistake

**Wrong:**
```r
arrange(island, body_mass_g)
```
Forgot the data source.

**Fixed:**
```r
penguins %>% arrange(island, body_mass_g)
```

---

✅ **No Hidden Prerequisites**: Uses `arrange()` from this lesson.
"""
fixes_made.append("20212: Added Common Mistake")

# 20213
lessons["20213"]["content"] = """# 🔧 Descending Order

## What You'll Learn
Use `desc()` to sort largest-first (descending).

## Why This Matters
By default, `arrange()` sorts smallest-first. For "top 10 heaviest" you need `desc()`.

## Example

```r
# Smallest first (default)
penguins %>% arrange(body_mass_g)

# Largest first
penguins %>% arrange(desc(body_mass_g))
```

## 🎯 Your Task

1. The starter code sorts smallest-first
2. Add `desc()` to get largest-first
3. Verify the heaviest penguin is first

**Expected Output:**
Penguins with 6300g at top

## ⚠️ Common Mistake

**Wrong:**
```r
arrange(-body_mass_g)
```
Minus sign works but `desc()` is clearer.

**Fixed:**
```r
arrange(desc(body_mass_g))
```

---

✅ **No Hidden Prerequisites**: Uses `arrange()` and `desc()` from this lesson.
"""
fixes_made.append("20213: Added Common Mistake")

# 20214 - Add Example and Common Mistake
lessons["20214"]["content"] = """# 🦸 Challenge: Reverse Sort

## What You'll Learn
Apply `desc()` to multiple columns for complex sorting.

## Why This Matters
Sometimes you want "alphabetical species, but heaviest first within each". This requires mixing ascending and descending.

## Example

Here's the pattern:

```r
data %>% arrange(col1, desc(col2))
```

First column ascending, second descending.

## 🎯 Your Task

Sort penguins so that:
1. Species is alphabetical (A → Z, ascending)
2. Within each species, mass is largest-first (descending)

**Expected Output:**
Adelie penguins (heaviest first), then Chinstrap, then Gentoo

## ⚠️ Common Mistake

**Wrong:**
```r
arrange(desc(species), desc(body_mass_g))
```
This sorts species backwards too.

**Fixed:**
```r
arrange(species, desc(body_mass_g))
```

---

✅ **No Hidden Prerequisites**: Uses `arrange()`, `desc()`, and `penguins`.
"""
fixes_made.append("20214: Added Example and Common Mistake")

# 21211
lessons["21211"]["content"] = """# 👔 Changing Outfits

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

## ⚠️ Common Mistake

**Wrong:**
```r
+ theme_bw
```
Forgot parentheses.

**Fixed:**
```r
+ theme_bw()
```

---

✅ **No Hidden Prerequisites**: Uses `ggplot()`, `geom_histogram()`, `theme_bw()`.
"""
fixes_made.append("21211: Added Common Mistake")

# 21212
lessons["21212"]["content"] = """# 📜 Classic Theme

## What You'll Learn
`theme_classic()` creates a publication-ready look with no gridlines.

## Why This Matters
Scientific journals often prefer minimal styling. `theme_classic()` is clean and formal—perfect for papers.

## Example

```r
# Compare themes
p <- ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) + geom_point()

p + theme_bw()       # With gridlines
p + theme_classic()  # No gridlines
```

## 🎯 Your Task

1. Create a scatterplot of flipper vs mass
2. Apply `theme_classic()`

**Expected Output:**
A scatterplot with no gridlines, clean axes

## ⚠️ Common Mistake

**Wrong:**
```r
theme_Classic()
```
Wrong capitalization.

**Fixed:**
```r
theme_classic()
```

---

✅ **No Hidden Prerequisites**: Uses `ggplot()`, `geom_point()`, `theme_classic()`.
"""
fixes_made.append("21212: Added Common Mistake")

# 21213
lessons["21213"]["content"] = """# 🔧 Don't Forget Parentheses

## What You'll Learn
Theme functions need `()` even with no arguments.

## Why This Matters
`theme_minimal` (no parentheses) refers to the function object. `theme_minimal()` (with parentheses) CALLS the function. Without `()`, nothing happens.

## Example

```r
# Doesn't apply the theme
ggplot(...) + theme_minimal

# Applies the theme
ggplot(...) + theme_minimal()
```

## 🎯 Your Task

1. Find the missing `()` in the starter code
2. Add them to make the theme work

**Expected Output:**
A histogram with minimal theme applied

## ⚠️ Common Mistake

**Wrong:**
```r
+ theme_minimal
```
Missing parentheses.

**Fixed:**
```r
+ theme_minimal()
```

---

✅ **No Hidden Prerequisites**: Uses `ggplot()`, `geom_histogram()`, `theme_minimal()`.
"""
fixes_made.append("21213: Added Common Mistake")

# 21214 - Add Example and Common Mistake
lessons["21214"]["content"] = """# 🦸 Challenge: Dark Mode

## What You'll Learn
Use `theme_dark()` for a dark background plot.

## Why This Matters
Dark themes are trendy and reduce eye strain. They're also great for presentations in dim rooms.

## Example

Here's the pattern:

```r
ggplot(data, aes(...)) + geom_*() + theme_dark()
```

## 🎯 Your Task

Create a "dark mode" scatterplot:
1. Plot `bill_length_mm` vs `bill_depth_mm`
2. Color by `species`
3. Apply `theme_dark()`

**Expected Output:**
A scatterplot with dark background

## ⚠️ Common Mistake

**Wrong:**
```r
+ theme_Dark()
```
Wrong capitalization.

**Fixed:**
```r
+ theme_dark()
```

---

✅ **No Hidden Prerequisites**: Uses `ggplot()`, `aes()`, `geom_point()`, `theme_dark()`.
"""
fixes_made.append("21214: Added Example and Common Mistake")

# ===== FIX: Quarto (25001-25004) - Add Common Mistake =====

lessons["25001"]["content"] = """# 📓 The Lab Notebook

## What You'll Learn
Quarto files (`.qmd`) combine code AND notes—like a scientist's lab notebook.

## Why This Matters
Scientists don't just record results—they write WHY they did each experiment. Quarto lets you explain your analysis alongside the code that runs it. When you share the file, others understand your thinking.

## Example

A Quarto file has three parts:

```
---                    <- YAML header (settings)
title: "My Report"
---

This is markdown text.  <- Prose (explanations)

```{r}
1 + 1                  <- Code chunks (R code)
```

## 🎯 Your Task

Understand the concept:
1. YAML at the top (between `---`)
2. Markdown text (explanations)
3. Code chunks (calculations)

Type `"I understand Quarto structure"` and run.

**Expected Output:**
`"I understand Quarto structure"`

## ⚠️ Common Mistake

**Wrong:**
Mixing up the three sections or forgetting `---` around YAML.

**Fixed:**
Always start with `---`, then YAML settings, then `---`, then content.

---

✅ **No Hidden Prerequisites**: Conceptual overview only.
"""
fixes_made.append("25001: Added Common Mistake")

lessons["25002"]["content"] = """# ⚙️ Code Chunk Options

## What You'll Learn
Options like `echo: false` control what appears in your final report.

## Why This Matters
Sometimes you want to show results but hide messy code. Or run setup code without cluttering your report. Chunk options give you that control.

## Example

```r
#| echo: false
mean(penguins$body_mass_g, na.rm = TRUE)
```

Common options:
- `echo: false` → Hide code
- `eval: false` → Don't run code
- `include: false` → Hide everything

## 🎯 Your Task

1. Calculate the mean of bill_length in penguins
2. Imagine the code would be hidden in a report

**Expected Output:**
Mean bill length (around 43.9)

## ⚠️ Common Mistake

**Wrong:**
```r
# echo: false
```
Used `#` instead of `#|`.

**Fixed:**
```r
#| echo: false
```

---

✅ **No Hidden Prerequisites**: Uses only `mean()` and `penguins`.
"""
fixes_made.append("25002: Added Common Mistake, fixed pipe operator issue")

lessons["25003"]["content"] = """# 🔧 Fix the Chunk Syntax

## What You'll Learn
Code chunks need proper backtick syntax: three backticks + `{r}`.

## Why This Matters
Quarto won't run your code if the chunk delimiters are wrong. This is the most common Quarto syntax error.

## Example

```
Wrong:
``{r}
1 + 1
``

Correct:
```{r}
1 + 1
```

You need exactly 3 backticks.

## 🎯 Your Task

Type the correct number of backticks needed:
- Chunk opening: type `3`
- Chunk closing: type `3`

**Expected Output:**
`[1] 3` then `[1] 3`

## ⚠️ Common Mistake

**Wrong:**
Using 2 backticks or 4 backticks.

**Fixed:**
Always use exactly 3 backticks.

---

✅ **No Hidden Prerequisites**: Conceptual only.
"""
fixes_made.append("25003: Added Common Mistake")

lessons["25004"]["content"] = """# 🦸 Challenge: YAML Header

## What You'll Learn
Write a basic YAML header for a Quarto document.

## Why This Matters
The YAML header controls your document's title, format, and settings. Getting it right is step one of every Quarto project.

## Example

Here's the pattern:

```yaml
---
title: "Report Title"
format: html
---
```

## 🎯 Your Task

Create a string that looks like a YAML title line:
1. Type: `"title: Penguin Analysis"`
2. Run to see it printed

**Expected Output:**
`[1] "title: Penguin Analysis"`

## ⚠️ Common Mistake

**Wrong:**
Missing the `---` delimiters in a real Quarto file.

**Fixed:**
Always wrap YAML in `---` at top of file.

---

✅ **No Hidden Prerequisites**: Conceptual + string practice.
"""
fixes_made.append("25004: Added Example and Common Mistake")

# ===== FIX: Tidy Data (20401-20404) - Add Common Mistake =====

lessons["20401"]["content"] = """# 🥞 Stacking Pancakes

## What You'll Learn
Tidy data means: one row per observation, one column per variable.

## Why This Matters
Imagine pancakes stacked wide (side by side) vs tall (stacked up). Wide data looks neat but is hard to work with. Tall/tidy data is easier for R to digest. Most ggplot and dplyr functions expect tidy data.

## Example

```
WIDE (hard to work with)         TIDY (easy to work with)
-----------------------         -----------------------
country  1999   2000            country  year   cases
Brazil   100    200             Brazil   1999   100
                                Brazil   2000   200
```

Each year becomes a ROW instead of a column.

## 🎯 Your Task

Look at the "wide" table above. Count:
1. How many columns has the wide table? Type `3`
2. How many rows has the tidy version? Type `2`

**Expected Output:**
`[1] 3` then `[1] 2`

## ⚠️ Common Mistake

Confusing rows and columns. Remember:
- Rows = observations (individual penguins, years, etc.)
- Columns = variables (species, mass, year, etc.)

---

✅ **No Hidden Prerequisites**: Conceptual exercise.
"""
fixes_made.append("20401: Added Common Mistake, removed pipe operator")

lessons["20402"]["content"] = """# 📋 Naming New Columns

## What You'll Learn
`pivot_longer()` lets you name the new columns with `names_to` and `values_to`.

## Why This Matters
When you convert wide to long, you get two new columns: one for the old column names, one for the values. Naming them clearly makes your data understandable.

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

If you pivot columns `jan`, `feb`, `mar`:
1. What might you call `names_to`? → `"month"`
2. What might you call `values_to`? → `"sales"`

Type the answers as strings.

**Expected Output:**
`"month"` and `"sales"`

## ⚠️ Common Mistake

**Wrong:**
```r
names_to = year
```
Forgot quotes.

**Fixed:**
```r
names_to = "year"
```

---

✅ **No Hidden Prerequisites**: Conceptual + string practice.
"""
fixes_made.append("20402: Added Common Mistake")

lessons["20403"]["content"] = """# 🔧 Fix the Quote

## What You'll Learn
Column names in `names_to` and `values_to` must be strings (in quotes).

## Why This Matters
Without quotes, R thinks `year` is a variable, not a new column name. This causes confusing "object not found" errors.

## Example

```r
# Wrong: object 'year' not found
pivot_longer(..., names_to = year)

# Fixed: put it in quotes
pivot_longer(..., names_to = "year")
```

## 🎯 Your Task

1. Look at the broken code pattern above
2. Remember: new column names need quotes

Type the fixed version: `'names_to = "year"'`

**Expected Output:**
`'names_to = "year"'`

## ⚠️ Common Mistake

**Wrong:**
```r
values_to = cases
```

**Fixed:**
```r
values_to = "cases"
```

---

✅ **No Hidden Prerequisites**: String quoting practice.
"""
fixes_made.append("20403: Added Common Mistake")

lessons["20404"]["content"] = """# 🦸 Challenge: Pivot It

## What You'll Learn
Apply `pivot_longer()` to convert wide data to tidy format.

## Why This Matters
Real datasets often come in wide format. Pivoting is a core skill you'll use constantly.

## Example

Here's the pattern:

```r
data %>%
  pivot_longer(
    cols = c(col1, col2),
    names_to = "name_column",
    values_to = "value_column"
  )
```

## 🎯 Your Task

Given `table4a` with columns for years:
1. Pivot columns `1999` and `2000` (use backticks: `` `1999` ``)
2. Name the new columns `"year"` and `"cases"`

**Expected Output:**
A tidy table with country, year, and cases columns

## ⚠️ Common Mistake

**Wrong:**
```r
cols = c(1999, 2000)
```
Numbers need backticks.

**Fixed:**
```r
cols = c(`1999`, `2000`)
```

---

✅ **No Hidden Prerequisites**: Uses `pivot_longer()` from this lesson. Uses `table4a` dataset.
"""
lessons["20404"]["starter_code"] = "# Pivot table4a from wide to long\n# table4a %>% pivot_longer(...)"
fixes_made.append("20404: Added Example and Common Mistake, removed library()")

# Save updated lessons
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("=" * 80)
print("COMPLIANCE PATCH COMPLETE")
print("=" * 80)
print(f"\nFixes made: {len(fixes_made)}")
for fix in fixes_made:
    print(f"  - {fix}")
