# Chapter 5: Data Structures
# Enhanced with detailed definitions, explanations, and "why it matters"

CHAPTER_5 = {
    "id": 7,
    "title": "Data Structures",
    "slug": "python-data-structures",
    "icon": "📦",
    "is_boss": False,
    "lessons": [
        {
            "id": 41,
            "title": "Lists Basics",
            "order": 1,
            "content": """# 📋 Lists: Collections of Items

## What is a List?

A **list** is an ordered collection that can hold multiple items. Think of it like a shopping list or a playlist.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Can mix types!
```

## Why Use Lists?

- Store multiple related items together
- Access items by position (index)
- Add, remove, or modify items
- Loop through all items

## Accessing Items by Index

Lists use **zero-based indexing** (counting starts at 0):

```python
fruits = ["apple", "banana", "cherry"]
#          [0]       [1]       [2]

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # cherry
print(fruits[-1]) # cherry (last item)
```

## List Length

```python
print(len(fruits))  # 3
```

---

## 🎯 Your Task

Create a list `colors = ["red", "green", "blue"]`.
Print the second item (index 1).
""",
            "starter_code": "# Create colors list\n\n\n# Print second item\n",
            "solution_code": "# Create colors list\ncolors = [\"red\", \"green\", \"blue\"]\n\n# Print second item\nprint(colors[1])",
            "expected_output": "green",
            "xp": 10
        },
        {
            "id": 42,
            "title": "List Methods",
            "order": 2,
            "content": """# 📝 Modifying Lists

## Common List Methods

| Method | What It Does | Example |
| --- | --- | --- |
| `.append(x)` | Add to end | `list.append(4)` |
| `.insert(i, x)` | Insert at index | `list.insert(0, "first")` |
| `.remove(x)` | Remove first occurrence | `list.remove("apple")` |
| `.pop()` | Remove and return last | `last = list.pop()` |
| `.pop(i)` | Remove at index | `list.pop(0)` |
| `.sort()` | Sort in place | `list.sort()` |
| `.reverse()` | Reverse in place | `list.reverse()` |

## Examples

```python
fruits = ["apple", "banana"]

# Add items
fruits.append("cherry")     # ["apple", "banana", "cherry"]
fruits.insert(0, "mango")   # ["mango", "apple", "banana", "cherry"]

# Remove items
fruits.remove("banana")     # ["mango", "apple", "cherry"]
last = fruits.pop()         # last = "cherry", list = ["mango", "apple"]
```

## Modifying Lists Changes the Original

Unlike strings (which are immutable), lists can be changed:

```python
nums = [3, 1, 2]
nums.sort()       # nums is now [1, 2, 3]
nums.reverse()    # nums is now [3, 2, 1]
```

---

## 🎯 Your Task

Start with: `numbers = [1, 2, 3]`
1. Append `4`
2. Print the list
""",
            "starter_code": "numbers = [1, 2, 3]\n\n# Append 4\n\n\n# Print list\n",
            "solution_code": "numbers = [1, 2, 3]\n\n# Append 4\nnumbers.append(4)\n\n# Print list\nprint(numbers)",
            "expected_output": "[1, 2, 3, 4]",
            "xp": 10
        },
        {
            "id": 43,
            "title": "List Slicing",
            "order": 3,
            "content": """# ✂️ Slicing Lists

## What is Slicing?

**Slicing** extracts a portion of a list:

```python
list[start:stop]  # Elements from start up to (not including) stop
```

## Examples

```python
nums = [0, 1, 2, 3, 4, 5]

nums[1:4]   # [1, 2, 3]     (index 1, 2, 3)
nums[:3]    # [0, 1, 2]     (start to index 2)
nums[3:]    # [3, 4, 5]     (index 3 to end)
nums[:]     # [0, 1, 2, 3, 4, 5]  (copy entire list)
```

## Negative Indices

```python
nums[-3:]   # [3, 4, 5]     (last 3 elements)
nums[:-2]   # [0, 1, 2, 3]  (all except last 2)
```

## Step in Slicing

```python
nums[::2]   # [0, 2, 4]     (every 2nd element)
nums[::-1]  # [5, 4, 3, 2, 1, 0]  (reversed!)
```

---

## 🎯 Your Task

Given: `letters = ["a", "b", "c", "d", "e"]`
Print the slice from index 1 to 3 (should be `["b", "c", "d"]`).
""",
            "starter_code": "letters = [\"a\", \"b\", \"c\", \"d\", \"e\"]\n\n# Print slice [1:4]\n",
            "solution_code": "letters = [\"a\", \"b\", \"c\", \"d\", \"e\"]\n\n# Print slice [1:4]\nprint(letters[1:4])",
            "expected_output": "['b', 'c', 'd']",
            "xp": 10
        },
        {
            "id": 44,
            "title": "Dictionaries",
            "order": 4,
            "content": """# 📖 Dictionaries: Key-Value Pairs

## What is a Dictionary?

A **dictionary** stores data as key-value pairs. Instead of accessing by index, you access by key name.

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

## Why Use Dictionaries?

- Access data by meaningful names (not numbers)
- Store related information together
- Fast lookups
- Real-world mapping (word → definition, ID → record)

## Accessing Values

```python
print(person["name"])  # Alice
print(person["age"])   # 25
```

## Adding/Modifying

```python
person["email"] = "alice@email.com"  # Add new key
person["age"] = 26                    # Modify existing
```

## Safe Access with .get()

```python
# If key doesn't exist:
person["phone"]           # KeyError!
person.get("phone")       # None (no error)
person.get("phone", "N/A")  # "N/A" (custom default)
```

---

## 🎯 Your Task

Create a dictionary:
```python
book = {"title": "Python 101", "author": "John Doe", "pages": 300}
```
Print the author.
""",
            "starter_code": "# Create book dictionary\n\n\n# Print author\n",
            "solution_code": "# Create book dictionary\nbook = {\"title\": \"Python 101\", \"author\": \"John Doe\", \"pages\": 300}\n\n# Print author\nprint(book[\"author\"])",
            "expected_output": "John Doe",
            "xp": 10
        },
        {
            "id": 45,
            "title": "Dictionary Methods",
            "order": 5,
            "content": """# 🔧 Dictionary Methods

## Common Methods

| Method | What It Does |
| --- | --- |
| `.keys()` | Get all keys |
| `.values()` | Get all values |
| `.items()` | Get key-value pairs |
| `.get(key)` | Safe access |
| `.update(dict2)` | Merge dictionaries |
| `.pop(key)` | Remove and return value |

## Examples

```python
scores = {"Alice": 85, "Bob": 92}

# Get keys and values
print(list(scores.keys()))    # ['Alice', 'Bob']
print(list(scores.values()))  # [85, 92]

# Loop through items
for name, score in scores.items():
    print(f"{name}: {score}")
```

## Checking if Key Exists

```python
if "Alice" in scores:
    print(scores["Alice"])
```

---

## 🎯 Your Task

Given:
```python
scores = {"Alice": 85, "Bob": 92}
```
Add `"Charlie": 78` and print all keys.
""",
            "starter_code": "scores = {\"Alice\": 85, \"Bob\": 92}\n\n# Add Charlie: 78\n\n\n# Print keys\n",
            "solution_code": "scores = {\"Alice\": 85, \"Bob\": 92}\n\n# Add Charlie: 78\nscores[\"Charlie\"] = 78\n\n# Print keys\nprint(list(scores.keys()))",
            "expected_output": "['Alice', 'Bob', 'Charlie']",
            "xp": 10
        },
        {
            "id": 46,
            "title": "Tuples",
            "order": 6,
            "content": """# 📌 Tuples: Immutable Sequences

## What is a Tuple?

A **tuple** is like a list, but it **cannot be changed** (immutable):

```python
point = (10, 20)
colors = ("red", "green", "blue")
```

## Tuples vs Lists

| Feature | List `[]` | Tuple `()` |
| --- | --- | --- |
| Mutable | ✅ Yes | ❌ No |
| Use case | Data that changes | Data that shouldn't change |
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |

## Why Use Tuples?

- Protect data from accidental changes
- Dictionary keys (must be immutable)
- Return multiple values from functions
- Slightly faster than lists

## Tuple Unpacking

Assign tuple values to multiple variables:

```python
point = (100, 200)
x, y = point  # x=100, y=200

# Swap variables!
a, b = b, a
```

---

## 🎯 Your Task

Create `coordinates = (100, 200)`.
Unpack into `x` and `y`.
Print `x` and `y`.
""",
            "starter_code": "# Create coordinates tuple\n\n\n# Unpack\n\n\n# Print x and y\n",
            "solution_code": "# Create coordinates tuple\ncoordinates = (100, 200)\n\n# Unpack\nx, y = coordinates\n\n# Print x and y\nprint(x)\nprint(y)",
            "expected_output": "100\n200",
            "xp": 10
        },
        {
            "id": 47,
            "title": "Sets",
            "order": 7,
            "content": """# 🎯 Sets: Unique Collections

## What is a Set?

A **set** is an unordered collection of unique items:

```python
numbers = {1, 2, 3, 2, 1}  # {1, 2, 3} - duplicates removed!
```

## Why Use Sets?

- Automatic duplicate removal
- Fast membership testing
- Mathematical set operations (union, intersection)

## Set Operations

```python
a = {1, 2, 3}
b = {2, 3, 4}

a | b  # {1, 2, 3, 4}  - Union
a & b  # {2, 3}        - Intersection
a - b  # {1}           - Difference
```

## Common Methods

```python
s = {1, 2, 3}
s.add(4)       # {1, 2, 3, 4}
s.remove(2)    # {1, 3, 4}
s.discard(10)  # No error if not found
```

---

## 🎯 Your Task

Create `letters = {"a", "b", "c"}`.
Add `"d"` and print the set.
""",
            "starter_code": "# Create set\n\n\n# Add \"d\"\n\n\n# Print set\n",
            "solution_code": "# Create set\nletters = {\"a\", \"b\", \"c\"}\n\n# Add \"d\"\nletters.add(\"d\")\n\n# Print set\nprint(letters)",
            "expected_output": "{'a', 'b', 'c', 'd'}",
            "xp": 10
        },
        {
            "id": 48,
            "title": "List Comprehension",
            "order": 8,
            "content": """# ⚡ List Comprehension

## What is List Comprehension?

A concise way to create lists:

```python
# Traditional way
squares = []
for x in range(5):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(5)]
```

Both produce: `[0, 1, 4, 9, 16]`

## Syntax

```python
[expression for item in iterable]
[expression for item in iterable if condition]
```

## Examples

```python
# Double each number
[x * 2 for x in range(5)]  # [0, 2, 4, 6, 8]

# Filter: only evens
[x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Transform strings
names = ["alice", "bob"]
[name.upper() for name in names]  # ["ALICE", "BOB"]
```

---

## 🎯 Your Task

Create a list `doubled` containing each number from 1-5 doubled.
Result: `[2, 4, 6, 8, 10]`
""",
            "starter_code": "# Create doubled list using comprehension\n\n\n# Print it\n",
            "solution_code": "# Create doubled list using comprehension\ndoubled = [x * 2 for x in range(1, 6)]\n\n# Print it\nprint(doubled)",
            "expected_output": "[2, 4, 6, 8, 10]",
            "xp": 10
        },
        {
            "id": 49,
            "title": "Nested Data Structures",
            "order": 9,
            "content": """# 🪆 Nested Data Structures

## Lists of Dictionaries

Very common pattern for storing collections of records:

```python
students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 92}
]

# Access
print(students[0]["name"])  # Alice
print(students[1]["grade"]) # 85
```

## Dictionaries of Lists

```python
grades = {
    "Alice": [90, 85, 88],
    "Bob": [78, 82, 80]
}

# Average for Alice
print(sum(grades["Alice"]) / len(grades["Alice"]))  # 87.67
```

## Looping Through Nested Structures

```python
for student in students:
    print(f"{student['name']}: {student['grade']}")
```

---

## 🎯 Your Task

Given:
```python
books = [
    {"title": "Python Guide", "pages": 200},
    {"title": "Data Science", "pages": 350}
]
```
Print the pages of the second book.
""",
            "starter_code": "books = [\n    {\"title\": \"Python Guide\", \"pages\": 200},\n    {\"title\": \"Data Science\", \"pages\": 350}\n]\n\n# Print pages of second book\n",
            "solution_code": "books = [\n    {\"title\": \"Python Guide\", \"pages\": 200},\n    {\"title\": \"Data Science\", \"pages\": 350}\n]\n\n# Print pages of second book\nprint(books[1][\"pages\"])",
            "expected_output": "350",
            "xp": 10
        }
    ]
}
