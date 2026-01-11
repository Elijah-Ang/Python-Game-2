import json
import re

ids_to_check = [13, 14, 15, 153, 154, 16, 17, 18, 155, 156, 19, 20, 21, 157, 158]
file_path = '/Users/elijahang/Python-Game-2/frontend/public/data/lessons.json'

with open(file_path, 'r') as f:
    data = json.load(f)

for lid in ids_to_check:
    lid_str = str(lid)
    if lid_str in data:
        lesson = data[lid_str]
        content = lesson.get('content', '')
        starter = lesson.get('starter_code', '')
        solution = lesson.get('solution_code', '')
        
        full_text = content + starter + solution
        
        # Check for Conditional Logic (Ch 3 stuff)
        has_if = re.search(r'\bif\b', full_text)
        has_else = re.search(r'\belse\b', full_text)
        has_bool = re.search(r'\bTrue\b|\bFalse\b', full_text)
        
        if has_if or has_else or has_bool:
            print(f"Lesson {lid} ({lesson['title']}) contains conditional logic!")
            if has_if: print(f"  - Found 'if'")
            if has_else: print(f"  - Found 'else'")
            if has_bool: print(f"  - Found Boolean")

