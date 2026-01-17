"""
Batch R-1 Reinforcer Rewrite Script - Concepts 2030, 2050, 2500, 2010
Priority 5-8: Hidden prereqs / Missing scaffolding
"""

import json

# Load lessons
with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

# ============================================
# CONCEPT 2030: Names & Spaces
# Teaches: snake_case naming, spacing around operators
# Issues: R2 uses pipes (hidden prereq), all very thin
# ============================================

lessons["20301"] = {
    **lessons["20301"],
    "title": "Analogy: Grammar for Code",
    "content": """# 📖 Grammar for Code

## What You'll Learn
Code style is like grammar—helps others (and future you) read your work.

## Why This Matters
Just as "you can manage withoutpunctuationbutitsurehappenseasiertoread", code without spaces is hard to read. Good style = fewer bugs + happier collaborators.

## Example

```r
# ❌ Hard to read
x<-10+y*2

# ✅ Easy to read
x <- 10 + y * 2
```

Spaces around `<-`, `+`, `*` make the code breathe.

## 🎯 Your Task

1. Look at the starter code below
2. Add spaces around `<-` and `+`
3. Run to verify it works

**Expected Output:**
`20`

## ⚠️ Common Mistake

**Wrong:**
```r
x< -10  # Space inside the arrow breaks it!
```

**Fixed:**
```r
x <- 10  # Space on both sides of arrow
```

---

✅ **No Hidden Prerequisites**: Uses only basic assignment from earlier lessons.
""",
    "starter_code": "# Add spaces around operators\nx<-10+10\nprint(x)",
    "solution_code": "x <- 10 + 10\nprint(x)",
    "expected_output": "[1] 20"
}

lessons["20302"] = {
    **lessons["20302"],
    "title": "Variation: snake_case Naming",
    "content": """# 🐍 snake_case Naming

## What You'll Learn
R uses `snake_case` (lowercase with underscores) for variable names.

## Why This Matters
Consistent naming helps everyone read code. When you see `flight_data`, you know it's a variable. When you see `FlightData`, that's usually a class in other languages—confusing in R!

## Example

```r
# ✅ Good (snake_case)
short_flights <- filter(flights, air_time < 60)

# ❌ Bad (camelCase, PascalCase)
shortFlights <- filter(flights, air_time < 60)
ShortFlights <- filter(flights, air_time < 60)
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

✅ **No Hidden Prerequisites**: Uses only variable assignment.
""",
    "starter_code": "# Rename using snake_case\nMyData <- penguins\nMyData",
    "solution_code": "my_data <- penguins\nmy_data",
    "expected_output": "# A tibble: 344 × 8"
}

lessons["20303"] = {
    **lessons["20303"],
    "title": "Fix the Code: Spacing Issues",
    "content": """# 🔧 Fix the Spacing

## What You'll Learn
Spot and fix common spacing mistakes in R code.

## Why This Matters
Bad spacing makes code hard to read and maintain. Most R style guides require spaces around operators.

## Example

The code below has multiple spacing issues:

```r
# Bad
mean(x,na.rm=TRUE)

# Good
mean(x, na.rm = TRUE)
```

Note: space AFTER comma, space around `=`.

## 🎯 Your Task

1. Look at the starter code—all the spaces are missing
2. Add a space after each comma
3. Add spaces around `=`
4. Run to verify it works

**Expected Output:**
Mean body mass value (around 4200)

## ⚠️ Common Mistake

**Wrong:**
```r
mean( x )  # Don't put space inside parentheses
```

**Fixed:**
```r
mean(x)  # No space inside, space after commas
```

---

✅ **No Hidden Prerequisites**: Uses `mean()` and basic R syntax.
""",
    "starter_code": "# Fix the spacing\nmean(penguins$body_mass_g,na.rm=TRUE)",
    "solution_code": "mean(penguins$body_mass_g, na.rm = TRUE)",
    "expected_output": "[1] 4201.754"
}

lessons["20304"] = {
    **lessons["20304"],
    "title": "Challenge: Clean Up This Code",
    "content": """# 🦸 Challenge: Clean Up This Code

## What You'll Learn
Apply all style rules: snake_case names + proper spacing.

## Why This Matters
In real projects, you'll often need to clean up messy code. This is practice for that.

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
my_result<- 10+15  # Missing spaces
```

**Fixed:**
```r
my_result <- 10 + 15  # Spaces around operators
```

---

✅ **No Hidden Prerequisites**: Uses only variable assignment.
""",
    "starter_code": "# Clean up this messy code\nMyResult<-10+15\nprint(MyResult)",
    "solution_code": "my_result <- 10 + 15\nprint(my_result)",
    "expected_output": "[1] 25"
}

# ============================================
# CONCEPT 2050: Scripts vs Console
# Teaches: Scripts save work, console is ephemeral
# Issues: R2 off-topic (ggplot), R4 no scaffold
# ============================================

lessons["20501"] = {
    **lessons["20501"],
    "title": "Analogy: The Recipe Card",
    "content": """# 📜 The Recipe Card

## What You'll Learn
Scripts are like recipe cards—saved, reproducible, shareable.

## Why This Matters
The console is like cooking from memory: quick but forgettable. A script (`.R` file) is like a recipe card: you can use it tomorrow, next year, or share it with a friend.

## Example

```
CONSOLE (ephemeral)       SCRIPT (.R file)
─────────────────         ─────────────────
❌ Lost on restart        ✅ Saved to disk
❌ Can't share            ✅ Share via email/git
❌ No history             ✅ Edit and rerun
```

## 🎯 Your Task

Imagine you're writing a script. Type these two lines:
1. `# My first script` (a comment describing your script)
2. `1 + 1` (some R code)

In a real script, this would be saved forever!

**Expected Output:**
`[1] 2`

## ⚠️ Common Mistake

Forgetting to save your script! Use `Cmd/Ctrl + S` frequently.

---

✅ **No Hidden Prerequisites**: Uses only basic R and comments.
""",
    "starter_code": "# Write a simple script with a comment and calculation\n",
    "solution_code": "# My first script\n1 + 1",
    "expected_output": "[1] 2"
}

lessons["20502"] = {
    **lessons["20502"],
    "title": "Variation: Running Line by Line",
    "content": """# ▶️ Running Line by Line

## What You'll Learn
You can run scripts line by line or all at once.

## Why This Matters
Running line by line helps you debug. Running all at once executes your full analysis. Both are essential skills.

## Example

```r
# Line 1: Create data
x <- 10

# Line 2: Calculate
x * 2

# Line 3: Print result
print("Done!")
```

- `Cmd/Ctrl + Enter`: Run current line
- `Cmd/Ctrl + Shift + S`: Run entire script

## 🎯 Your Task

1. Run the starter code line by line (each line does something different)
2. See how each step builds on the previous

**Expected Output:**
After running all lines: `[1] "Done!"`

## ⚠️ Common Mistake

Trying to use a variable before creating it. Run lines in order!

---

✅ **No Hidden Prerequisites**: Uses only basic R operations.
""",
    "starter_code": "# Run these lines one at a time\nx <- 5\ny <- x * 2\nprint(y)\nprint(\"Done!\")",
    "solution_code": "x <- 5\ny <- x * 2\nprint(y)\nprint(\"Done!\")",
    "expected_output": '[1] 10\n[1] "Done!"'
}

lessons["20503"] = {
    **lessons["20503"],
    "title": "Fix the Code: Typo in Function",
    "content": """# 🔧 Fix the Typo

## What You'll Learn
Function names must be spelled exactly right—`library` not `libary`.

## Why This Matters
Typos in function names cause "could not find function" errors. Learning to spot these now saves debugging time later.

## Example

```r
# ❌ Error: could not find function "libary"
libary(tidyverse)

# ✅ Works
library(tidyverse)
```

## 🎯 Your Task

1. Find the typo in the starter code
2. Fix `libary` → `library`
3. (Note: running this may not work in the browser, but fixing the typo is the goal)

**Expected Output:**
No error (or library loading message)

## ⚠️ Common Mistake

**Wrong:**
```r
Library(tidyverse)  # Capital L doesn't work
```

**Fixed:**
```r
library(tidyverse)  # All lowercase
```

---

✅ **No Hidden Prerequisites**: Uses only `library()` function.
""",
    "starter_code": "# Fix the typo in the function name\nlibary(tidyverse)",
    "solution_code": "library(tidyverse)",
    "expected_output": "# Loading tidyverse"
}

lessons["20504"] = {
    **lessons["20504"],
    "title": "Challenge: Script Header",
    "content": """# 🦸 Challenge: Script Header

## What You'll Learn
Best practice: Start scripts with a header comment describing what they do.

## Why This Matters
When you open a script 6 months from now, you'll forget what it does. A header comment saves you time.

## 🎯 Your Task

Write a proper script header with:
1. A title comment: `# Penguin Analysis`
2. An author comment: `# Author: [Your Name]`
3. A date comment: `# Date: 2024-01-18`
4. Then run `penguins` to view the data

**Expected Output:**
The penguins tibble (344 × 8)

## ⚠️ Common Mistake

Forgetting the `#` symbol—R will try to run "Penguin Analysis" as code!

---

✅ **No Hidden Prerequisites**: Uses only comments and `penguins`.
""",
    "starter_code": "# Write your script header below\n# Title:\n# Author:\n# Date:\n\n# Then view the data\n",
    "solution_code": "# Penguin Analysis\n# Author: Me\n# Date: 2024-01-18\n\npenguins",
    "expected_output": "# A tibble: 344 × 8"
}

# ============================================
# CONCEPT 2500: Quarto Basics
# Teaches: .qmd files, YAML, code chunks
# Issues: All reinforcers extremely thin
# ============================================

lessons["25001"] = {
    **lessons["25001"],
    "title": "Analogy: The Lab Notebook",
    "content": """# 📓 The Lab Notebook

## What You'll Learn
Quarto files (`.qmd`) combine code AND notes—like a scientist's lab notebook.

## Why This Matters
Scientists don't just record results—they write WHY they did each experiment. Quarto lets you explain your analysis alongside the code that runs it. When you share the file, others understand your thinking.

## Example

A Quarto file has three parts:
```
---                    ← YAML header (settings)
title: "My Report"
---

This is markdown text.  ← Prose (explanations)

```{r}
1 + 1                  ← Code chunks (R code)
```
```

## 🎯 Your Task

You can't run Quarto in this browser, but understand the concept:

1. YAML at the top (between `---`)
2. Markdown text (explanations)
3. Code chunks (calculations)

Type `"I understand Quarto structure"` and run.

**Expected Output:**
`"I understand Quarto structure"`

---

✅ **No Hidden Prerequisites**: Conceptual overview only.
""",
    "starter_code": "# Confirm you understand the 3 parts of Quarto\n",
    "solution_code": '"I understand Quarto structure"',
    "expected_output": '[1] "I understand Quarto structure"'
}

lessons["25002"] = {
    **lessons["25002"],
    "title": "Variation: Code Chunk Options",
    "content": """# ⚙️ Code Chunk Options

## What You'll Learn
Options like `echo: false` control what appears in your final report.

## Why This Matters
Sometimes you want to show results but hide messy code. Or run setup code without cluttering your report. Chunk options give you that control.

## Example

```
```{r}
#| echo: false       ← Hides the code, shows output
mean(penguins$body_mass_g, na.rm = TRUE)
```
```

Common options:
- `echo: false` → Hide code
- `eval: false` → Don't run code
- `include: false` → Hide everything

## 🎯 Your Task

In Quarto, you'd write `#| echo: false` to hide code. Here, just:
1. Calculate the mean of bill_length in penguins
2. Imagine the code would be hidden in a report

**Expected Output:**
Mean bill length (around 43.9)

---

✅ **No Hidden Prerequisites**: Uses only `mean()` and `penguins`.
""",
    "starter_code": "# Calculate mean bill length\nmean(penguins$bill_length_mm, na.rm = TRUE)",
    "solution_code": "mean(penguins$bill_length_mm, na.rm = TRUE)",
    "expected_output": "[1] 43.92193"
}

lessons["25003"] = {
    **lessons["25003"],
    "title": "Fix the Code: Chunk Syntax",
    "content": """# 🔧 Fix the Chunk Syntax

## What You'll Learn
Code chunks need proper backtick syntax: three backticks + `{r}`.

## Why This Matters
Quarto won't run your code if the chunk delimiters are wrong. This is the most common Quarto syntax error.

## Example

```
❌ Wrong (missing backticks or braces)
``{r}
1 + 1
``

✅ Correct
```{r}
1 + 1
```
```

## 🎯 Your Task

This exercise tests your understanding. Type the correct number of backticks needed:
- Chunk opening: type `3`
- Chunk closing: type `3`

**Expected Output:**
`[1] 3` then `[1] 3`

---

✅ **No Hidden Prerequisites**: Conceptual only.
""",
    "starter_code": "# How many backticks for chunk opening?\n3\n# How many for closing?\n3",
    "solution_code": "3\n3",
    "expected_output": "[1] 3\n[1] 3"
}

lessons["25004"] = {
    **lessons["25004"],
    "title": "Challenge: YAML Header",
    "content": """# 🦸 Challenge: YAML Header

## What You'll Learn
Write a basic YAML header for a Quarto document.

## Why This Matters
The YAML header controls your document's title, format, and settings. Getting it right is step one of every Quarto project.

## Example

```yaml
---
title: "My Report"
format: html
---
```

## 🎯 Your Task

Create a string that looks like a YAML title line:
1. Type: `"title: Penguin Analysis"`
2. Run to see it printed

In a real `.qmd` file, this would go between the `---` delimiters.

**Expected Output:**
`[1] "title: Penguin Analysis"`

---

✅ **No Hidden Prerequisites**: Conceptual + string practice.
""",
    "starter_code": "# Write a YAML title line as a string\n",
    "solution_code": '"title: Penguin Analysis"',
    "expected_output": '[1] "title: Penguin Analysis"'
}

# ============================================
# CONCEPT 2010: Coding Basics
# Teaches: R as calculator, assignment, vectors
# Issues: Reinforcers only test function calls
# ============================================

lessons["20101"] = {
    **lessons["20101"],
    "title": "Analogy: The Calculator",
    "content": """# 🧮 R is a Fancy Calculator

## What You'll Learn
At its core, R is just a calculator that follows math rules.

## Why This Matters
Before fancy statistics, R does basic math. Understanding PEMDAS (order of operations) helps you avoid bugs when calculations get complex.

## Example

```r
1 + 2 * 3        # → 7 (not 9! multiplication first)
(1 + 2) * 3      # → 9 (parentheses change order)
5 / 2            # → 2.5
5 %/% 2          # → 2 (integer division)
5 %% 2           # → 1 (remainder/modulo)
```

## 🎯 Your Task

1. Calculate `2 + 3 * 4` (what order does R use?)
2. Then calculate `(2 + 3) * 4` (force addition first)
3. Compare the results

**Expected Output:**
First: `14`, Second: `20`

## ⚠️ Common Mistake

Assuming left-to-right order. R follows PEMDAS!

---

✅ **No Hidden Prerequisites**: Uses only arithmetic operators.
""",
    "starter_code": "# Compare these two calculations\n2 + 3 * 4\n(2 + 3) * 4",
    "solution_code": "2 + 3 * 4\n(2 + 3) * 4",
    "expected_output": "[1] 14\n[1] 20"
}

lessons["20102"] = {
    **lessons["20102"],
    "title": "Variation: Saving Results",
    "content": """# 💾 Saving Results

## What You'll Learn
Use `<-` to save a calculation for later use.

## Why This Matters
Without saving results, you'd have to recalculate everything repeatedly. Variables store values so you can use them later—like writing down an answer.

## Example

```r
# Calculate and save
total <- 10 + 20

# Use the saved value
total * 2        # → 60
total + 5        # → 35
```

## 🎯 Your Task

1. Create a variable `my_sum` that stores `50 + 50`
2. Then calculate `my_sum * 2`
3. Run both lines

**Expected Output:**
`[1] 200`

## ⚠️ Common Mistake

**Wrong:**
```r
my_sum = 100
my_sum <- 100  # Both work but <- is preferred
```

Use `<-` for assignment in R (not `=`).

---

✅ **No Hidden Prerequisites**: Uses only assignment and arithmetic.
""",
    "starter_code": "# Save a calculation, then use it\nmy_sum <- 50 + 50\nmy_sum * 2",
    "solution_code": "my_sum <- 50 + 50\nmy_sum * 2",
    "expected_output": "[1] 200"
}

lessons["20103"] = {
    **lessons["20103"],
    "title": "Fix the Code: Broken Assignment",
    "content": """# 🔧 Fix the Assignment

## What You'll Learn
The assignment arrow `<-` must be typed correctly, with no spaces inside.

## Why This Matters
`x < - 5` (less than negative five) is NOT the same as `x <- 5` (assign five to x). This subtle error causes confusing bugs.

## Example

```r
# ❌ This compares x to -5 (wrong!)
x < - 5

# ✅ This assigns 5 to x
x <- 5
```

## 🎯 Your Task

1. Look at the starter code—there's a space breaking the arrow
2. Remove the space between `<` and `-`
3. Run to verify x equals 10

**Expected Output:**
`[1] 10`

## ⚠️ Common Mistake

Typing `<-` too quickly and getting `< -` (comparison to negative).

---

✅ **No Hidden Prerequisites**: Uses only assignment.
""",
    "starter_code": "# Fix the broken assignment arrow\nx < - 10\nprint(x)",
    "solution_code": "x <- 10\nprint(x)",
    "expected_output": "[1] 10"
}

lessons["20104"] = {
    **lessons["20104"],
    "title": "Challenge: Vector Math",
    "content": """# 🦸 Challenge: Vector Math

## What You'll Learn
Vectors store multiple values; math applies to ALL elements.

## Why This Matters
Data science = working with many values at once. Instead of adding 100 separately, vectors let you add all 100 with one operation.

## Example

```r
nums <- c(1, 2, 3)
nums * 10          # → 10, 20, 30 (all multiplied)
nums + 5           # → 6, 7, 8 (all added)
```

## 🎯 Your Task

1. Create a vector `prices <- c(10, 20, 30)`
2. Apply a 20% discount: `prices * 0.8`
3. Run to see the discounted prices

**Expected Output:**
`[1]  8 16 24`

## ⚠️ Common Mistake

**Wrong:**
```r
prices <- 10, 20, 30  # Missing c()
```

**Fixed:**
```r
prices <- c(10, 20, 30)  # Use c() to create vectors
```

---

✅ **No Hidden Prerequisites**: Uses only `c()` and arithmetic.
""",
    "starter_code": "# Create prices and apply 20% discount\nprices <- c(10, 20, 30)\nprices * 0.8",
    "solution_code": "prices <- c(10, 20, 30)\nprices * 0.8",
    "expected_output": "[1]  8 16 24"
}

# Save updated lessons
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("✅ Updated concepts 2030, 2050, 2500, 2010 reinforcers (16 lessons)")
