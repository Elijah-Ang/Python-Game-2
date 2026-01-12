import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ChevronDown, ChevronUp, Trophy } from 'lucide-react';

interface LessonItem {
    id: number;
    title: string;
    order: number;
    difficulty?: number;
}

interface Concept {
    name: string;
    icon: string;
    lessons: LessonItem[];
}

interface Chapter {
    id: number;
    title: string;
    icon: string;
    is_boss: boolean;
    lessons?: LessonItem[];
    concepts?: Concept[];
}

interface CourseDetails {
    id: number;
    title: string;
    chapters: Chapter[];
}

export const Course: React.FC = () => {
    const { slug } = useParams<{ slug: string }>();
    const [course, setCourse] = useState<CourseDetails | null>(null);
    const [expandedChapter, setExpandedChapter] = useState<number | null>(1);

    useEffect(() => {
        fetch(`${import.meta.env.BASE_URL}data/course-${slug}.json?t=${Date.now()}`)
            .then(res => res.json())
            .then(data => setCourse(data))
            .catch(err => console.error(err));
    }, [slug]);

    if (!course) return <div className="p-8 text-center animate-pulse">Loading Course...</div>;

    // Count total lessons including those in concepts
    const totalLessons = course.chapters.reduce((acc, ch) => {
        if (ch.concepts) {
            return acc + ch.concepts.reduce((cAcc, concept) => cAcc + concept.lessons.length, 0);
        }
        return acc + (ch.lessons?.length || 0);
    }, 0);

    // Helper to get all lessons from a chapter (either from concepts or flat lessons)
    const getChapterLessons = (chapter: Chapter): LessonItem[] => {
        if (chapter.concepts) {
            return chapter.concepts.flatMap(c => c.lessons);
        }
        return chapter.lessons || [];
    };

    return (
        <div className="min-h-screen bg-[var(--bg-color)]">
            {/* Course Banner */}
            <div
                className="h-[250px] w-full relative overflow-hidden"
                style={{
                    backgroundImage: `url(${import.meta.env.BASE_URL}assets/headers/${slug === 'sql-fundamentals' ? 'sql_landscape.png' :
                        slug === 'r-fundamentals' ? 'r_landscape.png' : 'python_landscape.png'
                        }?v=5)`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center'
                }}
            >
                <div className="absolute bottom-0 left-0 right-0 p-8">
                    <h1 className="text-5xl font-bold pixel-font text-white drop-shadow-lg">
                        {course.title}
                    </h1>
                    <p className="text-white/80 mt-2 max-w-xl">
                        {course.slug === 'python-basics' ? 'Master Python from fundamentals to Machine Learning.' :
                            course.slug === 'sql-fundamentals' ? 'Master SQL from basics to analytics engineering.' :
                                'Visualize and transform data with ggplot2 and dplyr.'} {totalLessons} exercises across {course.chapters.length} chapters.
                    </p>
                </div>

            </div>

            <div className="max-w-4xl mx-auto px-8 py-8">
                {/* All Chapters */}
                <div className="space-y-2">
                    {course.chapters.map((chapter) => {
                        const chapterLessons = getChapterLessons(chapter);
                        return (
                            <div key={chapter.id} className="border border-[var(--border-color)] rounded-lg overflow-hidden bg-[var(--bg-panel)]">
                                {/* Chapter Header */}
                                <button
                                    onClick={() => setExpandedChapter(expandedChapter === chapter.id ? null : chapter.id)}
                                    className="w-full flex items-center justify-between p-4 hover:bg-[rgba(255,255,255,0.05)] transition-colors"
                                >
                                    <div className="flex items-center gap-4">
                                        <div className={`w-10 h-10 rounded-full flex items-center justify-center text-xl ${chapter.is_boss
                                            ? 'bg-red-500/20 border-2 border-red-500'
                                            : 'bg-[var(--border-color)]'
                                            }`}>
                                            {chapter.icon || (chapter.is_boss ? <Trophy className="w-5 h-5" /> : '📘')}
                                        </div>
                                        <span className="font-medium text-lg">{chapter.title}</span>
                                        {chapter.is_boss && (
                                            <span className="text-xs bg-[rgba(239,68,68,0.2)] text-red-400 px-2 py-1 rounded">BOSS</span>
                                        )}
                                    </div>

                                    <div className="flex items-center gap-3">
                                        <span className="text-xs text-[var(--text-secondary)]">
                                            {chapterLessons.length} {chapterLessons.length === 1 ? 'exercise' : 'exercises'}
                                        </span>
                                        {expandedChapter === chapter.id ? (
                                            <ChevronUp className="w-5 h-5 text-[var(--text-secondary)]" />
                                        ) : (
                                            <ChevronDown className="w-5 h-5 text-[var(--text-secondary)]" />
                                        )}
                                    </div>
                                </button>

                                {/* Chapter Content (Expanded) */}
                                {expandedChapter === chapter.id && (
                                    <div className="border-t border-[var(--border-color)] p-4 bg-[var(--bg-color)]">
                                        {/* Render with concept subheadings if available */}
                                        {chapter.concepts ? (
                                            <div className="space-y-6">
                                                {chapter.concepts.map((concept, conceptIdx) => {
                                                    // Calculate the starting lesson number for this concept
                                                    const previousLessonsCount = chapter.concepts!
                                                        .slice(0, conceptIdx)
                                                        .reduce((acc, c) => acc + c.lessons.length, 0);

                                                    return (
                                                        <div key={concept.name}>
                                                            {/* Concept Subheading */}
                                                            <div className="flex items-center gap-2 mb-3 pb-2 border-b border-[var(--border-color)]">
                                                                <span className="text-lg">{concept.icon}</span>
                                                                <h3 className="font-bold text-[var(--accent-primary)]">{concept.name}</h3>
                                                                <span className="text-xs text-[var(--text-secondary)] ml-auto">
                                                                    {concept.lessons.length} exercises
                                                                </span>
                                                            </div>
                                                            {/* Concept Lessons */}
                                                            <div className="space-y-1 pl-2">
                                                                {concept.lessons.map((lesson, idx) => (
                                                                    <Link
                                                                        key={lesson.id}
                                                                        to={`/lesson/${lesson.id}`}
                                                                        className={`flex items-center justify-between p-3 rounded hover:bg-[rgba(255,255,255,0.05)] transition-colors group ${lesson.id > 9999 ? 'ml-12 border-l-2 border-[var(--border-color)] bg-[rgba(255,255,255,0.02)]' : ''
                                                                            }`}
                                                                    >
                                                                        <div className="flex items-center gap-3">
                                                                            <span className="text-xs text-[var(--text-secondary)] w-8">
                                                                                {previousLessonsCount + idx + 1}.
                                                                            </span>
                                                                            <span className="font-medium group-hover:text-[var(--accent-secondary)]">{lesson.title}</span>
                                                                        </div>

                                                                        <span className="px-4 py-1 bg-[var(--accent-secondary)] text-white text-sm font-medium rounded opacity-0 group-hover:opacity-100 transition-opacity">
                                                                            Start
                                                                        </span>
                                                                    </Link>
                                                                ))}
                                                            </div>
                                                        </div>
                                                    );
                                                })}
                                            </div>
                                        ) : (
                                            /* Fallback to flat lesson list for chapters without concepts */
                                            <div className="space-y-2">
                                                {(chapter.lessons || []).map((lesson, idx) => (
                                                    <Link
                                                        key={lesson.id}
                                                        to={`/lesson/${lesson.id}`}
                                                        className={`flex items-center justify-between p-3 rounded hover:bg-[rgba(255,255,255,0.05)] transition-colors group ${lesson.id > 9999 ? 'ml-12 border-l-2 border-[var(--border-color)] bg-[rgba(255,255,255,0.02)]' : ''
                                                            }`}
                                                    >
                                                        <div className="flex items-center gap-3">
                                                            <span className="text-xs text-[var(--text-secondary)] w-16">
                                                                {idx + 1}.
                                                            </span>
                                                            <span className="font-medium group-hover:text-[var(--accent-secondary)]">{lesson.title}</span>
                                                        </div>

                                                        <span className="px-4 py-1 bg-[var(--accent-secondary)] text-white text-sm font-medium rounded opacity-0 group-hover:opacity-100 transition-opacity">
                                                            Start
                                                        </span>
                                                    </Link>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                )}
                            </div>
                        );
                    })}
                </div>
            </div>
        </div>
    );
};
