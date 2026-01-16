"""
Batch Lesson Transformer: Add Interactive Components

This script processes lessons.json and injects interactive component tags
into lessons that don't already have them.
"""

import json
from pathlib import Path

INTERACTIVE_TAGS = ['<variableslider', '<draggablevaluebox', '<livecodeblock', '<parsonspuzzle', '<visualtable']

def get_language_from_lesson_id(lesson_id: str) -> str:
    """Determine language based on lesson ID."""
    id_num = int(lesson_id)
    if id_num >= 2001:
        return 'r'
    elif id_num >= 1001 and id_num < 2000:
        return 'sql'
    else:
        return 'python'

def inject_interaction(content: str, language: str) -> str:
    """Inject a livecodeblock component into the lesson content."""
    
    interactive_section = f'''
## Try It First

Run this example to see how it works:

<livecodeblock initialcode="# Modify this code" language="{language}"></livecodeblock>

'''
    
    # Find the best insertion point
    if '## 🎯 Your Task' in content:
        insert_point = content.find('## 🎯 Your Task')
        return content[:insert_point] + interactive_section + content[insert_point:]
    elif '## Your Task' in content:
        insert_point = content.find('## Your Task')
        return content[:insert_point] + interactive_section + content[insert_point:]
    elif '---' in content:
        # Insert before the last horizontal rule
        last_hr = content.rfind('---')
        return content[:last_hr] + interactive_section + content[last_hr:]
    else:
        # Just append at the end
        return content + interactive_section

def transform_lessons(input_path: str, output_path: str = None, dry_run: bool = True):
    """Transform all lessons to include interactive components."""
    
    with open(input_path, 'r') as f:
        lessons = json.load(f)
    
    stats = {'transformed': 0, 'skipped': 0, 'errors': 0}
    
    for lesson_id, lesson_data in lessons.items():
        try:
            content = lesson_data.get('content', '')
            
            # Skip if already has interactive components
            if any(tag in content.lower() for tag in INTERACTIVE_TAGS):
                stats['skipped'] += 1
                continue
            
            # Determine language
            language = get_language_from_lesson_id(lesson_id)
            
            # Transform content
            new_content = inject_interaction(content, language)
            
            if new_content != content:
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
    output_file = 'frontend/public/data/lessons.json'  # Write back to same file
    
    dry_run = '--apply' not in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN - use --apply to write changes")
    
    transform_lessons(input_file, output_file, dry_run=dry_run)
