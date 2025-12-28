# Chapter 9: Visualization
# Note: Matplotlib graphs will be captured and displayed in the output panel

CHAPTER_9 = {
    "id": 10,
    "title": "Data Visualization",
    "slug": "python-visualization",
    "icon": "📊",
    "is_boss": False,
    "lessons": [
        {
            "id": 76,
            "title": "Line Plot",
            "order": 1,
            "content": """# 📈 Line Charts

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

---

## 🎯 Your Task

Create a line plot with:
- x values: `[0, 1, 2, 3, 4]`
- y values: `[0, 1, 4, 9, 16]` (squares)

Call `plt.show()` to display.
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nx = [0, 1, 2, 3, 4]\ny = [0, 1, 4, 9, 16]\n\n# Create line plot and show\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nx = [0, 1, 2, 3, 4]\ny = [0, 1, 4, 9, 16]\n\n# Create line plot and show\nplt.plot(x, y)\nplt.show()",
            "expected_output": "[Graph: Line plot showing squares 0-16]",
            "xp": 10
        },
        {
            "id": 77,
            "title": "Bar Chart",
            "order": 2,
            "content": """# 📊 Bar Charts

```python
plt.bar(categories, values)
```

---

## 🎯 Your Task

Create a bar chart with:
- Categories: `["A", "B", "C"]`
- Values: `[25, 40, 30]`
""",
            "starter_code": "import matplotlib.pyplot as plt\n\ncategories = [\"A\", \"B\", \"C\"]\nvalues = [25, 40, 30]\n\n# Create bar chart\n",
            "solution_code": "import matplotlib.pyplot as plt\n\ncategories = [\"A\", \"B\", \"C\"]\nvalues = [25, 40, 30]\n\n# Create bar chart\nplt.bar(categories, values)\nplt.show()",
            "expected_output": "[Graph: Bar chart with A=25, B=40, C=30]",
            "xp": 10
        },
        {
            "id": 78,
            "title": "Scatter Plot",
            "order": 3,
            "content": """# ⭐ Scatter Plots

```python
plt.scatter(x, y)
```

---

## 🎯 Your Task

Create a scatter plot with:
- x: `[1, 2, 3, 4, 5]`
- y: `[2, 4, 5, 4, 5]`
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nx = [1, 2, 3, 4, 5]\ny = [2, 4, 5, 4, 5]\n\n# Create scatter plot\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nx = [1, 2, 3, 4, 5]\ny = [2, 4, 5, 4, 5]\n\n# Create scatter plot\nplt.scatter(x, y)\nplt.show()",
            "expected_output": "[Graph: Scatter plot with 5 points]",
            "xp": 10
        },
        {
            "id": 79,
            "title": "Histogram",
            "order": 4,
            "content": """# 📊 Histograms

```python
plt.hist(values, bins=10)
```

---

## 🎯 Your Task

Create a histogram of exam scores:
`scores = [65, 70, 75, 80, 85, 90, 95, 70, 75, 80, 85, 80]`
Use 5 bins.
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nscores = [65, 70, 75, 80, 85, 90, 95, 70, 75, 80, 85, 80]\n\n# Create histogram with 5 bins\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nscores = [65, 70, 75, 80, 85, 90, 95, 70, 75, 80, 85, 80]\n\n# Create histogram with 5 bins\nplt.hist(scores, bins=5)\nplt.show()",
            "expected_output": "[Graph: Histogram of score distribution]",
            "xp": 10
        },
        {
            "id": 80,
            "title": "Pie Chart",
            "order": 5,
            "content": """# 🥧 Pie Charts

```python
plt.pie(values, labels=labels)
```

---

## 🎯 Your Task

Create a pie chart showing market share:
- Labels: `["Apple", "Google", "Microsoft"]`
- Values: `[30, 45, 25]`
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nlabels = [\"Apple\", \"Google\", \"Microsoft\"]\nvalues = [30, 45, 25]\n\n# Create pie chart\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nlabels = [\"Apple\", \"Google\", \"Microsoft\"]\nvalues = [30, 45, 25]\n\n# Create pie chart\nplt.pie(values, labels=labels)\nplt.show()",
            "expected_output": "[Graph: Pie chart with 3 segments]",
            "xp": 10
        },
        {
            "id": 81,
            "title": "Adding Labels",
            "order": 6,
            "content": """# 🏷️ Chart Labels

```python
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("Chart Title")
```

---

## 🎯 Your Task

Create a line plot of temperatures `[20, 22, 25, 23, 21]` over days 1-5.
Add title: "Daily Temperature"
Add labels: "Day" and "Temp (°C)"
""",
            "starter_code": "import matplotlib.pyplot as plt\n\ndays = [1, 2, 3, 4, 5]\ntemps = [20, 22, 25, 23, 21]\n\n# Create plot with labels\n",
            "solution_code": "import matplotlib.pyplot as plt\n\ndays = [1, 2, 3, 4, 5]\ntemps = [20, 22, 25, 23, 21]\n\n# Create plot with labels\nplt.plot(days, temps)\nplt.title(\"Daily Temperature\")\nplt.xlabel(\"Day\")\nplt.ylabel(\"Temp (°C)\")\nplt.show()",
            "expected_output": "[Graph: Line plot with labeled axes]",
            "xp": 10
        },
        {
            "id": 82,
            "title": "Multiple Lines",
            "order": 7,
            "content": """# 📈 Multiple Lines

```python
plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.legend()
```

---

## 🎯 Your Task

Plot two lines for months 1-4:
- Sales A: `[10, 15, 13, 18]`
- Sales B: `[8, 12, 16, 14]`
Add a legend.
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nmonths = [1, 2, 3, 4]\nsales_a = [10, 15, 13, 18]\nsales_b = [8, 12, 16, 14]\n\n# Plot both lines with legend\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nmonths = [1, 2, 3, 4]\nsales_a = [10, 15, 13, 18]\nsales_b = [8, 12, 16, 14]\n\n# Plot both lines with legend\nplt.plot(months, sales_a, label=\"Sales A\")\nplt.plot(months, sales_b, label=\"Sales B\")\nplt.legend()\nplt.show()",
            "expected_output": "[Graph: Two line series with legend]",
            "xp": 10
        },
        {
            "id": 83,
            "title": "Colors and Styles",
            "order": 8,
            "content": """# 🎨 Styling

```python
plt.plot(x, y, color="red", linestyle="--", marker="o")
```

---

## 🎯 Your Task

Create a plot with:
- x: `[1, 2, 3, 4]`
- y: `[1, 4, 2, 3]`
- Red color, dashed line, circle markers
""",
            "starter_code": "import matplotlib.pyplot as plt\n\nx = [1, 2, 3, 4]\ny = [1, 4, 2, 3]\n\n# Plot with red, dashed, circles\n",
            "solution_code": "import matplotlib.pyplot as plt\n\nx = [1, 2, 3, 4]\ny = [1, 4, 2, 3]\n\n# Plot with red, dashed, circles\nplt.plot(x, y, color=\"red\", linestyle=\"--\", marker=\"o\")\nplt.show()",
            "expected_output": "[Graph: Red dashed line with circle markers]",
            "xp": 10
        },
        {
            "id": 84,
            "title": "Subplots",
            "order": 9,
            "content": """# 🖼️ Subplots

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x, y1)
ax2.bar(categories, values)
```

---

## 🎯 Your Task

Create 2 side-by-side subplots:
- Left: Line plot of `[1, 2, 3]`
- Right: Bar chart of `["A", "B"]` with `[5, 8]`
""",
            "starter_code": "import matplotlib.pyplot as plt\n\n# Create 1x2 subplots\n",
            "solution_code": "import matplotlib.pyplot as plt\n\n# Create 1x2 subplots\nfig, (ax1, ax2) = plt.subplots(1, 2)\nax1.plot([1, 2, 3])\nax2.bar([\"A\", \"B\"], [5, 8])\nplt.show()",
            "expected_output": "[Graph: Two subplots side by side]",
            "xp": 10
        }
    ]
}
