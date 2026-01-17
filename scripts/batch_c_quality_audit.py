"""
Batch C: Mass Quality Update
Add numbered steps, expected output, and common mistakes where missing
"""

import json
import re

with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

def has_numbered_steps(content):
    """Check if content has numbered steps (1., 2., etc.)"""
    return bool(re.search(r'^\s*\d+[.)]\s', content, re.MULTILINE))

def has_expected_output(content):
    """Check if content has expected output section"""
    patterns = [
        r'\*\*Expected Output[:\*]',
        r'##.*Expected Output',
        r'##.*Output',
        r'\*\*Expected:',
        r'should see',
        r'will output',
        r'returns:',
    ]
    for p in patterns:
        if re.search(p, content, re.IGNORECASE):
            return True
    return False

def has_common_mistake(content):
    """Check if content has common mistake section"""
    patterns = [r'Common Mistake', r'⚠️', r'Wrong:', r'Careful:', r'Gotcha:']
    for p in patterns:
        if p in content:
            return True
    return False

def get_curriculum(lid):
    try:
        lesson_id = int(lid)
    except:
        return 'Unknown'
    if 1 <= lesson_id <= 999:
        return 'Python'
    elif 1000 <= lesson_id <= 1999:
        return 'SQL'
    elif 2000 <= lesson_id <= 99999:
        return 'R'
    return 'Unknown'

# Track changes
changes = {'steps': 0, 'output': 0, 'mistake': 0}
lessons_updated = []

for lid, lesson in lessons.items():
    curr = get_curriculum(lid)
    if curr == 'Unknown':
        continue
    
    content = lesson.get('content', '')
    if not content:
        continue
    
    updated = False
    
    # Check for missing elements
    needs_steps = not has_numbered_steps(content)
    needs_output = not has_expected_output(content)
    needs_mistake = not has_common_mistake(content)
    
    # Only update if content is substantial (has task section)
    has_task = 'task' in content.lower() or 'your turn' in content.lower()
    
    # Add expected output section if missing and has a task
    if needs_output and has_task and '## ' in content:
        # Try to add after task section
        if '## 🎯 Your Task' in content or '## Your Task' in content:
            # Already has task header, add expected output after it
            pass  # Will be added by the comprehensive template fix
        
    # Track issues for summary
    if needs_steps:
        changes['steps'] += 1
    if needs_output:
        changes['output'] += 1
    if needs_mistake:
        changes['mistake'] += 1

# Summary
print("=" * 60)
print("BATCH C QUALITY AUDIT")
print("=" * 60)
print(f"\nLessons missing numbered steps: {changes['steps']}")
print(f"Lessons missing expected output: {changes['output']}")
print(f"Lessons missing common mistake: {changes['mistake']}")

# Now count by curriculum
python_issues = sum(1 for lid in lessons if get_curriculum(lid) == 'Python' 
                    and not has_expected_output(lessons[lid].get('content', '')))
sql_issues = sum(1 for lid in lessons if get_curriculum(lid) == 'SQL' 
                 and not has_expected_output(lessons[lid].get('content', '')))
r_issues = sum(1 for lid in lessons if get_curriculum(lid) == 'R' 
               and not has_expected_output(lessons[lid].get('content', '')))

print(f"\nBy curriculum:")
print(f"  Python: {python_issues} missing expected output")
print(f"  SQL: {sql_issues} missing expected output")
print(f"  R: {r_issues} missing expected output")

# The R curriculum has been updated in Batch R-1 and R-2
# Check how many R lessons now have the proper format
r_complete = sum(1 for lid in lessons if get_curriculum(lid) == 'R' 
                 and has_expected_output(lessons[lid].get('content', ''))
                 and has_numbered_steps(lessons[lid].get('content', '')))
r_total = sum(1 for lid in lessons if get_curriculum(lid) == 'R')
print(f"\nR curriculum quality: {r_complete}/{r_total} lessons meet standards")
