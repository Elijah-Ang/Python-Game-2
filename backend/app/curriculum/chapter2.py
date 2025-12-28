# Chapter 2: Loops
# Each exercise has specific data and exact expected output

CHAPTER_2 = {
    "id": 2,
    "title": "Loops (Iteration)",
    "slug": "python-loops",
    "icon": "🔁",
    "is_boss": False,
    "lessons": [
        {
            "id": 13,
            "title": "For Loop Basics",
            "order": 1,
            "content": """# 🔁 For Loops

A `for` loop repeats code for each item in a sequence:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

## 🎯 Your Task

Given this list:
```python
colors = ["red", "green", "blue"]
```

Print each color on a new line.
""",
            "starter_code": "colors = [\"red\", \"green\", \"blue\"]\n\n# Print each color\n",
            "solution_code": "colors = [\"red\", \"green\", \"blue\"]\n\n# Print each color\nfor color in colors:\n    print(color)",
            "expected_output": "red\ngreen\nblue",
            "xp": 10
        },
        {
            "id": 14,
            "title": "Looping Through Strings",
            "order": 2,
            "content": """# 📝 Looping Through Strings

Strings are sequences of characters:

```python
for letter in "Hello":
    print(letter)
```

---

## 🎯 Your Task

Loop through the word `"Python"` and print each letter.
""",
            "starter_code": "word = \"Python\"\n\n# Print each letter\n",
            "solution_code": "word = \"Python\"\n\n# Print each letter\nfor letter in word:\n    print(letter)",
            "expected_output": "P\ny\nt\nh\no\nn",
            "xp": 10
        },
        {
            "id": 15,
            "title": "Accumulating Values",
            "order": 3,
            "content": """# ➕ Accumulating Values

Add up values as you loop:

```python
total = 0
for num in [1, 2, 3]:
    total += num
print(total)  # 6
```

---

## 🎯 Your Task

Given: `numbers = [10, 20, 30, 40]`

Calculate and print the sum.
""",
            "starter_code": "numbers = [10, 20, 30, 40]\ntotal = 0\n\n# Add each number to total\n\n\n# Print the sum\n",
            "solution_code": "numbers = [10, 20, 30, 40]\ntotal = 0\n\n# Add each number to total\nfor num in numbers:\n    total += num\n\n# Print the sum\nprint(total)",
            "expected_output": "100",
            "xp": 10
        },
        {
            "id": 16,
            "title": "Using range()",
            "order": 4,
            "content": """# 📊 The range() Function

`range(n)` generates numbers 0 to n-1:

```python
for i in range(3):
    print(i)  # 0, 1, 2
```

---

## 🎯 Your Task

Use `range(5)` to print numbers 0 through 4.
""",
            "starter_code": "# Print 0 through 4 using range\n",
            "solution_code": "# Print 0 through 4 using range\nfor i in range(5):\n    print(i)",
            "expected_output": "0\n1\n2\n3\n4",
            "xp": 10
        },
        {
            "id": 17,
            "title": "range() with Start and End",
            "order": 5,
            "content": """# 📈 range(start, end)

`range(start, end)` goes from start to end-1:

```python
for i in range(2, 5):
    print(i)  # 2, 3, 4
```

---

## 🎯 Your Task

Print numbers from 5 to 10 (inclusive).
Use `range(5, 11)`.
""",
            "starter_code": "# Print 5 through 10\n",
            "solution_code": "# Print 5 through 10\nfor i in range(5, 11):\n    print(i)",
            "expected_output": "5\n6\n7\n8\n9\n10",
            "xp": 10
        },
        {
            "id": 18,
            "title": "range() with Step",
            "order": 6,
            "content": """# 🦘 range(start, end, step)

Add a step value to skip numbers:

```python
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

---

## 🎯 Your Task

Print even numbers from 2 to 10.
Use `range(2, 11, 2)`.
""",
            "starter_code": "# Print even numbers 2 to 10\n",
            "solution_code": "# Print even numbers 2 to 10\nfor i in range(2, 11, 2):\n    print(i)",
            "expected_output": "2\n4\n6\n8\n10",
            "xp": 10
        },
        {
            "id": 19,
            "title": "While Loop Basics",
            "order": 7,
            "content": """# ⏳ While Loops

A `while` loop runs while a condition is True:

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

---

## 🎯 Your Task

Start with `x = 1`. Print x and double it (`x *= 2`) while x <= 16.
""",
            "starter_code": "x = 1\n\n# While x <= 16, print x and double it\n",
            "solution_code": "x = 1\n\n# While x <= 16, print x and double it\nwhile x <= 16:\n    print(x)\n    x *= 2",
            "expected_output": "1\n2\n4\n8\n16",
            "xp": 10
        },
        {
            "id": 20,
            "title": "Loop Control: break",
            "order": 8,
            "content": """# 🛑 Breaking Out of Loops

`break` exits a loop immediately:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

## 🎯 Your Task

Loop through `[1, 2, 3, 4, 5, 6, 7]`.
Print each number, but `break` when you reach 5.
""",
            "starter_code": "numbers = [1, 2, 3, 4, 5, 6, 7]\n\n# Print each, break at 5\n",
            "solution_code": "numbers = [1, 2, 3, 4, 5, 6, 7]\n\n# Print each, break at 5\nfor num in numbers:\n    if num == 5:\n        break\n    print(num)",
            "expected_output": "1\n2\n3\n4",
            "xp": 10
        },
        {
            "id": 21,
            "title": "Loop Control: continue",
            "order": 9,
            "content": """# ⏭️ Skipping with continue

`continue` skips to the next iteration:

```python
for i in range(5):
    if i == 2:
        continue  # Skip 2
    print(i)
```

---

## 🎯 Your Task

Print numbers 1-5, but skip 3 using `continue`.
""",
            "starter_code": "# Print 1-5, skip 3\n",
            "solution_code": "# Print 1-5, skip 3\nfor i in range(1, 6):\n    if i == 3:\n        continue\n    print(i)",
            "expected_output": "1\n2\n4\n5",
            "xp": 10
        }
    ]
}
