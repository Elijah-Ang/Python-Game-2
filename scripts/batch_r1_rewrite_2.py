"""
Batch R-1 Reinforcer Rewrite Script - Concepts 2003, 2001, 2201
Updates lessons.json with properly aligned reinforcers.
"""

import json

# Load lessons
with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

# ============================================
# CONCEPT 2003: Mapping Data to Axes
# Teaches: mapping = aes(x = COLUMN, y = COLUMN)
# Current reinforcers teach data frames (WRONG)
# ============================================

lessons["20031"] = {
    **lessons["20031"],
    "title": "Analogy: The Coordinate System",
    "content": """# 📍 The Coordinate System

## What You'll Learn
How `aes(x = ..., y = ...)` maps data columns to the x and y axes—like plotting points on a map.

## Why This Matters
Think of a graph like a treasure map. The x-axis is "how far east" and y-axis is "how far north." When you write `aes(x = flipper_length_mm, y = body_mass_g)`, you're telling R: "Put flipper length on the x-axis and body mass on the y-axis."

## Example

```r
ggplot(
  data = penguins,
  mapping = aes(x = flipper_length_mm, y = body_mass_g)
)
```

This creates labeled axes—but no dots yet!

## 🎯 Your Task

1. Use `ggplot(data = penguins, mapping = aes(x = flipper_length_mm, y = body_mass_g))`
2. Run the code
3. Observe: axes are labeled but canvas is empty (no geom yet)

**Expected Output:**
Gray canvas with labeled x and y axes

## ⚠️ Common Mistake

**Wrong:**
```r
aes(x = "flipper_length_mm")  # Don't use quotes!
```

**Fixed:**
```r
aes(x = flipper_length_mm)  # Column names without quotes
```

---

✅ **No Hidden Prerequisites**: Uses only `ggplot()`, `aes()`, and `penguins` from this lesson.
""",
    "starter_code": "# Map flipper_length_mm to x and body_mass_g to y\n",
    "solution_code": "ggplot(data = penguins, mapping = aes(x = flipper_length_mm, y = body_mass_g))",
    "expected_output": "[Graph: Canvas with labeled axes]"
}

lessons["20032"] = {
    **lessons["20032"],
    "title": "Variation: Different Columns",
    "content": """# 🔄 Different Columns

## What You'll Learn
You can map ANY numeric columns to x and y—not just flipper_length_mm and body_mass_g.

## Why This Matters
The power of `aes()` is flexibility. The penguins dataset has many columns (bill_length_mm, bill_depth_mm, etc.). By changing what goes in `aes()`, you can explore different relationships.

## Example

```r
# Original: flipper vs body mass
aes(x = flipper_length_mm, y = body_mass_g)

# New: bill length vs bill depth
aes(x = bill_length_mm, y = bill_depth_mm)
```

## 🎯 Your Task

1. Create a ggplot with `penguins` data
2. Map `x = bill_length_mm` and `y = bill_depth_mm`
3. Run and verify axes show bill measurements

**Expected Output:**
Canvas with "bill_length_mm" on x-axis and "bill_depth_mm" on y-axis

## ⚠️ Common Mistake

**Wrong:**
```r
aes(x = bill_length, y = bill_depth)  # Missing _mm suffix
```

**Fixed:**
```r
aes(x = bill_length_mm, y = bill_depth_mm)
```

---

✅ **No Hidden Prerequisites**: Uses only `ggplot()`, `aes()`, and `penguins` columns.
""",
    "starter_code": "# Map bill_length_mm to x and bill_depth_mm to y\nggplot(data = penguins, mapping = aes(x = ___, y = ___))",
    "solution_code": "ggplot(data = penguins, mapping = aes(x = bill_length_mm, y = bill_depth_mm))",
    "expected_output": "[Graph: Canvas with bill measurement axes]"
}

lessons["20033"] = {
    **lessons["20033"],
    "title": "Fix the Code: Mapping Typo",
    "content": """# 🔧 Fix the Code

## What You'll Learn
How to spot common typos in `aes()` mappings.

## Why This Matters
R is case-sensitive and picky about spelling. A typo like `body_Mass_g` instead of `body_mass_g` will break your code with a confusing error.

## Example

Spot the error below:

```r
ggplot(data = penguins, mapping = aes(x = flipper_length_mm, y = Body_mass_g))
```

R is looking for `body_mass_g` (lowercase), not `Body_mass_g`.

## 🎯 Your Task

1. Look at the starter code
2. Find and fix the capitalization error in the y mapping
3. Run to confirm axes appear correctly

**Expected Output:**
Canvas with properly labeled axes

## ⚠️ Common Mistake

**Wrong:**
```r
y = body_mass_G  # Wrong case on 'g'
```

**Fixed:**
```r
y = body_mass_g  # All lowercase except after underscores
```

---

✅ **No Hidden Prerequisites**: Uses only `ggplot()`, `aes()`, and `penguins`.
""",
    "starter_code": "# Fix the capitalization error\nggplot(data = penguins, mapping = aes(x = flipper_length_mm, y = Body_mass_g))",
    "solution_code": "ggplot(data = penguins, mapping = aes(x = flipper_length_mm, y = body_mass_g))",
    "expected_output": "[Graph: Canvas with labeled axes]"
}

lessons["20034"] = {
    **lessons["20034"],
    "title": "Challenge: Map Your Own Axes",
    "content": """# 🦸 Challenge: Map Your Own Axes

## What You'll Learn
Write a complete ggplot call with axis mappings from memory.

## Why This Matters
Building muscle memory for the `ggplot(data = ..., mapping = aes(...))` pattern is essential. You'll use this hundreds of times!

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
ggplot(mpg, aes(displ, hwy))  # Too abbreviated
```

**Better:**
```r
ggplot(data = mpg, mapping = aes(x = displ, y = hwy))  # Explicit is clearer
```

---

✅ **No Hidden Prerequisites**: Uses `ggplot()` and `aes()` from this lesson; `mpg` is a built-in dataset.
""",
    "starter_code": "# Create a ggplot with mpg data, mapping displ to x and hwy to y\n",
    "solution_code": "ggplot(data = mpg, mapping = aes(x = displ, y = hwy))",
    "expected_output": "[Graph: Canvas with displ and hwy axes]"
}

# ============================================
# CONCEPT 2001: Meet the Penguins  
# Teaches: Intro to visualization, penguins dataset
# Current reinforcers teach variables (WRONG)
# ============================================

lessons["20011"] = {
    **lessons["20011"],
    "title": "Analogy: A Picture is Worth 344 Rows",
    "content": """# 📊 A Picture is Worth 344 Rows

## What You'll Learn
Why visualization is faster and more insightful than reading tables of numbers.

## Why This Matters
Imagine reading 344 rows of penguin measurements. Boring! Confusing! But a scatterplot shows the pattern instantly: longer flippers = heavier penguins. That's the power of visualization.

## Example

```r
# Just looking at the data shows rows and columns
penguins
```

You see 344 rows × 8 columns. But what does it *mean*? A graph shows the story.

## 🎯 Your Task

1. Type `penguins` and press Run
2. Notice: 344 rows of numbers—hard to see patterns!
3. Look for the columns `flipper_length_mm` and `body_mass_g`—we'll graph these next

**Expected Output:**
A tibble showing 344 rows and 8 columns of penguin data

## ⚠️ Common Mistake

**Wrong:**
```r
Penguins  # Capital P doesn't exist
```

**Fixed:**
```r
penguins  # All lowercase
```

---

✅ **No Hidden Prerequisites**: Uses only the `penguins` dataset introduced in this lesson.
""",
    "starter_code": "# View the penguins dataset\n",
    "solution_code": "penguins",
    "expected_output": "# A tibble: 344 × 8"
}

lessons["20012"] = {
    **lessons["20012"],
    "title": "Variation: Explore the Columns",
    "content": """# 🔍 Explore the Columns

## What You'll Learn
How to find out what columns are in a dataset using `names()`.

## Why This Matters
Before you can graph data, you need to know what columns exist. `names(penguins)` shows you all 8 column names—so you know what's available to map to x and y.

## Example

```r
names(penguins)
```

Returns: `"species"`, `"island"`, `"bill_length_mm"`, etc.

## 🎯 Your Task

1. Type `names(penguins)` and run it
2. Find the column for flipper length (hint: contains "flipper")
3. Find the column for body mass (hint: contains "mass")

**Expected Output:**
A character vector of 8 column names

## ⚠️ Common Mistake

**Wrong:**
```r
columns(penguins)  # There's no 'columns' function
```

**Fixed:**
```r
names(penguins)  # Use 'names' to see column names
```

---

✅ **No Hidden Prerequisites**: Uses only `names()` (base R) and `penguins`.
""",
    "starter_code": "# Get the column names of the penguins dataset\n",
    "solution_code": "names(penguins)",
    "expected_output": '[1] "species" "island" "bill_length_mm" "bill_depth_mm" "flipper_length_mm" "body_mass_g" "sex" "year"'
}

lessons["20013"] = {
    **lessons["20013"],
    "title": "Fix the Code: Dataset Name",
    "content": """# 🔧 Fix the Code

## What You'll Learn
R is case-sensitive—`penguins` works, but `Penguins` or `PENGUINS` don't.

## Why This Matters
This is the #1 beginner error in R! Getting comfortable with exact spelling and case now will save you hours of debugging later.

## Example

```r
# Error: object 'Penguins' not found
Penguins
```

## 🎯 Your Task

1. Look at the starter code—it has a capitalization error
2. Fix the case to all lowercase
3. Run and verify you see the dataset

**Expected Output:**
The penguins tibble (344 rows × 8 columns)

## ⚠️ Common Mistake

**Wrong:**
```r
PENGUINS  # All caps doesn't work
penGUins  # Random caps doesn't work
```

**Fixed:**
```r
penguins  # Exactly as defined
```

---

✅ **No Hidden Prerequisites**: Uses only the `penguins` dataset.
""",
    "starter_code": "# Fix the capitalization error\nPenguins",
    "solution_code": "penguins",
    "expected_output": "# A tibble: 344 × 8"
}

lessons["20014"] = {
    **lessons["20014"],
    "title": "Challenge: Find the Range",
    "content": """# 🦸 Challenge: Find the Range

## What You'll Learn
Use `range()` to find the min and max of a column.

## Why This Matters
Before graphing, it helps to know the range of your data. `range(penguins$flipper_length_mm, na.rm = TRUE)` tells you the smallest and largest flipper measurements—so you know what to expect on your axes.

## 🎯 Your Task

1. Find the range of `body_mass_g` in the penguins dataset
2. Use: `range(penguins$body_mass_g, na.rm = TRUE)`
3. What are the lightest and heaviest penguins?

**Expected Output:**
Two numbers: the minimum and maximum body mass

## ⚠️ Common Mistake

**Wrong:**
```r
range(body_mass_g)  # Error: object 'body_mass_g' not found
```

**Fixed:**
```r
range(penguins$body_mass_g, na.rm = TRUE)  # Specify dataset$column
```

---

✅ **No Hidden Prerequisites**: Uses `range()` (base R), `$` (base R), and `penguins`.
""",
    "starter_code": "# Find the range of body_mass_g in penguins\n# Hint: range(dataset$column, na.rm = TRUE)\n",
    "solution_code": "range(penguins$body_mass_g, na.rm = TRUE)",
    "expected_output": "[1] 2700 6300"
}

# ============================================
# CONCEPT 2201: Conditional Logic
# Teaches: if_else() and case_when() for conditional transformations
# Current reinforcers teach &/| operators (WRONG)
# ============================================

lessons["22011"] = {
    **lessons["22011"],
    "title": "Analogy: The Sorting Hat",
    "content": """# 🎩 The Sorting Hat

## What You'll Learn
How `if_else()` assigns one of two values based on a condition—like the Sorting Hat choosing between houses.

## Why This Matters
Data often needs labels. Is a flight "Late" or "On time"? Is a penguin "Heavy" or "Light"? `if_else()` looks at each row and assigns the right label—just like the Sorting Hat reads each student and assigns a house.

## Example

```r
flights %>% mutate(
  status = if_else(arr_delay > 0, "Late", "On time")
)
```

If delay > 0 → "Late". Otherwise → "On time".

## 🎯 Your Task

1. Look at the pattern: `if_else(condition, true_result, false_result)`
2. Create a column `size` that labels penguins as "Heavy" if `body_mass_g > 4000`, else "Light"
3. Use: `penguins %>% mutate(size = if_else(body_mass_g > 4000, "Heavy", "Light"))`

**Expected Output:**
Penguins tibble with a new `size` column

## ⚠️ Common Mistake

**Wrong:**
```r
if_else(body_mass_g > 4000, Heavy, Light)  # Missing quotes
```

**Fixed:**
```r
if_else(body_mass_g > 4000, "Heavy", "Light")  # Text needs quotes
```

---

✅ **No Hidden Prerequisites**: Uses `mutate()` (taught in Ch 3) and `if_else()` from this lesson.
""",
    "starter_code": '# Label penguins as "Heavy" (> 4000g) or "Light"\npenguins %>% mutate(\n  size = if_else(____)\n)',
    "solution_code": 'penguins %>% mutate(size = if_else(body_mass_g > 4000, "Heavy", "Light"))',
    "expected_output": "# A tibble with new 'size' column"
}

lessons["22012"] = {
    **lessons["22012"],
    "title": "Variation: Three or More Categories",
    "content": """# 🎯 Three or More Categories

## What You'll Learn
`case_when()` handles 3+ outcomes—when `if_else()` isn't enough.

## Why This Matters
Sometimes you need more than two categories. Flights can be "Early", "On time", "Late", or "Very late". `case_when()` checks conditions in order and assigns the first match.

## Example

```r
flights %>% mutate(
  status = case_when(
    arr_delay < -15     ~ "Early",
    abs(arr_delay) <= 15 ~ "On time",
    arr_delay < 60      ~ "Late",
    .default = "Very late"
  )
)
```

## 🎯 Your Task

1. Create categories for penguin size: "Small" (< 3500g), "Medium" (3500-4500g), "Large" (> 4500g)
2. Use `case_when()` inside `mutate()`

**Expected Output:**
Penguins with a `size_category` column

## ⚠️ Common Mistake

**Wrong:**
```r
case_when(
  x < 10 = "small"  # Wrong: use ~ not =
)
```

**Fixed:**
```r
case_when(
  x < 10 ~ "small"  # Use tilde ~
)
```

---

✅ **No Hidden Prerequisites**: Uses `mutate()` (Ch 3) and `case_when()` from this lesson.
""",
    "starter_code": '# Create size categories: Small, Medium, Large\npenguins %>% mutate(\n  size_category = case_when(\n    body_mass_g < 3500 ~ "Small",\n    body_mass_g <= 4500 ~ "Medium",\n    .default = "Large"\n  )\n)',
    "solution_code": 'penguins %>% mutate(size_category = case_when(body_mass_g < 3500 ~ "Small", body_mass_g <= 4500 ~ "Medium", .default = "Large"))',
    "expected_output": "# A tibble with 'size_category' column"
}

lessons["22013"] = {
    **lessons["22013"],
    "title": "Fix the Code: Syntax Errors",
    "content": """# 🔧 Fix the Code

## What You'll Learn
Spot common syntax errors in `if_else()` and `case_when()`.

## Why This Matters
The tilde `~` and the argument order in `if_else()` trip up beginners. Learning to read error messages now builds debugging skills.

## Example

The code below has an error. Can you find it?

```r
if_else(arr_delay > 0, "Late")  # Missing the FALSE value!
```

`if_else()` REQUIRES three arguments: condition, true, false.

## 🎯 Your Task

1. Look at the starter code
2. The `if_else()` is missing its third argument
3. Add "On time" as the false value

**Expected Output:**
Penguins tibble with `delay_status` column

## ⚠️ Common Mistake

**Wrong:**
```r
if_else(x > 0, "yes")  # Missing FALSE value
```

**Fixed:**
```r
if_else(x > 0, "yes", "no")  # All three required
```

---

✅ **No Hidden Prerequisites**: Uses `mutate()` and `if_else()`.
""",
    "starter_code": '# Fix the missing argument\npenguins %>% mutate(\n  heavy = if_else(body_mass_g > 4000, "Heavy")\n)',
    "solution_code": 'penguins %>% mutate(heavy = if_else(body_mass_g > 4000, "Heavy", "Light"))',
    "expected_output": "# A tibble with 'heavy' column"
}

lessons["22014"] = {
    **lessons["22014"],
    "title": "Challenge: Classify Flipper Length",
    "content": """# 🦸 Challenge: Classify Flipper Length

## What You'll Learn
Apply conditional logic independently to create meaningful categories.

## Why This Matters
Real data analysis constantly requires creating categories. This challenge tests your ability to use `if_else()` or `case_when()` without hand-holding.

## 🎯 Your Task

Create a new column `flipper_size` in penguins:
- If `flipper_length_mm >= 200`, label as "Long"
- Otherwise, label as "Short"

1. Start with `penguins %>% mutate(...)`
2. Use either `if_else()` or `case_when()`
3. Your new column should be named `flipper_size`

**Expected Output:**
Penguins tibble with a new `flipper_size` column

## ⚠️ Common Mistake

**Wrong:**
```r
if_else(flipper_length_mm >= 200, Long, Short)  # No quotes
```

**Fixed:**
```r
if_else(flipper_length_mm >= 200, "Long", "Short")  # Strings need quotes
```

---

✅ **No Hidden Prerequisites**: Uses `mutate()`, `if_else()`, and `penguins`.
""",
    "starter_code": '# Create flipper_size column ("Long" if >= 200mm, else "Short")\npenguins %>% mutate(\n  flipper_size = ____\n)',
    "solution_code": 'penguins %>% mutate(flipper_size = if_else(flipper_length_mm >= 200, "Long", "Short"))',
    "expected_output": "# A tibble with 'flipper_size' column"
}

# Save updated lessons
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("✅ Updated concepts 2003, 2001, 2201 reinforcers (12 lessons)")
