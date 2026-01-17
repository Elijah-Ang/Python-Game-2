"""
Batch R-1 Reinforcer Rewrite Script
Updates lessons.json with properly aligned reinforcers.
"""

import json

# Load lessons
with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

# ============================================
# CONCEPT 2002: The Empty Canvas
# Teaches: ggplot(data = penguins) creates empty canvas
# ============================================

# R1: Analogy - relate ggplot canvas to real-world painting
lessons["20021"] = {
    **lessons["20021"],
    "title": "Analogy: The Artist's Canvas",
    "content": """# 🎨 The Artist's Canvas

## What You'll Learn
How `ggplot()` creates a blank canvas, just like an artist starts with an empty page.

## Why This Matters
Every great painting starts with a blank canvas. In ggplot2, `ggplot(data = ...)` is that blank canvas. Until you add "paint" (geoms), nothing appears—just like a painter who has set up their easel but hasn't made the first brushstroke.

## Example

```r
# This creates a blank gray canvas
ggplot(data = penguins)
```

The result is a gray rectangle. That's not a bug—it's waiting for you to add layers!

## 🎯 Your Task

1. Type `ggplot(data = penguins)` to create your canvas
2. Run the code
3. Observe: You get a gray box (empty canvas ready for painting)

**Expected Output:**
A gray rectangle (the blank canvas)

## ⚠️ Common Mistake

**Wrong:**
```r
ggplot(penguins)  # Missing data = 
```

**Fixed:**
```r
ggplot(data = penguins)
```

---

✅ **No Hidden Prerequisites**: Uses only `ggplot()` and `penguins` from this lesson.
""",
    "starter_code": "# Create an empty canvas using the penguins dataset\n",
    "solution_code": "ggplot(data = penguins)",
    "expected_output": "[Graph: Empty gray canvas]"
}

# R2: Variation - try with different dataset
lessons["20022"] = {
    **lessons["20022"],
    "title": "Variation: Different Dataset",
    "content": """# 🔄 Different Dataset, Same Canvas

## What You'll Learn
The canvas pattern works with ANY dataset, not just penguins.

## Why This Matters
The `ggplot(data = ...)` pattern is universal. Once you learn it for penguins, you can instantly apply it to any dataset: cars, diamonds, your own data.

## Example

```r
# Canvas with penguins
ggplot(data = penguins)

# Canvas with mpg (cars data)
ggplot(data = mpg)
```

Both create the same blank canvas—just connected to different data.

## 🎯 Your Task

1. Type `ggplot(data = mpg)` to create a canvas with car data
2. Run the code
3. Confirm you see the same gray canvas

**Expected Output:**
A gray rectangle (the blank canvas)

## ⚠️ Common Mistake

**Wrong:**
```r
ggplot(data = "mpg")  # Don't put quotes around dataset names
```

**Fixed:**
```r
ggplot(data = mpg)
```

---

✅ **No Hidden Prerequisites**: Uses only `ggplot()` from this lesson; `mpg` is a built-in dataset.
""",
    "starter_code": "# Create a canvas using the mpg (cars) dataset\n",
    "solution_code": "ggplot(data = mpg)",
    "expected_output": "[Graph: Empty gray canvas]"
}

# R3: Fix the Code - fix a broken ggplot call
lessons["20023"] = {
    **lessons["20023"],
    "title": "Fix the Code: Missing Data",
    "content": """# 🔧 Fix the Code

## What You'll Learn
How to spot and fix the most common `ggplot()` error: forgetting `data =`.

## Why This Matters
R is picky about syntax. Writing `ggplot(penguins)` might work, but `ggplot(data = penguins)` is clearer and matches the documentation. Getting comfortable with these patterns now saves confusion later.

## Example

The code below has an issue. Can you fix it?

```r
# This could be clearer
ggplot(penguins)
```

While this works, the explicit `data =` is best practice.

## 🎯 Your Task

1. Look at the starter code below
2. Add `data = ` before `penguins`
3. Run to confirm you see the blank canvas

**Expected Output:**
A gray rectangle (the blank canvas)

## ⚠️ Common Mistake

**Wrong:**
```r
ggplot(Penguins)  # Case matters! 'Penguins' ≠ 'penguins'
```

**Fixed:**
```r
ggplot(data = penguins)
```

---

✅ **No Hidden Prerequisites**: Uses only `ggplot()` and `penguins` from this lesson.
""",
    "starter_code": "# Fix this code by adding 'data = '\nggplot(penguins)",
    "solution_code": "ggplot(data = penguins)",
    "expected_output": "[Graph: Empty gray canvas]"
}

# R4: Challenge - create canvas on your own
lessons["20024"] = {
    **lessons["20024"],
    "title": "Challenge: Your Own Canvas",
    "content": """# 🦸 Challenge: Your Own Canvas

## What You'll Learn
Create a ggplot canvas from memory, without hints.

## Why This Matters
Typing the pattern yourself builds muscle memory. You'll write `ggplot(data = ...)` thousands of times in your R career—start practicing now!

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
ggplot(data = diamond)  # Typo: 'diamond' not 'diamonds'
```

**Fixed:**
```r
ggplot(data = diamonds)
```

---

✅ **No Hidden Prerequisites**: Uses only `ggplot()` from this lesson; `diamonds` is a built-in dataset.
""",
    "starter_code": "# Create a blank canvas using the diamonds dataset\n# Hint: ggplot(data = ...)\n",
    "solution_code": "ggplot(data = diamonds)",
    "expected_output": "[Graph: Empty gray canvas]"
}

# Save updated lessons
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("✅ Updated concept 2002 reinforcers (20021-20024)")
