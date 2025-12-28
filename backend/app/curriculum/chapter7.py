# Chapter 7: Modules & Packages
# Enhanced with full detailed definitions and explanations

CHAPTER_7 = {
    "id": 9,
    "title": "Modules & Packages",
    "slug": "python-modules",
    "icon": "📦",
    "is_boss": False,
    "lessons": [
        {
            "id": 59,
            "title": "Importing Modules",
            "order": 1,
            "content": """# 📦 Importing Modules

## What is a Module?

A **module** is a file containing Python code (functions, classes, variables) that you can reuse in other programs. Think of it as a toolbox of pre-written code.

## Why Use Modules?

| Benefit | Description |
| --- | --- |
| **Don't reinvent the wheel** | Experts have already written tested code |
| **Organization** | Split large programs into manageable files |
| **Reusability** | Write once, use everywhere |
| **Community** | Access thousands of open-source packages |

## Built-in Modules

Python comes with many useful modules:

```python
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.14159...
print(math.floor(3.7))  # 3
print(math.ceil(3.2))   # 4
```

## How Import Works

When you write `import math`:
1. Python finds the module file
2. Runs the code once
3. Creates a namespace `math` with all its contents
4. You access items with `math.something`

---

## 🎯 Your Task

Import the `math` module and print the square root of `25`.
""",
            "starter_code": "# Import math\n\n\n# Print sqrt of 25\n",
            "solution_code": "# Import math\nimport math\n\n# Print sqrt of 25\nprint(math.sqrt(25))",
            "expected_output": "5.0",
            "xp": 10
        },
        {
            "id": 60,
            "title": "From Import",
            "order": 2,
            "content": """# 🎯 Specific Imports

## Import Only What You Need

Instead of importing the entire module, import specific items:

```python
from math import pi, sqrt

# Now use directly - no math. prefix needed!
print(pi)       # 3.14159...
print(sqrt(16)) # 4.0
```

## Comparison

| Style | Syntax | Usage |
| --- | --- | --- |
| Full import | `import math` | `math.sqrt(16)` |
| Specific import | `from math import sqrt` | `sqrt(16)` |

## Import All (Use Carefully!)

```python
from math import *  # Imports EVERYTHING
```

⚠️ **Warning**: This can cause naming conflicts if two modules have functions with the same name!

## Best Practices

```python
# Good - explicit about what you're using
from math import pi, sqrt, floor

# Good - clear namespace
import math

# Risky - unclear what's available
from math import *
```

---

## 🎯 Your Task

From the `math` module, import `pi` and print it rounded to 2 decimal places.
""",
            "starter_code": "# Import pi from math\n\n\n# Print rounded to 2 decimals\n",
            "solution_code": "# Import pi from math\nfrom math import pi\n\n# Print rounded to 2 decimals\nprint(round(pi, 2))",
            "expected_output": "3.14",
            "xp": 10
        },
        {
            "id": 61,
            "title": "Random Module",
            "order": 3,
            "content": """# 🎲 Random Numbers

## The random Module

Generate random values for games, simulations, testing, and more!

```python
import random

random.randint(1, 10)           # Random integer 1-10 (inclusive)
random.random()                  # Random float 0.0 to 1.0
random.choice(['a', 'b', 'c'])  # Random pick from list
random.shuffle(my_list)          # Shuffle list in place
random.sample(my_list, 3)        # Pick 3 random items
```

## Real-World Uses

- Games: dice rolls, card dealing, enemy spawns
- Testing: generating test data
- Statistics: sampling data
- Security: generating tokens (use `secrets` module for true security)

## Reproducibility with Seeds

For testing, you often need the same "random" results:

```python
random.seed(42)  # Set the seed
print(random.randint(1, 100))  # Always 82 with seed 42!
print(random.randint(1, 100))  # Always 35 with seed 42!
```

Resetting the seed gives the same sequence every time.

---

## 🎯 Your Task

Set `random.seed(42)`, then generate and print a random integer between 1 and 100 (inclusive).
""",
            "starter_code": "import random\n\n# Set seed for consistency\nrandom.seed(42)\n\n# Print random 1-100\n",
            "solution_code": "import random\n\n# Set seed for consistency\nrandom.seed(42)\n\n# Print random 1-100\nprint(random.randint(1, 100))",
            "expected_output": "82",
            "xp": 10
        },
        {
            "id": 62,
            "title": "Datetime Module",
            "order": 4,
            "content": """# 📅 Working with Dates and Times

## The datetime Module

Handle dates, times, and durations:

```python
from datetime import date, datetime, timedelta

# Current date/time
today = date.today()      # 2024-01-15
now = datetime.now()      # 2024-01-15 14:30:00

# Create specific dates
birthday = date(1995, 6, 15)
meeting = datetime(2024, 12, 25, 10, 30)
```

## Date Formatting

Convert dates to custom string formats:

```python
now = datetime.now()
now.strftime("%Y-%m-%d")     # "2024-01-15"
now.strftime("%B %d, %Y")    # "January 15, 2024"
now.strftime("%H:%M:%S")     # "14:30:00"
```

## Date Arithmetic

Add or subtract time using `timedelta`:

```python
from datetime import timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
```

---

## 🎯 Your Task

Create a date object for January 1, 2024 using `date(2024, 1, 1)` and print it.
""",
            "starter_code": "from datetime import date\n\n# Create Jan 1, 2024\n\n\n# Print it\n",
            "solution_code": "from datetime import date\n\n# Create Jan 1, 2024\nnew_year = date(2024, 1, 1)\n\n# Print it\nprint(new_year)",
            "expected_output": "2024-01-01",
            "xp": 10
        },
        {
            "id": 63,
            "title": "Collections Module",
            "order": 5,
            "content": """# 📊 Counter from Collections

## The Counter Class

`Counter` is a specialized dictionary for counting things:

```python
from collections import Counter

# Count items in a list
colors = ['red', 'blue', 'red', 'green', 'blue', 'red']
counts = Counter(colors)
print(counts)  # Counter({'red': 3, 'blue': 2, 'green': 1})

# Count characters in a string
letter_counts = Counter("mississippi")
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```

## Useful Counter Methods

```python
counts.most_common(2)      # [('red', 3), ('blue', 2)]
counts['red']              # 3
counts['purple']           # 0 (no KeyError!)
counts.total()             # Sum of all counts
```

## Why Use Counter?

- Count word frequencies in text
- Find most common items
- Tally votes or scores
- Analyze data distributions

---

## 🎯 Your Task

Count the letters in the word `"hello"` using Counter and print the result.
""",
            "starter_code": "from collections import Counter\n\nword = \"hello\"\n\n# Count and print\n",
            "solution_code": "from collections import Counter\n\nword = \"hello\"\n\n# Count and print\ncounts = Counter(word)\nprint(counts)",
            "expected_output": "Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})",
            "xp": 10
        },
        {
            "id": 64,
            "title": "Aliases",
            "order": 6,
            "content": """# 🏷️ Import Aliases

## Shortening Module Names

Some modules have long names. Use `as` to create shorter aliases:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

## Why Use Aliases?

1. **Less typing**: `np.array()` vs `numpy.array()`
2. **Industry standard**: Everyone uses these conventions
3. **Code readability**: Familiar patterns

## Common Conventions

| Module | Standard Alias |
| --- | --- |
| numpy | np |
| pandas | pd |
| matplotlib.pyplot | plt |
| seaborn | sns |
| tensorflow | tf |

## Creating Your Own Aliases

```python
import statistics as stats
print(stats.mean([1, 2, 3, 4, 5]))

import math as m
print(m.sqrt(16))  # 4.0
```

---

## 🎯 Your Task

Import `math` with the alias `m` and print `m.floor(7.8)`.
""",
            "starter_code": "# Import math as m\n\n\n# Print floor of 7.8\n",
            "solution_code": "# Import math as m\nimport math as m\n\n# Print floor of 7.8\nprint(m.floor(7.8))",
            "expected_output": "7",
            "xp": 10
        },
        {
            "id": 65,
            "title": "OS Path",
            "order": 7,
            "content": """# 📂 OS Path Operations

## Working with File Paths

The `os` module helps work with file paths in a **cross-platform** way:

```python
import os

# Join paths (works on Windows AND Mac/Linux)
path = os.path.join("folder", "subfolder", "file.txt")
# Windows: folder\\subfolder\\file.txt
# Mac/Linux: folder/subfolder/file.txt
```

## Common Path Operations

```python
import os

# Check if exists
os.path.exists("file.txt")     # True/False

# Get parts of a path
os.path.dirname("/a/b/c.txt")  # "/a/b"
os.path.basename("/a/b/c.txt") # "c.txt"
os.path.splitext("data.csv")   # ("data", ".csv")

# Get current directory
os.getcwd()

# List files in directory
os.listdir(".")
```

## Why Use os.path?

Never hardcode paths like `"folder/file.txt"` because:
- Windows uses `\\`, Mac/Linux use `/`
- `os.path.join()` handles this automatically!

---

## 🎯 Your Task

Use `os.path.join()` to combine `"data"` and `"report.csv"` into a path, then print it.
""",
            "starter_code": "import os\n\n# Join path parts\n\n\n# Print path\n",
            "solution_code": "import os\n\n# Join path parts\npath = os.path.join(\"data\", \"report.csv\")\n\n# Print path\nprint(path)",
            "expected_output": "data/report.csv",
            "xp": 10
        },
        {
            "id": 66,
            "title": "Itertools",
            "order": 8,
            "content": """# 🔄 Itertools Module

## Powerful Iteration Tools

The `itertools` module provides advanced iteration utilities:

```python
from itertools import combinations, permutations, product

# Combinations: order doesn't matter
list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]

# Permutations: order matters
list(permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Product: all combinations of multiple lists
list(product(['A', 'B'], [1, 2]))
# [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
```

## Other Useful Functions

```python
from itertools import cycle, count, chain

# Infinite repeating
colors = cycle(['red', 'green', 'blue'])
next(colors)  # 'red', 'green', 'blue', 'red'...

# Chain multiple iterables
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]
```

---

## 🎯 Your Task

Get all combinations of 2 items from the list `["A", "B", "C"]` and print the result.
""",
            "starter_code": "from itertools import combinations\n\nletters = [\"A\", \"B\", \"C\"]\n\n# Get pairs and print\n",
            "solution_code": "from itertools import combinations\n\nletters = [\"A\", \"B\", \"C\"]\n\n# Get pairs and print\npairs = list(combinations(letters, 2))\nprint(pairs)",
            "expected_output": "[('A', 'B'), ('A', 'C'), ('B', 'C')]",
            "xp": 10
        },
        {
            "id": 67,
            "title": "Functools",
            "order": 9,
            "content": """# ⚙️ Functools Module

## Functions That Work with Functions

`functools` provides higher-order functions - functions that work on other functions.

## The reduce Function

Applies a function cumulatively to reduce a list to a single value:

```python
from functools import reduce

# Sum all numbers: ((1+2)+3)+4 = 10
result = reduce(lambda x, y: x + y, [1, 2, 3, 4])

# Find maximum
max_val = reduce(lambda x, y: x if x > y else y, [3, 1, 4, 1, 5])
# Result: 5
```

## How reduce Works Step by Step

```python
reduce(lambda x, y: x * y, [2, 3, 4, 5])
# Step 1: 2 * 3 = 6
# Step 2: 6 * 4 = 24
# Step 3: 24 * 5 = 120
```

## Other Useful Functions

```python
from functools import partial

# Create a specialized function
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(5))  # 25
print(cube(5))    # 125
```

---

## 🎯 Your Task

Use `reduce` with a lambda to multiply all numbers in `[2, 3, 4]` together. Print the result (should be 24).
""",
            "starter_code": "from functools import reduce\n\nnumbers = [2, 3, 4]\n\n# Multiply all and print\n",
            "solution_code": "from functools import reduce\n\nnumbers = [2, 3, 4]\n\n# Multiply all and print\nresult = reduce(lambda x, y: x * y, numbers)\nprint(result)",
            "expected_output": "24",
            "xp": 10
        }
    ]
}
