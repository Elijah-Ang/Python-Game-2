
import json
import os

COURSE_FILE = 'frontend/public/data/course-r-fundamentals.json'
LESSONS_FILE = 'frontend/public/data/lessons.json'

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def inject_reinforcers(reinforcers_map):
    """
    reinforcers_map: dict where key is the ORIGINAL lesson_id (str), 
    and value is a list of 4 lesson objects (dicts).
    """
    course_data = load_json(COURSE_FILE)
    lessons_data = load_json(LESSONS_FILE)

    # 1. Update lessons.json
    for original_id, new_lessons in reinforcers_map.items():
        original_lesson = lessons_data.get(str(original_id))
        if not original_lesson:
            print(f"Warning: Original lesson {original_id} not found in lessons.json")
            continue

        for i, lesson in enumerate(new_lessons):
            # Construct new ID: "2001" -> "20011", "20012", etc.
            # Actually, to avoid collisions if we have 5-digit IDs later, let's use a standard appending scheme.
            # But the plan implies reusing the ID prefix. 
            # Let's assume the user is fine with 5 digit IDs for reinforcers.
            # 2001 -> 20011..4
            
            # Ensure lesson has the required fields
            lesson['id'] = int(f"{original_id}{i+1}")
            lesson['chapter_title'] = original_lesson.get('chapter_title', '')
            lesson['chapter_id'] = original_lesson.get('chapter_id', 0)
            
            # Add to lessons_data
            lessons_data[str(lesson['id'])] = lesson

    save_json(LESSONS_FILE, lessons_data)

    # 2. Update course-r-fundamentals.json (The Order)
    # We need to find where the original lesson is, and insert the new ones immediately after.
    
    # 2. Update course-r-fundamentals.json (The Order)
    # The file content is a dict with "chapters" list.
    
    root_list = course_data.get('chapters', [])
    
    for section in root_list:
        if 'concepts' not in section: continue
        for concept in section['concepts']:
            if 'lessons' not in concept: continue
            
            new_lesson_list = []
            for lesson in concept['lessons']:
                new_lesson_list.append(lesson)
                
                # If this is one of our targets
                if str(lesson['id']) in reinforcers_map:
                    # Append the 4 reinforcers
                    reinforcers = reinforcers_map[str(lesson['id'])]
                    for i, r_lesson in enumerate(reinforcers):
                        new_id = int(f"{lesson['id']}{i+1}")
                        new_entry = {
                            "id": new_id,
                            "title": r_lesson['title'],  # Use the title from the lesson content
                            "order": lesson['order'], # We will reorder later, just copy for now
                            "difficulty": 1 # Reinforcers are easy
                        }
                        new_lesson_list.append(new_entry)
            
            # Re-index the order
            for idx, lesson in enumerate(new_lesson_list):
                lesson['order'] = idx + 1
            
            concept['lessons'] = new_lesson_list

    save_json(COURSE_FILE, course_data)
    print("Successfully injected reinforcers.")

if __name__ == "__main__":
    # This block allows us to paste a dictionary here and run it.
    # For now, it does nothing until we call it with data.
    pass
