"""
Batch R-2 Rewrite Script - Part 1
Concepts: 2230 (Regex), 2250 (Dates), 2260 (Missing Values)
"""

import json

with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

# Metadata to add
def add_metadata(lesson):
    if 'gap_ids' not in lesson:
        lesson['gap_ids'] = []
    if 'R-REINF' not in lesson['gap_ids']:
        lesson['gap_ids'].append('R-REINF')
    lesson['batch_id'] = 'R-2'
    return lesson

# ===== CONCEPT 2230: Regex Basics =====

lessons["22301"] = add_metadata({
    **lessons["22301"],
    "title": "Analogy: Find & Replace",
    "content": """# 🔍 Find & Replace on Steroids

## What You'll Learn
How regex patterns let you search for text in flexible, powerful ways.

## Why This Matters
Imagine you need to find all phone numbers in a document, but they're written in different formats: "555-1234", "(555) 1234", "555.1234". A simple search won't work. Regex patterns describe *what you're looking for* rather than the exact text.

## Example

```r
library(stringr)

# Find digits
str_detect("Call 555-1234", "\\\\d+")
```

`\\d+` means "one or more digits". It matches "555" and "1234".

## 🎯 Your Task

1. Look at the pattern `\\d+` — it means "one or more digits"
2. Use `str_detect(\"My zip is 90210\", \"\\\\d+\")` to check if there are digits
3. Observe: returns TRUE because "90210" contains digits

**Expected Output:**
`TRUE`

## ⚠️ Common Mistake

**Wrong:**
```r
str_detect("hello", "\\d+")
```
Returns FALSE — no digits in "hello".

**Fixed:**
```r
str_detect("hello123", "\\\\d+")
```
Returns TRUE.

---

✅ **No Hidden Prerequisites**: Uses `str_detect()` from stringr (loaded with tidyverse).
"""
})

lessons["22302"] = add_metadata({
    **lessons["22302"],
    "title": "Variation: Anchors",
    "content": """# ⚓ Anchors: Start & End

## What You'll Learn
How `^` and `$` anchor patterns to the start or end of text.

## Why This Matters
Sometimes you only want matches at specific positions. "Find files that START with 'data_'" or "Find emails that END with '.edu'". Anchors give you this control.

## Example

```r
# Starts with "data"
str_detect("data_file.csv", "^data")

# Ends with ".csv"
str_detect("data_file.csv", "\\\\.csv$")
```

`^` = start of string, `$` = end of string.

## 🎯 Your Task

1. Check if "report_2024.xlsx" ENDS with ".xlsx"
2. Use: `str_detect(\"report_2024.xlsx\", \"\\\\.xlsx$\")`
3. The `\\.` escapes the dot (since `.` means "any character")

**Expected Output:**
`TRUE`

## ⚠️ Common Mistake

**Wrong:**
```r
str_detect("data.csv", ".csv$")
```
This matches "acsv" too because `.` means any character!

**Fixed:**
```r
str_detect("data.csv", "\\\\.csv$")
```
Escape the dot with `\\.`.

---

✅ **No Hidden Prerequisites**: Uses `str_detect()` and basic regex from this chapter.
"""
})

lessons["22303"] = add_metadata({
    **lessons["22303"],
    "title": "Fix the Code: Character Classes",
    "content": """# 🔧 Fix: Character Classes

## What You'll Learn
How to fix common character class mistakes in regex.

## Why This Matters
Character classes like `[aeiou]` match any one character from the set. Common errors include forgetting brackets or misusing special characters inside them.

## Example

```r
# Match vowels
str_extract("hello", "[aeiou]")
```

Returns "e" — the first vowel found.

## 🎯 Your Task

1. The code below tries to find vowels but has an error
2. Fix it by adding brackets around the letters
3. Run to verify it extracts "e"

**Broken:**
```r
str_extract("hello", "aeiou")
```

**Expected Output:**
`"e"` (the first vowel)

## ⚠️ Common Mistake

**Wrong:**
```r
str_extract("hello", "aeiou")
```
This looks for the literal string "aeiou".

**Fixed:**
```r
str_extract("hello", "[aeiou]")
```
Now it's a character class matching any vowel.

---

✅ **No Hidden Prerequisites**: Uses `str_extract()` from stringr.
"""
})

lessons["22304"] = add_metadata({
    **lessons["22304"],
    "title": "Challenge: Extract Digits",
    "content": """# 🦸 Challenge: Extract All Digits

## What You'll Learn
Apply regex to extract matching patterns from text.

## Why This Matters
Extracting specific parts of text (dates, IDs, prices) is a core data cleaning skill.

## Example

Pattern for extracting digits:
```r
str_extract_all(text, "\\\\d+")
```

This returns ALL matches as a list.

## 🎯 Your Task

From the string "Order #12345 shipped on 2024-01-15":
1. Extract all digit sequences
2. Use `str_extract_all()` with pattern `\\d+`
3. You should get: "12345", "2024", "01", "15"

**Expected Output:**
A list containing `c("12345", "2024", "01", "15")`

## ⚠️ Common Mistake

**Wrong:**
```r
str_extract()
```
This only gets the FIRST match ("12345").

**Fixed:**
```r
str_extract_all()
```
Gets ALL matches.

---

✅ **No Hidden Prerequisites**: Uses `str_extract_all()` from stringr.
"""
})

# ===== CONCEPT 2250: Dates & Times =====

lessons["22501"] = add_metadata({
    **lessons["22501"],
    "title": "Analogy: Universal Translator",
    "content": """# 🌍 The Universal Date Translator

## What You'll Learn
How lubridate converts date strings into proper date objects R can work with.

## Why This Matters
Dates come in many formats: "2024-01-15", "January 15, 2024", "15/01/2024". R needs to understand these are all the same date. lubridate's parser functions (`ymd`, `mdy`, `dmy`) handle this translation.

## Example

```r
library(lubridate)

ymd("2024-01-15")
mdy("January 15, 2024")
dmy("15-01-2024")
```

All three produce the same date object!

## 🎯 Your Task

1. Use `ymd()` to parse "2024-03-20"
2. Use `mdy()` to parse "March 20, 2024"
3. Both should give you the same date

**Expected Output:**
`"2024-03-20"` (as a Date object)

## ⚠️ Common Mistake

**Wrong:**
```r
ymd("03-20-2024")
```
Wrong order! ymd expects year-month-day.

**Fixed:**
```r
mdy("03-20-2024")
```
Use mdy for month-day-year.

---

✅ **No Hidden Prerequisites**: Uses lubridate (loaded with tidyverse).
"""
})

lessons["22502"] = add_metadata({
    **lessons["22502"],
    "title": "Variation: Month-Day-Year",
    "content": """# 📅 Different Date Formats

## What You'll Learn
How to parse dates in any format by choosing the right function.

## Why This Matters
US dates often use month-day-year ("01/15/2024"), while European dates use day-month-year ("15/01/2024"). Using the wrong parser gives wrong dates!

## Example

```r
# US format
mdy("01-15-2024")  # January 15

# European format
dmy("15-01-2024")  # Also January 15
```

## 🎯 Your Task

1. Parse "12/25/2024" using US format (month first)
2. Use `mdy()` not `dmy()`
3. Verify you get December 25, not the 12th day of month 25

**Expected Output:**
`"2024-12-25"` (Christmas Day)

## ⚠️ Common Mistake

**Wrong:**
```r
dmy("12/25/2024")
```
Tries to read as day=12, month=25 — error!

**Fixed:**
```r
mdy("12/25/2024")
```
Correctly reads month=12, day=25.

---

✅ **No Hidden Prerequisites**: Uses `mdy()` from lubridate.
"""
})

lessons["22503"] = add_metadata({
    **lessons["22503"],
    "title": "Fix the Code: Date Parsing",
    "content": """# 🔧 Fix: Wrong Date Parser

## What You'll Learn
How to identify and fix date parsing errors.

## Why This Matters
Silent date errors are dangerous. Parsing "10/11/2024" wrong could mean October 11 vs November 10 — a 1-month difference that breaks analysis!

## Example

```r
# Check your date is correct
parsed <- mdy("10/11/2024")
month(parsed)  # Should be 10 for October
day(parsed)    # Should be 11
```

## 🎯 Your Task

1. The date "31/12/2024" fails with `mdy()` (no month 31)
2. Fix it by using `dmy()` instead
3. Verify you get December 31

**Broken:**
```r
mdy("31/12/2024")  # Error!
```

**Expected Output:**
`"2024-12-31"` (New Year's Eve)

## ⚠️ Common Mistake

**Wrong:**
```r
mdy("31/12/2024")
```
Fails because there's no month 31.

**Fixed:**
```r
dmy("31/12/2024")
```
Correctly interprets day=31, month=12.

---

✅ **No Hidden Prerequisites**: Uses `dmy()` from lubridate.
"""
})

lessons["22504"] = add_metadata({
    **lessons["22504"],
    "title": "Challenge: Extract Year",
    "content": """# 🦸 Challenge: Get the Year

## What You'll Learn
Apply date extraction functions to get components.

## Why This Matters
Once you have a date object, you can extract year, month, day, weekday, etc. This is essential for time-based analysis.

## Example

```r
my_date <- ymd("2024-03-15")
year(my_date)   # 2024
month(my_date)  # 3
day(my_date)    # 15
```

## 🎯 Your Task

Given the date "2024-07-04" (US Independence Day):
1. Parse it with `ymd()`
2. Extract just the year using `year()`
3. Verify you get 2024

**Expected Output:**
`2024`

## ⚠️ Common Mistake

**Wrong:**
```r
year("2024-07-04")
```
This fails! You must parse the string first.

**Fixed:**
```r
year(ymd("2024-07-04"))
```
Parse, then extract.

---

✅ **No Hidden Prerequisites**: Uses `ymd()` and `year()` from lubridate.
"""
})

# ===== CONCEPT 2260: Missing Values =====

lessons["22601"] = add_metadata({
    **lessons["22601"],
    "title": "Analogy: Empty Seat",
    "content": """# 💺 The Empty Seat

## What You'll Learn
How `NA` represents missing data, and why it "poisons" calculations.

## Why This Matters
In R, `NA` means "I don't know the value." When you add "I don't know" to a number, the result is "I don't know" — that's why `NA` propagates through calculations.

## Example

```r
x <- c(1, 2, NA, 4)
sum(x)        # Returns NA
sum(x, na.rm = TRUE)  # Returns 7
```

The `na.rm = TRUE` argument tells R to ignore the empty seats.

## 🎯 Your Task

1. Create a vector `c(10, 20, NA, 40)`
2. Try `mean()` on it — you'll get NA
3. Add `na.rm = TRUE` to get the proper average

**Expected Output:**
Without na.rm: `NA`
With na.rm: `23.33...` (mean of 10, 20, 40)

## ⚠️ Common Mistake

**Wrong:**
```r
mean(c(10, 20, NA, 40))
```
Returns NA.

**Fixed:**
```r
mean(c(10, 20, NA, 40), na.rm = TRUE)
```
Returns 23.33.

---

✅ **No Hidden Prerequisites**: Uses base R `mean()` and `c()`.
"""
})

lessons["22602"] = add_metadata({
    **lessons["22602"],
    "title": "Variation: Replacing NAs",
    "content": """# 🔄 Replacing Missing Values

## What You'll Learn
How to replace NA values with a default using `replace_na()` or `coalesce()`.

## Why This Matters
Sometimes you want to fill gaps: replace missing ages with the median, missing countries with "Unknown", etc. `replace_na()` from tidyr makes this easy.

> 💡 The `%>%` takes your data and passes it to `mutate()` — think "take this, then modify it."

## Example

```r
library(tidyr)

df %>% mutate(
  column = replace_na(column, default_value)
)
```

## 🎯 Your Task

1. Given a vector `c(1, NA, 3, NA, 5)`
2. Use `replace_na()` to fill NAs with 0
3. Result should be `c(1, 0, 3, 0, 5)`

**Expected Output:**
`1 0 3 0 5`

## ⚠️ Common Mistake

**Wrong:**
```r
replace_na(x, "0")
```
Type mismatch if x is numeric — use `0` not `"0"`.

**Fixed:**
```r
replace_na(x, 0)
```
Correct numeric replacement.

---

✅ **No Hidden Prerequisites**: Uses `replace_na()` from tidyr.
"""
})

lessons["22603"] = add_metadata({
    **lessons["22603"],
    "title": "Fix the Code: NA Comparison",
    "content": """# 🔧 Fix: Comparing to NA

## What You'll Learn
Why `x == NA` doesn't work and what to use instead.

## Why This Matters
This is THE most common NA mistake. `NA == NA` returns NA, not TRUE! You must use `is.na()` to check for missing values.

## Example

```r
x <- c(1, NA, 3)

# Wrong approach
x == NA  # Returns NA NA NA

# Correct approach
is.na(x)  # Returns FALSE TRUE FALSE
```

## 🎯 Your Task

1. Look at the broken filter below
2. Fix it by replacing `== NA` with `is.na()`
3. Result should correctly filter missing values

**Broken:**
```r
penguins %>% filter(bill_length_mm == NA)
```
Returns 0 rows!

**Expected Output:**
Rows where bill_length_mm is missing

## ⚠️ Common Mistake

**Wrong:**
```r
filter(x == NA)
```
Never works!

**Fixed:**
```r
filter(is.na(x))
```
Use `is.na()` function.

---

✅ **No Hidden Prerequisites**: Uses `filter()`, `is.na()`, and `penguins`.
"""
})

lessons["22604"] = add_metadata({
    **lessons["22604"],
    "title": "Challenge: Drop Missing Rows",
    "content": """# 🦸 Challenge: Clean Data

## What You'll Learn
Apply `drop_na()` to remove rows with missing values.

## Why This Matters
Before analysis, you often need complete cases only. `drop_na()` from tidyr removes any row containing NA.

> 💡 The `%>%` takes `penguins` and passes it to `drop_na()` — think "take this data, then clean it."

## Example

```r
# Drop all rows with any NA
df %>% drop_na()

# Drop rows with NA in specific column
df %>% drop_na(column_name)
```

## 🎯 Your Task

1. Take the penguins dataset
2. Drop all rows that have NA in `body_mass_g`
3. Count how many rows remain

**Expected Output:**
342 rows (2 rows had missing body mass)

## ⚠️ Common Mistake

**Wrong:**
```r
penguins %>% drop_na
```
Forgot parentheses! `drop_na` is a function, not a column.

**Fixed:**
```r
penguins %>% drop_na()
```
With parentheses.

---

✅ **No Hidden Prerequisites**: Uses `drop_na()` from tidyr and `penguins`.
"""
})

# Save
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Batch R-2 Part 1 complete: 2230, 2250, 2260 (12 reinforcers)")
