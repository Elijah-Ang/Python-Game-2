import json
import re

ch2_ids = [13, 14, 15, 153, 154, 16, 17, 18, 155, 156, 19, 20, 21, 157, 158]
ch3_ids = [22, 23, 24, 159, 160, 25, 26, 27, 28, 161, 29, 30, 31, 162, 163]

file_path = '/Users/elijahang/Python-Game-2/frontend/public/data/lessons.json'

with open(file_path, 'r') as f:
    data = json.load(f)

print("--- CHAPTER 2 (LOOPS) CHECK ---")
for lid in ch2_ids:
    lid_str = str(lid)
    if lid_str in data:
        full_text = data[lid_str].get('content', '') + data[lid_str].get('starter_code', '') + data[lid_str].get('solution_code', '')
        
        # Check for Lists (untaught)
        if '[' in full_text or ']' in full_text:
            # exclude markdown links [text](url)
            # crude check: if [ followed by number or quote
            if re.search(r'\[\s*[\d"\']', full_text):
                print(f"Lesson {lid} ({data[lid_str]['title']}) uses Lists '[...]'")

        # Check for Functions (untaught)
        if 'def ' in full_text:
            print(f"Lesson {lid} ({data[lid_str]['title']}) uses Functions 'def'")

print("\n--- CHAPTER 3 (LOGIC) CHECK ---")
for lid in ch3_ids:
    lid_str = str(lid)
    if lid_str in data:
        full_text = data[lid_str].get('content', '') + data[lid_str].get('starter_code', '') + data[lid_str].get('solution_code', '')
        
        # Check for Functions (untaught)
        if 'def ' in full_text:
            print(f"Lesson {lid} ({data[lid_str]['title']}) uses Functions 'def'")
