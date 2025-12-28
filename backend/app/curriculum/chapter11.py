# Chapter 11: Statistics
# Enhanced with full detailed definitions and explanations

CHAPTER_11 = {
    "id": 13,
    "title": "Statistics",
    "slug": "python-statistics",
    "icon": "📉",
    "is_boss": False,
    "lessons": [
        {
            "id": 95,
            "title": "Mean (Average)",
            "order": 1,
            "content": """# 📊 Mean (Average)

## What is the Mean?

The **mean** (or average) is the sum of all values divided by the count:

$$\\text{mean} = \\frac{\\sum x}{n}$$

In Python:
```python
data = [10, 20, 30, 40, 50]
mean = sum(data) / len(data)  # 30.0
```

## Why Use the Mean?

The mean represents the **"typical" value** in a dataset. It's the most common measure of central tendency.

## Real-World Examples

| Use Case | Example |
| --- | --- |
| Economics | Average income |
| Sports | Player's batting average |
| Weather | Average daily temperature |
| Education | Class grade average |

## ⚠️ Sensitivity to Outliers

The mean can be **skewed by extreme values**:

```python
regular_salaries = [50000, 52000, 48000, 55000]
# Mean: $51,250

with_ceo = [50000, 52000, 48000, 55000, 10000000]
# Mean: $2,041,000 (not representative!)
```

For data with outliers, consider using the **median** instead.

---

## 🎯 Your Task

Calculate the mean of `[10, 20, 30, 40, 50]` and print it.
""",
            "starter_code": "data = [10, 20, 30, 40, 50]\n\n# Calculate mean\n",
            "solution_code": "data = [10, 20, 30, 40, 50]\n\n# Calculate mean\nmean = sum(data) / len(data)\nprint(mean)",
            "expected_output": "30.0",
            "xp": 10
        },
        {
            "id": 96,
            "title": "Median",
            "order": 2,
            "content": """# 📊 Median

## What is the Median?

The **median** is the middle value when data is sorted:

```python
sorted_data = [1, 3, 3, 6, 7, 8, 9]
                      ^
# Median = 6 (the middle one)
```

## For Even-Length Lists

Take the average of the two middle values:

```python
[1, 3, 6, 8]
    ^  ^
# Median = (3 + 6) / 2 = 4.5
```

## Calculating in Python

```python
def median(data):
    sorted_data = sorted(data)
    n = len(data)
    mid = n // 2
    
    if n % 2 == 0:  # Even length
        return (sorted_data[mid-1] + sorted_data[mid]) / 2
    else:           # Odd length
        return sorted_data[mid]
```

## Median vs Mean

| Measure | Affected by Outliers? | Best Use |
| --- | --- | --- |
| Mean | Yes | Symmetric data |
| Median | No | Skewed data |

Example: Median home prices are often reported instead of mean because a few mansions would skew the average.

---

## 🎯 Your Task

Find the median of `[3, 1, 4, 1, 5]` and print it.
""",
            "starter_code": "data = [3, 1, 4, 1, 5]\n\n# Sort and find median\n",
            "solution_code": "data = [3, 1, 4, 1, 5]\n\n# Sort and find median\nsorted_data = sorted(data)\nn = len(data)\nmedian = sorted_data[n // 2]\nprint(median)",
            "expected_output": "3",
            "xp": 10
        },
        {
            "id": 97,
            "title": "Mode",
            "order": 3,
            "content": """# 📊 Mode

## What is the Mode?

The **mode** is the value that appears most frequently:

```python
data = [1, 2, 2, 3, 3, 3, 4]
# Mode = 3 (appears 3 times)
```

## Using Counter

```python
from collections import Counter

data = [1, 2, 2, 3, 3, 3, 4]
counts = Counter(data)
# Counter({3: 3, 2: 2, 1: 1, 4: 1})

mode = counts.most_common(1)[0][0]  # 3
```

## Multiple Modes

Data can have:
- **One mode** (unimodal)
- **Two modes** (bimodal)
- **Many modes** (multimodal)
- **No mode** (all values equally frequent)

## When to Use Mode

- **Categorical data**: Most popular color, most common size
- **Discrete data**: Most frequent score
- **Finding trends**: Most common purchase amount

---

## 🎯 Your Task

Find the mode of `[1, 2, 2, 3, 3, 3, 4]` and print it.
""",
            "starter_code": "from collections import Counter\n\ndata = [1, 2, 2, 3, 3, 3, 4]\n\n# Find mode\n",
            "solution_code": "from collections import Counter\n\ndata = [1, 2, 2, 3, 3, 3, 4]\n\n# Find mode\ncounts = Counter(data)\nmode = counts.most_common(1)[0][0]\nprint(mode)",
            "expected_output": "3",
            "xp": 10
        },
        {
            "id": 98,
            "title": "Range",
            "order": 4,
            "content": """# 📏 Range

## What is the Range?

The **range** is the difference between the maximum and minimum values:

$$\\text{range} = \\max - \\min$$

```python
data = [5, 10, 15, 20, 25]
data_range = max(data) - min(data)  # 25 - 5 = 20
```

## What Range Tells Us

Range measures the **spread** or **dispersion** of data:
- **Small range**: Data is clustered together
- **Large range**: Data is spread out

## Example

| Class A Test Scores | Class B Test Scores |
| --- | --- |
| 70, 72, 75, 78, 80 | 50, 65, 75, 85, 100 |
| Range: 10 | Range: 50 |

Class A has more consistent performance; Class B has more variation.

## Limitations

- Ignores values between min and max
- Very sensitive to outliers
- Only uses 2 data points

For a better measure of spread, use **standard deviation**.

---

## 🎯 Your Task

Calculate the range of `[5, 10, 15, 20, 25]` and print it.
""",
            "starter_code": "data = [5, 10, 15, 20, 25]\n\n# Calculate range\n",
            "solution_code": "data = [5, 10, 15, 20, 25]\n\n# Calculate range\ndata_range = max(data) - min(data)\nprint(data_range)",
            "expected_output": "20",
            "xp": 10
        },
        {
            "id": 99,
            "title": "Variance",
            "order": 5,
            "content": """# 📊 Variance

## What is Variance?

**Variance** measures how spread out the data is from the mean. It's the average of squared differences from the mean:

$$\\text{variance} = \\frac{\\sum (x - \\mu)^2}{n}$$

## Step by Step Calculation

For data `[2, 4, 4, 4, 5, 5, 7, 9]`:

1. **Find the mean**: (2+4+4+4+5+5+7+9) / 8 = 5

2. **Calculate differences from mean**:
   - 2 - 5 = -3
   - 4 - 5 = -1
   - etc.

3. **Square the differences**: (-3)² = 9, (-1)² = 1, etc.

4. **Average the squared differences**: Sum / count

```python
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
```

## Why Square?

- Treats positive and negative differences equally
- Emphasizes larger differences

## Population vs Sample Variance

- **Population** (all data): divide by n
- **Sample** (from a larger population): divide by (n-1)

---

## 🎯 Your Task

Calculate the variance of `[2, 4, 4, 4, 5, 5, 7, 9]` and print it rounded to 2 decimals.
""",
            "starter_code": "data = [2, 4, 4, 4, 5, 5, 7, 9]\n\n# Calculate variance\n",
            "solution_code": "data = [2, 4, 4, 4, 5, 5, 7, 9]\n\n# Calculate variance\nmean = sum(data) / len(data)\nvariance = sum((x - mean) ** 2 for x in data) / len(data)\nprint(round(variance, 2))",
            "expected_output": "4.0",
            "xp": 10
        },
        {
            "id": 100,
            "title": "Standard Deviation",
            "order": 6,
            "content": """# 📊 Standard Deviation

## What is Standard Deviation?

**Standard deviation** is the square root of variance:

$$\\sigma = \\sqrt{\\text{variance}}$$

It's in the **same units as the original data**, making it more interpretable than variance.

## Calculation

```python
import math

data = [2, 4, 4, 4, 5, 5, 7, 9]
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = math.sqrt(variance)
```

## Interpreting Standard Deviation

For normally distributed data:
- **68%** of values are within 1 std dev of mean
- **95%** are within 2 std devs
- **99.7%** are within 3 std devs

## Example

Test scores with mean=75, std_dev=10:
- Most students (68%) score between 65-85
- Nearly all (95%) score between 55-95

## Low vs High Standard Deviation

| Low std dev | High std dev |
| --- | --- |
| Data close to mean | Data spread out |
| Consistent | Variable |

---

## 🎯 Your Task

Calculate the standard deviation of `[2, 4, 4, 4, 5, 5, 7, 9]` and print it rounded to 2 decimals.
""",
            "starter_code": "import math\n\ndata = [2, 4, 4, 4, 5, 5, 7, 9]\n\n# Calculate std dev\n",
            "solution_code": "import math\n\ndata = [2, 4, 4, 4, 5, 5, 7, 9]\n\n# Calculate std dev\nmean = sum(data) / len(data)\nvariance = sum((x - mean) ** 2 for x in data) / len(data)\nstd_dev = math.sqrt(variance)\nprint(round(std_dev, 2))",
            "expected_output": "2.0",
            "xp": 10
        },
        {
            "id": 101,
            "title": "Percentiles",
            "order": 7,
            "content": """# 📊 Percentiles

## What is a Percentile?

A **percentile** indicates the value below which a given percentage of data falls.

- **50th percentile**: 50% of data is below this value (this is the median!)
- **75th percentile (Q3)**: 75% of data is below
- **90th percentile**: "Top 10%" starts here

## Common Percentiles

| Percentile | Name | Meaning |
| --- | --- | --- |
| 25th | Q1 (First quartile) | Bottom quarter |
| 50th | Q2 (Median) | Middle |
| 75th | Q3 (Third quartile) | Top quarter |

## Using NumPy

```python
import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
np.percentile(data, 25)   # First quartile
np.percentile(data, 50)   # Median
np.percentile(data, 75)   # Third quartile
np.percentile(data, 90)   # 90th percentile
```

## Real-World Uses

- Test scores: "You're in the 95th percentile"
- Growth charts: "Baby is in the 75th percentile for weight"
- Performance reviews: "Top 10% of performers"

---

## 🎯 Your Task

Find the 75th percentile of `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and print it.
""",
            "starter_code": "import numpy as np\n\ndata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n\n# Find 75th percentile\n",
            "solution_code": "import numpy as np\n\ndata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n\n# Find 75th percentile\nresult = np.percentile(data, 75)\nprint(result)",
            "expected_output": "7.75",
            "xp": 10
        },
        {
            "id": 102,
            "title": "Correlation",
            "order": 8,
            "content": """# 📊 Correlation

## What is Correlation?

**Correlation** measures the relationship between two variables. The **correlation coefficient (r)** ranges from -1 to +1.

| Value | Meaning |
| --- | --- |
| +1 | Perfect positive correlation |
| 0 | No correlation |
| -1 | Perfect negative correlation |

## Visual Examples

- **Positive**: As X increases, Y increases (e.g., height and weight)
- **Negative**: As X increases, Y decreases (e.g., speed and travel time)
- **None**: No relationship (e.g., shoe size and IQ)

## Using NumPy

```python
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation = np.corrcoef(x, y)[0, 1]
print(correlation)  # 1.0 (perfect positive)
```

## Correlation ≠ Causation!

Just because two variables are correlated doesn't mean one causes the other:
- Ice cream sales and drowning deaths are correlated (both increase in summer)
- But ice cream doesn't cause drowning!

---

## 🎯 Your Task

Find the correlation between x `[1, 2, 3, 4, 5]` and y `[2, 4, 6, 8, 10]`. Print it rounded to 1 decimal.
""",
            "starter_code": "import numpy as np\n\nx = [1, 2, 3, 4, 5]\ny = [2, 4, 6, 8, 10]\n\n# Calculate correlation\n",
            "solution_code": "import numpy as np\n\nx = [1, 2, 3, 4, 5]\ny = [2, 4, 6, 8, 10]\n\n# Calculate correlation\ncorr = np.corrcoef(x, y)[0, 1]\nprint(round(corr, 1))",
            "expected_output": "1.0",
            "xp": 10
        },
        {
            "id": 103,
            "title": "Z-Score",
            "order": 9,
            "content": """# 📊 Z-Score

## What is a Z-Score?

A **Z-score** tells you how many standard deviations a value is from the mean:

$$z = \\frac{x - \\mu}{\\sigma}$$

Where:
- x = the value
- μ = mean
- σ = standard deviation

## Interpreting Z-Scores

| Z-Score | Meaning |
| --- | --- |
| 0 | Exactly at the mean |
| +1 | One std dev above mean |
| +2 | Two std devs above mean (unusual) |
| -1 | One std dev below mean |
| +3 or higher | Very unusual (outlier) |

## Example

Test scores: mean = 75, std = 10

- Score of 85: z = (85-75)/10 = **+1** (above average)
- Score of 65: z = (65-75)/10 = **-1** (below average)
- Score of 95: z = (95-75)/10 = **+2** (exceptional!)

## Why Use Z-Scores?

- Compare values from different distributions
- Identify outliers (z > 3 or z < -3)
- Standardize data for machine learning

---

## 🎯 Your Task

For a distribution with mean=80 and std=10, calculate the z-score for value 90 and print it.
""",
            "starter_code": "scores = [70, 80, 90]\nvalue = 90\nmean = 80\nstd_dev = 10\n\n# Calculate z-score\n",
            "solution_code": "scores = [70, 80, 90]\nvalue = 90\nmean = 80\nstd_dev = 10\n\n# Calculate z-score\nz = (value - mean) / std_dev\nprint(z)",
            "expected_output": "1.0",
            "xp": 10
        }
    ]
}
