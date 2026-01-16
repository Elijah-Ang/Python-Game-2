import json
import re

# Load data
base_path = '/Users/elijahang/Python-Game-2/frontend/public/data/'
with open(base_path + 'lessons.json', 'r') as f:
    lessons = json.load(f)
with open(base_path + 'course-python-basics.json', 'r') as f:
    python_course = json.load(f)

# Concept Map (Keyword -> Earliest Valid Chapter Index)
# 0: Variables
# 1: Logic
# 2: Loops
# 3: Functions
# 5: Data Structures
# 7: Modules
keyword_to_min_chapter_idx = {
    'if': 1, 'else': 1, 'elif': 1,
    'for': 2, 'while': 2, 'break': 2, 'continue': 2,
    'def': 3, 'return': 3, 'lambda': 3,
    'import': 7, 
}

# Chapter sequence mapping
chapter_sequence = {}
for idx, chapter in enumerate(python_course['chapters']):
    chapter_sequence[chapter['id']] = idx

issues = []

for lesson_id, lesson in lessons.items():
    if not lesson.get('chapter_id'): continue
    if int(lesson_id) >= 1000: continue # Skip SQL/R for now

    chapter_id = lesson['chapter_id']
    if chapter_id not in chapter_sequence: continue
    
    current_idx = chapter_sequence[chapter_id]
    
    # CHECK ONLY CODE FIELDS
    code_content = (lesson.get('starter_code', '') + '\n' + lesson.get('solution_code', ''))
    
    # Remove comments from code
    code_content = re.sub(r'#.*', '', code_content)
    
    for keyword, min_idx in keyword_to_min_chapter_idx.items():
        if min_idx > current_idx:
            # Found a future keyword in CODE!
            if re.search(r'\b' + re.escape(keyword) + r'\b', code_content):
                issues.append({
                    'lesson': lesson_id,
                    'title': lesson['title'],
                    'chapter': chapter_id,
                    'current_idx': current_idx,
                    'keyword': keyword,
                    'min_idx': min_idx,
                    'snippet': code_content[:500] # Debug
                })

print(f"Found {len(issues)} code issues.")
for i in issues:
    print(f"Lesson {i['lesson']} '{i['title']}' uses '{i['keyword']}' (Intro at Index {i['min_idx']})")
