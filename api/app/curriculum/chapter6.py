# Chapter 6: File Handling
# Enhanced with detailed definitions and explanations

CHAPTER_6 = {
    "id": 8,
    "title": "File Handling",
    "slug": "python-files",
    "icon": "📁",
    "is_boss": False,
    "lessons": [
        {
            "id": 50,
            "title": "Reading Files",
            "order": 1,
            "content": """# 📖 Reading Files

## Why Work with Files?

Programs need to read and write data that persists beyond when they run: configuration files, user data, logs, exports, and more.

## The with Statement

Python's `with` statement automatically handles opening and closing files:

```python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
# File automatically closed when block ends
```

## File Modes

| Mode | Description |
| --- | --- |
| `"r"` | Read (default) |
| `"w"` | Write (overwrites!) |
| `"a"` | Append |
| `"r+"` | Read and write |

Note: In this browser environment, we'll simulate file operations with strings.

---

## 🎯 Your Task

Create a string `data = "Hello from file!"` and print it as if you read it from a file.
""",
            "starter_code": "# Simulate file content\ndata = \"Hello from file!\"\n\n# Print it\n",
            "solution_code": "# Simulate file content\ndata = \"Hello from file!\"\n\n# Print it\nprint(data)",
            "expected_output": "Hello from file!",
            "xp": 10
        },
        {
            "id": 51,
            "title": "Reading Lines",
            "order": 2,
            "content": """# 📋 Reading Line by Line

## Processing Files Line by Line

For large files, reading line by line is memory efficient:

```python
with open("file.txt") as f:
    for line in f:
        print(line.strip())  # strip() removes newline
```

## Other Reading Methods

```python
f.read()        # Entire file as one string
f.readline()    # One line at a time
f.readlines()   # List of all lines
```

## Working with Multi-line Strings

In the browser, we simulate files with multi-line strings:

```python
content = \"\"\"Line 1
Line 2
Line 3\"\"\"

for line in content.split('\\n'):
    print(line)
```

---

## 🎯 Your Task

Given this multiline string:
```python
file_content = \"\"\"Line 1
Line 2
Line 3\"\"\"
```
Loop through each line and print it.
""",
            "starter_code": "file_content = \"\"\"Line 1\nLine 2\nLine 3\"\"\"\n\n# Print each line\n",
            "solution_code": "file_content = \"\"\"Line 1\nLine 2\nLine 3\"\"\"\n\n# Print each line\nfor line in file_content.split('\\n'):\n    print(line)",
            "expected_output": "Line 1\nLine 2\nLine 3",
            "xp": 10
        },
        {
            "id": 52,
            "title": "CSV Data",
            "order": 3,
            "content": """# 📊 Working with CSV

## What is CSV?

**CSV** (Comma-Separated Values) is a common format for data exchange:

```
name,age,city
Alice,25,NYC
Bob,30,LA
```

Each line is a row, values separated by commas.

## Parsing CSV Manually

```python
csv_data = "name,age\\nAlice,25\\nBob,30"
lines = csv_data.split('\\n')

header = lines[0].split(',')  # ['name', 'age']
for line in lines[1:]:
    values = line.split(',')
    print(dict(zip(header, values)))
```

## The csv Module

Python has a built-in module for complex CSV:

```python
import csv
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## 🎯 Your Task

Given: `csv_data = "name,age,city\\nAlice,25,NYC\\nBob,30,LA"`
Skip the header and print each person's name.
""",
            "starter_code": "csv_data = \"name,age,city\\nAlice,25,NYC\\nBob,30,LA\"\n\n# Skip header and print names\n",
            "solution_code": "csv_data = \"name,age,city\\nAlice,25,NYC\\nBob,30,LA\"\n\n# Skip header and print names\nlines = csv_data.split('\\n')\nfor line in lines[1:]:\n    name = line.split(',')[0]\n    print(name)",
            "expected_output": "Alice\nBob",
            "xp": 10
        },
        {
            "id": 53,
            "title": "JSON Basics",
            "order": 4,
            "content": """# 📦 JSON Data

## What is JSON?

**JSON** (JavaScript Object Notation) is the standard for web data:

```json
{"name": "Alice", "age": 25, "skills": ["Python", "SQL"]}
```

## Working with JSON in Python

```python
import json

# Parse JSON string → Python dict
data = json.loads('{"name": "Alice", "age": 25}')
print(data["name"])  # Alice

# Python dict → JSON string
json_str = json.dumps({"name": "Bob"})
print(json_str)  # {"name": "Bob"}
```

## JSON and Files

```python
# Read from file
with open("data.json") as f:
    data = json.load(f)

# Write to file
with open("output.json", "w") as f:
    json.dump(data, f)
```

---

## 🎯 Your Task

Given: `json_str = '{"name": "Alice", "score": 95}'`
Parse it and print the name.
""",
            "starter_code": "import json\n\njson_str = '{\"name\": \"Alice\", \"score\": 95}'\n\n# Parse and print name\n",
            "solution_code": "import json\n\njson_str = '{\"name\": \"Alice\", \"score\": 95}'\n\n# Parse and print name\ndata = json.loads(json_str)\nprint(data[\"name\"])",
            "expected_output": "Alice",
            "xp": 10
        },
        {
            "id": 54,
            "title": "String Processing",
            "order": 5,
            "content": """# 🔍 Processing Text Data

## Common String Operations

When working with file data, you often need to clean and parse text:

```python
text = "  hello world  "

text.strip()       # Remove whitespace
text.split()       # Split by whitespace
text.split(',')    # Split by comma
text.replace('a', 'b')
text.upper() / text.lower()
```

## Splitting Strings

```python
# Split by whitespace (default)
"hello world".split()  # ['hello', 'world']

# Split by specific character
"a,b,c".split(',')     # ['a', 'b', 'c']

# Split with limit
"a,b,c,d".split(',', 2)  # ['a', 'b', 'c,d']
```

---

## 🎯 Your Task

Given: `text = "apple,banana,cherry"`
Split by comma and print each fruit.
""",
            "starter_code": "text = \"apple,banana,cherry\"\n\n# Split and print each\n",
            "solution_code": "text = \"apple,banana,cherry\"\n\n# Split and print each\nfruits = text.split(',')\nfor fruit in fruits:\n    print(fruit)",
            "expected_output": "apple\nbanana\ncherry",
            "xp": 10
        },
        {
            "id": 55,
            "title": "Data Parsing",
            "order": 6,
            "content": """# 🔧 Parsing Structured Data

## Extracting Information

Real data is often messy and needs parsing:

```python
log = "2024-01-15 14:30:00 - User logged in"

# Split and extract
parts = log.split(' - ')
timestamp = parts[0]  # "2024-01-15 14:30:00"
message = parts[1]    # "User logged in"
```

## Multiple Levels of Parsing

```python
timestamp = "2024-01-15 14:30:00"
date, time = timestamp.split(' ')
year, month, day = date.split('-')
```

---

## 🎯 Your Task

Given: `log = "2024-01-15: User logged in"`
Extract and print just the date part.
""",
            "starter_code": "log = \"2024-01-15: User logged in\"\n\n# Extract and print date\n",
            "solution_code": "log = \"2024-01-15: User logged in\"\n\n# Extract and print date\ndate = log.split(':')[0]\nprint(date)",
            "expected_output": "2024-01-15",
            "xp": 10
        },
        {
            "id": 56,
            "title": "Counting Words",
            "order": 7,
            "content": """# 📊 Word Count

## Counting Elements in Text

Word count is a fundamental text analysis operation:

```python
text = "Hello world hello"
words = text.split()
print(len(words))  # 3
```

## Counting Specific Items

```python
from collections import Counter
words = "the cat sat on the mat".split()
counts = Counter(words)
print(counts)  # Counter({'the': 2, 'cat': 1, 'sat': 1, ...})
```

---

## 🎯 Your Task

Given: `text = "The quick brown fox jumps"`
Count and print the number of words.
""",
            "starter_code": "text = \"The quick brown fox jumps\"\n\n# Count and print\n",
            "solution_code": "text = \"The quick brown fox jumps\"\n\n# Count and print\nwords = text.split()\nprint(len(words))",
            "expected_output": "5",
            "xp": 10
        },
        {
            "id": 57,
            "title": "Search in Text",
            "order": 8,
            "content": """# 🔍 Finding Text

## Checking for Substrings

```python
text = "Hello, World!"

# Check if contains
"World" in text      # True
"world" in text      # False (case-sensitive)
"world" in text.lower()  # True (after lowercasing)

# Find position
text.find("World")   # 7 (index)
text.find("xyz")     # -1 (not found)
```

## String Methods for Searching

```python
text.startswith("Hello")  # True
text.endswith("!")        # True
text.count("l")           # 3
```

---

## 🎯 Your Task

Given: `message = "Welcome to Python programming"`
Check if "Python" is in the message. Print `"Found"` if yes.
""",
            "starter_code": "message = \"Welcome to Python programming\"\n\n# Check for \"Python\"\n",
            "solution_code": "message = \"Welcome to Python programming\"\n\n# Check for \"Python\"\nif \"Python\" in message:\n    print(\"Found\")",
            "expected_output": "Found",
            "xp": 10
        },
        {
            "id": 58,
            "title": "Replace Text",
            "order": 9,
            "content": """# 🔄 Replacing Text

## The replace() Method

```python
text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text)  # Hello Python
```

## Multiple Replacements

```python
text = "a-b-c-d"
clean = text.replace("-", " ")
print(clean)  # a b c d
```

## Case-Sensitive

Replace is case-sensitive:
```python
"Hello World".replace("world", "Python")  # "Hello World" (no change!)
"Hello World".replace("World", "Python")  # "Hello Python"
```

---

## 🎯 Your Task

Given: `text = "Hello World"`
Replace "World" with "Python" and print.
""",
            "starter_code": "text = \"Hello World\"\n\n# Replace and print\n",
            "solution_code": "text = \"Hello World\"\n\n# Replace and print\nnew_text = text.replace(\"World\", \"Python\")\nprint(new_text)",
            "expected_output": "Hello Python",
            "xp": 10
        }
    ]
}
