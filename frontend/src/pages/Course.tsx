import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ChevronDown, ChevronUp, Trophy } from 'lucide-react';

interface LessonItem {
    id: number;
    title: string;
    order: number;
}

interface Chapter {
    id: number;
    title: string;
    icon: string;
    is_boss: boolean;
    lessons: LessonItem[];
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
        fetch(`/api/courses/${slug}`)
            .then(res => res.json())
            .then(data => setCourse(data))
            .catch(err => console.error(err));
    }, [slug]);

    if (!course) return <div className="p-8 text-center animate-pulse">Loading Course...</div>;

    const totalLessons = course.chapters.reduce((acc, ch) => acc + ch.lessons.length, 0);

    return (
        <div className="min-h-screen bg-[var(--bg-color)]">
            {/* Course Banner */}
            <div
                className="h-64 relative overflow-hidden"
                style={{
                    backgroundImage: 'linear-gradient(135deg, #1a4d2e 0%, #2d5a3d 50%, #1e3a29 100%)'
                }}
            >
                <div className="absolute bottom-0 left-0 right-0 p-8 bg-gradient-to-t from-[var(--bg-color)] to-transparent">
                    <span className="inline-block px-3 py-1 bg-[var(--accent-secondary)] text-white text-xs font-bold rounded mb-2">
                        BEGINNER → ADVANCED
                    </span>
                    <h1 className="text-5xl font-bold pixel-font text-white drop-shadow-lg">
                        {course.title}
                    </h1>
                    <p className="text-white/80 mt-2 max-w-xl">
                        Master Python from fundamentals to Machine Learning. {totalLessons} exercises across {course.chapters.length} chapters.
                    </p>
                </div>
                <div className="absolute bottom-4 right-8 text-6xl opacity-80">🐍</div>
            </div>

            <div className="max-w-4xl mx-auto px-8 py-8">
                {/* All Chapters */}
                <div className="space-y-2">
                    {course.chapters.map((chapter) => (
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
                                        {chapter.lessons.length} {chapter.lessons.length === 1 ? 'exercise' : 'exercises'}
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
                                    <div className="space-y-2">
                                        {chapter.lessons.map((lesson, idx) => (
                                            <Link
                                                key={lesson.id}
                                                to={`/lesson/${lesson.id}`}
                                                className="flex items-center justify-between p-3 rounded hover:bg-[rgba(255,255,255,0.05)] transition-colors group"
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
                                </div>
                            )}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};
