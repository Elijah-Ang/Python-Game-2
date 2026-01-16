import json
import re

# Load data
base_path = '/Users/elijahang/Python-Game-2/frontend/public/data/'
with open(base_path + 'lessons.json', 'r') as f:
    lessons = json.load(f)
with open(base_path + 'course-python-basics.json', 'r') as f:
    python_course = json.load(f)

# Build Concept Map (Concept -> Earliest Chapter Order)
concept_map = {
    'def': 4, 'return': 4, 'lambda': 4,  # Functions (Ch 4)
    'for': 2, 'while': 2, 'break': 2, 'continue': 2, # Loops (Ch 2) - taught AFTER Logic (Ch 3) in this file order?
    # Wait, let's verify chapter order
    'if': 3, 'else': 3, 'elif': 3, # Logic (Ch 3)
    'list': 7, '[': 7, ']': 7, # Data Structures (Ch 7) - strict check might be hard for []
    'dict': 7, '{': 7, '}': 7, 
    'import': 9, 'from': 9, # Modules (Ch 9)
    'class': 99, 'object': 99 # Not explicitly in basics?
}

# Real Chapter Order
# 1: Variables
# 3: Logic (Index 1)
# 2: Loops (Index 2)
# 4: Functions (Index 3)
# 7: Data Structures (Index 6?)
# Let's map Chapter ID to *Sequence Index*
chapter_sequence = {}
for idx, chapter in enumerate(python_course['chapters']):
    chapter_sequence[chapter['id']] = idx
    # print(f"Chapter {chapter['id']}: {chapter['title']} at index {idx}")

# Refine Concept Map based on Sequence Index
# Variables (0)
# Logic (1): if, else, elif, and, or, not
# Loops (2): for, while, break, continue
# Functions (3): def, return, lambda
# Data Structures (4? No, check file): 
# Ch 7 is index 5.
# Ch 8 File Handling index 6.

keyword_to_min_chapter_idx = {
    'if': 1, 'else': 1, 'elif': 1,
    'for': 2, 'while': 2, 'break': 2, 'continue': 2,
    'def': 3, 'return': 3, 'lambda': 3,
    'import': 7, # Modules is Ch 9, index 7?
}

# Scan Lessons
issues = []

for lesson_id, lesson in lessons.items():
    if not lesson.get('chapter_id'): continue
    
    # Only check Python lessons (ID < 1000)
    if int(lesson_id) >= 1000: continue

    # Current Lesson's context
    chapter_id = lesson['chapter_id']
    if chapter_id not in chapter_sequence: continue
    
    current_idx = chapter_sequence[chapter_id]
    
    content = lesson.get('content', '') + lesson.get('solution_code', '')
    
    # Check for keywords
    for keyword, min_idx in keyword_to_min_chapter_idx.items():
        if min_idx > current_idx:
            # Found a future keyword!
            # Use regex to ensure whole word
            if re.search(r'\b' + re.escape(keyword) + r'\b', content):
                issues.append({
                    'lesson': lesson_id,
                    'title': lesson['title'],
                    'chapter': chapter_id,
                    'current_idx': current_idx,
                    'keyword': keyword,
                    'min_idx': min_idx
                })

print(f"Found {len(issues)} potential issues.")
for i in issues:
    print(f"Lesson {i['lesson']} '{i['title']}' (Ch {i['chapter']}) uses '{i['keyword']}' (Intro at Index {i['min_idx']})")

