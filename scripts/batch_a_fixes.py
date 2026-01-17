"""
Batch A Implementation: Critical Hidden Prerequisites
Focus on adding micro-bridges for the most impactful hidden prereqs
"""

import json

with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

changes_made = []

# ========================================
# PYTHON: Add range() explanation
# ========================================

# Find first loop lesson and add range() bridge
for lid in ['100', '101', '102']:
    if lid in lessons:
        content = lessons[lid].get('content', '')
        if 'range()' in content and '## Understanding range()' not in content:
            # Add range() micro-bridge if not already present
            bridge = """

## 🔢 Understanding range()

Before we loop, you need to know `range()`:

```python
range(5)     # Produces: 0, 1, 2, 3, 4
range(1, 6)  # Produces: 1, 2, 3, 4, 5
range(0, 10, 2)  # Produces: 0, 2, 4, 6, 8 (step of 2)
```

`range()` creates a sequence of numbers. We use it to control how many times a loop runs.

"""
            # Insert after the first heading
            if '##' in content:
                parts = content.split('\n## ', 1)
                if len(parts) == 2:
                    content = parts[0] + bridge + '\n## ' + parts[1]
                    lessons[lid]['content'] = content
                    changes_made.append(f"Python {lid}: Added range() micro-bridge")
            break

# ========================================
# PYTHON: Add return value explanation
# ========================================

for lid in ['300', '301', '302']:
    if lid in lessons:
        content = lessons[lid].get('content', '')
        if 'return' in content.lower() and '## What return Does' not in content:
            bridge = """

## 🔙 What `return` Does

A function can send a value back to where it was called:

```python
def double(x):
    return x * 2

result = double(5)  # result is now 10
```

- Without `return`, function returns `None`
- `return` immediately exits the function
- The returned value can be stored in a variable

"""
            if '##' in content:
                parts = content.split('\n## ', 1)
                if len(parts) == 2:
                    content = parts[0] + bridge + '\n## ' + parts[1]
                    lessons[lid]['content'] = content
                    changes_made.append(f"Python {lid}: Added return micro-bridge")
            break

# ========================================
# SQL: Add window function PARTITION BY explanation
# ========================================

window_lessons = ['10200', '10201', '10202']
for lid in window_lessons:
    if lid in lessons:
        content = lessons[lid].get('content', '')
        if 'PARTITION BY' in content and '## How PARTITION BY Works' not in content:
            bridge = """

## 🔲 How PARTITION BY Works

Think of `PARTITION BY` as creating invisible groups:

```sql
SELECT 
    name,
    department,
    salary,
    AVG(salary) OVER (PARTITION BY department) as dept_avg
FROM employees;
```

- `PARTITION BY department` creates a separate "window" for each department
- The `AVG()` is calculated within each window, not the whole table
- Unlike `GROUP BY`, you keep all original rows

"""
            if '##' in content:
                parts = content.split('\n## ', 1)
                if len(parts) == 2:
                    content = parts[0] + bridge + '\n## ' + parts[1]
                    lessons[lid]['content'] = content
                    changes_made.append(f"SQL {lid}: Added PARTITION BY micro-bridge")
            break

# ========================================
# R: Enhance pipe explanation (already done in Batch R-1/R-2, verify)
# ========================================

# Check if R pipe lessons already have bridge
for lid in ['20301', '2031']:
    if lid in lessons:
        content = lessons[lid].get('content', '')
        if '%>%' in content:
            if '💡' in content or 'pipe' in content.lower():
                changes_made.append(f"R {lid}: Pipe bridge already present ✓")
            else:
                # Add pipe bridge
                bridge = """
> 💡 The `%>%` (pipe) takes the output from the left side and passes it as the first argument to the function on the right. Think of it as "take this, then do that."

"""
                lessons[lid]['content'] = content.replace('## ', bridge + '\n## ', 1)
                changes_made.append(f"R {lid}: Added pipe micro-bridge")

# Save changes
with open('frontend/public/data/lessons.json', 'w') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("=" * 60)
print("BATCH A IMPLEMENTATION COMPLETE")
print("=" * 60)
print(f"\nChanges made: {len(changes_made)}")
for change in changes_made:
    print(f"  ✓ {change}")
