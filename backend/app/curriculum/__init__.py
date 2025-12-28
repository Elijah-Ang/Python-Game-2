# Curriculum Loader - Combines all chapters
from .chapter1 import CHAPTER_1
from .chapter2 import CHAPTER_2
from .chapter3 import CHAPTER_3
from .chapter4 import CHAPTER_4
from .chapter5 import CHAPTER_5
from .chapter6 import CHAPTER_6
from .chapter7 import CHAPTER_7
from .chapter8 import CHAPTER_8
from .chapter9 import CHAPTER_9
from .chapter10 import CHAPTER_10
from .chapter11 import CHAPTER_11
from .chapter12 import CHAPTER_12
from .bosses import BOSS_LEVELS

def get_all_chapters():
    """Returns all chapters in order with bosses inserted."""
    chapters = [
        CHAPTER_1,   # 12 exercises
        CHAPTER_2,   # 9 exercises
        CHAPTER_3,   # 9 exercises
        CHAPTER_4,   # 9 exercises
        BOSS_LEVELS[0],  # Sand Sphinx
        CHAPTER_5,   # 9 exercises
        CHAPTER_6,   # 9 exercises
        CHAPTER_7,   # 9 exercises
        CHAPTER_8,   # 9 exercises
        CHAPTER_9,   # 9 exercises
        CHAPTER_10,  # 9 exercises
        CHAPTER_11,  # 9 exercises
        CHAPTER_12,  # 9 exercises
        BOSS_LEVELS[1],  # Final Boss
    ]
    return chapters

def get_all_lessons():
    """Returns flat list of all lessons with enhanced fields."""
    lessons = []
    for chapter in get_all_chapters():
        for lesson in chapter["lessons"]:
            # Add chapter metadata
            lesson["chapter_id"] = chapter["id"]
            lesson["chapter_title"] = chapter["title"]
            lesson["chapter_icon"] = chapter.get("icon", "📘")
            
            # The existing starter_code IS the solution code
            # We'll provide it but frontend will hide it initially
            if "solution_code" not in lesson:
                lesson["solution_code"] = lesson.get("starter_code", "")
            
            # Generate expected output hint from lesson content if not provided
            if "expected_output" not in lesson:
                # Extract from lesson content if there's example output
                lesson["expected_output"] = extract_expected_output(lesson.get("content", ""))
            
            lessons.append(lesson)
    return lessons

def extract_expected_output(content: str) -> str:
    """Try to extract expected output from lesson content."""
    # Look for output examples in the content
    lines = content.split("\n")
    output_lines = []
    in_output = False
    
    for line in lines:
        if "Output:" in line or "output:" in line:
            in_output = True
            continue
        if in_output:
            if line.startswith("```") or line.startswith("#") or line.startswith("##"):
                break
            if line.strip():
                output_lines.append(line.strip())
                if len(output_lines) >= 3:
                    break
    
    if output_lines:
        return "\n".join(output_lines)
    
    # Default helpful message
    return "Run your code to see the output!"

def get_lesson_by_id(lesson_id: int):
    """Get a specific lesson by ID."""
    for lesson in get_all_lessons():
        if lesson["id"] == lesson_id:
            return lesson
    return None

def get_chapter_by_id(chapter_id: int):
    """Get a specific chapter by ID."""
    for chapter in get_all_chapters():
        if chapter["id"] == chapter_id:
            return chapter
    return None

def get_total_exercises():
    """Get total count of exercises."""
    return len(get_all_lessons())
