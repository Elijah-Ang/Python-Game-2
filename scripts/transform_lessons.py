"""
Batch Lesson Transformer: Add Interactive Components

This script processes lessons.json and injects interactive component tags
based on the lesson's chapter and type.
"""

import json
import re
from pathlib import Path

# Component mappings by chapter/concept type
INTERACTION_MAP = {
    # Python chapters
    1: {  # Variables, Types & Memory
        'components': ['draggablevaluebox', 'valuechip', 'visualmemorybox'],
        'pattern': r'(## Interactive Demo.*?)(## )',
        'replacement': '''## Interactive Demo

Drag a value into the box:

<div style="display: flex; gap: 10px; flex-wrap: wrap; margin: 10px 0;">
<valuechip value="{value1}"></valuechip>
<valuechip value="{value2}"></valuechip>
<valuechip value="{value3}"></valuechip>
</div>

<draggablevaluebox name="{varname}" acceptedvalues='[{value1}, {value2}, {value3}]'></draggablevaluebox>

\\2'''
    },
    2: {  # Loops
        'components': ['variableslider', 'livecodeblock'],
        'pattern': None,  # Will add at end
        'template': '''

## Try It Yourself

Adjust the loop bound:

<variableslider name="loop_bound" min="1" max="10" initial="5" label="Loop iterations"></variableslider>

'''
    },
    3: {  # Logic & Control Flow
        'components': ['livecodeblock'],
        'pattern': None,
        'template': '''

## Experiment

Modify the condition value:

<livecodeblock initialcode="{sample_code}" language="python" highlightline="1"></livecodeblock>

'''
    },
    4: {  # Functions
        'components': ['parsonspuzzle'],
        'pattern': None,
        'template': '''

## Arrange the Code

<parsonspuzzle correctorder='["{line1}", "{line2}", "{line3}"]'></parsonspuzzle>

'''
    },
    # SQL chapters (1001+)
    1001: {  # SELECT basics
        'components': ['visualtable'],
        'pattern': None,
        'template': '''

## Explore the Data

<visualtable 
    data='[{"id": 1, "name": "Alice", "age": 30}, {"id": 2, "name": "Bob", "age": 25}]'
    columns='["id", "name", "age"]'
    allowsort="true"
    allowfilter="true"
></visualtable>

'''
    },
}

def get_chapter_id_from_lesson(lesson_data: dict) -> int:
    """Extract chapter ID from lesson data."""
    return lesson_data.get('chapter_id', 1)

def inject_interaction(content: str, chapter_id: int, lesson_data: dict) -> str:
    """Inject interactive components based on chapter type."""
    config = INTERACTION_MAP.get(chapter_id)
    
    if not config:
        # Default: add a simple live code block at the end before "Your Task"
        if '## 🎯 Your Task' in content:
            insert_point = content.find('## 🎯 Your Task')
            interactive_section = '''
## Try It First

Run this example to see how it works:

<livecodeblock initialcode="# Modify this code" language="python"></livecodeblock>

'''
            content = content[:insert_point] + interactive_section + content[insert_point:]
    else:
        if config.get('template'):
            # Add template before "Your Task"
            if '## 🎯 Your Task' in content:
                insert_point = content.find('## 🎯 Your Task')
                content = content[:insert_point] + config['template'] + content[insert_point:]
    
    return content

def transform_lessons(input_path: str, output_path: str = None, dry_run: bool = True):
    """Transform all lessons to include interactive components."""
    
    with open(input_path, 'r') as f:
        lessons = json.load(f)
    
    stats = {'transformed': 0, 'skipped': 0, 'errors': 0}
    
    for lesson_id, lesson_data in lessons.items():
        try:
            chapter_id = get_chapter_id_from_lesson(lesson_data)
            original_content = lesson_data.get('content', '')
            
            # Skip if already has interactive components
            if any(tag in original_content.lower() for tag in 
                   ['<variableslider', '<draggablevaluebox', '<livecodeblock', '<parsonspuzzle', '<visualtable']):
                stats['skipped'] += 1
                continue
            
            # Transform content
            new_content = inject_interaction(original_content, chapter_id, lesson_data)
            
            if new_content != original_content:
                lessons[lesson_id]['content'] = new_content
                lessons[lesson_id]['interaction_required'] = True
                stats['transformed'] += 1
                print(f"✅ Transformed lesson {lesson_id}: {lesson_data.get('title', 'Unknown')}")
            else:
                stats['skipped'] += 1
                
        except Exception as e:
            stats['errors'] += 1
            print(f"❌ Error in lesson {lesson_id}: {e}")
    
    # Write output
    if not dry_run and output_path:
        with open(output_path, 'w') as f:
            json.dump(lessons, f, indent=2, ensure_ascii=False)
        print(f"\n✅ Written to {output_path}")
    
    print(f"\n📊 Stats: {stats}")
    return lessons, stats

if __name__ == '__main__':
    import sys
    
    input_file = 'frontend/public/data/lessons.json'
    output_file = 'frontend/public/data/lessons_interactive.json'
    
    dry_run = '--apply' not in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN - use --apply to write changes")
    
    transform_lessons(input_file, output_file, dry_run=dry_run)
