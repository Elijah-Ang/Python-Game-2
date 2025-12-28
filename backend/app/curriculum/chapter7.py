# Chapter 7: Modules
CHAPTER_7 = {
    "id": 8,
    "title": "Modules & Packages",
    "slug": "python-modules",
    "icon": "📦",
    "is_boss": False,
    "lessons": [
        {
            "id": 58,
            "title": "Importing Modules",
            "order": 1,
            "content": """# 📦 Importing Modules

```python
import math
print(math.sqrt(16))  # 4.0
```

---

## 🎯 Your Task

Import `math` and print the square root of `25`.
""",
            "starter_code": "# Import math\n\n\n# Print sqrt of 25\n",
            "solution_code": "# Import math\nimport math\n\n# Print sqrt of 25\nprint(math.sqrt(25))",
            "expected_output": "5.0",
            "xp": 10
        },
        {
            "id": 59,
            "title": "From Import",
            "order": 2,
            "content": """# 🎯 Specific Imports

```python
from math import pi
print(pi)  # 3.14159...
```

---

## 🎯 Your Task

From `math`, import `pi` and print it rounded to 2 decimal places.
""",
            "starter_code": "# Import pi from math\n\n\n# Print rounded to 2 decimals\n",
            "solution_code": "# Import pi from math\nfrom math import pi\n\n# Print rounded to 2 decimals\nprint(round(pi, 2))",
            "expected_output": "3.14",
            "xp": 10
        },
        {
            "id": 60,
            "title": "Random Module",
            "order": 3,
            "content": """# 🎲 Random Numbers

```python
import random
random.randint(1, 10)  # Random 1-10
```

Note: For consistent output, we use `random.seed()`.

---

## 🎯 Your Task

Set `random.seed(42)`, then generate and print a random number 1-100.
""",
            "starter_code": "import random\n\n# Set seed for consistency\nrandom.seed(42)\n\n# Print random 1-100\n",
            "solution_code": "import random\n\n# Set seed for consistency\nrandom.seed(42)\n\n# Print random 1-100\nprint(random.randint(1, 100))",
            "expected_output": "82",
            "xp": 10
        },
        {
            "id": 61,
            "title": "Datetime Module",
            "order": 4,
            "content": """# 📅 Working with Dates

```python
from datetime import date
today = date.today()
```

---

## 🎯 Your Task

Create a date for January 1, 2024 and print it.
Use `date(2024, 1, 1)`.
""",
            "starter_code": "from datetime import date\n\n# Create Jan 1, 2024\n\n\n# Print it\n",
            "solution_code": "from datetime import date\n\n# Create Jan 1, 2024\nnew_year = date(2024, 1, 1)\n\n# Print it\nprint(new_year)",
            "expected_output": "2024-01-01",
            "xp": 10
        },
        {
            "id": 62,
            "title": "Collections Module",
            "order": 5,
            "content": """# 📊 Counter

```python
from collections import Counter
Counter(['a', 'b', 'a'])  # {'a': 2, 'b': 1}
```

---

## 🎯 Your Task

Count letters in `"hello"` using Counter.
Print the result.
""",
            "starter_code": "from collections import Counter\n\nword = \"hello\"\n\n# Count and print\n",
            "solution_code": "from collections import Counter\n\nword = \"hello\"\n\n# Count and print\ncounts = Counter(word)\nprint(counts)",
            "expected_output": "Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})",
            "xp": 10
        },
        {
            "id": 63,
            "title": "Aliases",
            "order": 6,
            "content": """# 🏷️ Import Aliases

```python
import numpy as np
import pandas as pd
```

---

## 🎯 Your Task

Import `math` as `m` and print `m.floor(7.8)`.
""",
            "starter_code": "# Import math as m\n\n\n# Print floor of 7.8\n",
            "solution_code": "# Import math as m\nimport math as m\n\n# Print floor of 7.8\nprint(m.floor(7.8))",
            "expected_output": "7",
            "xp": 10
        },
        {
            "id": 64,
            "title": "OS Path",
            "order": 7,
            "content": """# 📂 OS Path Operations

```python
import os
os.path.join("folder", "file.txt")
```

---

## 🎯 Your Task

Join `"data"` and `"report.csv"` into a path.
Print the result.
""",
            "starter_code": "import os\n\n# Join path parts\n\n\n# Print path\n",
            "solution_code": "import os\n\n# Join path parts\npath = os.path.join(\"data\", \"report.csv\")\n\n# Print path\nprint(path)",
            "expected_output": "data/report.csv",
            "xp": 10
        },
        {
            "id": 65,
            "title": "Itertools",
            "order": 8,
            "content": """# 🔄 Itertools

```python
from itertools import combinations
list(combinations([1,2,3], 2))
```

---

## 🎯 Your Task

Get all pairs (combinations of 2) from `["A", "B", "C"]`.
Print the list of pairs.
""",
            "starter_code": "from itertools import combinations\n\nletters = [\"A\", \"B\", \"C\"]\n\n# Get pairs and print\n",
            "solution_code": "from itertools import combinations\n\nletters = [\"A\", \"B\", \"C\"]\n\n# Get pairs and print\npairs = list(combinations(letters, 2))\nprint(pairs)",
            "expected_output": "[('A', 'B'), ('A', 'C'), ('B', 'C')]",
            "xp": 10
        },
        {
            "id": 66,
            "title": "Functools",
            "order": 9,
            "content": """# ⚙️ Functools

```python
from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3])  # 6
```

---

## 🎯 Your Task

Use `reduce` to multiply all numbers in `[2, 3, 4]`.
Print the result (should be 24).
""",
            "starter_code": "from functools import reduce\n\nnumbers = [2, 3, 4]\n\n# Multiply all and print\n",
            "solution_code": "from functools import reduce\n\nnumbers = [2, 3, 4]\n\n# Multiply all and print\nresult = reduce(lambda x, y: x * y, numbers)\nprint(result)",
            "expected_output": "24",
            "xp": 10
        }
    ]
}
