# Chapter 4: Functions
# Each exercise has specific data and exact expected output

CHAPTER_4 = {
    "id": 4,
    "title": "Functions",
    "slug": "python-functions",
    "icon": "⚙️",
    "is_boss": False,
    "lessons": [
        {
            "id": 31,
            "title": "Defining Functions",
            "order": 1,
            "content": """# 🔧 Creating Functions

Functions are reusable blocks of code:

```python
def greet():
    print("Hello!")

greet()  # Call the function
```

---

## 🎯 Your Task

Define a function called `say_hello` that prints `"Hello, World!"`.
Then call it.
""",
            "starter_code": "# Define the function\n\n\n# Call the function\n",
            "solution_code": "# Define the function\ndef say_hello():\n    print(\"Hello, World!\")\n\n# Call the function\nsay_hello()",
            "expected_output": "Hello, World!",
            "xp": 10
        },
        {
            "id": 32,
            "title": "Function Parameters",
            "order": 2,
            "content": """# 📥 Parameters

Functions can receive data:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

---

## 🎯 Your Task

Define `greet(name)` that prints `"Welcome, {name}!"`.
Call it with `"Python"`.
""",
            "starter_code": "# Define greet with name parameter\n\n\n# Call with \"Python\"\n",
            "solution_code": "# Define greet with name parameter\ndef greet(name):\n    print(f\"Welcome, {name}!\")\n\n# Call with \"Python\"\ngreet(\"Python\")",
            "expected_output": "Welcome, Python!",
            "xp": 10
        },
        {
            "id": 33,
            "title": "Return Values",
            "order": 3,
            "content": """# 📤 Return Values

Functions can return data:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

---

## 🎯 Your Task

Define `double(n)` that returns `n * 2`.
Call it with `7` and print the result.
""",
            "starter_code": "# Define double function\n\n\n# Call with 7 and print\n",
            "solution_code": "# Define double function\ndef double(n):\n    return n * 2\n\n# Call with 7 and print\nresult = double(7)\nprint(result)",
            "expected_output": "14",
            "xp": 10
        },
        {
            "id": 34,
            "title": "Multiple Parameters",
            "order": 4,
            "content": """# 📊 Multiple Parameters

```python
def add(a, b, c):
    return a + b + c
```

---

## 🎯 Your Task

Define `calculate_area(width, height)` that returns `width * height`.
Call it with `5` and `3`, print the result.
""",
            "starter_code": "# Define calculate_area\n\n\n# Call with 5, 3 and print\n",
            "solution_code": "# Define calculate_area\ndef calculate_area(width, height):\n    return width * height\n\n# Call with 5, 3 and print\narea = calculate_area(5, 3)\nprint(area)",
            "expected_output": "15",
            "xp": 10
        },
        {
            "id": 35,
            "title": "Default Parameters",
            "order": 5,
            "content": """# ⚙️ Default Values

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Hello, Guest!
greet("Alice")  # Hello, Alice!
```

---

## 🎯 Your Task

Define `power(base, exp=2)` that returns `base ** exp`.
Call it with just `4` (should return 16).
""",
            "starter_code": "# Define power with default exp=2\n\n\n# Call with just 4\n",
            "solution_code": "# Define power with default exp=2\ndef power(base, exp=2):\n    return base ** exp\n\n# Call with just 4\nresult = power(4)\nprint(result)",
            "expected_output": "16",
            "xp": 10
        },
        {
            "id": 36,
            "title": "Keyword Arguments",
            "order": 6,
            "content": """# 🏷️ Keyword Arguments

Name your arguments when calling:

```python
def info(name, age):
    print(f"{name} is {age}")

info(age=25, name="Alice")
```

---

## 🎯 Your Task

Define `describe(item, price)` that prints `"{item}: ${price}"`.
Call it with keyword arguments: `price=9.99, item="Book"`.
""",
            "starter_code": "# Define describe\n\n\n# Call with keyword arguments\n",
            "solution_code": "# Define describe\ndef describe(item, price):\n    print(f\"{item}: ${price}\")\n\n# Call with keyword arguments\ndescribe(price=9.99, item=\"Book\")",
            "expected_output": "Book: $9.99",
            "xp": 10
        },
        {
            "id": 37,
            "title": "Lambda Functions",
            "order": 7,
            "content": """# ⚡ Lambda Functions

One-line anonymous functions:

```python
square = lambda x: x ** 2
print(square(5))  # 25
```

---

## 🎯 Your Task

Create a lambda function `triple` that multiplies by 3.
Call it with `10` and print the result.
""",
            "starter_code": "# Create lambda triple\n\n\n# Call with 10\n",
            "solution_code": "# Create lambda triple\ntriple = lambda x: x * 3\n\n# Call with 10\nprint(triple(10))",
            "expected_output": "30",
            "xp": 10
        },
        {
            "id": 38,
            "title": "Docstrings",
            "order": 8,
            "content": """# 📝 Documenting Functions

Add docstrings to explain your function:

```python
def add(a, b):
    \"\"\"Returns the sum of a and b.\"\"\"
    return a + b
```

---

## 🎯 Your Task

Define `multiply(a, b)` with a docstring.
Return `a * b` and call with `6, 7`.
""",
            "starter_code": "# Define multiply with docstring\n\n\n# Call with 6, 7\n",
            "solution_code": "# Define multiply with docstring\ndef multiply(a, b):\n    \"\"\"Returns the product of a and b.\"\"\"\n    return a * b\n\n# Call with 6, 7\nprint(multiply(6, 7))",
            "expected_output": "42",
            "xp": 10
        },
        {
            "id": 39,
            "title": "Scope",
            "order": 9,
            "content": """# 🔭 Variable Scope

Variables inside functions are local:

```python
def my_func():
    x = 10  # Local to function
    print(x)

my_func()
```

---

## 🎯 Your Task

Define a function `show_secret()` that:
1. Creates a local variable `secret = "Python rocks!"`
2. Prints it

Call the function.
""",
            "starter_code": "# Define show_secret\n\n\n# Call it\n",
            "solution_code": "# Define show_secret\ndef show_secret():\n    secret = \"Python rocks!\"\n    print(secret)\n\n# Call it\nshow_secret()",
            "expected_output": "Python rocks!",
            "xp": 10
        }
    ]
}
