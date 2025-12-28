# Chapter 11: Statistics
CHAPTER_11 = {
    "id": 12,
    "title": "Statistics",
    "slug": "python-statistics",
    "icon": "📉",
    "is_boss": False,
    "lessons": [
        {
            "id": 94,
            "title": "Mean (Average)",
            "order": 1,
            "content": """# 📊 Mean (Average)

The mean is the sum divided by count:

```python
mean = sum(data) / len(data)
```

---

## 🎯 Your Task

Calculate the mean of `[10, 20, 30, 40, 50]`.
Print the result.
""",
            "starter_code": "data = [10, 20, 30, 40, 50]\n\n# Calculate mean\n",
            "solution_code": "data = [10, 20, 30, 40, 50]\n\n# Calculate mean\nmean = sum(data) / len(data)\nprint(mean)",
            "expected_output": "30.0",
            "xp": 10
        },
        {
            "id": 95,
            "title": "Median",
            "order": 2,
            "content": """# 📊 Median

The middle value when sorted:

```python
sorted_data = sorted(data)
n = len(data)
median = sorted_data[n // 2]
```

---

## 🎯 Your Task

Find the median of `[3, 1, 4, 1, 5]`.
Print the result.
""",
            "starter_code": "data = [3, 1, 4, 1, 5]\n\n# Sort and find median\n",
            "solution_code": "data = [3, 1, 4, 1, 5]\n\n# Sort and find median\nsorted_data = sorted(data)\nn = len(data)\nmedian = sorted_data[n // 2]\nprint(median)",
            "expected_output": "3",
            "xp": 10
        },
        {
            "id": 96,
            "title": "Mode",
            "order": 3,
            "content": """# 📊 Mode

Most frequent value:

```python
from collections import Counter
counts = Counter(data)
mode = counts.most_common(1)[0][0]
```

---

## 🎯 Your Task

Find the mode of `[1, 2, 2, 3, 3, 3, 4]`.
Print the result.
""",
            "starter_code": "from collections import Counter\n\ndata = [1, 2, 2, 3, 3, 3, 4]\n\n# Find mode\n",
            "solution_code": "from collections import Counter\n\ndata = [1, 2, 2, 3, 3, 3, 4]\n\n# Find mode\ncounts = Counter(data)\nmode = counts.most_common(1)[0][0]\nprint(mode)",
            "expected_output": "3",
            "xp": 10
        },
        {
            "id": 97,
            "title": "Range",
            "order": 4,
            "content": """# 📏 Range

Difference between max and min:

```python
data_range = max(data) - min(data)
```

---

## 🎯 Your Task

Calculate the range of `[5, 10, 15, 20, 25]`.
Print the result.
""",
            "starter_code": "data = [5, 10, 15, 20, 25]\n\n# Calculate range\n",
            "solution_code": "data = [5, 10, 15, 20, 25]\n\n# Calculate range\ndata_range = max(data) - min(data)\nprint(data_range)",
            "expected_output": "20",
            "xp": 10
        },
        {
            "id": 98,
            "title": "Variance",
            "order": 5,
            "content": """# 📊 Variance

Average of squared differences from mean:

```python
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
```

---

## 🎯 Your Task

Calculate variance of `[2, 4, 4, 4, 5, 5, 7, 9]`.
Print rounded to 2 decimals.
""",
            "starter_code": "data = [2, 4, 4, 4, 5, 5, 7, 9]\n\n# Calculate variance\n",
            "solution_code": "data = [2, 4, 4, 4, 5, 5, 7, 9]\n\n# Calculate variance\nmean = sum(data) / len(data)\nvariance = sum((x - mean) ** 2 for x in data) / len(data)\nprint(round(variance, 2))",
            "expected_output": "4.0",
            "xp": 10
        },
        {
            "id": 99,
            "title": "Standard Deviation",
            "order": 6,
            "content": """# 📊 Standard Deviation

Square root of variance:

```python
import math
std_dev = math.sqrt(variance)
```

---

## 🎯 Your Task

Calculate std dev of `[2, 4, 4, 4, 5, 5, 7, 9]`.
Print rounded to 2 decimals.
""",
            "starter_code": "import math\n\ndata = [2, 4, 4, 4, 5, 5, 7, 9]\n\n# Calculate std dev\n",
            "solution_code": "import math\n\ndata = [2, 4, 4, 4, 5, 5, 7, 9]\n\n# Calculate std dev\nmean = sum(data) / len(data)\nvariance = sum((x - mean) ** 2 for x in data) / len(data)\nstd_dev = math.sqrt(variance)\nprint(round(std_dev, 2))",
            "expected_output": "2.0",
            "xp": 10
        },
        {
            "id": 100,
            "title": "Percentiles",
            "order": 7,
            "content": """# 📊 Percentiles

Position in sorted data:

```python
import numpy as np
np.percentile(data, 50)  # 50th percentile = median
```

---

## 🎯 Your Task

Find the 75th percentile of `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.
Print the result.
""",
            "starter_code": "import numpy as np\n\ndata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n\n# Find 75th percentile\n",
            "solution_code": "import numpy as np\n\ndata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n\n# Find 75th percentile\nresult = np.percentile(data, 75)\nprint(result)",
            "expected_output": "7.75",
            "xp": 10
        },
        {
            "id": 101,
            "title": "Correlation",
            "order": 8,
            "content": """# 📊 Correlation

Relationship between two variables:

```python
import numpy as np
np.corrcoef(x, y)[0, 1]
```

---

## 🎯 Your Task

Find correlation between:
- x: `[1, 2, 3, 4, 5]`
- y: `[2, 4, 6, 8, 10]` (perfect positive)

Print rounded to 1 decimal.
""",
            "starter_code": "import numpy as np\n\nx = [1, 2, 3, 4, 5]\ny = [2, 4, 6, 8, 10]\n\n# Calculate correlation\n",
            "solution_code": "import numpy as np\n\nx = [1, 2, 3, 4, 5]\ny = [2, 4, 6, 8, 10]\n\n# Calculate correlation\ncorr = np.corrcoef(x, y)[0, 1]\nprint(round(corr, 1))",
            "expected_output": "1.0",
            "xp": 10
        },
        {
            "id": 102,
            "title": "Z-Score",
            "order": 9,
            "content": """# 📊 Z-Score

How many std devs from mean:

```python
z = (value - mean) / std_dev
```

---

## 🎯 Your Task

Given scores `[70, 80, 90]` (mean=80, std=10):
Calculate z-score for 90 and print it.
""",
            "starter_code": "scores = [70, 80, 90]\nvalue = 90\nmean = 80\nstd_dev = 10\n\n# Calculate z-score\n",
            "solution_code": "scores = [70, 80, 90]\nvalue = 90\nmean = 80\nstd_dev = 10\n\n# Calculate z-score\nz = (value - mean) / std_dev\nprint(z)",
            "expected_output": "1.0",
            "xp": 10
        }
    ]
}
