import json
import re

ids_to_check = [13, 14, 15, 153, 154, 16, 17, 18, 155, 156, 19, 20, 21, 157, 158]
file_path = '/Users/elijahang/Python-Game-2/frontend/public/data/lessons.json'

print(f"Reading {file_path}...")
with open(file_path, 'r') as f:
    data = json.load(f)

for lid in ids_to_check:
    lid_str = str(lid)
    if lid_str in data:
        # print(f"Checking {lid}...")
        lesson = data[lid_str]
        content = lesson.get('content', '')
        starter = lesson.get('starter_code', '')
        solution = lesson.get('solution_code', '')
        
        full_text = content + starter + solution
        
        has_if = re.search(r'\bif\b', full_text)
        has_else = re.search(r'\belse\b', full_text)
        # Check for boolean literals or comparison operators often used in while
        has_bool = re.search(r'\bTrue\b|\bFalse\b', full_text)
        
        if has_if or has_else or has_bool:
            print(f"Lesson {lid} ({lesson['title']}) matches:")
            if has_if: print(f"  - 'if'")
            if has_else: print(f"  - 'else'")
            if has_bool: print(f"  - Boolean")
    else:
        print(f"Lesson {lid} not found in lessons.json")
