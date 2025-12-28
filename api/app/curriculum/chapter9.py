# Chapter 9: Data Visualization
# Enhanced with full detailed definitions and explanations

CHAPTER_9 = {
    "id": 11,
    "title": "Data Visualization",
    "slug": "python-visualization",
    "icon": "📊",
    "is_boss": False,
    "lessons": [
        {
            "id": 77,
            "title": "Line Plot",
            "order": 1,
            "content": """# 📈 Creating Line Charts

## Why Visualize Data?

Visualizations help us:
- **Understand patterns** at a glance
- **Communicate insights** to others
- **Spot trends, outliers, and anomalies**
- **Tell stories with data**

## Matplotlib: Python's Plotting Library

```python
import matplotlib.pyplot as plt

# Create a simple line plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]  # Squares

plt.plot(x, y)
plt.show()
```

## How plt.plot() Works

1. Create a figure and axes
2. Plot the data points
3. Connect them with lines
4. `plt.show()` displays the result

## When to Use Line Charts

- **Time series data** (stock prices over time)
- **Trends** (website traffic by month)
- **Continuous data** where order matters

---

## 🎯 Your Task

Create a line plot with x values `[0, 1, 2, 3, 4]` and y values `[0, 1, 4, 9, 16]` (squares).
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nx = [0, 1, 2, 3, 4]\ny = [0, 1, 4, 9, 16]\n\n# Create line plot and show\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nx = [0, 1, 2, 3, 4]\ny = [0, 1, 4, 9, 16]\n\n# Create line plot and show\nplt.plot(x, y)\nplt.show()",
            "expected_output": "[Graph: Line plot showing squares 0-16]",
            "xp": 10
        },
        {
            "id": 78,
            "title": "Bar Chart",
            "order": 2,
            "content": """# 📊 Bar Charts

## When to Use Bar Charts

Bar charts are perfect for:
- **Comparing categories** (sales by region)
- **Showing quantities** across groups
- **Discrete, categorical data**

## Creating a Bar Chart

```python
import matplotlib.pyplot as plt

categories = ["Apples", "Oranges", "Bananas"]
values = [25, 40, 30]

plt.bar(categories, values)
plt.show()
```

## Customization Options

```python
# Horizontal bars
plt.barh(categories, values)

# Custom colors
plt.bar(categories, values, color=['red', 'orange', 'yellow'])

# Add border
plt.bar(categories, values, edgecolor='black', linewidth=1)
```

## Bar Chart vs Line Chart

| Bar Chart | Line Chart |
| --- | --- |
| Categorical data | Sequential data |
| Comparing groups | Showing trends |
| No inherent order | Order matters |

---

## 🎯 Your Task

Create a bar chart with categories `["A", "B", "C"]` and values `[25, 40, 30]`.
""",
            "starter_code": "import matplotlib.pyplot as plt\n\ncategories = [\"A\", \"B\", \"C\"]\nvalues = [25, 40, 30]\n\n# Create bar chart\n",
            "solution_code": "import matplotlib.pyplot as plt\n\ncategories = [\"A\", \"B\", \"C\"]\nvalues = [25, 40, 30]\n\n# Create bar chart\nplt.bar(categories, values)\nplt.show()",
            "expected_output": "[Graph: Bar chart with A=25, B=40, C=30]",
            "xp": 10
        },
        {
            "id": 79,
            "title": "Scatter Plot",
            "order": 3,
            "content": """# ⭐ Scatter Plots

## When to Use Scatter Plots

Scatter plots show the **relationship between two variables**:
- Do taller people weigh more?
- Does more advertising lead to more sales?
- Is there a correlation?

## Creating a Scatter Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

plt.scatter(x, y)
plt.show()
```

## Customization

```python
# Size and color
plt.scatter(x, y, s=100, c='red')

# Different sizes per point
sizes = [20, 50, 100, 200, 500]
plt.scatter(x, y, s=sizes)

# Color by a third variable
colors = [1, 2, 3, 4, 5]
plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()  # Add color legend
```

## Reading Scatter Plots

- **Positive correlation**: Points trend up-right
- **Negative correlation**: Points trend down-right
- **No correlation**: Points randomly scattered

---

## 🎯 Your Task

Create a scatter plot with x `[1, 2, 3, 4, 5]` and y `[2, 4, 5, 4, 5]`.
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nx = [1, 2, 3, 4, 5]\ny = [2, 4, 5, 4, 5]\n\n# Create scatter plot\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nx = [1, 2, 3, 4, 5]\ny = [2, 4, 5, 4, 5]\n\n# Create scatter plot\nplt.scatter(x, y)\nplt.show()",
            "expected_output": "[Graph: Scatter plot with 5 points]",
            "xp": 10
        },
        {
            "id": 80,
            "title": "Histogram",
            "order": 4,
            "content": """# 📊 Histograms

## What is a Histogram?

A histogram shows the **distribution** of data - how values are spread across ranges (bins).

## Bar Chart vs Histogram

| Bar Chart | Histogram |
| --- | --- |
| Categorical data | Continuous data |
| Each bar is a category | Each bar is a range |
| Bars have gaps | Bars touch |

## Creating a Histogram

```python
import matplotlib.pyplot as plt

scores = [65, 70, 75, 80, 85, 90, 95, 70, 75, 80]

plt.hist(scores, bins=5)
plt.show()
```

## Bins: Dividing Your Data

The `bins` parameter controls how data is grouped:
- More bins = more detail
- Fewer bins = smoother view

```python
plt.hist(data, bins=10)   # Default
plt.hist(data, bins=20)   # More detail
plt.hist(data, bins=[0, 50, 70, 90, 100])  # Custom edges
```

## Reading Histograms

- **Normal distribution**: Bell curve shape
- **Skewed right**: Tail extends right
- **Skewed left**: Tail extends left
- **Uniform**: All bars similar height

---

## 🎯 Your Task

Create a histogram of exam scores `[65, 70, 75, 80, 85, 90, 95, 70, 75, 80, 85, 80]` with 5 bins.
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nscores = [65, 70, 75, 80, 85, 90, 95, 70, 75, 80, 85, 80]\n\n# Create histogram with 5 bins\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nscores = [65, 70, 75, 80, 85, 90, 95, 70, 75, 80, 85, 80]\n\n# Create histogram with 5 bins\nplt.hist(scores, bins=5)\nplt.show()",
            "expected_output": "[Graph: Histogram of score distribution]",
            "xp": 10
        },
        {
            "id": 81,
            "title": "Pie Chart",
            "order": 5,
            "content": """# 🥧 Pie Charts

## When to Use Pie Charts

Pie charts show **parts of a whole**:
- Market share percentages
- Budget allocation
- Survey response distribution

## Creating a Pie Chart

```python
import matplotlib.pyplot as plt

labels = ["Rent", "Food", "Transport", "Entertainment"]
values = [30, 25, 20, 25]

plt.pie(values, labels=labels)
plt.show()
```

## Customization

```python
# Add percentages
plt.pie(values, labels=labels, autopct='%1.1f%%')

# Explode a slice
explode = [0.1, 0, 0, 0]  # First slice stands out
plt.pie(values, labels=labels, explode=explode)

# Custom colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
plt.pie(values, labels=labels, colors=colors)

# Make it a circle (equal aspect ratio)
plt.axis('equal')
```

## Pie Chart Best Practices

- Use for **5 or fewer categories** (too many is confusing)
- Label clearly
- Start largest slice at 12 o'clock
- Consider bar charts for precise comparisons

---

## 🎯 Your Task

Create a pie chart showing market share with labels `["Apple", "Google", "Microsoft"]` and values `[30, 45, 25]`.
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nlabels = [\"Apple\", \"Google\", \"Microsoft\"]\nvalues = [30, 45, 25]\n\n# Create pie chart\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nlabels = [\"Apple\", \"Google\", \"Microsoft\"]\nvalues = [30, 45, 25]\n\n# Create pie chart\nplt.pie(values, labels=labels)\nplt.show()",
            "expected_output": "[Graph: Pie chart with 3 segments]",
            "xp": 10
        },
        {
            "id": 82,
            "title": "Adding Labels",
            "order": 6,
            "content": """# 🏷️ Chart Labels and Titles

## Professional Charts Need Labels

A chart without labels is like a map without names - useless!

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])

# Add labels and title
plt.title("My Chart Title")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")

plt.show()
```

## More Customization

```python
# Font sizes
plt.title("Title", fontsize=16, fontweight='bold')
plt.xlabel("X Label", fontsize=12)
plt.ylabel("Y Label", fontsize=12)

# Add a grid
plt.grid(True)
plt.grid(True, linestyle='--', alpha=0.7)

# Set axis limits
plt.xlim(0, 10)
plt.ylim(0, 100)

# Add text annotation
plt.text(x, y, "Label here")
```

## Complete Example

```python
plt.plot(days, temps)
plt.title("Daily Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
```

---

## 🎯 Your Task

Plot temperatures `[20, 22, 25, 23, 21]` over days 1-5. Add title "Daily Temperature" and labels "Day" and "Temp (°C)".
""",
            "starter_code": "import matplotlib.pyplot as plt\n\ndays = [1, 2, 3, 4, 5]\ntemps = [20, 22, 25, 23, 21]\n\n# Create plot with labels\n",
            "solution_code": "import matplotlib.pyplot as plt\n\ndays = [1, 2, 3, 4, 5]\ntemps = [20, 22, 25, 23, 21]\n\n# Create plot with labels\nplt.plot(days, temps)\nplt.title(\"Daily Temperature\")\nplt.xlabel(\"Day\")\nplt.ylabel(\"Temp (°C)\")\nplt.show()",
            "expected_output": "[Graph: Line plot with labeled axes]",
            "xp": 10
        },
        {
            "id": 83,
            "title": "Multiple Lines",
            "order": 7,
            "content": """# 📈 Plotting Multiple Series

## Comparing Multiple Datasets

Plot multiple lines to compare trends:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [1, 4, 9, 16]

plt.plot(x, y1, label="Linear")
plt.plot(x, y2, label="Quadratic")
plt.legend()  # Show the legend!
plt.show()
```

## The Legend

The `label` parameter names each line, and `plt.legend()` displays them:

```python
plt.plot(x, y1, label="Sales 2023")
plt.plot(x, y2, label="Sales 2024")
plt.legend()

# Position the legend
plt.legend(loc='upper left')
plt.legend(loc='best')  # Auto-position
```

## Different Line Styles

```python
plt.plot(x, y1, 'b-', label="Solid blue")   # blue, solid
plt.plot(x, y2, 'r--', label="Dashed red")  # red, dashed
plt.plot(x, y3, 'g:', label="Dotted green") # green, dotted
```

---

## 🎯 Your Task

Plot two sales lines for months 1-4. Sales A: `[10, 15, 13, 18]`, Sales B: `[8, 12, 16, 14]`. Add a legend.
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nmonths = [1, 2, 3, 4]\nsales_a = [10, 15, 13, 18]\nsales_b = [8, 12, 16, 14]\n\n# Plot both lines with legend\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nmonths = [1, 2, 3, 4]\nsales_a = [10, 15, 13, 18]\nsales_b = [8, 12, 16, 14]\n\n# Plot both lines with legend\nplt.plot(months, sales_a, label=\"Sales A\")\nplt.plot(months, sales_b, label=\"Sales B\")\nplt.legend()\nplt.show()",
            "expected_output": "[Graph: Two line series with legend]",
            "xp": 10
        },
        {
            "id": 84,
            "title": "Colors and Styles",
            "order": 8,
            "content": """# 🎨 Styling Your Charts

## Color Options

Matplotlib supports many color formats:

```python
# Named colors
plt.plot(x, y, color='red')
plt.plot(x, y, color='skyblue')

# Hex codes
plt.plot(x, y, color='#FF5733')

# RGB tuples (0-1 range)
plt.plot(x, y, color=(0.2, 0.4, 0.6))
```

## Line Styles

| Style | Code |
| --- | --- |
| Solid | `'-'` |
| Dashed | `'--'` |
| Dotted | `':'` |
| Dash-dot | `'-.'` |

## Markers

| Marker | Code |
| --- | --- |
| Circle | `'o'` |
| Square | `'s'` |
| Triangle | `'^'` |
| X | `'x'` |
| Plus | `'+'` |

## Combining Styles

```python
plt.plot(x, y, color='red', linestyle='--', marker='o', 
         linewidth=2, markersize=8)
```

---

## 🎯 Your Task

Create a line plot with red color, dashed line style, and circle markers for x `[1, 2, 3, 4]`, y `[1, 4, 2, 3]`.
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nx = [1, 2, 3, 4]\ny = [1, 4, 2, 3]\n\n# Plot with red, dashed, circles\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nx = [1, 2, 3, 4]\ny = [1, 4, 2, 3]\n\n# Plot with red, dashed, circles\nplt.plot(x, y, color=\"red\", linestyle=\"--\", marker=\"o\")\nplt.show()",
            "expected_output": "[Graph: Red dashed line with circle markers]",
            "xp": 10
        },
        {
            "id": 85,
            "title": "Subplots",
            "order": 9,
            "content": """# 🖼️ Multiple Plots in One Figure

## Why Subplots?

Combine related visualizations for comparison:
- Before/after comparisons
- Different metrics side by side
- Dashboard-style layouts

## Creating Subplots

```python
import matplotlib.pyplot as plt

# Create 1 row, 2 columns of plots
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot([1, 2, 3], [1, 4, 9])
ax1.set_title("Line Plot")

ax2.bar(["A", "B", "C"], [10, 20, 15])
ax2.set_title("Bar Chart")

plt.tight_layout()  # Prevent overlap
plt.show()
```

## Grid Layouts

```python
# 2 rows, 2 columns
fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, y1)    # Top left
axes[0, 1].bar(x, y2)     # Top right
axes[1, 0].scatter(x, y3) # Bottom left
axes[1, 1].hist(data)     # Bottom right
```

## Figure Size

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
```

---

## 🎯 Your Task

Create 2 side-by-side subplots: left with a line plot of `[1, 2, 3]`, right with a bar chart of categories `["A", "B"]` with values `[5, 8]`.
""",
            "starter_code": "import matplotlib.pyplot as plt\n\n# Create 1x2 subplots\n",
            "solution_code": "import matplotlib.pyplot as plt\n\n# Create 1x2 subplots\nfig, (ax1, ax2) = plt.subplots(1, 2)\nax1.plot([1, 2, 3])\nax2.bar([\"A\", \"B\"], [5, 8])\nplt.show()",
            "expected_output": "[Graph: Two subplots side by side]",
            "xp": 10
        }
    ]
}
