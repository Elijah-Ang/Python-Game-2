from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    current_streak = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    progress = relationship("UserProgress", back_populates="user")

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    difficulty = Column(String)

    chapters = relationship("Chapter", back_populates="course")

class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String)
    order_index = Column(Integer)
    is_boss = Column(Boolean, default=False)
    
    course = relationship("Course", back_populates="chapters")
    lessons = relationship("Lesson", back_populates="chapter")

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"))
    title = Column(String)
    content_markdown = Column(Text) # The instructional text
    starter_code = Column(Text)
    solution_code = Column(Text)
    order_index = Column(Integer)
    xp_reward = Column(Integer, default=10)
    
    chapter = relationship("Chapter", back_populates="lessons")

class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    status = Column(String, default="locked") # locked, unlocked, completed
    code_submitted = Column(Text, nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("User", back_populates="progress")
    # lesson relationship could be added if needed
