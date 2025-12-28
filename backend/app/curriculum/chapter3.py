# Chapter 3: Logic & Control Flow
# Each exercise has specific data and exact expected output

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
            "content": """# 🎯 If Statements

Execute code only if a condition is True:

```python
age = 20
if age >= 18:
    print("Adult")
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
            "content": """# ⚖️ If-Else

Do one thing or another:

```python
if condition:
    # if True
else:
    # if False
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
            "content": """# 📊 Multiple Conditions

Use `elif` for multiple checks:

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
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

| Operator | Meaning |
| --- | --- |
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater or equal |
| `<=` | Less or equal |

---

## 🎯 Your Task

Given `a = 10` and `b = 10`:
Print whether they are equal.
Print: `Equal: True`
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

`and` - Both must be True:

```python
if age >= 18 and has_license:
    print("Can drive")
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

`or` - At least one must be True:

```python
if is_weekend or is_holiday:
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

`not` - Reverses the condition:

```python
if not is_banned:
    print("Access granted")
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

If statements inside if statements:

```python
if has_account:
    if is_verified:
        print("Full access")
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

Ternary operator: `value_if_true if condition else value_if_false`

```python
status = "Adult" if age >= 18 else "Minor"
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
