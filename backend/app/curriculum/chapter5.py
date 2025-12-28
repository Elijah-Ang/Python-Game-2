# Chapter 5: Data Structures
# Each exercise has specific data and exact expected output

CHAPTER_5 = {
    "id": 6,
    "title": "Data Structures",
    "slug": "python-data-structures",
    "icon": "📦",
    "is_boss": False,
    "lessons": [
        {
            "id": 40,
            "title": "Lists Basics",
            "order": 1,
            "content": """# 📋 Lists

Lists store multiple items:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
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
            "id": 41,
            "title": "List Methods",
            "order": 2,
            "content": """# 📝 List Methods

```python
fruits = ["apple"]
fruits.append("banana")   # Add to end
fruits.insert(0, "mango") # Insert at index
fruits.remove("apple")    # Remove item
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
            "id": 42,
            "title": "List Slicing",
            "order": 3,
            "content": """# ✂️ Slicing Lists

```python
nums = [0, 1, 2, 3, 4, 5]
nums[1:4]   # [1, 2, 3]
nums[:3]    # [0, 1, 2]
nums[3:]    # [3, 4, 5]
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
            "id": 43,
            "title": "Dictionaries",
            "order": 4,
            "content": """# 📖 Dictionaries

Key-value pairs:

```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Alice
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
            "id": 44,
            "title": "Dictionary Methods",
            "order": 5,
            "content": """# 🔧 Dictionary Methods

```python
d = {"a": 1}
d["b"] = 2       # Add
d.get("c", 0)    # Get with default
d.keys()         # All keys
d.values()       # All values
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
            "id": 45,
            "title": "Tuples",
            "order": 6,
            "content": """# 📌 Tuples

Immutable sequences:

```python
point = (10, 20)
x, y = point  # Unpacking
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
            "id": 46,
            "title": "Sets",
            "order": 7,
            "content": """# 🎯 Sets

Unique items only:

```python
nums = {1, 2, 2, 3}  # {1, 2, 3}
nums.add(4)
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
            "id": 47,
            "title": "List Comprehension",
            "order": 8,
            "content": """# ⚡ List Comprehension

Create lists concisely:

```python
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]
```

---

## 🎯 Your Task

Create a list `doubled` containing each number from 1-5 doubled.
[2, 4, 6, 8, 10]
""",
            "starter_code": "# Create doubled list using comprehension\n\n\n# Print it\n",
            "solution_code": "# Create doubled list using comprehension\ndoubled = [x * 2 for x in range(1, 6)]\n\n# Print it\nprint(doubled)",
            "expected_output": "[2, 4, 6, 8, 10]",
            "xp": 10
        },
        {
            "id": 48,
            "title": "Nested Data Structures",
            "order": 9,
            "content": """# 🪆 Nested Structures

Lists of dictionaries:

```python
students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85}
]
print(students[0]["name"])  # Alice
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
