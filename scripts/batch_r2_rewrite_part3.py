"""
Batch R-2 Rewrite Script - Part 3
Concepts: 2330 (Lists), 2400 (Functions), 2410 (Iteration)
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

# ===== CONCEPT 2330: Lists & Rectangling =====

lessons["23301"] = add_metadata({
    **lessons["23301"],
    "title": "Analogy: Unpacking Boxes",
    "content": """# 📦 Unpacking Nested Boxes

## What You'll Learn
How to extract data from nested lists into tidy data frames.

## Why This Matters
API responses and JSON data come as deeply nested lists. "Rectangling" flattens these into the rows-and-columns format you need for analysis.

## Example

```r
library(tidyr)

# A nested list
data <- list(
  list(name = "Alice", score = 90),
  list(name = "Bob", score = 85)
)

# Flatten to data frame
tibble(data = data) %>% unnest_wider(data)
```

## 🎯 Your Task

1. Understand: `unnest_wider()` turns each list element into columns
2. This is called "rectangling" — making messy data rectangular
3. The inverse is `unnest_longer()` — turns elements into rows

**Expected Output:**
A tibble with `name` and `score` columns

## ⚠️ Common Mistake

**Wrong:**
```r
data[[1]]$name
```
Manual extraction doesn't scale.

**Fixed:**
```r
tibble(data) %>% unnest_wider(data)
```
Works on the whole list at once.

---

✅ **No Hidden Prerequisites**: Uses `unnest_wider()` from tidyr.
"""
})

lessons["23302"] = add_metadata({
    **lessons["23302"],
    "title": "Variation: Going Longer",
    "content": """# ↕️ Unnest Longer

## What You'll Learn
How `unnest_longer()` turns list elements into rows rather than columns.

## Why This Matters
When each list element is a single value (not named), `unnest_longer()` creates one row per element. Choose wider vs longer based on your data structure.

## Example

```r
# Each person has multiple scores
data <- tibble(
  name = c("Alice", "Bob"),
  scores = list(c(90, 85, 88), c(77, 80))
)

data %>% unnest_longer(scores)
```

## 🎯 Your Task

1. `unnest_wider()` = list → columns (like unpacking key-value pairs)
2. `unnest_longer()` = list → rows (like stacking multiple values)
3. Try `unnest_longer()` on a list column with multiple values

**Expected Output:**
Multiple rows per original row

## ⚠️ Common Mistake

**Wrong:**
Using `unnest_wider()` on simple vectors — creates weird columns.

**Fixed:**
Use `unnest_longer()` for vectors, `unnest_wider()` for named lists.

---

✅ **No Hidden Prerequisites**: Uses `unnest_longer()` from tidyr.
"""
})

lessons["23303"] = add_metadata({
    **lessons["23303"],
    "title": "Fix the Code: Plural",
    "content": """# 🔧 Fix: Column Name

## What You'll Learn
Common errors when working with list columns.

## Why This Matters
The column name in `unnest_*()` must match exactly. Typos cause "column not found" errors.

## Example

```r
df <- tibble(items = list(1, 2, 3))

# Wrong column name
df %>% unnest_longer(item)  # Error!

# Correct
df %>% unnest_longer(items)
```

## 🎯 Your Task

1. The code has a typo in the column name
2. Fix `unnest_longer(score)` to `unnest_longer(scores)`
3. Column names are case-sensitive too!

**Broken:**
```r
df %>% unnest_longer(score)
```

**Expected Output:**
The unnested data frame

## ⚠️ Common Mistake

**Wrong:**
```r
unnest_longer(Score)
```
Case matters!

**Fixed:**
```r
unnest_longer(scores)
```

---

✅ **No Hidden Prerequisites**: Uses `unnest_longer()` from tidyr.
"""
})

lessons["23304"] = add_metadata({
    **lessons["23304"],
    "title": "Challenge: Rectangle JSON",
    "content": """# 🦸 Challenge: Flatten Data

## What You'll Learn
Apply rectangling to convert nested data to a tibble.

## Why This Matters
This is the core skill for working with API data.

## Example

```r
# Typical pattern
tibble(data = nested_list) %>%
  unnest_wider(data)
```

## 🎯 Your Task

Given this structure:
```r
people <- list(
  list(name = "Alice", age = 30),
  list(name = "Bob", age = 25)
)
```

1. Wrap it in a tibble: `tibble(data = people)`
2. Unnest with `unnest_wider(data)`
3. Result should have `name` and `age` columns

**Expected Output:**
A 2-row tibble with name and age columns

## ⚠️ Common Mistake

**Wrong:**
```r
as.data.frame(people)
```
Doesn't handle nested lists well.

**Fixed:**
```r
tibble(data = people) %>% unnest_wider(data)
```

---

✅ **No Hidden Prerequisites**: Uses `tibble()`, `unnest_wider()`.
"""
})

# ===== CONCEPT 2400: Functions & Tidy Eval =====

lessons["24001"] = add_metadata({
    **lessons["24001"],
    "title": "Analogy: Recipe Card",
    "content": """# 📝 Writing Recipe Cards

## What You'll Learn
How to create your own functions to avoid repeating code.

## Why This Matters
If you copy-paste code more than twice, make it a function. Functions encapsulate logic so you can reuse it with different inputs.

## Example

```r
# A simple function
add_ten <- function(x) {
  x + 10
}

add_ten(5)   # Returns 15
add_ten(100) # Returns 110
```

## 🎯 Your Task

1. Functions have: `name <- function(arguments) { body }`
2. The last expression is automatically returned
3. Try creating a function that doubles a number

**Expected Output:**
A reusable function

## ⚠️ Common Mistake

**Wrong:**
```r
add_ten <- function x { x + 10 }
```
Missing parentheses around argument!

**Fixed:**
```r
add_ten <- function(x) { x + 10 }
```

---

✅ **No Hidden Prerequisites**: Base R function syntax.
"""
})

lessons["24002"] = add_metadata({
    **lessons["24002"],
    "title": "Variation: Multiple Args",
    "content": """# 🔢 Multiple Arguments

## What You'll Learn
How to create functions with multiple parameters.

## Why This Matters
Real functions often need more than one input: `convert_temp(value, from, to)`, `filter_data(df, column, threshold)`.

## Example

```r
greet <- function(name, greeting = "Hello") {
  paste(greeting, name)
}

greet("Alice")           # "Hello Alice"
greet("Bob", "Hi")       # "Hi Bob"
```

The `= "Hello"` sets a default value.

## 🎯 Your Task

1. Create a function `power(x, n)` that returns `x^n`
2. Add a default: `n = 2` for squaring
3. Test: `power(3)` should return 9

**Expected Output:**
9 (3 squared)

## ⚠️ Common Mistake

**Wrong:**
```r
function(x, n = 2, )  # Trailing comma
```
No trailing commas allowed.

**Fixed:**
```r
function(x, n = 2)
```

---

✅ **No Hidden Prerequisites**: Base R function arguments.
"""
})

lessons["24003"] = add_metadata({
    **lessons["24003"],
    "title": "Fix the Code: Braces",
    "content": """# 🔧 Fix: Function Syntax

## What You'll Learn
Common syntax errors in function definitions.

## Why This Matters
Missing braces or mismatched parentheses cause cryptic errors.

## Example

```r
# Wrong - missing opening brace
square <- function(x)
  x * x
}

# Fixed
square <- function(x) {
  x * x
}
```

## 🎯 Your Task

1. The function below is missing a brace
2. Add the opening `{` after the argument list
3. Ensure `}` closes it properly

**Broken:**
```r
double <- function(x)
  x * 2
}
```

**Expected Output:**
A working function

## ⚠️ Common Mistake

**Wrong:**
Mismatched braces or parentheses.

**Fixed:**
Every `{` needs a `}`, every `(` needs a `)`.

---

✅ **No Hidden Prerequisites**: Base R syntax.
"""
})

lessons["24004"] = add_metadata({
    **lessons["24004"],
    "title": "Challenge: Write Function",
    "content": """# 🦸 Challenge: Your Own Function

## What You'll Learn
Apply function syntax to create a useful helper.

## Why This Matters
Creating custom functions is how you build reusable analysis tools.

## Example

```r
my_function <- function(arg1, arg2) {
  # do something
  result
}
```

## 🎯 Your Task

Create a function `summarize_column(df, col)` that:
1. Takes a data frame and column name
2. Returns the mean of that column (handle NAs)
3. Test on penguins$body_mass_g

**Expected Output:**
The mean value (around 4200 for body_mass_g)

## ⚠️ Common Mistake

**Wrong:**
```r
function(df, col) mean(df$col)
```
`$col` looks for a column literally named "col"!

**Fixed:**
```r
function(df, col) mean(df[[col]], na.rm = TRUE)
```
Use `[[]]` for programmatic column access.

---

✅ **No Hidden Prerequisites**: Base R functions and `[[]]` subsetting.
"""
})

# ===== CONCEPT 2410: Iteration: across & map =====

lessons["24101"] = add_metadata({
    **lessons["24101"],
    "title": "Analogy: Assembly Line",
    "content": """# 🏭 The Assembly Line

## What You'll Learn
How `across()` applies operations to multiple columns at once.

## Why This Matters
Instead of `mutate(a = round(a), b = round(b), c = round(c))`, you write one line. `across()` is like an assembly line processing many items identically.

> 💡 The `%>%` takes your data and passes it to `mutate()`.

## Example

```r
penguins %>% mutate(
  across(where(is.numeric), round)
)
```

Rounds ALL numeric columns at once.

## 🎯 Your Task

1. `across()` goes inside `mutate()` or `summarize()`
2. First arg: which columns (use `where()`, `starts_with()`, etc.)
3. Second arg: what function to apply

**Expected Output:**
All numeric columns rounded

## ⚠️ Common Mistake

**Wrong:**
```r
across(round, where(is.numeric))
```
Arguments in wrong order!

**Fixed:**
```r
across(where(is.numeric), round)
```
Columns first, function second.

---

✅ **No Hidden Prerequisites**: Uses `across()` from dplyr.
"""
})

lessons["24102"] = add_metadata({
    **lessons["24102"],
    "title": "Variation: map()",
    "content": """# 🗺️ Map: Apply to Each

## What You'll Learn
How `map()` applies a function to each element of a list.

## Why This Matters
`map()` is for lists what `across()` is for columns. It iterates and applies a function to each element, returning a list of results.

## Example

```r
library(purrr)

numbers <- list(1, 2, 3)
map(numbers, ~ .x * 2)
```

Returns: list(2, 4, 6)

## 🎯 Your Task

1. `map(list, function)` applies to each element
2. `.x` in the formula represents each element
3. Try `map(1:3, ~ .x^2)` to square each

**Expected Output:**
list(1, 4, 9)

## ⚠️ Common Mistake

**Wrong:**
```r
map(1:3, .x^2)
```
Missing the `~` for formula notation.

**Fixed:**
```r
map(1:3, ~ .x^2)
```

---

✅ **No Hidden Prerequisites**: Uses `map()` from purrr.
"""
})

lessons["24103"] = add_metadata({
    **lessons["24103"],
    "title": "Fix the Code: across()",
    "content": """# 🔧 Fix: across() Syntax

## What You'll Learn
Common errors when using `across()`.

## Why This Matters
The `across()` syntax is particular. Missing the column selector or using wrong function format causes errors.

## Example

```r
# Wrong - forgot column selector
mutate(across(mean))

# Fixed - specify which columns
mutate(across(where(is.numeric), mean))
```

## 🎯 Your Task

1. The code is missing the column selector
2. Add `everything()` or `where(is.numeric)`
3. Now across knows which columns to process

**Broken:**
```r
penguins %>% mutate(across(round))
```

**Expected Output:**
Rounded numeric columns

## ⚠️ Common Mistake

**Wrong:**
```r
across(round)
```
across() needs to know WHICH columns!

**Fixed:**
```r
across(where(is.numeric), round)
```

---

✅ **No Hidden Prerequisites**: Uses `across()` and `where()`.
"""
})

lessons["24104"] = add_metadata({
    **lessons["24104"],
    "title": "Challenge: Summarize All",
    "content": """# 🦸 Challenge: Summary Stats

## What You'll Learn
Apply iteration to compute summaries across columns.

## Why This Matters
Getting mean of every numeric column is a one-liner with `across()`.

> 💡 The `%>%` takes `penguins` and passes it to `summarize()`.

## Example

```r
df %>% summarize(
  across(where(is.numeric), mean, na.rm = TRUE)
)
```

## 🎯 Your Task

Use penguins to:
1. Select all numeric columns with `where(is.numeric)`
2. Calculate the mean of each
3. Remember `na.rm = TRUE` for missing values

**Expected Output:**
One row with mean for each numeric column

## ⚠️ Common Mistake

**Wrong:**
```r
summarize(across(mean))
```
Missing column selector AND na.rm.

**Fixed:**
```r
summarize(across(where(is.numeric), mean, na.rm = TRUE))
```

---

✅ **No Hidden Prerequisites**: Uses `summarize()`, `across()`, `where()`.
"""
})

with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Batch R-2 Part 3 complete: 2330, 2400, 2410 (12 reinforcers)")
