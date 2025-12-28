# Chapter 4: Functions
# Enhanced with detailed definitions, explanations, and "why it matters"

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

## What is a Function?

A **function** is a reusable block of code that performs a specific task. Instead of writing the same code over and over, you define it once and call it whenever needed.

## Real-World Analogy

Think of a function like a **recipe**:
- You write the recipe once
- Every time you want that dish, you follow the same recipe
- You don't have to figure it out from scratch each time!

## Why Use Functions?

1. **Reusability**: Write once, use many times
2. **Organization**: Break complex code into manageable pieces
3. **Readability**: Give meaningful names to code blocks
4. **Maintenance**: Fix bugs in one place

## Defining a Function

```python
def function_name():
    # Code inside the function
    print("Hello from the function!")
```

- `def` keyword starts the definition
- `function_name` is what you call it
- `():` parentheses and colon are required
- Indented code is the function body

## Calling a Function

The function doesn't run until you **call** it:

```python
def greet():
    print("Hello!")

greet()  # Call the function - output: Hello!
greet()  # Call it again!
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
            "content": """# 📥 Parameters: Passing Data to Functions

## What are Parameters?

Parameters let you pass data INTO a function. They're like ingredients for a recipe - different ingredients, different results!

```python
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

## Parameters vs Arguments

| Term | Definition |
| --- | --- |
| **Parameter** | Variable in function definition |
| **Argument** | Actual value passed when calling |

```python
def greet(name):    # 'name' is the PARAMETER
    print(f"Hello, {name}!")

greet("Alice")      # "Alice" is the ARGUMENT
```

## Multiple Parameters

Functions can have multiple parameters:

```python
def add(a, b):
    result = a + b
    print(result)

add(5, 3)  # Output: 8
add(10, 20)  # Output: 30
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
            "content": """# 📤 Return Values: Getting Data Back

## What is Return?

`return` sends a value back to where the function was called. This value can be stored, used in calculations, or printed.

```python
def add(a, b):
    return a + b  # Send the result back

result = add(5, 3)  # result now equals 8
print(result)       # Output: 8
```

## Return vs Print

| `print()` | `return` |
| --- | --- |
| Shows output to screen | Sends value back to caller |
| Value is lost after printing | Value can be used further |
| Debugging/user display | Building blocks for programs |

```python
# With print - can't use the result
def add_print(a, b):
    print(a + b)

x = add_print(5, 3)  # Prints 8, but x is None!

# With return - can use the result
def add_return(a, b):
    return a + b

y = add_return(5, 3)  # y equals 8
z = y * 2             # z equals 16
```

## Return Ends the Function

Code after `return` doesn't run:

```python
def example():
    return "Done"
    print("This never runs!")  # Unreachable!
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
            "content": """# 📊 Working with Multiple Parameters

## Functions with Several Inputs

Functions often need multiple pieces of data:

```python
def calculate_area(width, height):
    return width * height

area = calculate_area(5, 3)
print(area)  # 15
```

## Order Matters (Positional Arguments)

Arguments are matched to parameters by position:

```python
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet("John", "Doe")    # Hello, John Doe!
greet("Doe", "John")    # Hello, Doe John! (wrong order!)
```

## Practical Example

```python
def create_email(username, domain):
    return f"{username}@{domain}"

email = create_email("alice", "gmail.com")
print(email)  # alice@gmail.com
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
            "content": """# ⚙️ Default Parameter Values

## What are Default Values?

You can give parameters default values. If no argument is passed, the default is used:

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet()         # Hello, Guest! (uses default)
```

## Why Use Defaults?

- Make functions more flexible
- Reduce required arguments
- Provide sensible fallbacks

## Rules for Default Parameters

Default parameters must come AFTER non-default ones:

```python
# CORRECT - default at the end
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# ERROR - default before non-default
def greet(greeting="Hello", name):  # SyntaxError!
    print(f"{greeting}, {name}!")
```

---

## 🎯 Your Task

Define `power(base, exp=2)` that returns `base ** exp`.
Call it with just `4` (should return 16 since exp defaults to 2).
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

## What are Keyword Arguments?

You can specify arguments by name, not just position:

```python
def greet(name, greeting):
    print(f"{greeting}, {name}!")

# Using keyword arguments
greet(name="Alice", greeting="Hi")
greet(greeting="Hello", name="Bob")  # Order doesn't matter!
```

## Why Use Keyword Arguments?

1. **Clarity**: Makes code more readable
2. **Flexibility**: Call in any order
3. **Skip defaults**: Override only specific defaults

```python
def create_user(name, age, email, is_admin=False):
    # ...
    
# Skip to the argument you need
create_user("Alice", 25, "a@b.com", is_admin=True)
```

## Mixing Positional and Keyword

Positional arguments must come before keyword arguments:

```python
def func(a, b, c):
    print(a, b, c)

func(1, 2, c=3)      # OK
func(1, b=2, c=3)    # OK
func(a=1, 2, 3)      # ERROR!
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
            "content": """# ⚡ Lambda Functions: One-Line Functions

## What is a Lambda?

A **lambda** is a small anonymous function defined in one line:

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2
```

## Lambda Syntax

```python
lambda arguments: expression
```

- No `def` or `return` keywords
- Expression is automatically returned
- Can have multiple arguments

## Examples

```python
# One argument
double = lambda x: x * 2
print(double(5))  # 10

# Two arguments
add = lambda a, b: a + b
print(add(3, 4))  # 7

# Conditional
is_adult = lambda age: "Adult" if age >= 18 else "Minor"
print(is_adult(20))  # Adult
```

## When to Use Lambda

- Short, simple operations
- Passing to other functions (like `sort`, `map`, `filter`)
- One-time use functions

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
            "content": """# 📝 Documenting Functions with Docstrings

## What is a Docstring?

A **docstring** is a string that describes what your function does. It goes right after the function definition:

```python
def add(a, b):
    \"\"\"Returns the sum of a and b.\"\"\"
    return a + b
```

## Why Write Docstrings?

1. Help other developers understand your code
2. Remind yourself what the function does
3. Tools can auto-generate documentation
4. Shows up in `help()` function!

```python
help(add)
# Output:
# add(a, b)
#     Returns the sum of a and b.
```

## Multi-line Docstrings

For more complex functions:

```python
def calculate_tip(bill, tip_percent=15):
    \"\"\"
    Calculate the tip amount for a bill.
    
    Args:
        bill: Total bill amount
        tip_percent: Tip percentage (default 15)
    
    Returns:
        The tip amount as a float
    \"\"\"
    return bill * (tip_percent / 100)
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
            "title": "Variable Scope",
            "order": 9,
            "content": """# 🔭 Variable Scope

## What is Scope?

**Scope** determines where a variable can be accessed. Variables created inside a function only exist inside that function!

```python
def my_function():
    x = 10  # Local variable - only exists inside function
    print(x)

my_function()  # Output: 10
print(x)       # ERROR! x doesn't exist here
```

## Local vs Global

| Type | Where Created | Where Accessible |
| --- | --- | --- |
| **Local** | Inside a function | Only that function |
| **Global** | Outside all functions | Everywhere |

```python
y = 20  # Global variable

def show():
    print(y)  # Can read global variable

show()  # Output: 20
```

## Shadowing

A local variable can have the same name as a global (but it's a different variable!):

```python
x = 100  # Global

def test():
    x = 5  # Local - different variable!
    print(x)  # 5

test()
print(x)  # 100 (global unchanged)
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
