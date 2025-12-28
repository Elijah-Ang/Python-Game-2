import json
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models

def seed_db():
    db = SessionLocal()
    
    # Check if data exists
    if db.query(models.Course).count() > 0:
        print("Database already seeded.")
        return

    # Load JSON
    with open("backend/app/content/curriculum.json", "r") as f:
        data = json.load(f)

    for course_data in data:
        course = models.Course(
            slug=course_data["slug"],
            title=course_data["title"],
            description=course_data["description"],
            difficulty=course_data["difficulty"]
        )
        db.add(course)
        db.commit()
        db.refresh(course)

        for ch_data in course_data["chapters"]:
            chapter = models.Chapter(
                course_id=course.id,
                title=ch_data["title"],
                order_index=ch_data["order"],
                is_boss=ch_data.get("is_boss", False)
            )
            db.add(chapter)
            db.commit()
            db.refresh(chapter)

            if "lessons" in ch_data:
                for lesson_data in ch_data["lessons"]:
                    lesson = models.Lesson(
                        chapter_id=chapter.id,
                        title=lesson_data.get("title", 'Lesson'),
                        content_markdown=lesson_data.get("content", ""),
                        starter_code=lesson_data.get("starter_code", ""),
                        solution_code=lesson_data.get("solution_code", ""),
                        order_index=lesson_data.get("order", 1),
                        xp_reward=lesson_data.get("xp", 10)
                    )
                    db.add(lesson)
            db.commit()

    print("Seeding complete.")
    db.close()

if __name__ == "__main__":
    # Ensure tables exist
    models.Base.metadata.create_all(bind=engine)
    seed_db()
