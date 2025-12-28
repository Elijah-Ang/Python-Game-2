# Chapter 3: Logic & Control Flow
# Enhanced with detailed definitions, explanations, and "why it matters"

CHAPTER_3 = {
    "id": 3,
    "title": "Logic & Control Flow",
    "slug": "python-logic",
    "icon": "🔀",
    "is_boss": False,
    "lessons": [
        {
            "id": 22,
            "title": "If Statements",
            "order": 1,
            "content": """# 🎯 If Statements: Making Decisions

## What is an If Statement?

An `if` statement lets your code make decisions. It runs code ONLY when a condition is True.

## Real-World Analogy

Think of a bouncer at a club:
- **IF** you're 21 or older → you can enter
- Otherwise → you're turned away

In Python:
```python
age = 25
if age >= 21:
    print("Welcome!")
```

## The Basic Syntax

```python
if condition:
    # This code runs if condition is True
    # Notice the indentation!
```

**Important**: The colon `:` and indentation are required!

## How Python Evaluates Conditions

Python checks if the condition is `True` or `False`:

```python
age = 20
if age >= 18:  # 20 >= 18 is True
    print("You're an adult!")  # This runs!

if age >= 21:  # 20 >= 21 is False
    print("You can drink!")  # This does NOT run
```

---

## 🎯 Your Task

Given `score = 85`:
- If score >= 70, print `"Pass"`
""",
            "starter_code": "score = 85\n\n# If score >= 70, print Pass\n",
            "solution_code": "score = 85\n\n# If score >= 70, print Pass\nif score >= 70:\n    print(\"Pass\")",
            "expected_output": "Pass",
            "xp": 10
        },
        {
            "id": 23,
            "title": "If-Else",
            "order": 2,
            "content": """# ⚖️ If-Else: Two Paths

## Adding an Alternative

What if you want to do something when the condition is False? Use `else`:

```python
if condition:
    # Runs if True
else:
    # Runs if False
```

## Example

```python
age = 15
if age >= 18:
    print("You can vote!")
else:
    print("Too young to vote")
# Output: Too young to vote
```

## Only ONE Path Runs

With if-else, exactly ONE block runs - never both, never neither:

```python
temperature = 75
if temperature > 80:
    print("Hot!")
else:
    print("Nice weather!")
# Output: Nice weather! (only this one runs)
```

## Common Mistake

Don't use two separate `if` statements when you want if-else:

```python
# WRONG - both might run!
if x > 0:
    print("Positive")
if x <= 0:
    print("Non-positive")

# RIGHT - only one runs
if x > 0:
    print("Positive")
else:
    print("Non-positive")
```

---

## 🎯 Your Task

Given `temperature = 35`:
- If temperature > 30, print `"Hot"`
- Else print `"Nice"`
""",
            "starter_code": "temperature = 35\n\n# Check if hot or nice\n",
            "solution_code": "temperature = 35\n\n# Check if hot or nice\nif temperature > 30:\n    print(\"Hot\")\nelse:\n    print(\"Nice\")",
            "expected_output": "Hot",
            "xp": 10
        },
        {
            "id": 24,
            "title": "If-Elif-Else",
            "order": 3,
            "content": """# 📊 Multiple Conditions with Elif

## When You Have More Than Two Options

`elif` (short for "else if") lets you check multiple conditions:

```python
if condition1:
    # First choice
elif condition2:
    # Second choice
elif condition3:
    # Third choice
else:
    # Default (if nothing else matches)
```

## Example: Letter Grades

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)  # B
```

## Order Matters!

Python checks conditions from top to bottom and stops at the first True:

```python
score = 95

# WRONG order - 95 >= 60 is True, so prints D!
if score >= 60: print("D")
elif score >= 70: print("C")
elif score >= 80: print("B")
elif score >= 90: print("A")

# CORRECT order - checks highest first
if score >= 90: print("A")
elif score >= 80: print("B")
elif score >= 70: print("C")
elif score >= 60: print("D")
```

---

## 🎯 Your Task

Given `score = 75`:
- >= 90: print `"A"`
- >= 80: print `"B"`
- >= 70: print `"C"`
- else: print `"F"`
""",
            "starter_code": "score = 75\n\n# Determine grade\n",
            "solution_code": "score = 75\n\n# Determine grade\nif score >= 90:\n    print(\"A\")\nelif score >= 80:\n    print(\"B\")\nelif score >= 70:\n    print(\"C\")\nelse:\n    print(\"F\")",
            "expected_output": "C",
            "xp": 10
        },
        {
            "id": 25,
            "title": "Comparison Operators",
            "order": 4,
            "content": """# ⚖️ Comparison Operators

## Comparing Values

Comparison operators compare two values and return `True` or `False`:

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater or equal | `5 >= 5` | `True` |
| `<=` | Less or equal | `5 <= 3` | `False` |

## Common Mistake: = vs ==

```python
# = is ASSIGNMENT (storing a value)
x = 5

# == is COMPARISON (checking equality)
if x == 5:
    print("x is five!")
```

## Comparing Strings

You can compare strings too:

```python
name = "Alice"
if name == "Alice":
    print("Hello, Alice!")

# Alphabetical comparison
"apple" < "banana"  # True (a comes before b)
```

---

## 🎯 Your Task

Given `a = 10` and `b = 10`:
Check if they are equal and print: `Equal: True`
""",
            "starter_code": "a = 10\nb = 10\n\n# Check if equal\nresult = a == b\nprint(f\"Equal: {result}\")",
            "solution_code": "a = 10\nb = 10\n\n# Check if equal\nresult = a == b\nprint(f\"Equal: {result}\")",
            "expected_output": "Equal: True",
            "xp": 10
        },
        {
            "id": 26,
            "title": "Logical AND",
            "order": 5,
            "content": """# 🔗 Logical AND

## Combining Conditions

`and` requires BOTH conditions to be True:

```python
if condition1 and condition2:
    # Runs only if BOTH are True
```

## Real-World Example

To enter a bar, you need to be 21+ AND have ID:

```python
age = 25
has_id = True

if age >= 21 and has_id:
    print("Welcome!")
else:
    print("Sorry, can't enter")
```

## Truth Table for AND

| A | B | A and B |
| --- | --- | --- |
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

Only True if BOTH are True!

## Multiple ANDs

You can chain multiple conditions:

```python
if age >= 18 and has_license and not is_suspended:
    print("You can drive!")
```

---

## 🎯 Your Task

Given:
- `age = 25`
- `has_ticket = True`

If age >= 18 AND has_ticket, print `"Can enter"`
""",
            "starter_code": "age = 25\nhas_ticket = True\n\n# Check both conditions\n",
            "solution_code": "age = 25\nhas_ticket = True\n\n# Check both conditions\nif age >= 18 and has_ticket:\n    print(\"Can enter\")",
            "expected_output": "Can enter",
            "xp": 10
        },
        {
            "id": 27,
            "title": "Logical OR",
            "order": 6,
            "content": """# 🔀 Logical OR

## Either Condition

`or` requires AT LEAST ONE condition to be True:

```python
if condition1 or condition2:
    # Runs if EITHER (or both) is True
```

## Real-World Example

Free shipping if order is $50+ OR member is premium:

```python
order_total = 35
is_premium = True

if order_total >= 50 or is_premium:
    print("Free shipping!")
else:
    print("Shipping: $5")
```

## Truth Table for OR

| A | B | A or B |
| --- | --- | --- |
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | **False** |

Only False if BOTH are False!

## Combining AND and OR

Use parentheses for clarity:

```python
if (is_weekend or is_holiday) and not is_working:
    print("Day off!")
```

---

## 🎯 Your Task

Given:
- `is_member = False`
- `has_coupon = True`

If is_member OR has_coupon, print `"Discount applied"`
""",
            "starter_code": "is_member = False\nhas_coupon = True\n\n# Check if either is true\n",
            "solution_code": "is_member = False\nhas_coupon = True\n\n# Check if either is true\nif is_member or has_coupon:\n    print(\"Discount applied\")",
            "expected_output": "Discount applied",
            "xp": 10
        },
        {
            "id": 28,
            "title": "Logical NOT",
            "order": 7,
            "content": """# ❌ Logical NOT

## Reversing Conditions

`not` flips True to False and False to True:

```python
is_raining = False
if not is_raining:
    print("No umbrella needed!")
```

## Truth Table for NOT

| A | not A |
| --- | --- |
| True | False |
| False | True |

## When to Use NOT

```python
# Instead of checking for False
if logged_in == False:  # Works but awkward
    print("Please log in")

# Use NOT (more Pythonic!)
if not logged_in:
    print("Please log in")
```

## NOT with Collections

```python
# Check if list is empty
items = []
if not items:  # Empty list is "falsy"
    print("Cart is empty!")

# Check if string is empty
name = ""
if not name:
    print("Name is required!")
```

---

## 🎯 Your Task

Given `is_blocked = False`:
If NOT blocked, print `"Welcome!"`
""",
            "starter_code": "is_blocked = False\n\n# If not blocked\n",
            "solution_code": "is_blocked = False\n\n# If not blocked\nif not is_blocked:\n    print(\"Welcome!\")",
            "expected_output": "Welcome!",
            "xp": 10
        },
        {
            "id": 29,
            "title": "Nested Conditionals",
            "order": 8,
            "content": """# 🪆 Nested If Statements

## If Inside If

You can put if statements inside other if statements:

```python
if has_account:
    if is_verified:
        print("Full access")
    else:
        print("Please verify your email")
else:
    print("Please create an account")
```

## When to Nest

Useful when second check only makes sense if first is True:

```python
if user_input:  # First check: did they enter anything?
    if user_input.isdigit():  # Only check this if there's input
        print("Valid number!")
    else:
        print("Not a number")
else:
    print("No input provided")
```

## Avoid Deep Nesting

Too many levels becomes hard to read:

```python
# BAD - too nested!
if a:
    if b:
        if c:
            if d:
                do_something()

# BETTER - use AND
if a and b and c and d:
    do_something()
```

---

## 🎯 Your Task

Given:
- `logged_in = True`
- `is_admin = True`

If logged_in, check if is_admin:
- If admin: print `"Admin panel"`
- Else: print `"User dashboard"`
""",
            "starter_code": "logged_in = True\nis_admin = True\n\n# Nested check\n",
            "solution_code": "logged_in = True\nis_admin = True\n\n# Nested check\nif logged_in:\n    if is_admin:\n        print(\"Admin panel\")\n    else:\n        print(\"User dashboard\")",
            "expected_output": "Admin panel",
            "xp": 10
        },
        {
            "id": 30,
            "title": "Ternary Operator",
            "order": 9,
            "content": """# ⚡ One-Line Conditionals

## The Ternary Operator

Python has a shorthand for simple if-else:

```python
value_if_true if condition else value_if_false
```

## Example

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult
```

This is equivalent to:
```python
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

## When to Use

✅ Good for simple, short conditions:
```python
result = "Pass" if score >= 70 else "Fail"
message = f"Welcome, {name}!" if name else "Welcome, Guest!"
```

❌ Avoid for complex logic:
```python
# Too complex for ternary - use regular if-else
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
```

---

## 🎯 Your Task

Given `points = 150`:
Set `level` to `"Gold"` if points >= 100, else `"Silver"`.
Print the level.
""",
            "starter_code": "points = 150\n\n# Set level using ternary\n\n\n# Print level\n",
            "solution_code": "points = 150\n\n# Set level using ternary\nlevel = \"Gold\" if points >= 100 else \"Silver\"\n\n# Print level\nprint(level)",
            "expected_output": "Gold",
            "xp": 10
        }
    ]
}
