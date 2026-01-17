const fs = require('fs');
const path = require('path');

const lessonsPath = path.resolve(__dirname, '../frontend/public/data/lessons.json');
const pythonCoursePath = path.resolve(__dirname, '../frontend/public/data/course-python-basics.json');
const sqlCoursePath = path.resolve(__dirname, '../frontend/public/data/course-sql-fundamentals.json');

const lessons = JSON.parse(fs.readFileSync(lessonsPath, 'utf8'));
const pythonCourse = JSON.parse(fs.readFileSync(pythonCoursePath, 'utf8'));
const sqlCourse = JSON.parse(fs.readFileSync(sqlCoursePath, 'utf8'));

const getChapterLessonIds = (chapter) => {
  const ids = [];
  if (!chapter) return ids;
  if (Array.isArray(chapter.lessons)) {
    chapter.lessons.forEach((lesson) => ids.push(String(lesson.id)));
    return ids;
  }
  (chapter.concepts || []).forEach((concept) => {
    (concept.lessons || []).forEach((lesson) => ids.push(String(lesson.id)));
  });
  return ids;
};

const stripW3SchoolsChapter = (course) => {
  const removed = [];
  course.chapters = (course.chapters || []).filter((chapter) => {
    const title = String(chapter.title || '').toLowerCase();
    if (title.includes('w3schools coverage')) {
      removed.push(...getChapterLessonIds(chapter));
      return false;
    }
    return true;
  });
  return removed;
};

const pythonRemoved = stripW3SchoolsChapter(pythonCourse);
const sqlRemoved = stripW3SchoolsChapter(sqlCourse);
const removedLessonIds = new Set([...pythonRemoved, ...sqlRemoved]);

removedLessonIds.forEach((id) => {
  if (lessons[id]) {
    delete lessons[id];
  }
});

fs.writeFileSync(pythonCoursePath, JSON.stringify(pythonCourse, null, 2));
fs.writeFileSync(sqlCoursePath, JSON.stringify(sqlCourse, null, 2));
fs.writeFileSync(lessonsPath, JSON.stringify(lessons, null, 2));

console.log(
  `Removed W3Schools coverage chapters and ${removedLessonIds.size} lessons from lessons.json.`
);
