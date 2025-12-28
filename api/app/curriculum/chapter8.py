# Chapter 8: Pandas & Data Wrangling
# Enhanced with full detailed definitions and explanations

CHAPTER_8 = {
    "id": 10,
    "title": "Pandas & Data Wrangling",
    "slug": "python-pandas",
    "icon": "🐼",
    "is_boss": False,
    "lessons": [
        {
            "id": 68,
            "title": "Creating DataFrames",
            "order": 1,
            "content": """# 🐼 Pandas DataFrames

## What is Pandas?

**Pandas** is Python's premier library for data analysis. It provides powerful tools for working with tabular data (rows and columns).

## What is a DataFrame?

A **DataFrame** is a 2D table with labeled rows and columns - like a spreadsheet or SQL table.

```python
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["NYC", "LA", "Chicago"]
}

df = pd.DataFrame(data)
print(df)
```

Output:
```
      name  age     city
0    Alice   25      NYC
1      Bob   30       LA
2  Charlie   35  Chicago
```

## Why Pandas?

| Feature | Benefit |
| --- | --- |
| Handles millions of rows | Process big data efficiently |
| Built-in data cleaning | Handle missing values, duplicates |
| Powerful grouping | Aggregate and summarize data |
| File I/O | Read CSV, Excel, JSON, SQL |

---

## 🎯 Your Task

Create a DataFrame from `{"name": ["Alice", "Bob"], "score": [85, 90]}` and print it.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\"], \"score\": [85, 90]}\n\n# Create DataFrame\n\n\n# Print it\n",
            "solution_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\"], \"score\": [85, 90]}\n\n# Create DataFrame\ndf = pd.DataFrame(data)\n\n# Print it\nprint(df)",
            "expected_output": "    name  score\n0  Alice     85\n1    Bob     90",
            "xp": 10
        },
        {
            "id": 69,
            "title": "Selecting Columns",
            "order": 2,
            "content": """# 📊 Selecting Data from DataFrames

## Accessing Columns

There are several ways to select data:

```python
# Single column → returns a Series
df["name"]
df.name  # Dot notation (if column name is valid identifier)

# Multiple columns → returns a DataFrame
df[["name", "age"]]
```

## Accessing Rows

```python
# By position (integer index)
df.iloc[0]       # First row
df.iloc[0:3]     # First 3 rows
df.iloc[-1]      # Last row

# By label
df.loc[0]        # Row with label 0
df.loc[0:2]      # Rows with labels 0 through 2 (inclusive!)

# Handy shortcuts
df.head(3)       # First 3 rows
df.tail(2)       # Last 2 rows
```

## Selecting Both Rows and Columns

```python
# Specific rows and columns
df.loc[0:2, ["name", "age"]]
df.iloc[0:3, 0:2]
```

---

## 🎯 Your Task

Given a DataFrame with name, age, and city columns, print only the "name" column.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\"], \"age\": [25, 30], \"city\": [\"NYC\", \"LA\"]}\ndf = pd.DataFrame(data)\n\n# Print name column\n",
            "solution_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\"], \"age\": [25, 30], \"city\": [\"NYC\", \"LA\"]}\ndf = pd.DataFrame(data)\n\n# Print name column\nprint(df[\"name\"])",
            "expected_output": "0    Alice\n1      Bob\nName: name, dtype: object",
            "xp": 10
        },
        {
            "id": 70,
            "title": "Filtering Rows",
            "order": 3,
            "content": """# 🔍 Filtering Data

## Boolean Indexing

Filter rows based on conditions:

```python
# Rows where age > 25
df[df["age"] > 25]

# Rows where name is "Alice"
df[df["name"] == "Alice"]

# Rows where score is between 80 and 90
df[(df["score"] >= 80) & (df["score"] <= 90)]
```

## Multiple Conditions

Use `&` for AND, `|` for OR (wrap each condition in parentheses):

```python
# AND: both conditions must be true
df[(df["age"] > 25) & (df["city"] == "NYC")]

# OR: at least one must be true
df[(df["age"] > 40) | (df["score"] > 90)]
```

## Filtering with isin()

```python
# Check if value is in a list
df[df["city"].isin(["NYC", "LA"])]
```

## Filtering String Columns

```python
df[df["name"].str.contains("li")]     # Contains "li"
df[df["name"].str.startswith("A")]    # Starts with "A"
```

---

## 🎯 Your Task

Filter rows where score > 80 and print the result.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\", \"Charlie\"], \"score\": [85, 70, 95]}\ndf = pd.DataFrame(data)\n\n# Filter score > 80\n",
            "solution_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\", \"Charlie\"], \"score\": [85, 70, 95]}\ndf = pd.DataFrame(data)\n\n# Filter score > 80\nprint(df[df[\"score\"] > 80])",
            "expected_output": "      name  score\n0    Alice     85\n2  Charlie     95",
            "xp": 10
        },
        {
            "id": 71,
            "title": "Basic Statistics",
            "order": 4,
            "content": """# 📈 Statistics in Pandas

## Quick Column Statistics

Pandas makes statistical analysis easy:

```python
df["column"].mean()     # Average
df["column"].median()   # Middle value
df["column"].sum()      # Total
df["column"].min()      # Minimum
df["column"].max()      # Maximum
df["column"].std()      # Standard deviation
df["column"].count()    # Count non-null values
```

## Get All Stats at Once

```python
df.describe()
```

Returns count, mean, std, min, 25%, 50%, 75%, max for all numeric columns!

## Statistics Across the DataFrame

```python
df.mean()         # Mean of each column
df.sum(axis=1)    # Sum across each row
```

## Value Distribution

```python
df["column"].value_counts()   # Count each unique value
df["column"].unique()         # Get unique values
df["column"].nunique()        # Count unique values
```

---

## 🎯 Your Task

Calculate and print the mean of the "value" column.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"value\": [10, 20, 30, 40, 50]}\ndf = pd.DataFrame(data)\n\n# Print mean\n",
            "solution_code": "import pandas as pd\n\ndata = {\"value\": [10, 20, 30, 40, 50]}\ndf = pd.DataFrame(data)\n\n# Print mean\nprint(df[\"value\"].mean())",
            "expected_output": "30.0",
            "xp": 10
        },
        {
            "id": 72,
            "title": "Adding Columns",
            "order": 5,
            "content": """# ➕ Creating New Columns

## Calculate from Existing Columns

Create new columns based on existing data:

```python
# Simple calculation
df["total"] = df["price"] * df["quantity"]

# Using multiple columns
df["profit"] = df["revenue"] - df["cost"]

# Apply a function
df["age_in_months"] = df["age"] * 12
```

## Transform String Columns

```python
df["name_upper"] = df["name"].str.upper()
df["name_length"] = df["name"].str.len()
df["first_initial"] = df["name"].str[0]
```

## Conditional Columns

```python
# Using apply with lambda
df["status"] = df["score"].apply(lambda x: "Pass" if x >= 70 else "Fail")

# Using numpy where
import numpy as np
df["status"] = np.where(df["score"] >= 70, "Pass", "Fail")
```

## Modify Existing Columns

```python
df["price"] = df["price"] * 1.10  # 10% increase
```

---

## 🎯 Your Task

Add a "total" column that equals price × quantity, then print the DataFrame.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"price\": [100, 200], \"quantity\": [2, 3]}\ndf = pd.DataFrame(data)\n\n# Add total column\n\n\n# Print df\n",
            "solution_code": "import pandas as pd\n\ndata = {\"price\": [100, 200], \"quantity\": [2, 3]}\ndf = pd.DataFrame(data)\n\n# Add total column\ndf[\"total\"] = df[\"price\"] * df[\"quantity\"]\n\n# Print df\nprint(df)",
            "expected_output": "   price  quantity  total\n0    100         2    200\n1    200         3    600",
            "xp": 10
        },
        {
            "id": 73,
            "title": "GroupBy",
            "order": 6,
            "content": """# 📊 Grouping and Aggregating

## The Power of GroupBy

Group data by categories and calculate statistics:

```python
# Group by one column
df.groupby("category").sum()
df.groupby("category")["value"].mean()

# Group by multiple columns
df.groupby(["year", "category"]).count()
```

## How GroupBy Works

1. **Split**: Divide data into groups
2. **Apply**: Calculate statistic for each group
3. **Combine**: Merge results

```python
# Multiple aggregations at once
df.groupby("category").agg({
    "sales": "sum",
    "profit": "mean",
    "orders": "count"
})
```

## Common Use Cases

- Sales by region
- Average score by grade level
- Count of users by country
- Revenue by product category

---

## 🎯 Your Task

Group the data by category and print the sum of values for each category.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"category\": [\"A\", \"B\", \"A\"], \"value\": [10, 20, 30]}\ndf = pd.DataFrame(data)\n\n# Group and sum\n",
            "solution_code": "import pandas as pd\n\ndata = {\"category\": [\"A\", \"B\", \"A\"], \"value\": [10, 20, 30]}\ndf = pd.DataFrame(data)\n\n# Group and sum\nprint(df.groupby(\"category\").sum())",
            "expected_output": "          value\ncategory       \nA            40\nB            20",
            "xp": 10
        },
        {
            "id": 74,
            "title": "Sorting",
            "order": 7,
            "content": """# 🔄 Sorting DataFrames

## Sort by Column

```python
# Ascending (default)
df.sort_values("score")

# Descending
df.sort_values("score", ascending=False)

# Sort by multiple columns
df.sort_values(["grade", "score"], ascending=[True, False])
```

## Sort by Index

```python
df.sort_index()                    # Sort by row labels
df.sort_index(ascending=False)     # Reverse order
```

## Keeping Changes

By default, sorting returns a new DataFrame:

```python
# Returns new DataFrame
sorted_df = df.sort_values("score")

# Modify in place
df.sort_values("score", inplace=True)
```

## Practical Example

```python
# Top 10 highest scores
top_10 = df.sort_values("score", ascending=False).head(10)
```

---

## 🎯 Your Task

Sort the DataFrame by score in descending order and print it.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\", \"Charlie\"], \"score\": [85, 95, 70]}\ndf = pd.DataFrame(data)\n\n# Sort by score descending\n",
            "solution_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\", \"Charlie\"], \"score\": [85, 95, 70]}\ndf = pd.DataFrame(data)\n\n# Sort by score descending\nprint(df.sort_values(\"score\", ascending=False))",
            "expected_output": "      name  score\n1      Bob     95\n0    Alice     85\n2  Charlie     70",
            "xp": 10
        },
        {
            "id": 75,
            "title": "Handling Missing Data",
            "order": 8,
            "content": """# ❓ Handling Missing Values

## Detecting Missing Data

In Pandas, missing values are represented as `NaN` (Not a Number):

```python
import numpy as np

df.isna()           # True where NaN
df.notna()          # True where NOT NaN
df.isna().sum()     # Count NaN per column
df.isna().any()     # Any NaN in each column?
```

## Dealing with Missing Data

```python
# Drop rows with any NaN
df.dropna()

# Drop rows where specific column is NaN
df.dropna(subset=["name"])

# Fill NaN with a value
df.fillna(0)
df.fillna(df.mean())  # Fill with column mean
df.fillna(method="ffill")  # Forward fill
```

## Real-World Approach

Decide based on context:
- **Drop**: If few missing and rows not critical
- **Fill with value**: If you have a sensible default
- **Fill with statistic**: Mean, median, mode for numeric data
- **Keep as-is**: Some algorithms handle NaN

---

## 🎯 Your Task

Fill NaN values with 0 and print the result.
""",
            "starter_code": "import pandas as pd\nimport numpy as np\n\ndata = {\"value\": [1, np.nan, 3]}\ndf = pd.DataFrame(data)\n\n# Fill NaN with 0\n",
            "solution_code": "import pandas as pd\nimport numpy as np\n\ndata = {\"value\": [1, np.nan, 3]}\ndf = pd.DataFrame(data)\n\n# Fill NaN with 0\nprint(df.fillna(0))",
            "expected_output": "   value\n0    1.0\n1    0.0\n2    3.0",
            "xp": 10
        },
        {
            "id": 76,
            "title": "Value Counts",
            "order": 9,
            "content": """# 📊 Counting Unique Values

## value_counts()

See the distribution of values in a column:

```python
df["color"].value_counts()
# red      10
# blue      7
# green     3
```

## Options

```python
# Normalize to get percentages
df["color"].value_counts(normalize=True)
# red      0.50
# blue     0.35
# green    0.15

# Include NaN values
df["color"].value_counts(dropna=False)

# Sort by index instead of count
df["color"].value_counts().sort_index()
```

## Use Cases

- Analyze category distributions
- Find most common values
- Detect class imbalance in ML
- Quality check data

## With groupby

```python
# Count by multiple columns
df.groupby(["year", "category"]).size()
```

---

## 🎯 Your Task

Count how many times each color appears and print the result.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"color\": [\"red\", \"blue\", \"red\", \"green\", \"blue\", \"red\"]}\ndf = pd.DataFrame(data)\n\n# Count colors\n",
            "solution_code": "import pandas as pd\n\ndata = {\"color\": [\"red\", \"blue\", \"red\", \"green\", \"blue\", \"red\"]}\ndf = pd.DataFrame(data)\n\n# Count colors\nprint(df[\"color\"].value_counts())",
            "expected_output": "color\nred      3\nblue     2\ngreen    1\nName: count, dtype: int64",
            "xp": 10
        }
    ]
}
