# Chapter 8: Pandas & Data Wrangling
CHAPTER_8 = {
    "id": 9,
    "title": "Pandas & Data Wrangling",
    "slug": "python-pandas",
    "icon": "🐼",
    "is_boss": False,
    "lessons": [
        {
            "id": 67,
            "title": "Creating DataFrames",
            "order": 1,
            "content": """# 🐼 Pandas DataFrames

A DataFrame is a 2D table.

```python
import pandas as pd
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
```

---

## 🎯 Your Task

Create a DataFrame from:
```python
data = {"name": ["Alice", "Bob"], "score": [85, 90]}
```
Print the DataFrame.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\"], \"score\": [85, 90]}\n\n# Create DataFrame\n\n\n# Print it\n",
            "solution_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\"], \"score\": [85, 90]}\n\n# Create DataFrame\ndf = pd.DataFrame(data)\n\n# Print it\nprint(df)",
            "expected_output": "    name  score\n0  Alice     85\n1    Bob     90",
            "xp": 10
        },
        {
            "id": 68,
            "title": "Selecting Columns",
            "order": 2,
            "content": """# 📊 Selecting Columns

```python
df["column_name"]  # Returns a Series
df[["col1", "col2"]]  # Returns DataFrame
```

---

## 🎯 Your Task

Given:
```python
data = {"name": ["Alice", "Bob"], "age": [25, 30], "city": ["NYC", "LA"]}
df = pd.DataFrame(data)
```
Print only the "name" column.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\"], \"age\": [25, 30], \"city\": [\"NYC\", \"LA\"]}\ndf = pd.DataFrame(data)\n\n# Print name column\n",
            "solution_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\"], \"age\": [25, 30], \"city\": [\"NYC\", \"LA\"]}\ndf = pd.DataFrame(data)\n\n# Print name column\nprint(df[\"name\"])",
            "expected_output": "0    Alice\n1      Bob\nName: name, dtype: object",
            "xp": 10
        },
        {
            "id": 69,
            "title": "Filtering Rows",
            "order": 3,
            "content": """# 🔍 Filtering Data

```python
df[df["age"] > 25]  # Rows where age > 25
```

---

## 🎯 Your Task

Given:
```python
data = {"name": ["Alice", "Bob", "Charlie"], "score": [85, 70, 95]}
df = pd.DataFrame(data)
```
Print rows where score > 80.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\", \"Charlie\"], \"score\": [85, 70, 95]}\ndf = pd.DataFrame(data)\n\n# Filter score > 80\n",
            "solution_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\", \"Charlie\"], \"score\": [85, 70, 95]}\ndf = pd.DataFrame(data)\n\n# Filter score > 80\nprint(df[df[\"score\"] > 80])",
            "expected_output": "      name  score\n0    Alice     85\n2  Charlie     95",
            "xp": 10
        },
        {
            "id": 70,
            "title": "Basic Statistics",
            "order": 4,
            "content": """# 📈 Statistics

```python
df["column"].mean()
df["column"].sum()
df.describe()
```

---

## 🎯 Your Task

Given:
```python
data = {"value": [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)
```
Print the mean of "value".
""",
            "starter_code": "import pandas as pd\n\ndata = {\"value\": [10, 20, 30, 40, 50]}\ndf = pd.DataFrame(data)\n\n# Print mean\n",
            "solution_code": "import pandas as pd\n\ndata = {\"value\": [10, 20, 30, 40, 50]}\ndf = pd.DataFrame(data)\n\n# Print mean\nprint(df[\"value\"].mean())",
            "expected_output": "30.0",
            "xp": 10
        },
        {
            "id": 71,
            "title": "Adding Columns",
            "order": 5,
            "content": """# ➕ Adding Columns

```python
df["new_col"] = df["a"] + df["b"]
```

---

## 🎯 Your Task

Given:
```python
data = {"price": [100, 200], "quantity": [2, 3]}
df = pd.DataFrame(data)
```
Add a "total" column (price × quantity). Print df.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"price\": [100, 200], \"quantity\": [2, 3]}\ndf = pd.DataFrame(data)\n\n# Add total column\n\n\n# Print df\n",
            "solution_code": "import pandas as pd\n\ndata = {\"price\": [100, 200], \"quantity\": [2, 3]}\ndf = pd.DataFrame(data)\n\n# Add total column\ndf[\"total\"] = df[\"price\"] * df[\"quantity\"]\n\n# Print df\nprint(df)",
            "expected_output": "   price  quantity  total\n0    100         2    200\n1    200         3    600",
            "xp": 10
        },
        {
            "id": 72,
            "title": "GroupBy",
            "order": 6,
            "content": """# 📊 Grouping Data

```python
df.groupby("column").sum()
```

---

## 🎯 Your Task

Given:
```python
data = {"category": ["A", "B", "A"], "value": [10, 20, 30]}
df = pd.DataFrame(data)
```
Group by category and print the sum.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"category\": [\"A\", \"B\", \"A\"], \"value\": [10, 20, 30]}\ndf = pd.DataFrame(data)\n\n# Group and sum\n",
            "solution_code": "import pandas as pd\n\ndata = {\"category\": [\"A\", \"B\", \"A\"], \"value\": [10, 20, 30]}\ndf = pd.DataFrame(data)\n\n# Group and sum\nprint(df.groupby(\"category\").sum())",
            "expected_output": "          value\ncategory       \nA            40\nB            20",
            "xp": 10
        },
        {
            "id": 73,
            "title": "Sorting",
            "order": 7,
            "content": """# 🔄 Sorting Data

```python
df.sort_values("column", ascending=False)
```

---

## 🎯 Your Task

Given:
```python
data = {"name": ["Alice", "Bob", "Charlie"], "score": [85, 95, 70]}
df = pd.DataFrame(data)
```
Sort by score descending and print.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\", \"Charlie\"], \"score\": [85, 95, 70]}\ndf = pd.DataFrame(data)\n\n# Sort by score descending\n",
            "solution_code": "import pandas as pd\n\ndata = {\"name\": [\"Alice\", \"Bob\", \"Charlie\"], \"score\": [85, 95, 70]}\ndf = pd.DataFrame(data)\n\n# Sort by score descending\nprint(df.sort_values(\"score\", ascending=False))",
            "expected_output": "      name  score\n1      Bob     95\n0    Alice     85\n2  Charlie     70",
            "xp": 10
        },
        {
            "id": 74,
            "title": "Handling Missing Data",
            "order": 8,
            "content": """# ❓ Missing Values

```python
df.dropna()     # Remove rows with NaN
df.fillna(0)    # Replace NaN with 0
```

---

## 🎯 Your Task

Given:
```python
import numpy as np
data = {"value": [1, np.nan, 3]}
df = pd.DataFrame(data)
```
Fill NaN with 0 and print.
""",
            "starter_code": "import pandas as pd\nimport numpy as np\n\ndata = {\"value\": [1, np.nan, 3]}\ndf = pd.DataFrame(data)\n\n# Fill NaN with 0\n",
            "solution_code": "import pandas as pd\nimport numpy as np\n\ndata = {\"value\": [1, np.nan, 3]}\ndf = pd.DataFrame(data)\n\n# Fill NaN with 0\nprint(df.fillna(0))",
            "expected_output": "   value\n0    1.0\n1    0.0\n2    3.0",
            "xp": 10
        },
        {
            "id": 75,
            "title": "Value Counts",
            "order": 9,
            "content": """# 📊 Counting Values

```python
df["column"].value_counts()
```

---

## 🎯 Your Task

Given:
```python
data = {"color": ["red", "blue", "red", "green", "blue", "red"]}
df = pd.DataFrame(data)
```
Count each color and print.
""",
            "starter_code": "import pandas as pd\n\ndata = {\"color\": [\"red\", \"blue\", \"red\", \"green\", \"blue\", \"red\"]}\ndf = pd.DataFrame(data)\n\n# Count colors\n",
            "solution_code": "import pandas as pd\n\ndata = {\"color\": [\"red\", \"blue\", \"red\", \"green\", \"blue\", \"red\"]}\ndf = pd.DataFrame(data)\n\n# Count colors\nprint(df[\"color\"].value_counts())",
            "expected_output": "color\nred      3\nblue     2\ngreen    1\nName: count, dtype: int64",
            "xp": 10
        }
    ]
}
