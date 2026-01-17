"""
R Curriculum Reinforcer Audit Script - Phase 1A

Extracts all concept→reinforcer mappings from the R curriculum and
reads lesson content to enable scoring.
"""

import json
from pathlib import Path

def load_r_course_structure():
    """Load the R course structure file."""
    with open('frontend/public/data/course-r-fundamentals.json', 'r') as f:
        return json.load(f)

def load_lessons():
    """Load all lessons from lessons.json."""
    with open('frontend/public/data/lessons.json', 'r') as f:
        return json.load(f)

def extract_concept_reinforcer_mappings(course_data):
    """
    Extract all concept → reinforcer mappings from the R course.
    
    Pattern: Each concept lesson is followed by exactly 4 reinforcers.
    Reinforcer IDs follow pattern: concept_id + 1, +2, +3, +4 (e.g., 2001 → 20011, 20012, 20013, 20014)
    """
    mappings = []
    
    for chapter in course_data['chapters']:
        chapter_title = chapter['title']
        
        for concept_group in chapter['concepts']:
            concept_name = concept_group['name']
            lessons = concept_group['lessons']
            
            # Identify concept lessons (IDs like 2001, 2002, 2010, etc.)
            # Reinforcers have 5-digit IDs (20011, 20012, etc.)
            
            i = 0
            while i < len(lessons):
                lesson = lessons[i]
                lesson_id = lesson['id']
                
                # A concept lesson has a 4-digit ID starting with 2
                # Check if next 4 lessons are reinforcers
                if 2000 <= lesson_id <= 2999:  # Main concept lesson
                    reinforcers = []
                    
                    # Look for the next 4 lessons as potential reinforcers
                    for r in range(1, 5):
                        if i + r < len(lessons):
                            next_lesson = lessons[i + r]
                            next_id = next_lesson['id']
                            
                            # Reinforcer IDs: concept_id * 10 + 1, 2, 3, 4
                            expected_reinforcer_id = lesson_id * 10 + r
                            
                            if next_id == expected_reinforcer_id:
                                reinforcers.append({
                                    'id': next_id,
                                    'title': next_lesson['title'],
                                    'order': next_lesson.get('order', 0)
                                })
                    
                    if len(reinforcers) == 4:
                        mappings.append({
                            'chapter': chapter_title,
                            'concept_name': concept_name,
                            'concept': {
                                'id': lesson_id,
                                'title': lesson['title'],
                                'order': lesson.get('order', 0)
                            },
                            'reinforcers': reinforcers
                        })
                        i += 5  # Skip to next concept (concept + 4 reinforcers)
                    else:
                        # Concept without full reinforcers
                        if len(reinforcers) > 0:
                            mappings.append({
                                'chapter': chapter_title,
                                'concept_name': concept_name,
                                'concept': {
                                    'id': lesson_id,
                                    'title': lesson['title'],
                                    'order': lesson.get('order', 0)
                                },
                                'reinforcers': reinforcers,
                                'incomplete': True
                            })
                        i += 1
                else:
                    i += 1
    
    return mappings

def analyze_reinforcer_content(lesson_id, lessons_data):
    """
    Analyze a single reinforcer's content for scoring.
    Returns content metrics for manual scoring.
    """
    lesson = lessons_data.get(str(lesson_id))
    if not lesson:
        return {'found': False, 'reason': 'Lesson not found'}
    
    content = lesson.get('content', '')
    starter_code = lesson.get('starter_code', '')
    solution_code = lesson.get('solution_code', '')
    
    return {
        'found': True,
        'title': lesson.get('title', ''),
        'content_length': len(content),
        'has_explanation': '##' in content and len(content) > 200,
        'has_starter_code': bool(starter_code.strip()),
        'has_solution': bool(solution_code.strip()),
        'content_preview': content[:300] if content else '',
        'starter_preview': starter_code[:150] if starter_code else '',
        'solution_preview': solution_code[:150] if solution_code else ''
    }

def main():
    print("Loading R course structure...")
    course_data = load_r_course_structure()
    
    print("Loading lessons data...")
    lessons_data = load_lessons()
    
    print("Extracting concept-reinforcer mappings...")
    mappings = extract_concept_reinforcer_mappings(course_data)
    
    print(f"\nFound {len(mappings)} concept-reinforcer sets\n")
    
    # Output full mapping
    print("="*100)
    print("FULL R CURRICULUM CONCEPT-REINFORCER MAPPING")
    print("="*100)
    
    for i, m in enumerate(mappings, 1):
        print(f"\n[{i}] {m['chapter']} / {m['concept_name']}")
        print(f"    Concept: {m['concept']['id']} - {m['concept']['title']}")
        
        if m.get('incomplete'):
            print(f"    ⚠️ INCOMPLETE: Only {len(m['reinforcers'])} reinforcers found")
        
        for j, r in enumerate(m['reinforcers'], 1):
            print(f"      R{j}: {r['id']} - {r['title']}")
            
            # Get content analysis
            analysis = analyze_reinforcer_content(r['id'], lessons_data)
            if not analysis['found']:
                print(f"          ❌ {analysis['reason']}")
            else:
                content_flag = "✅" if analysis['has_explanation'] else "⚠️ Short"
                code_flag = "✅" if analysis['has_starter_code'] else "❌ No starter"
                print(f"          Content: {content_flag} ({analysis['content_length']} chars) | Code: {code_flag}")
    
    # Save detailed output to JSON
    output = {
        'summary': {
            'total_concept_sets': len(mappings),
            'total_reinforcers': sum(len(m['reinforcers']) for m in mappings),
            'incomplete_sets': sum(1 for m in mappings if m.get('incomplete', False))
        },
        'mappings': mappings
    }
    
    with open('scripts/r_reinforcer_audit_mapping.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\n\nDetailed mapping saved to scripts/r_reinforcer_audit_mapping.json")
    print(f"\nSummary: {output['summary']}")

if __name__ == '__main__':
    main()
