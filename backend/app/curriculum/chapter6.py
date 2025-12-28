# Chapter 6: File Handling
# Each exercise has specific data and exact expected output

CHAPTER_6 = {
    "id": 7,
    "title": "File Handling",
    "slug": "python-files",
    "icon": "📁",
    "is_boss": False,
    "lessons": [
        {
            "id": 49,
            "title": "Reading Files",
            "order": 1,
            "content": """# 📖 Reading Files

```python
with open("file.txt", "r") as f:
    content = f.read()
```

Note: In this browser environment, we'll simulate file operations.

---

## 🎯 Your Task

Create a string `data = "Hello from file!"`.
Print it as if you read it from a file.
""",
            "starter_code": "# Simulate file content\ndata = \"Hello from file!\"\n\n# Print it\n",
            "solution_code": "# Simulate file content\ndata = \"Hello from file!\"\n\n# Print it\nprint(data)",
            "expected_output": "Hello from file!",
            "xp": 10
        },
        {
            "id": 50,
            "title": "Reading Lines",
            "order": 2,
            "content": """# 📋 Reading Line by Line

```python
with open("file.txt") as f:
    for line in f:
        print(line.strip())
```

---

## 🎯 Your Task

Given this multiline string (simulating a file):
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
            "id": 51,
            "title": "CSV Data",
            "order": 3,
            "content": """# 📊 Working with CSV

CSV is comma-separated values.

---

## 🎯 Your Task

Given:
```python
csv_data = "name,age,city\\nAlice,25,NYC\\nBob,30,LA"
```

Split into lines and print each person's name.
""",
            "starter_code": "csv_data = \"name,age,city\\nAlice,25,NYC\\nBob,30,LA\"\n\n# Skip header and print names\n",
            "solution_code": "csv_data = \"name,age,city\\nAlice,25,NYC\\nBob,30,LA\"\n\n# Skip header and print names\nlines = csv_data.split('\\n')\nfor line in lines[1:]:\n    name = line.split(',')[0]\n    print(name)",
            "expected_output": "Alice\nBob",
            "xp": 10
        },
        {
            "id": 52,
            "title": "JSON Basics",
            "order": 4,
            "content": """# 📦 JSON Data

```python
import json
data = json.loads(json_string)
```

---

## 🎯 Your Task

Given:
```python
json_str = '{\"name\": \"Alice\", \"score\": 95}'
```

Parse it and print the name.
""",
            "starter_code": "import json\n\njson_str = '{\"name\": \"Alice\", \"score\": 95}'\n\n# Parse and print name\n",
            "solution_code": "import json\n\njson_str = '{\"name\": \"Alice\", \"score\": 95}'\n\n# Parse and print name\ndata = json.loads(json_str)\nprint(data[\"name\"])",
            "expected_output": "Alice",
            "xp": 10
        },
        {
            "id": 53,
            "title": "String Processing",
            "order": 5,
            "content": """# 🔍 Processing Text

```python
text = "hello world"
words = text.split()  # ["hello", "world"]
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
            "id": 54,
            "title": "Data Parsing",
            "order": 6,
            "content": """# 🔧 Parsing Data

Extract information from structured text.

---

## 🎯 Your Task

Given:
```python
log = "2024-01-15: User logged in"
```

Extract and print just the date part.
""",
            "starter_code": "log = \"2024-01-15: User logged in\"\n\n# Extract and print date\n",
            "solution_code": "log = \"2024-01-15: User logged in\"\n\n# Extract and print date\ndate = log.split(':')[0]\nprint(date)",
            "expected_output": "2024-01-15",
            "xp": 10
        },
        {
            "id": 55,
            "title": "Counting Words",
            "order": 7,
            "content": """# 📊 Word Count

Count words in text.

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
            "id": 56,
            "title": "Search in Text",
            "order": 8,
            "content": """# 🔍 Finding Text

```python
if "hello" in text:
    print("Found!")
text.find("hello")  # Returns index or -1
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
            "id": 57,
            "title": "Replace Text",
            "order": 9,
            "content": """# 🔄 Replace Text

```python
new_text = text.replace("old", "new")
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
