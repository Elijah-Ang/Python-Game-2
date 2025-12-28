# Chapter 1: Variables, Types & Memory
# Enhanced with detailed definitions, explanations, and "why it matters"
# Plus expected_output and solution_code for verification

CHAPTER_1 = {
    "id": 1,
    "title": "Variables, Types & Memory",
    "slug": "python-variables",
    "icon": "🏠",
    "is_boss": False,
    "lessons": [
        # === VARIABLES (4 exercises) ===
        {
            "id": 1,
            "title": "What is a Variable?",
            "order": 1,
            "content": """# 📦 What is a Variable?

## Definition
A **variable** is a named container that stores data in your computer's memory. Think of it like a labeled box where you can put things and retrieve them later.

## Why Do We Need Variables?

Imagine you're calculating someone's age. Without variables, you'd have to remember the number (like 25) and type it every time. With a variable, you give it a name (like `age`) and the computer remembers it for you!

## Real-World Analogy

Think of a variable like a **sticky note on a box**:
- The **box** holds something (a piece of data)
- The **sticky note** has a name written on it (the variable name)
- When you need what's inside, you just look for the note!

## How to Create a Variable

In Python, creating a variable is simple:

```python
# variable_name = value
age = 25
name = "Alice"
price = 19.99
```

The `=` sign means "store this value in this variable name."

## Key Vocabulary

| Term | Meaning |
| --- | --- |
| **Variable** | A named container for data |
| **Value** | The actual data stored (like 25 or "Alice") |
| **Assignment** | The act of storing a value in a variable using `=` |

---

## 🎯 Your Task

Create a variable called `student` and set it to `"Alice"`. Then print it!
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

## Why Does Naming Matter?

Good variable names make your code **readable**. Compare:

```python
# Bad - What is x? What is y?
x = 25
y = 75000

# Good - Clear what each variable represents!
age = 25
salary = 75000
```

When you (or someone else) read the code later, good names save time and prevent confusion.

## Python's Naming Rules

These are rules you MUST follow or Python will give an error:

| Rule | ✅ Valid | ❌ Invalid |
| --- | --- | --- |
| Can start with letter or _ | `name`, `_count` | — |
| Cannot start with number | — | `2name` |
| No spaces allowed | `my_name` | `my name` |
| Only letters, numbers, _ | `user_1` | `user-name` |
| Case sensitive | `Age` ≠ `age` | — |

## Naming Conventions (Best Practices)

These aren't required, but make your code professional:

```python
# ✅ Use snake_case (lowercase with underscores)
user_name = "Alice"
total_price = 99.99

# ❌ Avoid starting with uppercase (reserved for classes)
UserName = "Alice"  # Works but not conventional

# ✅ Be descriptive
customer_email = "alice@email.com"

# ❌ Avoid single letters (except for loops)
e = "alice@email.com"  # What is 'e'?
```

---

## 🎯 Your Task

Create these two properly named variables:
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

## What is Reassignment?

Variables can change! You can update a variable by assigning a new value:

```python
score = 0          # Start at 0
print(score)       # Output: 0

score = 100        # Now it's 100!
print(score)       # Output: 100
```

## Why Does This Matter?

In real programs, values change constantly:
- A player's score goes up
- A shopping cart total increases
- A countdown timer decreases

## How It Works in Memory

When you reassign:
1. Python finds the variable name
2. Throws away the old value
3. Stores the new value

```python
temperature = 72   # Box now holds 72
temperature = 85   # Box now holds 85 (72 is gone!)
```

## Using the Current Value

You can use a variable's current value to calculate a new one:

```python
count = 5
count = count + 1  # Take current (5), add 1, store result (6)
print(count)       # Output: 6
```

Shorthand version:
```python
count += 1  # Same as: count = count + 1
```

---

## 🎯 Your Task

1. Start with `points = 0`
2. Add 10 to points using `+=`
3. Add 5 more to points using `+=`
4. Print the final value (should be 15)
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

## Assigning Multiple Variables

You can create several variables at once:

```python
# One per line (most clear)
name = "Alice"
age = 25
city = "New York"

# All on one line (for related values)
x, y, z = 10, 20, 30
```

## Swapping Variables

Sometimes you need to swap two values. Python makes this easy:

```python
a = 5
b = 10

# Swap them!
a, b = b, a

print(a)  # 10
print(b)  # 5
```

In other languages, you'd need a temporary variable. Python handles it elegantly!

## Using Variables Together

Variables can reference each other:

```python
price = 20
quantity = 3
total = price * quantity  # total is now 60

print(f"Total: ${total}")
```

---

## 🎯 Your Task

Create variables for a product's name, price, and quantity:
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
        # === STRINGS (4 exercises) ===
        {
            "id": 5,
            "title": "What are Strings?",
            "order": 5,
            "content": """# 📝 What is a String?

## Definition

A **string** is a sequence of characters (letters, numbers, symbols, spaces) surrounded by quotes. It's how we represent text in programming.

```python
message = "Hello, World!"
name = 'Alice'  # Single or double quotes both work
```

## Why Do We Need Strings?

Nearly every program works with text:
- User names, emails, addresses
- Messages and notifications
- File paths and URLs
- Any data that isn't purely numeric

## Types of Quotes

Python accepts three types:

```python
# Single quotes
greeting = 'Hello'

# Double quotes (same as single)
greeting = "Hello"

# Triple quotes (for multi-line text)
poem = \"\"\"Roses are red,
Violets are blue,
Python is awesome,
And so are you!\"\"\"
```

## When to Use Which?

```python
# Use double quotes if string contains single quote
sentence = "It's a beautiful day"

# Use single quotes if string contains double quote
html = '<div class="container">'
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
            "content": """# 🔗 Joining Strings Together

## What is Concatenation?

**Concatenation** means joining strings end-to-end. Use the `+` operator:

```python
first = "Hello"
second = "World"
combined = first + second
print(combined)  # HelloWorld
```

## Adding Spaces

Notice there's no automatic space! You must add it:

```python
combined = first + " " + second
print(combined)  # Hello World
```

## Why Use Concatenation?

Building messages with dynamic data:

```python
name = "Alice"
message = "Welcome, " + name + "!"
print(message)  # Welcome, Alice!
```

## Repeating Strings

Use `*` to repeat a string:

```python
line = "-" * 20
print(line)  # --------------------

cheer = "Hip " * 2 + "Hooray!"
print(cheer)  # Hip Hip Hooray!
```

---

## 🎯 Your Task

Given:
- `first_name` = `"Jane"`
- `last_name` = `"Smith"`

Create `full_name` by joining them with a space.
Then print: `Welcome, Jane Smith!`
""",
            "starter_code": "# Given names\nfirst_name = \"Jane\"\nlast_name = \"Smith\"\n\n# Join them into full_name\n\n\n# Print welcome message\n",
            "solution_code": "# Given names\nfirst_name = \"Jane\"\nlast_name = \"Smith\"\n\n# Join them into full_name\nfull_name = first_name + \" \" + last_name\n\n# Print welcome message\nprint(\"Welcome, \" + full_name + \"!\")",
            "expected_output": "Welcome, Jane Smith!",
            "xp": 10
        },
        {
            "id": 7,
            "title": "F-Strings (Formatted Strings)",
            "order": 7,
            "content": """# ✨ F-Strings: The Modern Way

## What are F-Strings?

F-strings (formatted string literals) let you embed variables directly in text. Just add `f` before the quote and put variables in `{}`:

```python
name = "Alice"
age = 25
message = f"My name is {name} and I'm {age} years old."
print(message)
# Output: My name is Alice and I'm 25 years old.
```

## Why F-Strings are Better

Compare concatenation vs f-strings:

```python
# Old way (messy)
message = "Hello, " + name + "! You have " + str(score) + " points."

# F-string way (clean!)
message = f"Hello, {name}! You have {score} points."
```

F-strings are:
- Easier to read
- Less error-prone
- No need to convert numbers to strings

## Expressions Inside F-Strings

You can put any expression in `{}`:

```python
price = 19.99
quantity = 3
print(f"Total: ${price * quantity}")  # Total: $59.97

# Formatting numbers
print(f"Price: ${price:.2f}")  # Price: $19.99 (2 decimal places)
```

---

## 🎯 Your Task

Given:
- `item` = `"Coffee"`
- `price` = `4.50`

Use an f-string to print: `Coffee costs $4.5`
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

## What are Methods?

Methods are **actions** you can perform on strings. Use dot notation: `string.method()`

## Common String Methods

```python
text = "Hello World"

text.upper()      # "HELLO WORLD"
text.lower()      # "hello world"
text.title()      # "Hello World"
text.strip()      # Removes whitespace from ends
text.replace("Hello", "Hi")  # "Hi World"
text.split(" ")   # ["Hello", "World"]
len(text)         # 11 (length - not a method, but useful!)
```

## Why These Are Useful

| Method | Use Case |
| --- | --- |
| `.upper()/.lower()` | Case-insensitive comparison |
| `.strip()` | Clean user input |
| `.replace()` | Find and replace text |
| `.split()` | Break text into parts |

## Example: Cleaning User Input

```python
user_input = "  Alice  "
clean_name = user_input.strip().title()
print(clean_name)  # "Alice"
```

## Chaining Methods

Methods return new strings, so you can chain them:

```python
messy = "   hELLo wORLD   "
clean = messy.strip().lower().title()
print(clean)  # "Hello World"
```

---

## 🎯 Your Task

Given: `messy_email = "  JOHN@EMAIL.COM  "`

Clean it up:
1. Remove extra spaces with `.strip()`
2. Convert to lowercase with `.lower()`
3. Print the result: `john@email.com`
""",
            "starter_code": "# Messy email\nmessy_email = \"  JOHN@EMAIL.COM  \"\n\n# Clean it: strip and lowercase\n\n\n# Print cleaned email\n",
            "solution_code": "# Messy email\nmessy_email = \"  JOHN@EMAIL.COM  \"\n\n# Clean it: strip and lowercase\nclean_email = messy_email.strip().lower()\n\n# Print cleaned email\nprint(clean_email)",
            "expected_output": "john@email.com",
            "xp": 10
        },
        # === NUMBERS (4 exercises) ===
        {
            "id": 9,
            "title": "Numbers: Integers and Floats",
            "order": 9,
            "content": """# 🔢 Numbers in Python

## Two Main Types of Numbers

Python has two types of numbers:

| Type | Definition | Examples |
| --- | --- | --- |
| **Integer (int)** | Whole numbers, no decimal | `10`, `-5`, `0`, `1000` |
| **Float** | Numbers with decimals | `3.14`, `-2.5`, `0.0` |

## Why Two Types?

- **Integers** are precise and faster (good for counting)
- **Floats** are needed for measurements, science, money

```python
count = 42       # Integer - exact count
price = 19.99    # Float - needs decimals
temperature = 98.6
```

## Python Auto-Detects the Type

```python
whole = 10      # Python sees int
decimal = 10.0  # Python sees float

# Check the type
print(type(whole))    # <class 'int'>
print(type(decimal))  # <class 'float'>
```

## Converting Between Types

```python
x = 10
y = float(x)    # 10.0 (now a float)

z = 10.7
w = int(z)      # 10 (decimals cut off, not rounded!)
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

## Basic Operations

Python supports all standard math:

| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 2` | `2.5` |
| `**` | Power | `5 ** 2` | `25` |
| `//` | Floor Division | `5 // 2` | `2` |
| `%` | Modulo (remainder) | `5 % 2` | `1` |

## Understanding Floor Division and Modulo

- `//` gives the **whole number** part of division
- `%` gives the **remainder**

```python
17 // 5  # 3 (17 goes into 5 three times)
17 % 5   # 2 (with 2 left over)
```

## Order of Operations (PEMDAS)

Python follows standard math order:
1. **P**arentheses `()`
2. **E**xponents `**`
3. **M**ultiplication & **D**ivision `* / // %`
4. **A**ddition & **S**ubtraction `+ -`

```python
result = 2 + 3 * 4      # 14 (not 20!)
result = (2 + 3) * 4    # 20 (parentheses first)
```

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
            "content": """# 📝 Shorthand Math Operations

## What is Compound Assignment?

Instead of writing `x = x + 5`, Python has shorter versions:

| Long Form | Shorthand | Meaning |
| --- | --- | --- |
| `x = x + 5` | `x += 5` | Add 5 to x |
| `x = x - 5` | `x -= 5` | Subtract 5 from x |
| `x = x * 5` | `x *= 5` | Multiply x by 5 |
| `x = x / 5` | `x /= 5` | Divide x by 5 |
| `x = x ** 2` | `x **= 2` | Square x |

## Why Use Shorthand?

1. Less typing
2. Clearer intent (you're modifying, not replacing)
3. Industry standard practice

```python
score = 0
score += 10   # Player earns 10 points
score += 25   # Player earns 25 more
score -= 5    # Player loses 5 points
print(score)  # 30
```

## Common Use: Counters and Accumulators

```python
# Counting
count = 0
count += 1
count += 1
count += 1
print(count)  # 3

# Running total
total = 0
total += 100
total += 50
total += 25
print(total)  # 175
```

---

## 🎯 Your Task

Simulate a game:
1. Start `health = 100`
2. Take 25 damage (use `-=`)
3. Heal 10 health (use `+=`)
4. Print final health (should be 85)
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
            "content": """# ⭕ Booleans: True or False

## What is a Boolean?

A **Boolean** (named after mathematician George Boole) can only be one of two values:
- `True`
- `False`

```python
is_sunny = True
is_raining = False
```

## Why Are Booleans Important?

Booleans are the foundation of **decision making** in code:

```python
is_adult = age >= 18
is_logged_in = True
has_permission = user_role == "admin"
```

We'll use these extensively in the Logic chapter!

## Type Conversion

You can convert between types:

```python
# To integer
int("42")       # 42
int(3.7)        # 3 (truncates, doesn't round!)

# To float
float("3.14")   # 3.14
float(5)        # 5.0

# To string
str(42)         # "42"
str(3.14)       # "3.14"

# To boolean
bool(1)         # True
bool(0)         # False
bool("")        # False (empty string)
bool("hello")   # True (non-empty string)
```

## Common Use: User Input

```python
# input() always returns a string!
age_text = "25"
age = int(age_text)  # Convert to number for math
```

---

## 🎯 Your Task

Given: `age_text = "25"`

1. Convert it to an integer using `int()`
2. Add 5 to get age in 5 years
3. Print the future age (should be 30)
""",
            "starter_code": "# Age as a string\nage_text = \"25\"\n\n# Convert to integer\n\n\n# Add 5 years\n\n\n# Print future age\n",
            "solution_code": "# Age as a string\nage_text = \"25\"\n\n# Convert to integer\nage = int(age_text)\n\n# Add 5 years\nfuture_age = age + 5\n\n# Print future age\nprint(future_age)",
            "expected_output": "30",
            "xp": 10
        }
    ]
}
