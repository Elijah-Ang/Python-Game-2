# Chapter 1: Variables, Types & Memory
# Each exercise has specific data, clear instructions, and exact expected output

CHAPTER_1 = {
    "id": 1,
    "title": "Variables, Types & Memory",
    "slug": "python-variables",
    "icon": "🏠",
    "is_boss": False,
    "lessons": [
        {
            "id": 1,
            "title": "What is a Variable?",
            "order": 1,
            "content": """# 📦 What is a Variable?

## Definition
A **variable** is a named container that stores data. Think of it like a labeled box.

## How to Create a Variable
```python
age = 25
name = "Alice"
```

The `=` sign stores the value on the right into the variable name on the left.

---

## 🎯 Your Task

Create a variable called `student` and set it to `"Alice"`. Then print it.

The code should:
1. Create variable `student` with value `"Alice"`
2. Print the variable
""",
            "starter_code": "# Create a variable called student with value \"Alice\"\n\n\n# Print the variable\n",
            "solution_code": "# Create a variable called student with value \"Alice\"\nstudent = \"Alice\"\n\n# Print the variable\nprint(student)",
            "expected_output": "Alice",
            "xp": 10
        },
        {
            "id": 2,
            "title": "Naming Variables",
            "order": 2,
            "content": """# 🏷️ How to Name Variables

## Rules
- Can start with letter or underscore
- Cannot start with number
- No spaces allowed
- Only letters, numbers, underscore

## Good Examples
```python
user_name = "Bob"
total_price = 99.99
```

---

## 🎯 Your Task

Create these two variables:
- `first_name` = `"John"`
- `last_name` = `"Doe"`

Then print both.
""",
            "starter_code": "# Create first_name variable\n\n\n# Create last_name variable\n\n\n# Print both\n",
            "solution_code": "# Create first_name variable\nfirst_name = \"John\"\n\n# Create last_name variable\nlast_name = \"Doe\"\n\n# Print both\nprint(first_name)\nprint(last_name)",
            "expected_output": "John\nDoe",
            "xp": 10
        },
        {
            "id": 3,
            "title": "Reassigning Variables",
            "order": 3,
            "content": """# 🔄 Changing Variable Values

Variables can be updated:

```python
score = 0
score = 100  # Now it's 100!
```

You can use the current value:
```python
count = 5
count = count + 1  # Now it's 6
count += 1         # Shorthand, now it's 7
```

---

## 🎯 Your Task

1. Start with `points = 0`
2. Add 10 to points
3. Add 5 more to points
4. Print the final value

Use `+=` for the additions.
""",
            "starter_code": "# Start with 0 points\npoints = 0\n\n# Add 10 points\n\n\n# Add 5 more points\n\n\n# Print final value\n",
            "solution_code": "# Start with 0 points\npoints = 0\n\n# Add 10 points\npoints += 10\n\n# Add 5 more points\npoints += 5\n\n# Print final value\nprint(points)",
            "expected_output": "15",
            "xp": 10
        },
        {
            "id": 4,
            "title": "Multiple Variables",
            "order": 4,
            "content": """# 📋 Working with Multiple Variables

Variables can be used together:

```python
price = 20
quantity = 3
total = price * quantity  # 60
```

---

## 🎯 Your Task

Create these variables:
- `product` = `"Laptop"`
- `price` = `999`
- `quantity` = `2`

Calculate `total` as price × quantity, then print:
```
Product: Laptop
Total: 1998
```
""",
            "starter_code": "# Product information\nproduct = \"Laptop\"\nprice = 999\nquantity = 2\n\n# Calculate total\n\n\n# Print product and total\n",
            "solution_code": "# Product information\nproduct = \"Laptop\"\nprice = 999\nquantity = 2\n\n# Calculate total\ntotal = price * quantity\n\n# Print product and total\nprint(f\"Product: {product}\")\nprint(f\"Total: {total}\")",
            "expected_output": "Product: Laptop\nTotal: 1998",
            "xp": 10
        },
        {
            "id": 5,
            "title": "What are Strings?",
            "order": 5,
            "content": """# 📝 What is a String?

A **string** is text surrounded by quotes:

```python
message = "Hello, World!"
name = 'Alice'
```

---

## 🎯 Your Task

Create these strings:
- `greeting` = `"Hello"`
- `name` = `"Python"`

Print: `Hello, Python!`
""",
            "starter_code": "# Create greeting\ngreeting = \"Hello\"\n\n# Create name\nname = \"Python\"\n\n# Print greeting, name!\n",
            "solution_code": "# Create greeting\ngreeting = \"Hello\"\n\n# Create name\nname = \"Python\"\n\n# Print greeting, name!\nprint(f\"{greeting}, {name}!\")",
            "expected_output": "Hello, Python!",
            "xp": 10
        },
        {
            "id": 6,
            "title": "String Concatenation",
            "order": 6,
            "content": """# 🔗 Joining Strings

Use `+` to join strings:

```python
first = "Hello"
second = "World"
combined = first + " " + second  # "Hello World"
```

---

## 🎯 Your Task

Given:
- `first_name` = `"Jane"`
- `last_name` = `"Smith"`

Create `full_name` by joining them with a space, then print:
`Welcome, Jane Smith!`
""",
            "starter_code": "# Given names\nfirst_name = \"Jane\"\nlast_name = \"Smith\"\n\n# Join them into full_name\n\n\n# Print welcome message\n",
            "solution_code": "# Given names\nfirst_name = \"Jane\"\nlast_name = \"Smith\"\n\n# Join them into full_name\nfull_name = first_name + \" \" + last_name\n\n# Print welcome message\nprint(\"Welcome, \" + full_name + \"!\")",
            "expected_output": "Welcome, Jane Smith!",
            "xp": 10
        },
        {
            "id": 7,
            "title": "F-Strings",
            "order": 7,
            "content": """# ✨ F-Strings: The Modern Way

F-strings let you embed variables in text:

```python
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age}")
```

---

## 🎯 Your Task

Given:
- `item` = `"Coffee"`
- `price` = `4.50`

Print: `Coffee costs $4.50`
""",
            "starter_code": "# Given data\nitem = \"Coffee\"\nprice = 4.50\n\n# Print using f-string\n",
            "solution_code": "# Given data\nitem = \"Coffee\"\nprice = 4.50\n\n# Print using f-string\nprint(f\"{item} costs ${price}\")",
            "expected_output": "Coffee costs $4.5",
            "xp": 10
        },
        {
            "id": 8,
            "title": "String Methods",
            "order": 8,
            "content": """# 🛠️ String Methods

Strings have built-in methods:

```python
text = "Hello World"
text.upper()   # "HELLO WORLD"
text.lower()   # "hello world"
text.strip()   # Removes whitespace from ends
```

---

## 🎯 Your Task

Given: `messy_email = "  JOHN@EMAIL.COM  "`

Clean it up:
1. Remove extra spaces with `.strip()`
2. Convert to lowercase with `.lower()`
3. Print the result
""",
            "starter_code": "# Messy email\nmessy_email = \"  JOHN@EMAIL.COM  \"\n\n# Clean it: strip and lowercase\n\n\n# Print cleaned email\n",
            "solution_code": "# Messy email\nmessy_email = \"  JOHN@EMAIL.COM  \"\n\n# Clean it: strip and lowercase\nclean_email = messy_email.strip().lower()\n\n# Print cleaned email\nprint(clean_email)",
            "expected_output": "john@email.com",
            "xp": 10
        },
        {
            "id": 9,
            "title": "Numbers: Integers and Floats",
            "order": 9,
            "content": """# 🔢 Numbers in Python

Two types:
- **Integer (int)**: `10`, `-5`, `0`
- **Float**: `3.14`, `-2.5`, `0.0`

```python
age = 25        # int
price = 19.99   # float
```

---

## 🎯 Your Task

Create:
- `quantity` = `5` (integer)
- `unit_price` = `12.50` (float)
- `total` = quantity × unit_price

Print: `Total: 62.5`
""",
            "starter_code": "# Create quantity (integer)\nquantity = 5\n\n# Create unit_price (float)\nunit_price = 12.50\n\n# Calculate total\n\n\n# Print total\n",
            "solution_code": "# Create quantity (integer)\nquantity = 5\n\n# Create unit_price (float)\nunit_price = 12.50\n\n# Calculate total\ntotal = quantity * unit_price\n\n# Print total\nprint(f\"Total: {total}\")",
            "expected_output": "Total: 62.5",
            "xp": 10
        },
        {
            "id": 10,
            "title": "Math Operations",
            "order": 10,
            "content": """# ➕ Math in Python

| Operator | Meaning |
| --- | --- |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor division |
| `%` | Modulo (remainder) |

---

## 🎯 Your Task

Calculate a restaurant tip:
- `bill` = `80.00`
- `tip_percent` = `20`
- Calculate `tip` as 20% of bill
- Calculate `total` as bill + tip

Print: `Tip: 16.0` and `Total: 96.0`
""",
            "starter_code": "# Bill amount\nbill = 80.00\ntip_percent = 20\n\n# Calculate tip (20% of bill)\n\n\n# Calculate total\n\n\n# Print tip and total\n",
            "solution_code": "# Bill amount\nbill = 80.00\ntip_percent = 20\n\n# Calculate tip (20% of bill)\ntip = bill * (tip_percent / 100)\n\n# Calculate total\ntotal = bill + tip\n\n# Print tip and total\nprint(f\"Tip: {tip}\")\nprint(f\"Total: {total}\")",
            "expected_output": "Tip: 16.0\nTotal: 96.0",
            "xp": 10
        },
        {
            "id": 11,
            "title": "Compound Assignment",
            "order": 11,
            "content": """# 📝 Shorthand Math

Instead of `x = x + 5`, use `x += 5`:

| Long | Short |
| --- | --- |
| `x = x + 5` | `x += 5` |
| `x = x - 5` | `x -= 5` |
| `x = x * 5` | `x *= 5` |

---

## 🎯 Your Task

Simulate a game:
1. Start `health = 100`
2. Take 25 damage (use `-=`)
3. Heal 10 health (use `+=`)
4. Print final health

Expected: `85`
""",
            "starter_code": "# Start with full health\nhealth = 100\n\n# Take 25 damage\n\n\n# Heal 10 health\n\n\n# Print final health\n",
            "solution_code": "# Start with full health\nhealth = 100\n\n# Take 25 damage\nhealth -= 25\n\n# Heal 10 health\nhealth += 10\n\n# Print final health\nprint(health)",
            "expected_output": "85",
            "xp": 10
        },
        {
            "id": 12,
            "title": "Booleans and Type Conversion",
            "order": 12,
            "content": """# ⭕ Booleans

Booleans are `True` or `False`:

```python
is_active = True
is_finished = False
```

## Type Conversion

```python
int("42")     # 42
str(42)       # "42"
float("3.14") # 3.14
```

---

## 🎯 Your Task

Given: `age_text = "25"`

1. Convert it to an integer using `int()`
2. Add 5 to get age in 5 years
3. Print the future age

Expected: `30`
""",
            "starter_code": "# Age as a string\nage_text = \"25\"\n\n# Convert to integer\n\n\n# Add 5 years\n\n\n# Print future age\n",
            "solution_code": "# Age as a string\nage_text = \"25\"\n\n# Convert to integer\nage = int(age_text)\n\n# Add 5 years\nfuture_age = age + 5\n\n# Print future age\nprint(future_age)",
            "expected_output": "30",
            "xp": 10
        }
    ]
}
