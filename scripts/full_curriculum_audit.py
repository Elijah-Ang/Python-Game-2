"""
Deep Curriculum Audit - Hidden Prerequisites & Narrative Flow
"""

import json
import re
from collections import defaultdict

with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

# Track concept introduction order per curriculum
concept_first_seen = {'Python': {}, 'SQL': {}, 'R': {}}

# Python concepts with order of introduction (expected)
PYTHON_CONCEPT_ORDER = [
    # Ch 1: Basics
    ('print', 'ch1'), ('variable', 'ch1'), ('=', 'ch1'),
    # Ch 2: Types
    ('int', 'ch2'), ('float', 'ch2'), ('str', 'ch2'), ('type', 'ch2'),
    # Ch 3: Strings
    ('len', 'ch3'), ('+', 'ch3'), ('f-string', 'ch3'),
    # Ch 4: Conditionals
    ('if', 'ch4'), ('elif', 'ch4'), ('else', 'ch4'), ('==', 'ch4'), ('!=', 'ch4'),
    # Ch 5: Lists
    ('list', 'ch5'), ('[]', 'ch5'), ('append', 'ch5'), ('index', 'ch5'),
    # Ch 6: Loops
    ('for', 'ch6'), ('while', 'ch6'), ('range', 'ch6'), ('break', 'ch6'),
    # Ch 7: Functions
    ('def', 'ch7'), ('return', 'ch7'), ('parameter', 'ch7'),
    # Ch 8: Dictionaries
    ('dict', 'ch8'), ('{}', 'ch8'), ('keys', 'ch8'), ('values', 'ch8'),
]

# SQL concepts with order
SQL_CONCEPT_ORDER = [
    # Ch 1: Basics
    ('SELECT', 'ch1'), ('FROM', 'ch1'), ('*', 'ch1'),
    # Ch 2: Filtering
    ('WHERE', 'ch2'), ('=', 'ch2'), ('AND', 'ch2'), ('OR', 'ch2'),
    # Ch 3: Sorting
    ('ORDER BY', 'ch3'), ('ASC', 'ch3'), ('DESC', 'ch3'),
    # Ch 4: Limiting
    ('LIMIT', 'ch4'),
    # Ch 5: Aggregates
    ('COUNT', 'ch5'), ('SUM', 'ch5'), ('AVG', 'ch5'), ('MAX', 'ch5'), ('MIN', 'ch5'),
    # Ch 6: Grouping
    ('GROUP BY', 'ch6'), ('HAVING', 'ch6'),
    # Ch 7: Joins
    ('JOIN', 'ch7'), ('ON', 'ch7'), ('LEFT JOIN', 'ch7'), ('INNER JOIN', 'ch7'),
]

# R concepts with order
R_CONCEPT_ORDER = [
    # Ch 1: ggplot intro
    ('penguins', 'ch1'), ('ggplot', 'ch1'), ('aes', 'ch1'), ('geom_point', 'ch1'),
    # Ch 2: Workflow
    ('<-', 'ch2'), ('c()', 'ch2'),
    # Ch 3: dplyr basics
    ('%>%', 'ch3'), ('filter', 'ch3'), ('select', 'ch3'), ('mutate', 'ch3'),
    ('arrange', 'ch3'), ('summarize', 'ch3'),
]

def get_curriculum(lid):
    try:
        lesson_id = int(lid)
    except:
        return 'Unknown'
    if 1 <= lesson_id <= 999:
        return 'Python'
    elif 1000 <= lesson_id <= 1999:
        return 'SQL'
    elif 2000 <= lesson_id <= 2999:
        return 'R'
    return 'Unknown'

def get_chapter(lid):
    try:
        lesson_id = int(lid)
    except:
        return 0
    # Python: 1-99 ch1, 100-199 ch2, etc.
    if 1 <= lesson_id <= 999:
        return (lesson_id - 1) // 100 + 1
    # SQL: 1000-1099 ch1, 1100-1199 ch2, etc.
    elif 1000 <= lesson_id <= 1999:
        return ((lesson_id - 1000) // 100) + 1
    # R: use chapter_id from lesson
    return 0

# Find lessons ordered by ID
sorted_lessons = sorted(
    [(lid, l) for lid, l in lessons.items() if get_curriculum(lid) != 'Unknown'],
    key=lambda x: int(x[0])
)

# Separate by curriculum
curricula = {'Python': [], 'SQL': [], 'R': []}
for lid, lesson in sorted_lessons:
    curr = get_curriculum(lid)
    if curr in curricula:
        curricula[curr].append((lid, lesson))

# Analyze each curriculum
findings = []

for curr, lessons_list in curricula.items():
    print(f"\n{'='*60}")
    print(f"{curr} CURRICULUM ANALYSIS")
    print(f"{'='*60}")
    print(f"Total lessons: {len(lessons_list)}")
    
    # Group by chapter
    by_chapter = defaultdict(list)
    for lid, lesson in lessons_list:
        ch = lesson.get('chapter_id', get_chapter(lid))
        by_chapter[ch].append((lid, lesson))
    
    print(f"Chapters: {len(by_chapter)}")
    for ch in sorted(by_chapter.keys()):
        ch_lessons = by_chapter[ch]
        ch_title = ch_lessons[0][1].get('chapter_title', f'Chapter {ch}')
        print(f"  Ch {ch}: {len(ch_lessons)} lessons - {ch_title}")
    
    # Find concept lessons vs reinforcer/exercise lessons
    concept_lessons = []
    reinforcer_lessons = []
    for lid, lesson in lessons_list:
        lid_int = int(lid)
        title = lesson.get('title', '')
        
        # R: 4-digit concept, 5-digit reinforcer
        if curr == 'R':
            if lid_int < 10000:
                concept_lessons.append((lid, lesson))
            else:
                reinforcer_lessons.append((lid, lesson))
        # Python/SQL: chapter concept vs exercise
        else:
            # Exercises typically have "Exercise" in title or follow a pattern
            if 'exercise' in title.lower() or lid_int % 10 != 0:
                reinforcer_lessons.append((lid, lesson))
            else:
                concept_lessons.append((lid, lesson))
    
    print(f"\nConcept lessons: {len(concept_lessons)}")
    print(f"Exercise/Reinforcer lessons: {len(reinforcer_lessons)}")

# Sample some lessons to check quality
print("\n" + "="*60)
print("SAMPLE LESSON QUALITY CHECK")
print("="*60)

sample_ids = ['1', '10', '100', '1000', '1010', '2001', '2010']
for sid in sample_ids:
    if sid in lessons:
        l = lessons[sid]
        content = l.get('content', '')[:200]
        print(f"\n{sid}: {l.get('title', 'No title')}")
        print(f"  Content preview: {content[:100]}...")
        print(f"  Has starter_code: {'Yes' if l.get('starter_code') else 'No'}")
        print(f"  Has solution_code: {'Yes' if l.get('solution_code') else 'No'}")
