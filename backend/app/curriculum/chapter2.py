# Chapter 2: Loops (Iteration)
# Enhanced with detailed definitions, explanations, and "why it matters"

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
            "content": """# 🔁 For Loops: Repeat Actions

## What is a Loop?

A **loop** lets you repeat code multiple times without writing it over and over. It's one of the most powerful tools in programming!

## Real-World Analogy

Imagine you need to greet 100 guests at a party. Instead of saying "Hello" 100 times manually, you'd use a loop: "For each guest, say Hello."

## The For Loop

A `for` loop repeats code for each item in a sequence:

```python
# For each item in the sequence...
for item in sequence:
    # Do something with item
    print(item)
```

## Example: Looping Through a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Output:
```
apple
banana
cherry
```

## How It Works Step by Step

1. Python takes the first item ("apple") and stores it in `fruit`
2. Runs the indented code (prints "apple")
3. Takes the next item ("banana") and stores it in `fruit`
4. Runs the indented code (prints "banana")
5. Continues until no items left

---

## 🎯 Your Task

Given this list:
```python
colors = ["red", "green", "blue"]
```

Use a for loop to print each color on a new line.
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

## Strings Are Sequences Too!

A string is actually a sequence of characters. You can loop through it just like a list:

```python
word = "Hello"
for letter in word:
    print(letter)
```

Output:
```
H
e
l
l
o
```

## Why Loop Through Strings?

Common use cases:
- Counting specific characters
- Checking each character for validity
- Transforming characters one by one
- Finding patterns

## Example: Count Vowels

```python
text = "hello world"
vowel_count = 0
for char in text:
    if char in "aeiou":
        vowel_count += 1
print(f"Vowels: {vowel_count}")  # Vowels: 3
```

## Understanding Characters

Each loop iteration gives you ONE character:

```python
for char in "ABC":
    print(f"Character: '{char}'")
# Output:
# Character: 'A'
# Character: 'B'
# Character: 'C'
```

---

## 🎯 Your Task

Loop through the word `"Python"` and print each letter on a separate line.
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
            "content": """# ➕ Accumulating Values in Loops

## The Accumulator Pattern

One of the most common loop patterns: start with a value, then update it each iteration.

```python
# Start with an initial value
total = 0

# Loop and accumulate
for num in [1, 2, 3, 4, 5]:
    total += num  # Add each number

print(total)  # 15
```

## How It Works Step by Step

| Iteration | `num` | `total` before | Action | `total` after |
| --- | --- | --- | --- | --- |
| 1 | 1 | 0 | 0 + 1 | 1 |
| 2 | 2 | 1 | 1 + 2 | 3 |
| 3 | 3 | 3 | 3 + 3 | 6 |
| 4 | 4 | 6 | 6 + 4 | 10 |
| 5 | 5 | 10 | 10 + 5 | 15 |

## Other Accumulator Examples

```python
# Product
product = 1
for num in [2, 3, 4]:
    product *= num
print(product)  # 24

# String building
sentence = ""
words = ["Hello", "World", "!"]
for word in words:
    sentence += word + " "
print(sentence)  # "Hello World ! "
```

---

## 🎯 Your Task

Given: `numbers = [10, 20, 30, 40]`

Calculate and print the sum using the accumulator pattern.
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

## What is range()?

`range()` generates a sequence of numbers. It's perfect when you need to repeat something a specific number of times.

```python
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4
```

## Why Start at 0?

Python (like most languages) uses **zero-based indexing**. This means counting starts at 0, not 1.

```python
range(5)  # Generates: 0, 1, 2, 3, 4 (that's 5 numbers!)
```

## Common Pattern: Repeat N Times

If you just want to repeat something:

```python
for i in range(3):
    print("Hello!")
# Output: Hello! Hello! Hello!
```

## range() Returns a Special Object

Note: `range()` doesn't create a list immediately (to save memory). But it works in for loops!

```python
print(range(5))       # range(0, 5) - the object
print(list(range(5))) # [0, 1, 2, 3, 4] - converted to list
```

---

## 🎯 Your Task

Use `range(5)` to print numbers 0 through 4, each on a new line.
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

## Two Arguments: Start and Stop

With two arguments, you control where to start:

```python
range(start, stop)  # From start up to (but not including) stop
```

## Example

```python
for i in range(2, 5):
    print(i)
# Output: 2, 3, 4
```

Notice: 5 is NOT included! Python ranges are **exclusive** of the end value.

## Mental Model

Think of it as: "start here, stop BEFORE this"

```python
range(1, 4)   # 1, 2, 3 (stops before 4)
range(5, 10)  # 5, 6, 7, 8, 9 (stops before 10)
```

## To Include the End Number

If you want 1-10 inclusive, use `range(1, 11)`:

```python
for i in range(1, 11):
    print(i, end=" ")
# Output: 1 2 3 4 5 6 7 8 9 10
```

---

## 🎯 Your Task

Print numbers from 5 to 10 (inclusive).
Use `range(5, 11)` since the end is exclusive.
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

## Three Arguments: Adding a Step

The third argument controls how much to increment:

```python
range(start, stop, step)
```

## Example: Skip by 2

```python
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8
```

## Common Step Patterns

```python
# Even numbers (0-10)
range(0, 11, 2)  # 0, 2, 4, 6, 8, 10

# Odd numbers (1-9)
range(1, 10, 2)  # 1, 3, 5, 7, 9

# Count by 5s
range(0, 26, 5)  # 0, 5, 10, 15, 20, 25

# Count by 10s
range(10, 101, 10)  # 10, 20, 30, ... 100
```

## Counting Backwards

Use a negative step to go in reverse:

```python
for i in range(10, 0, -1):
    print(i)
# Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

---

## 🎯 Your Task

Print even numbers from 2 to 10 (inclusive).
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

## For vs While

| Loop Type | Use Case |
| --- | --- |
| `for` | When you know how many times to loop |
| `while` | When you loop until a condition changes |

## While Loop Syntax

```python
while condition:
    # Do something
    # Update something (to eventually stop!)
```

## Example

```python
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0, 1, 2, 3, 4
```

## ⚠️ Warning: Infinite Loops!

If the condition never becomes False, the loop runs forever!

```python
# DANGER! Never stops!
while True:
    print("Forever...")

# SAFE: Will eventually stop
x = 0
while x < 10:
    print(x)
    x += 1  # This makes x eventually reach 10
```

## When to Use While

- User input validation (keep asking until valid)
- Game loops (run until game over)
- Processing data until a condition is met

---

## 🎯 Your Task

Start with `x = 1`. 
Use a while loop to print x and double it (`x *= 2`) while x <= 16.
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

## The break Statement

`break` immediately exits the loop, even if there are more items:

```python
for i in range(10):
    if i == 5:
        break  # Exit NOW!
    print(i)
# Output: 0, 1, 2, 3, 4
```

## Why Use break?

- **Early exit**: Stop when you find what you're looking for
- **Performance**: Don't process unnecessary items
- **Error handling**: Exit if something goes wrong

## Example: Find First Match

```python
names = ["Alice", "Bob", "Charlie", "Diana"]
target = "Charlie"

for name in names:
    if name == target:
        print(f"Found {target}!")
        break
    print(f"Checking {name}...")

# Output:
# Checking Alice...
# Checking Bob...
# Found Charlie!
```

Notice: We never check Diana because we broke out early!

---

## 🎯 Your Task

Loop through `[1, 2, 3, 4, 5, 6, 7]`.
Print each number, but use `break` to exit when you reach 5.
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

## The continue Statement

`continue` skips the rest of the current iteration and moves to the next one:

```python
for i in range(5):
    if i == 2:
        continue  # Skip 2
    print(i)
# Output: 0, 1, 3, 4
```

## break vs continue

| Statement | What It Does |
| --- | --- |
| `break` | **EXIT** the entire loop |
| `continue` | **SKIP** to next iteration |

## Example: Skip Negative Numbers

```python
numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        continue  # Skip negatives
    print(num)
# Output: 1, 3, 5
```

## When to Use continue

- Skip invalid data
- Filter out unwanted items
- Process only items that meet criteria

```python
# Process only adults
for person in people:
    if person.age < 18:
        continue
    # ... process adult ...
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
