"""
Create Missing R Reinforcers - Part 1
Concepts: 2005, 2006, 2011, 2012
"""

import json

with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

def create_reinforcer(concept_id, role_num, title, content):
    """Create a reinforcer lesson."""
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

# ===== 2005: Coloring by Species =====
lessons["20051"] = create_reinforcer(2005, 1, "Analogy: Color Coding",
"""# 🎨 Color as Information

## What You'll Learn
How mapping a variable to `color` in `aes()` creates meaningful visual distinctions.

## Why This Matters
Color isn't just decoration—it carries data. Different colors = different groups. This is how you reveal patterns across categories.

## Example

```r
ggplot(data = penguins, aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  geom_point()
```

Each species gets its own color automatically!

## 🎯 Your Task

1. Identify which aesthetic maps to color
2. Understand: color is for CATEGORICAL variables (like species)
3. Observe how the legend appears automatically

**Expected Output:**
A scatterplot with 3 distinct colors (one per species)

## ⚠️ Common Mistake

**Wrong:**
```r
geom_point(color = species)
```
Color must be in `aes()` to map data, not in geom.

**Fixed:**
```r
aes(color = species)
```

---

✅ **No Hidden Prerequisites**: Uses `ggplot()`, `aes()`, `geom_point()`, and `penguins` from prior lessons.
""")

lessons["20052"] = create_reinforcer(2005, 2, "Variation: Color vs Fill",
"""# 🔲 Color vs Fill

## What You'll Learn
When to use `color` vs `fill` for different geoms.

## Why This Matters
Points and lines use `color`. Bars and boxes use `fill` for the inside, `color` for the border. Choosing wrong = invisible or ugly plots.

## Example

```r
# For points: use color
ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  geom_point()

# For bars: use fill
ggplot(penguins, aes(x = species, fill = species)) +
  geom_bar()
```

## 🎯 Your Task

1. Try `color = species` with `geom_bar()` — see how it only colors the outline
2. Switch to `fill = species` — now the bars are filled
3. Observe the difference

**Expected Output:**
Bars filled with colors (not just outlined)

## ⚠️ Common Mistake

**Wrong:**
```r
geom_bar(aes(color = species))
```
Only colors the outline.

**Fixed:**
```r
geom_bar(aes(fill = species))
```

---

✅ **No Hidden Prerequisites**: Uses `geom_bar()` which is introduced in this chapter.
""")

lessons["20053"] = create_reinforcer(2005, 3, "Fix the Code: Aesthetic Inside Geom",
"""# 🔧 Fix: Aes Placement

## What You'll Learn
Why aesthetic mappings belong in `aes()`, not as regular arguments.

## Why This Matters
`color = species` outside `aes()` doesn't work — R looks for a color named "species". Inside `aes()`, it knows to map the column.

## Example

```r
# Wrong — looks for color literally called "species"
ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point(color = species)  # Error!

# Fixed — mapping goes in aes()
ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  geom_point()
```

## 🎯 Your Task

1. The starter code has `color = species` outside aes()
2. Move it inside `aes()`
3. Run to see the colored scatterplot

**Expected Output:**
A scatterplot with points colored by species

## ⚠️ Common Mistake

**Wrong:**
```r
geom_point(color = species)
```

**Fixed:**
```r
aes(..., color = species)
```

---

✅ **No Hidden Prerequisites**: Uses aesthetic mapping from this lesson.
""")

lessons["20054"] = create_reinforcer(2005, 4, "Challenge: Color by Island",
"""# 🦸 Challenge: Another Variable

## What You'll Learn
Apply color mapping independently to a different variable.

## Why This Matters
You can color by any categorical variable — not just species. This tests your understanding.

## Example

Pattern:
```r
aes(..., color = categorical_variable)
```

## 🎯 Your Task

Create a scatterplot of `flipper_length_mm` vs `body_mass_g`, but color by `island` instead of species:
1. Start with `ggplot(data = penguins, ...)`
2. Map color to `island` in aes()
3. Add `geom_point()`

**Expected Output:**
A scatterplot with 3 colors (one per island: Biscoe, Dream, Torgersen)

## ⚠️ Common Mistake

**Wrong:**
```r
color = "island"
```
Quotes make it a literal string, not a column reference.

**Fixed:**
```r
color = island
```

---

✅ **No Hidden Prerequisites**: Uses concepts from this lesson with a different column.
""")

# ===== 2006: Adding a Trend Line =====
lessons["20061"] = create_reinforcer(2006, 1, "Analogy: The Best-Fit Line",
"""# 📈 Drawing the Trend

## What You'll Learn
How `geom_smooth()` adds a trend line that summarizes the relationship between x and y.

## Why This Matters
Individual points show data; the trend line shows the pattern. It's like connecting the dots to see where things are heading.

## Example

```r
ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point() +
  geom_smooth()
```

This adds a curved line with a shaded confidence interval.

## 🎯 Your Task

1. Add `geom_smooth()` after `geom_point()`
2. Observe the trend line appears
3. Notice the gray shaded area (confidence band)

**Expected Output:**
Scatterplot with a curved blue line and gray shading

## ⚠️ Common Mistake

**Wrong:**
Forgetting `+` between layers.

**Fixed:**
```r
geom_point() +
geom_smooth()
```

---

✅ **No Hidden Prerequisites**: Uses `geom_smooth()` from this lesson.
""")

lessons["20062"] = create_reinforcer(2006, 2, "Variation: Straight Line",
"""# 📏 Linear Trend

## What You'll Learn
How to make `geom_smooth()` draw a straight line instead of a curve.

## Why This Matters
Curved lines (loess) are default. For simple linear relationships, use `method = \"lm\"` for a straight regression line.

## Example

```r
ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point() +
  geom_smooth(method = "lm")
```

## 🎯 Your Task

1. Add `method = \"lm\"` to geom_smooth()
2. Compare: curved vs straight line
3. "lm" = linear model

**Expected Output:**
A straight trend line (not curved)

## ⚠️ Common Mistake

**Wrong:**
```r
geom_smooth(method = lm)
```
Missing quotes.

**Fixed:**
```r
geom_smooth(method = "lm")
```

---

✅ **No Hidden Prerequisites**: Uses `geom_smooth()` with an argument.
""")

lessons["20063"] = create_reinforcer(2006, 3, "Fix the Code: Remove Shading",
"""# 🔧 Fix: Confidence Interval

## What You'll Learn
How to remove the shaded confidence band.

## Why This Matters
Sometimes the gray band is distracting. `se = FALSE` removes it for a cleaner look.

## Example

```r
# With shading (default)
geom_smooth()

# Without shading
geom_smooth(se = FALSE)
```

## 🎯 Your Task

1. The starter code has a noisy shaded band
2. Add `se = FALSE` to remove it
3. Verify the line is clean

**Expected Output:**
Just the trend line, no gray shading

## ⚠️ Common Mistake

**Wrong:**
```r
geom_smooth(se = "FALSE")
```
FALSE is a logical value, not a string.

**Fixed:**
```r
geom_smooth(se = FALSE)
```

---

✅ **No Hidden Prerequisites**: Uses `geom_smooth()` argument.
""")

lessons["20064"] = create_reinforcer(2006, 4, "Challenge: Trend by Group",
"""# 🦸 Challenge: Separate Trends

## What You'll Learn
Apply trend lines per group by adding color.

## Why This Matters
When you color by a variable, `geom_smooth()` automatically creates separate trend lines for each group.

## Example

Pattern:
```r
aes(..., color = group_variable) +
geom_smooth()
```

## 🎯 Your Task

Create a scatterplot with SEPARATE trend lines for each species:
1. Map `color = species` in aes()
2. Add both `geom_point()` AND `geom_smooth()`
3. You should see 3 separate trend lines

**Expected Output:**
Three different colored trend lines (one per species)

## ⚠️ Common Mistake

**Wrong:**
Adding species only to geom_point(), not in main aes().

**Fixed:**
Put `color = species` in the `ggplot(aes(...))` so all layers inherit it.

---

✅ **No Hidden Prerequisites**: Combines color mapping with geom_smooth().
""")

# ===== 2011: Names & Comments =====
lessons["20111"] = create_reinforcer(2011, 1, "Analogy: Labels on Boxes",
"""# 🏷️ Naming Your Variables

## What You'll Learn
Why good variable names make code readable.

## Why This Matters
`x` and `temp` mean nothing. `penguin_mass_kg` tells you exactly what's inside. Future-you will thank present-you.

## Example

```r
# Bad
x <- 4200

# Good
avg_penguin_mass_g <- 4200
```

## 🎯 Your Task

1. Compare the two variable names above
2. Which one would you understand in 6 months?
3. Use snake_case: words_separated_by_underscores

**Expected Output:**
Understanding that descriptive names help readability

## ⚠️ Common Mistake

**Wrong:**
```r
avgPenguinMass  # CamelCase (not R convention)
```

**Fixed:**
```r
avg_penguin_mass  # snake_case (R convention)
```

---

✅ **No Hidden Prerequisites**: Uses basic assignment `<-`.
""")

lessons["20112"] = create_reinforcer(2011, 2, "Variation: Comments",
"""# 💬 Adding Comments

## What You'll Learn
How to add explanatory notes that R ignores.

## Why This Matters
Comments explain WHY, not what. Code shows what; comments explain the reasoning.

## Example

```r
# Convert grams to kilograms
mass_kg <- body_mass_g / 1000
```

The `#` makes R ignore everything after it on that line.

## 🎯 Your Task

1. Add a comment explaining what the code does
2. Use `#` at the start
3. Run to verify R ignores your comment

**Expected Output:**
Code runs successfully; comment is ignored

## ⚠️ Common Mistake

**Wrong:**
```r
// This is a comment
```
R uses `#`, not `//`.

**Fixed:**
```r
# This is a comment
```

---

✅ **No Hidden Prerequisites**: Uses basic R syntax.
""")

lessons["20113"] = create_reinforcer(2011, 3, "Fix the Code: Invalid Name",
"""# 🔧 Fix: Variable Names

## What You'll Learn
Which characters are NOT allowed in variable names.

## Why This Matters
Names can't start with numbers or contain spaces/special characters. This causes errors.

## Example

```r
# Invalid
2nd_value <- 10      # Starts with number
my value <- 10       # Has a space
my-value <- 10       # Has a hyphen

# Valid
second_value <- 10
my_value <- 10
```

## 🎯 Your Task

1. Fix the invalid variable name in the starter code
2. Replace spaces or invalid chars with underscores
3. Verify it runs

**Expected Output:**
No error; variable is created

## ⚠️ Common Mistake

**Wrong:**
```r
1st_penguin <- "Adelie"
```

**Fixed:**
```r
first_penguin <- "Adelie"
```

---

✅ **No Hidden Prerequisites**: Basic R naming rules.
""")

lessons["20114"] = create_reinforcer(2011, 4, "Challenge: Rename for Clarity",
"""# 🦸 Challenge: Better Names

## What You'll Learn
Apply naming best practices to improve code.

## Why This Matters
Readable code is maintainable code.

## Example

Pattern: `what_it_contains_units`

## 🎯 Your Task

Improve these variable names:
1. `x` → a descriptive name
2. `d` → what does it represent?
3. `temp` → be specific

**Expected Output:**
Three variables with clear, descriptive names

## ⚠️ Common Mistake

**Wrong:**
```r
n <- 344  # What is n?
```

**Fixed:**
```r
penguin_count <- 344
```

---

✅ **No Hidden Prerequisites**: Naming conventions only.
""")

# Save
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Part 1 complete: Created reinforcers for 2005, 2006, 2011 (12 reinforcers)")
