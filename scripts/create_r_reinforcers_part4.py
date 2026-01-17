"""
Create Missing R Reinforcers - Part 4 (Final)
Concepts: 2061, 2070, 2071
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
        "chapter_id": concept.get("chapter_id", 7),
        "chapter_title": concept.get("chapter_title", ""),
        "gap_ids": ["R-REINF"],
        "batch_id": "R-3"
    }

# ===== 2061: Handling Messy Data =====
lessons["20611"] = create_reinforcer(2061, 1, "Analogy: Cleaning Your Room",
"""# 🧹 Data Cleaning Basics

## What You'll Learn
Common data problems and how to spot them.

## Why This Matters
Real data is messy: missing values, typos, inconsistent formats. Cleaning comes before analysis.

## Example

Common issues to look for:
- `NA`, `N/A`, `""` — missing values
- `"Yes"`, `"yes"`, `"YES"` — inconsistent capitalization
- `"2024-01-15"` vs `"01/15/2024"` — date format mismatches

## 🎯 Your Task

1. Look for missing values in your data
2. Check for inconsistent spelling
3. List the cleaning steps needed

**Expected Output:**
A mental checklist of data issues to fix

## ⚠️ Common Mistake

**Wrong:**
Jumping into analysis without checking data quality.

**Fixed:**
Always run `summary()` and `glimpse()` first.

---

✅ **No Hidden Prerequisites**: Conceptual overview of data cleaning.
""")

lessons["20612"] = create_reinforcer(2061, 2, "Variation: Standardizing Text",
"""# 📝 Consistent Text

## What You'll Learn
How to standardize text data for analysis.

## Why This Matters  
`"Male"`, `"male"`, `"M"` should all be the same. Inconsistency breaks grouping.

## Example

```r
library(stringr)

# Standardize to lowercase
mutate(gender = str_to_lower(gender))

# Replace values
mutate(gender = case_when(
  gender %in% c("m", "male") ~ "male",
  gender %in% c("f", "female") ~ "female"
))
```

## 🎯 Your Task

1. Use `str_to_lower()` to normalize case
2. Use `case_when()` to map variants to standards
3. Verify counts are now correct

**Expected Output:**
Consistent values for grouping

## ⚠️ Common Mistake

**Wrong:**
Filtering on original messy values.

**Fixed:**
Clean first, then filter/group.

---

✅ **No Hidden Prerequisites**: Uses `str_to_lower()` and `case_when()`.
""")

lessons["20613"] = create_reinforcer(2061, 3, "Fix the Code: NA Handling",
"""# 🔧 Fix: Missing Value Strategy

## What You'll Learn
Choose the right NA handling approach.

## Why This Matters
`drop_na()` loses data. `replace_na()` makes assumptions. Pick wisely.

## Example

```r
# Option 1: Remove rows with NA (loses data)
drop_na(column)

# Option 2: Replace NA with a value
replace_na(column, 0)

# Option 3: Ignore NA in calculations
mean(column, na.rm = TRUE)
```

## 🎯 Your Task

1. Identify how many NAs exist with `sum(is.na(x))`
2. Decide: drop, replace, or ignore?
3. Apply the appropriate strategy

**Expected Output:**
Clean data or proper NA handling

## ⚠️ Common Mistake

**Wrong:**
```r
drop_na()  # Drops ALL rows with ANY NA
```

**Fixed:**
```r
drop_na(column_name)  # Only drop if THIS column is NA
```

---

✅ **No Hidden Prerequisites**: NA handling strategies.
""")

lessons["20614"] = create_reinforcer(2061, 4, "Challenge: Clean a Dataset",
"""# 🦸 Challenge: Full Cleaning Pipeline

## What You'll Learn
Apply a complete data cleaning workflow.

## Why This Matters
This is what real data analysis looks like.

> 💡 The `%>%` chains your cleaning steps.

## Example

Pattern:
```r
raw_data %>%
  drop_na(key_column) %>%
  mutate(text_col = str_to_lower(text_col)) %>%
  filter(value > 0)
```

## 🎯 Your Task

Clean a dataset by:
1. Removing rows with NA in important columns
2. Standardizing text columns
3. Filtering out invalid values

**Expected Output:**
A clean, analysis-ready dataset

## ⚠️ Common Mistake

Don't modify original data — save to a new variable.

---

✅ **No Hidden Prerequisites**: Combines cleaning techniques.
""")

# ===== 2070: Google is Your Friend =====
lessons["20701"] = create_reinforcer(2070, 1, "Analogy: Asking the Oracle",
"""# 🔮 Searching for Help

## What You'll Learn
How to effectively search for R help online.

## Why This Matters
Every programmer Googles. The skill is knowing WHAT to search and WHERE to look.

## Example

Good search queries:
- `r ggplot change axis labels`
- `r dplyr filter multiple conditions`
- `r error "object not found"` (include error message!)

## 🎯 Your Task

1. Include "r" or "rstats" in your search
2. Include the function or package name
3. Include the specific error message if applicable

**Expected Output:**
Understanding of effective search strategies

## ⚠️ Common Mistake

**Wrong:**
`why doesn't my code work`

**Fixed:**
`r ggplot error: object 'x' not found`

---

✅ **No Hidden Prerequisites**: Search skills, no code required.
""")

lessons["20702"] = create_reinforcer(2070, 2, "Variation: Stack Overflow Tips",
"""# 📚 Reading Stack Overflow

## What You'll Learn
How to evaluate and use Stack Overflow answers.

## Why This Matters
Not all answers are equal. Look for upvotes, check the date, and read comments.

## Example

Good answer signs:
- ✓ Green checkmark (accepted)
- Many upvotes
- Clear explanation
- Recent (R changes over time)

## 🎯 Your Task

1. Check if answer is accepted (green checkmark)
2. Read the explanation, not just the code
3. Check comments for updates/corrections

**Expected Output:**
Ability to evaluate answer quality

## ⚠️ Common Mistake

**Wrong:**
Copying code without understanding it.

**Fixed:**
Read the explanation, understand why it works.

---

✅ **No Hidden Prerequisites**: Reading comprehension skills.
""")

lessons["20703"] = create_reinforcer(2070, 3, "Fix the Code: Adapting Answers",
"""# 🔧 Fix: Making Code Work for You

## What You'll Learn
Why copied code often needs adaptation.

## Why This Matters
The answer uses their variable names and data. You need to substitute yours.

## Example

```r
# Stack Overflow answer uses 'df' and 'value'
df %>% filter(value > 10)

# Your data uses 'penguins' and 'body_mass_g'
penguins %>% filter(body_mass_g > 4000)
```

## 🎯 Your Task

1. Identify placeholder names in the answer
2. Substitute your actual column/data names
3. Test incrementally

**Expected Output:**
Working code adapted to your data

## ⚠️ Common Mistake

**Wrong:**
Running answer code directly without changes.

**Fixed:**
Replace placeholder names with your actual names.

---

✅ **No Hidden Prerequisites**: Code adaptation skills.
""")

lessons["20704"] = create_reinforcer(2070, 4, "Challenge: Find and Apply",
"""# 🦸 Challenge: Solve with Search

## What You'll Learn
Apply the full search-and-adapt workflow.

## Why This Matters
This is what you'll do daily as a data scientist.

## Example

Workflow:
1. Define the problem clearly
2. Search with good keywords
3. Evaluate answers
4. Adapt to your code
5. Test

## 🎯 Your Task

Using search, find how to:
1. Rotate x-axis labels 45 degrees in ggplot
2. Find and adapt the answer
3. Apply it to your plot

**Expected Output:**
A plot with rotated axis labels

## ⚠️ Common Mistake

Giving up after the first failed search — try different keywords!

---

✅ **No Hidden Prerequisites**: Research skills.
""")

# ===== 2071: Making Reprexes =====
lessons["20711"] = create_reinforcer(2071, 1, "Analogy: The Minimal Bug Report",
"""# 🐛 Reproducible Examples

## What You'll Learn
What a reprex (minimal reproducible example) is and why it helps.

## Why This Matters
When asking for help, a reprex lets others run your exact problem. No reprex = no answer.

## Example

Good reprex components:
1. Library calls needed
2. Small sample data
3. Code that shows the problem
4. Expected vs actual result

## 🎯 Your Task

1. Understand: reprex = code others can run
2. It must include everything needed
3. It should be as SMALL as possible

**Expected Output:**
Understanding of reprex requirements

## ⚠️ Common Mistake

**Wrong:**
```r
# This doesn't work
my_function()
```
No context, no data, no one can help.

**Fixed:**
Include all necessary context.

---

✅ **No Hidden Prerequisites**: Conceptual understanding.
""")

lessons["20712"] = create_reinforcer(2071, 2, "Variation: Using reprex Package",
"""# 📦 The reprex Package

## What You'll Learn
How the `reprex` package automates reprex creation.

## Why This Matters
`reprex::reprex()` formats your code and output for easy sharing.

## Example

```r
# Install once
install.packages("reprex")

# Copy your code to clipboard, then run:
reprex::reprex()
```

This creates formatted output ready for Stack Overflow.

## 🎯 Your Task

1. Install/load the reprex package
2. Copy problematic code
3. Run `reprex::reprex()` to format it

**Expected Output:**
Formatted reprex ready to share

## ⚠️ Common Mistake

**Wrong:**
Forgetting to load required packages in the reprex.

**Fixed:**
Include ALL library() calls at the top.

---

✅ **No Hidden Prerequisites**: Uses `reprex` package.
""")

lessons["20713"] = create_reinforcer(2071, 3, "Fix the Code: Minimal Data",
"""# 🔧 Fix: Creating Sample Data

## What You'll Learn
How to create minimal sample data for a reprex.

## Why This Matters
Don't share your whole dataset. Create a tiny example that shows the problem.

## Example

```r
# Wrong: uses your private/large data
my_huge_data %>% filter(...)

# Fixed: create minimal example
sample_data <- tibble(
  x = c(1, 2, 3, NA),
  y = c("a", "b", "a", "b")
)
sample_data %>% filter(...)
```

## 🎯 Your Task

1. Create a tiny tibble with 3-5 rows
2. Include only columns relevant to the problem
3. Include the problematic values (like NA)

**Expected Output:**
Self-contained code anyone can run

## ⚠️ Common Mistake

**Wrong:**
```r
read_csv("my_local_file.csv")  # No one has this!
```

**Fixed:**
Create sample data inline.

---

✅ **No Hidden Prerequisites**: Data creation with `tibble()`.
""")

lessons["20714"] = create_reinforcer(2071, 4, "Challenge: Create a Reprex",
"""# 🦸 Challenge: Build a Reprex

## What You'll Learn
Create a complete, shareable reprex.

## Why This Matters
A good reprex gets you help faster.

## Example

Complete reprex structure:
```r
library(tidyverse)

# Sample data
df <- tibble(x = c(1, 2, NA), y = c("a", "b", "c"))

# Problem: why does this return NA?
mean(df$x)

# Expected: 1.5
# Actual: NA
```

## 🎯 Your Task

Create a reprex that demonstrates:
1. A filtering problem with NA values
2. Include library calls
3. Include sample data
4. Show expected vs actual

**Expected Output:**
A complete reprex someone could run

## ⚠️ Common Mistake

Missing the "expected vs actual" — people need to know what's wrong!

---

✅ **No Hidden Prerequisites**: Combines all reprex elements.
""")

# Save
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Part 4 complete: Created reinforcers for 2061, 2070, 2071 (12 reinforcers)")
print("\nALL 48 MISSING REINFORCERS CREATED")
