"""
Script to add new OOP and Error Handling chapters to the Python curriculum.
This will update both lessons.json and course-python-basics.json.
"""
import json
import os

# Define paths
LESSONS_PATH = "/Users/elijahang/Python-Game-2/frontend/public/data/lessons.json"
COURSE_PATH = "/Users/elijahang/Python-Game-2/frontend/public/data/course-python-basics.json"

# Define OOP lessons (IDs 300-311)
OOP_LESSONS = {
    "300": {
        "id": 300,
        "title": "What is Object-Oriented Programming?",
        "content": """# 🎯 What is Object-Oriented Programming?

## The Big Idea

**Object-Oriented Programming (OOP)** is a way of organizing code around "objects" - bundles of data and behavior that model real-world things.

## Real-World Analogy

Think about a **car**:
- **Attributes** (data): color, brand, speed, fuel level
- **Behaviors** (methods): start(), drive(), brake(), refuel()

In OOP, we create a "Car" class that defines these attributes and behaviors, then create individual car objects.

## Why OOP?

| Benefit | Description |
| --- | --- |
| **Organization** | Group related data and functions together |
| **Reusability** | Create templates (classes) and reuse them |
| **Modularity** | Change one part without breaking others |
| **Real-world modeling** | Code mirrors how we think about things |

## Procedural vs Object-Oriented

```python
# Procedural: functions with separate data
name = "Alice"
balance = 1000
def deposit(amount):
    global balance
    balance += amount

# OOP: data and functions bundled together
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
```

---

## 🎯 Your Task

Print "OOP organizes code around objects!" to confirm you understand the concept.
""",
        "starter_code": "# Print the OOP motto\n",
        "solution_code": '# Print the OOP motto\nprint("OOP organizes code around objects!")',
        "expected_output": "OOP organizes code around objects!",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    },
    "301": {
        "id": 301,
        "title": "Creating a Class",
        "content": """# 🏗️ Creating Your First Class

## What is a Class?

A **class** is a blueprint for creating objects. It defines what attributes and methods objects will have.

## Basic Class Syntax

```python
class Dog:
    pass  # Empty class for now
```

- `class` keyword starts the definition
- Class names use **PascalCase** (capitalize each word)
- `:` and indentation like functions

## Creating an Object (Instance)

```python
class Dog:
    pass

my_dog = Dog()  # Create an instance
print(type(my_dog))  # <class '__main__.Dog'>
```

## Adding Attributes

```python
class Dog:
    pass

my_dog = Dog()
my_dog.name = "Buddy"  # Add attribute
my_dog.age = 3
print(f"{my_dog.name} is {my_dog.age} years old")
```

## Multiple Instances

Each object is independent:

```python
dog1 = Dog()
dog1.name = "Buddy"

dog2 = Dog()
dog2.name = "Max"

print(dog1.name)  # Buddy
print(dog2.name)  # Max
```

---

## 🎯 Your Task

Create a class called `Cat`. Create an instance called `my_cat`, give it a `name` attribute of "Whiskers", and print the name.
""",
        "starter_code": "# Define Cat class\n\n\n# Create instance and set name\n\n\n# Print name\n",
        "solution_code": '''# Define Cat class
class Cat:
    pass

# Create instance and set name
my_cat = Cat()
my_cat.name = "Whiskers"

# Print name
print(my_cat.name)''',
        "expected_output": "Whiskers",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    },
    "302": {
        "id": 302,
        "title": "The __init__ Method",
        "content": """# 🎬 The __init__ Method (Constructor)

## The Problem

Adding attributes after creation is tedious:

```python
dog = Dog()
dog.name = "Buddy"
dog.age = 3
dog.breed = "Golden"  # So much typing!
```

## The Solution: __init__

The `__init__` method runs automatically when you create an object:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Now creation is clean!
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Buddy
```

## How __init__ Works

1. You call `Dog("Buddy", 3)`
2. Python creates a new Dog object
3. Calls `__init__(self, "Buddy", 3)` automatically
4. `self` refers to the new object being created
5. Attributes are attached to `self`

## The `self` Parameter

`self` is a reference to the current instance:

```python
class Dog:
    def __init__(self, name):
        self.name = name  # self.name is the attribute
                          # name is the parameter
```

Always the first parameter in methods!

---

## 🎯 Your Task

Create a `Person` class with `__init__` that takes `name` and `age`. Create person "Alice" age 25, print their name.
""",
        "starter_code": "# Define Person class with __init__\n\n\n# Create person and print name\n",
        "solution_code": '''# Define Person class with __init__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create person and print name
alice = Person("Alice", 25)
print(alice.name)''',
        "expected_output": "Alice",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    },
    "303": {
        "id": 303,
        "title": "Instance Methods",
        "content": """# ⚙️ Instance Methods

## What are Methods?

**Methods** are functions that belong to a class. They can access and modify the object's data.

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says Woof!")
    
    def greet(self, person):
        print(f"{self.name} greets {person}!")
```

## Calling Methods

```python
my_dog = Dog("Buddy")
my_dog.bark()           # Buddy says Woof!
my_dog.greet("Alice")   # Buddy greets Alice!
```

## self in Methods

`self` gives access to the object's attributes:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"New balance: ${self.balance}")
    
    def get_balance(self):
        return self.balance
```

## Methods Can Return Values

```python
account = BankAccount(100)
account.deposit(50)           # New balance: $150
print(account.get_balance())  # 150
```

---

## 🎯 Your Task

Create a `Calculator` class with a `square` method that takes a number and returns its square. Test with 5.
""",
        "starter_code": "# Define Calculator class with square method\n\n\n# Create calculator and test\n",
        "solution_code": '''# Define Calculator class with square method
class Calculator:
    def square(self, n):
        return n ** 2

# Create calculator and test
calc = Calculator()
print(calc.square(5))''',
        "expected_output": "25",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    },
    "304": {
        "id": 304,
        "title": "Class Attributes vs Instance Attributes",
        "content": """# 📊 Class vs Instance Attributes

## Two Types of Attributes

| Type | Belongs To | Shared? |
| --- | --- | --- |
| **Instance** | Each object | No - unique per object |
| **Class** | The class itself | Yes - shared by all |

## Instance Attributes

Defined in `__init__`, unique to each object:

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute

dog1 = Dog("Buddy")
dog2 = Dog("Max")
# Each dog has its own name
```

## Class Attributes

Defined outside `__init__`, shared by all:

```python
class Dog:
    species = "Canis familiaris"  # Class attribute
    
    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris (same!)
```

## Use Case: Counting Instances

```python
class Dog:
    count = 0  # Class attribute
    
    def __init__(self, name):
        self.name = name
        Dog.count += 1  # Increment class attribute

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(Dog.count)  # 2
```

---

## 🎯 Your Task

Create a `Student` class with a class attribute `school = "Python Academy"` and instance attribute `name`. Print the school.
""",
        "starter_code": "# Define Student with class and instance attributes\n\n\n# Create student and print school\n",
        "solution_code": '''# Define Student with class and instance attributes
class Student:
    school = "Python Academy"
    
    def __init__(self, name):
        self.name = name

# Create student and print school
student = Student("Alice")
print(student.school)''',
        "expected_output": "Python Academy",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    },
    "305": {
        "id": 305,
        "title": "Inheritance Basics",
        "content": """# 👨‍👩‍👧 Inheritance: Building on Existing Classes

## What is Inheritance?

**Inheritance** lets a class inherit attributes and methods from another class.

- **Parent class** (superclass): The class being inherited from
- **Child class** (subclass): The class that inherits

## Basic Syntax

```python
class Animal:  # Parent
    def speak(self):
        print("Some sound")

class Dog(Animal):  # Child inherits from Animal
    pass

my_dog = Dog()
my_dog.speak()  # "Some sound" - inherited!
```

## Why Use Inheritance?

1. **Code reuse**: Don't repeat common code
2. **Hierarchy**: Model "is-a" relationships
3. **Specialization**: Add features to base classes

## Real Example

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} is starting")

class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

my_car = Car("Toyota")
my_car.start()  # Inherited from Vehicle
my_car.honk()   # Defined in Car
```

---

## 🎯 Your Task

Create `Animal` class with a `move` method that prints "Moving...". Create `Dog` that inherits from `Animal`. Make a dog and call `move()`.
""",
        "starter_code": "# Define Animal class\n\n\n# Define Dog that inherits from Animal\n\n\n# Create dog and move\n",
        "solution_code": '''# Define Animal class
class Animal:
    def move(self):
        print("Moving...")

# Define Dog that inherits from Animal
class Dog(Animal):
    pass

# Create dog and move
dog = Dog()
dog.move()''',
        "expected_output": "Moving...",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    },
    "306": {
        "id": 306,
        "title": "Method Overriding",
        "content": """# 🔄 Method Overriding

## Customizing Inherited Behavior

A child class can **override** a parent's method by defining it again:

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):  # Override!
        print("Woof!")

class Cat(Animal):
    def speak(self):  # Override!
        print("Meow!")

dog = Dog()
dog.speak()  # Woof!

cat = Cat()
cat.speak()  # Meow!
```

## How It Works

When you call a method:
1. Python first looks in the object's class
2. If not found, looks in parent class
3. Uses the first match found

## Using super() to Call Parent

Sometimes you want to extend, not replace:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent's __init__
        self.breed = breed
```

---

## 🎯 Your Task

Create `Shape` with `area()` returning 0. Create `Square(Shape)` that overrides `area()` to return `side * side`. Test with side=4.
""",
        "starter_code": "# Define Shape class\n\n\n# Define Square that overrides area\n\n\n# Test\n",
        "solution_code": '''# Define Shape class
class Shape:
    def area(self):
        return 0

# Define Square that overrides area
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

# Test
sq = Square(4)
print(sq.area())''',
        "expected_output": "16",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    },
    "307": {
        "id": 307,
        "title": "The super() Function",
        "content": """# 🦸 The super() Function

## Why super()?

`super()` lets you call methods from the parent class. Essential for:
- Extending `__init__` without rewriting
- Adding to parent behavior instead of replacing

## Using super() in __init__

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # Initialize parent
        self.student_id = student_id

s = Student("Alice", "A123")
print(s.name)        # Alice (from Person)
print(s.student_id)  # A123 (from Student)
```

## Extending Other Methods

```python
class Animal:
    def speak(self):
        print("*makes sound*")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call parent first
        print("Woof!")   # Then add more

dog = Dog()
dog.speak()
# *makes sound*
# Woof!
```

## Common Pattern

```python
class Parent:
    def method(self):
        # Base behavior
        pass

class Child(Parent):
    def method(self):
        super().method()  # Keep parent behavior
        # Add child-specific behavior
```

---

## 🎯 Your Task

Create `Employee` with `__init__(name)`. Create `Manager(Employee)` with `__init__(name, department)` using super(). Print manager's name.
""",
        "starter_code": "# Define Employee\n\n\n# Define Manager using super()\n\n\n# Test\n",
        "solution_code": '''# Define Employee
class Employee:
    def __init__(self, name):
        self.name = name

# Define Manager using super()
class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

# Test
m = Manager("Alice", "Engineering")
print(m.name)''',
        "expected_output": "Alice",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    },
    "308": {
        "id": 308,
        "title": "Encapsulation",
        "content": """# 🔒 Encapsulation: Protecting Data

## What is Encapsulation?

**Encapsulation** means bundling data with methods, and controlling access to internal state.

## Private Attributes (Convention)

In Python, prefix with `_` or `__`:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # "Private" - don't touch!
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def get_balance(self):
        return self._balance
```

## Why Encapsulate?

1. **Validation**: Control how data is changed
2. **Safety**: Prevent invalid states
3. **Flexibility**: Change internals without breaking code

## Getter and Setter Pattern

```python
class Person:
    def __init__(self, age):
        self._age = age
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age must be positive!")

p = Person(25)
p.set_age(-5)  # "Age must be positive!"
p.set_age(30)  # Works!
```

---

## 🎯 Your Task

Create a `Counter` class with a private `_count` starting at 0. Add `increment()` and `get_count()` methods. Increment twice and print count.
""",
        "starter_code": "# Define Counter with encapsulation\n\n\n# Test\n",
        "solution_code": '''# Define Counter with encapsulation
class Counter:
    def __init__(self):
        self._count = 0
    
    def increment(self):
        self._count += 1
    
    def get_count(self):
        return self._count

# Test
c = Counter()
c.increment()
c.increment()
print(c.get_count())''',
        "expected_output": "2",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    },
    "309": {
        "id": 309,
        "title": "Polymorphism",
        "content": """# 🎭 Polymorphism: Many Forms

## What is Polymorphism?

**Polymorphism** means "many forms" - the same interface can work with different types.

## Example: Same Method, Different Behavior

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

# Same interface, different results
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    print(animal.speak())
# Woof!
# Meow!
# Quack!
```

## Why Polymorphism Matters

Write code that works with **any** object that has the right methods:

```python
def make_speak(animal):
    print(animal.speak())

make_speak(Dog())   # Works!
make_speak(Cat())   # Works!
make_speak(Duck())  # Works!
```

## Duck Typing

Python's philosophy: "If it walks like a duck and quacks like a duck, it's a duck."

We don't check types - we just use methods. If it has `speak()`, we can use it!

---

## 🎯 Your Task

Create `Circle` and `Rectangle` classes, each with `describe()`. Circle says "I am a circle", Rectangle says "I am a rectangle". Loop through a list and call describe on each.
""",
        "starter_code": "# Define shapes with describe method\n\n\n# Create list and loop\n",
        "solution_code": '''# Define shapes with describe method
class Circle:
    def describe(self):
        print("I am a circle")

class Rectangle:
    def describe(self):
        print("I am a rectangle")

# Create list and loop
shapes = [Circle(), Rectangle()]
for shape in shapes:
    shape.describe()''',
        "expected_output": "I am a circle\nI am a rectangle",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    },
    "310": {
        "id": 310,
        "title": "The __str__ Method",
        "content": """# 📝 The __str__ Method

## Making Objects Printable

By default, printing an object shows unhelpful info:

```python
class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("Buddy")
print(dog)  # <__main__.Dog object at 0x...>
```

## Define __str__ for Nice Output

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Dog({self.name}, {self.age} years)"

dog = Dog("Buddy", 3)
print(dog)  # Dog(Buddy, 3 years)
```

## When __str__ is Called

- `print(obj)`
- `str(obj)`
- f-strings: `f"{obj}"`

## Real Example

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

p = Product("Coffee", 4.99)
print(p)  # Coffee: $4.99
```

---

## 🎯 Your Task

Create a `Book` class with `title` and `author`. Add `__str__` to return "Title by Author". Create a book and print it.
""",
        "starter_code": "# Define Book with __str__\n\n\n# Test\n",
        "solution_code": '''# Define Book with __str__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"

# Test
book = Book("Python 101", "John Doe")
print(book)''',
        "expected_output": "Python 101 by John Doe",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    },
    "311": {
        "id": 311,
        "title": "OOP Challenge: Build a Library",
        "content": """# 📚 OOP Challenge: Build a Library System

## Put It All Together!

Let's build a mini library system using everything you've learned:
- Classes and objects
- __init__ and __str__
- Instance methods
- Encapsulation

## The Challenge

Create:
1. A `Book` class with title and available status
2. A `Library` class that manages books

```python
# Expected usage:
library = Library()
library.add_book("Python 101")
library.add_book("Data Science Guide")
library.list_books()
# Available: Python 101
# Available: Data Science Guide

library.checkout("Python 101")
library.list_books()
# Checked out: Python 101
# Available: Data Science Guide
```

## Hints

- Library needs a list to store books
- Book needs a way to track if it's checked out
- Use methods to modify state

---

## 🎯 Your Task

Create the Library system. Add 2 books, list them.
""",
        "starter_code": '''# Define Book class
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True
    
    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"{status}: {self.title}"

# Define Library class
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title):
        self.books.append(Book(title))
    
    def list_books(self):
        for book in self.books:
            print(book)

# Test the system
library = Library()
library.add_book("Python 101")
library.add_book("Data Science Guide")
library.list_books()
''',
        "solution_code": '''# Define Book class
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True
    
    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"{status}: {self.title}"

# Define Library class
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title):
        self.books.append(Book(title))
    
    def list_books(self):
        for book in self.books:
            print(book)

# Test the system
library = Library()
library.add_book("Python 101")
library.add_book("Data Science Guide")
library.list_books()''',
        "expected_output": "Available: Python 101\nAvailable: Data Science Guide",
        "chapter_id": 12,
        "chapter_title": "Object-Oriented Programming"
    }
}

# Error Handling lessons (IDs 320-325)
ERROR_HANDLING_LESSONS = {
    "320": {
        "id": 320,
        "title": "What are Exceptions?",
        "content": """# ⚠️ What are Exceptions?

## When Things Go Wrong

An **exception** is an error that occurs during program execution:

```python
print(10 / 0)  # ZeroDivisionError!
print(int("abc"))  # ValueError!
my_list[100]  # IndexError!
```

## Common Exceptions

| Exception | Cause |
| --- | --- |
| `ZeroDivisionError` | Dividing by zero |
| `TypeError` | Wrong type operation |
| `ValueError` | Right type, wrong value |
| `IndexError` | List index out of range |
| `KeyError` | Dict key not found |
| `FileNotFoundError` | File doesn't exist |

## Why Handle Exceptions?

Without handling, your program crashes:

```python
print("Starting...")
print(10 / 0)  # CRASH!
print("This never runs")
```

With handling, you can recover gracefully!

---

## 🎯 Your Task

Run code that causes a `ZeroDivisionError`. Print "Attempting division..." before it.
""",
        "starter_code": '# This will cause an error\nprint("Attempting division...")\nprint(10 / 0)',
        "solution_code": '# This will cause an error\nprint("Attempting division...")\n# print(10 / 0)  # Would crash!\nprint("Error: Cannot divide by zero!")',
        "expected_output": "Attempting division...\nError: Cannot divide by zero!",
        "chapter_id": 13,
        "chapter_title": "Error Handling"
    },
    "321": {
        "id": 321,
        "title": "Try-Except Blocks",
        "content": """# 🛡️ Try-Except: Catching Errors

## The Try-Except Pattern

```python
try:
    # Code that might fail
    risky_operation()
except:
    # Code that runs if an error occurs
    handle_error()
```

## Basic Example

```python
try:
    result = 10 / 0
except:
    print("Something went wrong!")
    result = 0

print(f"Result: {result}")  # Result: 0
```

The program doesn't crash!

## Catching Specific Exceptions

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
```

## Multiple Except Blocks

```python
try:
    value = my_list[index]
    result = 10 / value
except IndexError:
    print("Index out of range!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

## 🎯 Your Task

Use try-except to safely convert "abc" to an integer. Print "Invalid number!" if it fails.
""",
        "starter_code": '# Try to convert "abc" to int\n\n',
        "solution_code": '''# Try to convert "abc" to int
try:
    num = int("abc")
except ValueError:
    print("Invalid number!")''',
        "expected_output": "Invalid number!",
        "chapter_id": 13,
        "chapter_title": "Error Handling"
    },
    "322": {
        "id": 322,
        "title": "The Finally Block",
        "content": """# 🔚 Finally: Always Runs

## What is Finally?

The `finally` block runs no matter what - error or not:

```python
try:
    risky_operation()
except:
    handle_error()
finally:
    cleanup()  # ALWAYS runs!
```

## Why Use Finally?

- Close files
- Release resources
- Cleanup even after errors

```python
try:
    file = open("data.txt")
    process(file)
except FileNotFoundError:
    print("File missing!")
finally:
    print("Cleanup complete")  # Always runs
```

## Complete Pattern

```python
try:
    # Try this
    result = 10 / 2
except ZeroDivisionError:
    # If division by zero
    result = 0
else:
    # If NO exception
    print("Division succeeded!")
finally:
    # ALWAYS execute
    print("Done!")
```

---

## 🎯 Your Task

Try dividing 10 by 2. Use finally to print "Calculation complete!" after.
""",
        "starter_code": "# Try division with finally\n\n",
        "solution_code": '''# Try division with finally
try:
    result = 10 / 2
    print(result)
finally:
    print("Calculation complete!")''',
        "expected_output": "5.0\nCalculation complete!",
        "chapter_id": 13,
        "chapter_title": "Error Handling"
    },
    "323": {
        "id": 323,
        "title": "Raising Exceptions",
        "content": """# 🚀 Raising Your Own Exceptions

## The raise Statement

You can create your own errors:

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

check_age(-5)  # ValueError: Age cannot be negative!
```

## Why Raise Exceptions?

- Validate input
- Signal errors to callers
- Enforce rules

## Common Pattern

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

# Caller handles it
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

## Accessing the Error Message

```python
except ValueError as e:
    print(f"Got error: {e}")
```

---

## 🎯 Your Task

Create a function `check_positive(n)` that raises `ValueError` with message "Must be positive!" if n <= 0. Call it with -5 in a try block.
""",
        "starter_code": "# Define check_positive\n\n\n# Test with try-except\n",
        "solution_code": '''# Define check_positive
def check_positive(n):
    if n <= 0:
        raise ValueError("Must be positive!")
    return n

# Test with try-except
try:
    check_positive(-5)
except ValueError as e:
    print(e)''',
        "expected_output": "Must be positive!",
        "chapter_id": 13,
        "chapter_title": "Error Handling"
    },
    "324": {
        "id": 324,
        "title": "Custom Exceptions",
        "content": """# 🎨 Creating Custom Exceptions

## Why Custom Exceptions?

Built-in exceptions are generic. Custom ones are specific to your app:

```python
class InsufficientFundsError(Exception):
    pass

class AccountLockedError(Exception):
    pass
```

## How to Create

Inherit from `Exception`:

```python
class ValidationError(Exception):
    def __init__(self, message, field):
        super().__init__(message)
        self.field = field
```

## Using Custom Exceptions

```python
class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative")
    return age

try:
    set_age(-5)
except NegativeAgeError as e:
    print(f"Invalid: {e}")
```

---

## 🎯 Your Task

Create `InvalidEmailError` exception. Write a function that raises it for "@" missing in email. Test with "badmail".
""",
        "starter_code": "# Define custom exception\n\n\n# Define validation function\n\n\n# Test\n",
        "solution_code": '''# Define custom exception
class InvalidEmailError(Exception):
    pass

# Define validation function
def check_email(email):
    if "@" not in email:
        raise InvalidEmailError("Email must contain @")
    return email

# Test
try:
    check_email("badmail")
except InvalidEmailError as e:
    print(e)''',
        "expected_output": "Email must contain @",
        "chapter_id": 13,
        "chapter_title": "Error Handling"
    },
    "325": {
        "id": 325,
        "title": "Error Handling Best Practices",
        "content": """# ✅ Error Handling Best Practices

## 1. Be Specific

```python
# 🔴 Bad - catches everything
try:
    risky()
except:
    pass

# 🟢 Good - catches specific errors
try:
    risky()
except ValueError:
    handle_value_error()
except TypeError:
    handle_type_error()
```

## 2. Don't Silence Errors

```python
# 🔴 Bad - error disappears
except:
    pass

# 🟢 Good - at least log it
except Exception as e:
    print(f"Error: {e}")
```

## 3. Use else for Success Code

```python
try:
    result = calculate()
except CalculationError:
    result = default
else:
    # Only runs if NO exception
    save_result(result)
```

## 4. Clean Up with finally

```python
file = None
try:
    file = open("data.txt")
    process(file)
finally:
    if file:
        file.close()  # Always close!
```

## 5. Let Exceptions Propagate

```python
# Sometimes it's okay to NOT catch
def load_config(path):
    # Let FileNotFoundError propagate
    # Caller should handle it
    return open(path).read()
```

---

## 🎯 Your Task

Demonstrate good practices: Try to parse "42" as an integer. Use else to print "Parsed: 42" on success.
""",
        "starter_code": "# Good error handling example\n\n",
        "solution_code": '''# Good error handling example
try:
    num = int("42")
except ValueError:
    print("Invalid number!")
else:
    print(f"Parsed: {num}")''',
        "expected_output": "Parsed: 42",
        "chapter_id": 13,
        "chapter_title": "Error Handling"
    }
}

def update_lessons_json():
    """Add new lessons to lessons.json"""
    print("Loading lessons.json...")
    with open(LESSONS_PATH, 'r') as f:
        lessons = json.load(f)
    
    print(f"Current lesson count: {len(lessons)}")
    
    # Add OOP lessons
    for lesson_id, lesson in OOP_LESSONS.items():
        lessons[lesson_id] = lesson
        print(f"  Added lesson {lesson_id}: {lesson['title']}")
    
    # Add Error Handling lessons
    for lesson_id, lesson in ERROR_HANDLING_LESSONS.items():
        lessons[lesson_id] = lesson
        print(f"  Added lesson {lesson_id}: {lesson['title']}")
    
    print(f"New lesson count: {len(lessons)}")
    
    # Save
    with open(LESSONS_PATH, 'w') as f:
        json.dump(lessons, f, indent=2)
    print("✅ lessons.json updated!")

def update_course_json():
    """Add new chapters to course-python-basics.json"""
    print("\nLoading course-python-basics.json...")
    with open(COURSE_PATH, 'r') as f:
        course = json.load(f)
    
    # Define new OOP chapter
    oop_chapter = {
        "id": 12,
        "title": "Object-Oriented Programming",
        "icon": "🏛️",
        "is_boss": False,
        "concepts": [
            {
                "name": "Classes Basics",
                "icon": "🏗️",
                "lessons": [
                    {"id": 300, "title": "What is Object-Oriented Programming?", "order": 1},
                    {"id": 301, "title": "Creating a Class", "order": 2},
                    {"id": 302, "title": "The __init__ Method", "order": 3},
                    {"id": 303, "title": "Instance Methods", "order": 4}
                ]
            },
            {
                "name": "Attributes",
                "icon": "📊",
                "lessons": [
                    {"id": 304, "title": "Class Attributes vs Instance Attributes", "order": 5}
                ]
            },
            {
                "name": "Inheritance",
                "icon": "👨‍👩‍👧",
                "lessons": [
                    {"id": 305, "title": "Inheritance Basics", "order": 6},
                    {"id": 306, "title": "Method Overriding", "order": 7},
                    {"id": 307, "title": "The super() Function", "order": 8}
                ]
            },
            {
                "name": "Advanced OOP",
                "icon": "🚀",
                "lessons": [
                    {"id": 308, "title": "Encapsulation", "order": 9},
                    {"id": 309, "title": "Polymorphism", "order": 10},
                    {"id": 310, "title": "The __str__ Method", "order": 11},
                    {"id": 311, "title": "OOP Challenge: Build a Library", "order": 12}
                ]
            }
        ]
    }
    
    # Define Error Handling chapter
    error_chapter = {
        "id": 13,
        "title": "Error Handling",
        "icon": "🛡️",
        "is_boss": False,
        "concepts": [
            {
                "name": "Exceptions Basics",
                "icon": "⚠️",
                "lessons": [
                    {"id": 320, "title": "What are Exceptions?", "order": 1},
                    {"id": 321, "title": "Try-Except Blocks", "order": 2},
                    {"id": 322, "title": "The Finally Block", "order": 3}
                ]
            },
            {
                "name": "Advanced Error Handling",
                "icon": "🚀",
                "lessons": [
                    {"id": 323, "title": "Raising Exceptions", "order": 4},
                    {"id": 324, "title": "Custom Exceptions", "order": 5},
                    {"id": 325, "title": "Error Handling Best Practices", "order": 6}
                ]
            }
        ]
    }
    
    # Add chapters if not already present
    existing_ids = [ch["id"] for ch in course["chapters"]]
    
    if 12 not in existing_ids:
        course["chapters"].append(oop_chapter)
        print("  Added OOP chapter (12)")
    
    if 13 not in existing_ids:
        course["chapters"].append(error_chapter)
        print("  Added Error Handling chapter (13)")
    
    # Save
    with open(COURSE_PATH, 'w') as f:
        json.dump(course, f, indent=2)
    print("✅ course-python-basics.json updated!")

if __name__ == "__main__":
    print("🚀 Starting curriculum enhancement...")
    update_lessons_json()
    update_course_json()
    print("\n✨ Done! OOP and Error Handling chapters added.")
