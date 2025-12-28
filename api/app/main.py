from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from .curriculum import get_all_chapters, get_all_lessons, get_lesson_by_id
from .ai_verifier import verify_code

app = FastAPI(title="Data Science Adventure - Python Learning")

# Add CORS for Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Vercel serverless handler
try:
    from mangum import Mangum
    handler = Mangum(app)
except ImportError:
    handler = None

# Request/Response models
class VerifyRequest(BaseModel):
    lesson_id: int
    user_code: str
    actual_output: str

class VerifyResponse(BaseModel):
    correct: bool
    feedback: str
    suggestions: list[str] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Data Science Adventure API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/courses")
def get_courses():
    """List all courses (we have one: Python Basics)"""
    chapters = get_all_chapters()
    lessons = get_all_lessons()
    return [
        {
            "id": 1,
            "slug": "python-basics",
            "title": "Python for Data Science",
            "description": "Learn Python from fundamentals to Machine Learning",
            "difficulty": "beginner",
            "chapters_count": len(chapters),
            "lessons_count": len(lessons)
        }
    ]

@app.get("/courses/{course_slug}")
def get_course_details(course_slug: str):
    """Get course with all chapters and lessons"""
    if course_slug != "python-basics":
        raise HTTPException(status_code=404, detail="Course not found")
    
    chapters = get_all_chapters()
    return {
        "id": 1,
        "title": "Python for Data Science",
        "chapters": [
            {
                "id": ch["id"],
                "title": ch["title"],
                "icon": ch.get("icon", "📘"),
                "is_boss": ch.get("is_boss", False),
                "lessons": [
                    {
                        "id": l["id"],
                        "title": l["title"],
                        "order": l["order"]
                    } for l in ch["lessons"]
                ]
            } for ch in chapters
        ]
    }

@app.get("/lessons/{lesson_id}")
def get_lesson(lesson_id: int):
    """Get a specific lesson with all content"""
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    
    return {
        "id": lesson["id"],
        "title": lesson["title"],
        "content": lesson["content"],
        "starter_code": lesson.get("starter_code", "# Write your code here\n"),
        "solution_code": lesson.get("solution_code", lesson.get("starter_code", "")),
        "expected_output": lesson.get("expected_output", ""),
        "chapter_id": lesson.get("chapter_id"),
        "chapter_title": lesson.get("chapter_title")
    }

@app.get("/lessons")
def list_lessons():
    """List all lessons"""
    lessons = get_all_lessons()
    return [
        {
            "id": l["id"],
            "title": l["title"],
            "chapter_id": l.get("chapter_id"),
            "chapter_title": l.get("chapter_title")
        } for l in lessons
    ]

@app.post("/verify", response_model=VerifyResponse)
async def verify_code_endpoint(request: VerifyRequest):
    """
    Verify user's code by comparing output to expected output.
    No AI - just output comparison!
    """
    lesson = get_lesson_by_id(request.lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    
    result = verify_code(
        expected_output=lesson.get("expected_output", ""),
        actual_output=request.actual_output,
        user_code=request.user_code
    )
    
    return VerifyResponse(
        correct=result["correct"],
        feedback=result["feedback"],
        suggestions=result.get("suggestions", [])
    )

