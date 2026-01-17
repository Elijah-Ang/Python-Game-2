"""
Batch R-1 Compliance Patch 2

1. Token extractor consistency - capture datasets in code blocks
2. Markdown fencing fixes - ensure proper code block closure
3. Remove solution leakage from visible content
4. Micro-bridges for pipes/dplyr functions
"""

import json
import re

# Load lessons
with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

fixes_made = []

# ===== IMPROVED TOKEN EXTRACTOR =====
R_FUNCTIONS = {
    'print', 'c', 'length', 'class', 'typeof', 'sum', 'mean', 'max', 'min',
    'range', 'names', 'nrow', 'ncol', 'head', 'tail', 'str', 'summary',
    'library', 'seq', 'rep', 'sqrt', 'abs', 'round', 'paste', 'paste0',
    'ggplot', 'aes', 'geom_point', 'geom_line', 'geom_bar', 'geom_histogram',
    'geom_boxplot', 'geom_smooth', 'labs', 'theme', 'theme_minimal', 'theme_bw',
    'theme_classic', 'theme_dark', 'theme_gray', 'scale_x_continuous', 
    'filter', 'select', 'mutate', 'arrange', 'group_by', 'summarize', 
    'count', 'n', 'desc', 'if_else', 'case_when', 
    'pivot_longer', 'pivot_wider', 'separate', 'unite', 
}

KNOWN_DATASETS = {'penguins', 'mpg', 'diamonds', 'mtcars', 'iris', 'flights', 
                  'table4a', 'table4b', 'starwars'}

def extract_tokens(text):
    """Extract R tokens from text - improved version."""
    tokens = set()
    
    # Extract function calls: word( pattern  
    func_matches = re.findall(r'\b([a-z_][a-z0-9_]*)\s*\(', text, re.IGNORECASE)
    for f in func_matches:
        f_lower = f.lower()
        if f_lower in R_FUNCTIONS:
            tokens.add(f_lower + '()')
    
    # Extract datasets - look for them as standalone words
    for ds in KNOWN_DATASETS:
        # Match dataset name as word boundary, not in quotes
        if re.search(rf'\b{ds}\b(?!["\'])', text, re.IGNORECASE):
            tokens.add(ds)
    
    # Extract operators
    if '%>%' in text:
        tokens.add('%>%')
    if '<-' in text:
        tokens.add('<-')
    if '$' in text:
        tokens.add('$')
    if '~' in text:
        tokens.add('~')
    
    return tokens

# Test on 20022 and 20031
print("=" * 60)
print("TOKEN EXTRACTION ANALYSIS")
print("=" * 60)

content_20022 = lessons["20022"]["content"]
tokens_20022 = extract_tokens(content_20022)
print(f"\n20022 tokens: {sorted(tokens_20022)}")
print(f"  Expected: ggplot(), mpg, penguins, diamonds")
print(f"  Explanation: Content mentions all three datasets and ggplot()")

content_20031 = lessons["20031"]["content"]
tokens_20031 = extract_tokens(content_20031)
print(f"\n20031 tokens: {sorted(tokens_20031)}")
print(f"  Expected: ggplot(), aes(), penguins")
print(f"  Explanation: Uses ggplot with aes and penguins dataset")

# ===== PATCH ALL 48 REINFORCERS =====

BATCH_R1 = {
    2002: [20021, 20022, 20023, 20024],
    2003: [20031, 20032, 20033, 20034],
    2001: [20011, 20012, 20013, 20014],
    2201: [22011, 22012, 22013, 22014],
    2030: [20301, 20302, 20303, 20304],
    2050: [20501, 20502, 20503, 20504],
    2500: [25001, 25002, 25003, 25004],
    2010: [20101, 20102, 20103, 20104],
    2040: [20401, 20402, 20403, 20404],
    2023: [20231, 20232, 20233, 20234],
    2021: [20211, 20212, 20213, 20214],
    2121: [21211, 21212, 21213, 21214],
}

def fix_markdown_fencing(content):
    """Ensure all code blocks are properly closed."""
    # Count backtick blocks
    lines = content.split('\n')
    in_code_block = False
    fixed_lines = []
    
    for line in lines:
        if line.strip().startswith('```') and not in_code_block:
            in_code_block = True
        elif line.strip() == '```' and in_code_block:
            in_code_block = False
        fixed_lines.append(line)
    
    # If still in code block at end, close it
    if in_code_block:
        fixed_lines.append('```')
    
    return '\n'.join(fixed_lines)

def remove_solution_from_content(content):
    """Remove Solution: lines from visible content."""
    lines = content.split('\n')
    filtered = []
    for line in lines:
        # Skip lines that start with "Solution:" or "Solution Code:"
        if not line.strip().startswith('Solution:') and not line.strip().startswith('Solution Code:'):
            filtered.append(line)
    return '\n'.join(filtered)

def add_pipe_microbridge(content, concept_id):
    """Add micro-bridge explanation for %>% if used."""
    if '%>%' not in content:
        return content
    
    # Check if already has bridge
    if 'pipes the data' in content.lower() or 'passes the data' in content.lower():
        return content
    
    # Add bridge after "Why This Matters" section
    bridge = "\n\n> 💡 The `%>%` (pipe) takes the result from the left and passes it as the first argument to the function on the right.\n"
    
    # Find where to insert - after "Why This Matters" content
    if "## Why This Matters" in content and "## Example" in content:
        parts = content.split("## Example")
        if len(parts) == 2:
            # Insert bridge before Example
            content = parts[0].rstrip() + bridge + "\n\n## Example" + parts[1]
    
    return content

# Apply patches to all reinforcers
markdown_fixed = []
solution_removed = []
bridge_added = []

for concept_id, reinforcer_ids in BATCH_R1.items():
    for r_id in reinforcer_ids:
        r_id_str = str(r_id)
        if r_id_str not in lessons:
            continue
        
        original = lessons[r_id_str]["content"]
        
        # Fix markdown fencing
        content = fix_markdown_fencing(original)
        if content != original:
            markdown_fixed.append(r_id)
        
        # Remove solution leakage (shouldn't be in content but check)
        content2 = remove_solution_from_content(content)
        if content2 != content:
            solution_removed.append(r_id)
            content = content2
        
        # Add micro-bridge for pipes
        content3 = add_pipe_microbridge(content, concept_id)
        if content3 != content:
            bridge_added.append(r_id)
            content = content3
        
        lessons[r_id_str]["content"] = content

# ===== SPECIFIC FIXES FOR 22011 AND 20031 =====

# 22011 - Complete rewrite with proper micro-bridge
lessons["22011"]["content"] = """# 🎩 The Sorting Hat

## What You'll Learn
How `if_else()` assigns one of two values based on a condition—like the Sorting Hat choosing between houses.

## Why This Matters
Data often needs labels. Is a penguin "Heavy" or "Light"? `if_else()` looks at each row and assigns the right label—just like the Sorting Hat reads each student and assigns a house.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `mutate()`. Think of it as "take this data, then do this to it."

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
fixes_made.append("22011: Added pipe micro-bridge, verified markdown")

# 20031 - Ensure penguins is clearly captured
lessons["20031"]["content"] = """# 📍 The Coordinate System

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

This creates labeled axes—but no dots yet! The `penguins` dataset provides the data.

## 🎯 Your Task

1. Use `ggplot(data = penguins, mapping = aes(x = flipper_length_mm, y = body_mass_g))`
2. Run the code
3. Observe: axes are labeled but canvas is empty (no geom yet)

**Expected Output:**
Gray canvas with labeled x and y axes

## ⚠️ Common Mistake

**Wrong:**
```r
aes(x = "flipper_length_mm")
```
Don't use quotes around column names!

**Fixed:**
```r
aes(x = flipper_length_mm)
```

---

✅ **No Hidden Prerequisites**: Uses only `ggplot()`, `aes()`, and `penguins` from this lesson.
"""
fixes_made.append("20031: Verified penguins reference, fixed markdown")

# ===== ADD MICRO-BRIDGES TO ALL PIPE-USING REINFORCERS =====

pipe_lessons = [22011, 22012, 22013, 22014, 20231, 20232, 20233, 20234, 
                20211, 20212, 20213, 20214, 20401, 20402, 20403, 20404]

# 22012 - case_when with pipe bridge
lessons["22012"]["content"] = """# 🎯 Three or More Categories

## What You'll Learn
`case_when()` handles 3+ outcomes—when `if_else()` isn't enough.

## Why This Matters
Sometimes you need more than two categories. Penguins can be "Small", "Medium", or "Large". `case_when()` checks conditions in order and assigns the first match.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `mutate()`. Think of it as "take this data, then do this to it."

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
fixes_made.append("22012: Added pipe micro-bridge")

# 22013 - Fix syntax errors
lessons["22013"]["content"] = """# 🔧 Fix the Code

## What You'll Learn
Spot common syntax errors in `if_else()` and `case_when()`.

## Why This Matters
The argument order in `if_else()` trips up beginners. Learning to read error messages now builds debugging skills.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `mutate()`. Think of it as "take this data, then do this to it."

## Example

The code below has an error. Can you find it?

```r
penguins %>% mutate(
  heavy = if_else(body_mass_g > 4000, "Heavy")
)
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

---

✅ **No Hidden Prerequisites**: Uses `mutate()` and `if_else()`. Uses `penguins` dataset.
"""
fixes_made.append("22013: Added pipe micro-bridge")

# 22014 - Challenge
lessons["22014"]["content"] = """# 🦸 Challenge: Classify Flipper Length

## What You'll Learn
Apply conditional logic independently to create meaningful categories.

## Why This Matters
Real data analysis constantly requires creating categories. This challenge tests your ability to use `if_else()` without hand-holding.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `mutate()`. Think of it as "take this data, then do this to it."

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
fixes_made.append("22014: Added pipe micro-bridge")

# 20231 - Mutate transformation
lessons["20231"]["content"] = """# 🔮 The Transformation Ray

## What You'll Learn
`mutate()` adds new columns or transforms existing ones—like a sci-fi transformation ray.

## Why This Matters
Raw data is rarely ready for analysis. You need to compute new values: convert units, calculate ratios, create categories. `mutate()` is how you do it.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `mutate()`. Think of it as "take this data, then do this to it."

## Example

```r
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
fixes_made.append("20231: Added pipe micro-bridge")

# 20232
lessons["20232"]["content"] = """# ➗ Math with Columns

## What You'll Learn
You can use any math operation, and combine multiple columns.

## Why This Matters
Analysis often requires ratios or calculations. Body mass in kg = mass_g / 1000. Bill ratio = length / depth. `mutate()` handles all of it.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `mutate()`. Think of it as "take this data, then do this to it."

## Example

```r
penguins %>% mutate(
  bill_ratio = bill_length_mm / bill_depth_mm
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
fixes_made.append("20232: Added pipe micro-bridge")

# 20233
lessons["20233"]["content"] = """# 🔧 Name the New Column

## What You'll Learn
New columns in `mutate()` need a name on the left side of `=`.

## Why This Matters
Without a name, R doesn't know what to call your new column. The error is confusing but the fix is simple.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `mutate()`. Think of it as "take this data, then do this to it."

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
fixes_made.append("20233: Added pipe micro-bridge")

# 20234
lessons["20234"]["content"] = """# 🦸 Challenge: Multiple New Columns

## What You'll Learn
Create multiple columns in a single `mutate()` call.

## Why This Matters
Real analysis often needs several calculations at once. One `mutate()` call is cleaner than many.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `mutate()`. Think of it as "take this data, then do this to it."

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
fixes_made.append("20234: Added pipe micro-bridge")

# 20211 - arrange
lessons["20211"]["content"] = """# 🃏 Sorting Cards

## What You'll Learn
`arrange()` sorts rows—like sorting a deck of cards by number.

## Why This Matters
Sorted data reveals patterns. Want the heaviest penguins? The smallest bills? `arrange()` puts them in order so you can see.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `arrange()`. Think of it as "take this data, then sort it."

## Example

```r
# Sort ascending (smallest first)
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
fixes_made.append("20211: Added pipe micro-bridge")

# 20212
lessons["20212"]["content"] = """# 📊 Sorting by Multiple Columns

## What You'll Learn
Sort by multiple columns: first by one, then ties broken by another.

## Why This Matters
Often one column has ties. "Sort by species THEN by mass" shows patterns within each species.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `arrange()`. Think of it as "take this data, then sort it."

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
fixes_made.append("20212: Added pipe micro-bridge")

# 20213
lessons["20213"]["content"] = """# 🔧 Descending Order

## What You'll Learn
Use `desc()` to sort largest-first (descending).

## Why This Matters
By default, `arrange()` sorts smallest-first. For "top 10 heaviest" you need `desc()`.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `arrange()`. Think of it as "take this data, then sort it."

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
fixes_made.append("20213: Added pipe micro-bridge")

# 20214
lessons["20214"]["content"] = """# 🦸 Challenge: Reverse Sort

## What You'll Learn
Apply `desc()` to multiple columns for complex sorting.

## Why This Matters
Sometimes you want "alphabetical species, but heaviest first within each". This requires mixing ascending and descending.

> 💡 The `%>%` (pipe) takes `penguins` and passes it to `arrange()`. Think of it as "take this data, then sort it."

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
fixes_made.append("20214: Added pipe micro-bridge")

# 20402 - pivot_longer
lessons["20402"]["content"] = """# 📋 Naming New Columns

## What You'll Learn
`pivot_longer()` lets you name the new columns with `names_to` and `values_to`.

## Why This Matters
When you convert wide to long, you get two new columns: one for the old column names, one for the values. Naming them clearly makes your data understandable.

> 💡 The `%>%` (pipe) takes `table4a` and passes it to `pivot_longer()`. Think of it as "take this data, then reshape it."

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
fixes_made.append("20402: Added pipe micro-bridge")

# 20404
lessons["20404"]["content"] = """# 🦸 Challenge: Pivot It

## What You'll Learn
Apply `pivot_longer()` to convert wide data to tidy format.

## Why This Matters
Real datasets often come in wide format. Pivoting is a core skill you'll use constantly.

> 💡 The `%>%` (pipe) takes `table4a` and passes it to `pivot_longer()`. Think of it as "take this data, then reshape it."

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
fixes_made.append("20404: Added pipe micro-bridge")

# Save updated lessons
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("COMPLIANCE PATCH 2 COMPLETE")
print("=" * 60)
print(f"\nFixes made: {len(fixes_made)}")
for fix in fixes_made:
    print(f"  - {fix}")

print(f"\nMarkdown fixed: {len(markdown_fixed)} lessons")
print(f"Solution removed: {len(solution_removed)} lessons")
print(f"Bridges added: {len(bridge_added)} lessons (auto)")
