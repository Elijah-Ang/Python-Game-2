import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Play, Lock } from 'lucide-react';

interface Course {
    id: number;
    slug: string;
    title: string;
    description: string;
    difficulty: string;
    chapters_count: number;
}

export const Dashboard: React.FC = () => {
    const [courses, setCourses] = useState<Course[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch(`${import.meta.env.BASE_URL}data/courses.json?t=${Date.now()}`)
            .then(res => res.json())
            .then(data => {
                setCourses(data);
                setLoading(false);
            })
            .catch(err => {
                console.error("Failed to fetch courses", err);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <div className="p-8 text-center animate-pulse">Loading World Map...</div>;
    }

    return (
        <div className="p-8 max-w-6xl mx-auto">
            <div className="mb-8 text-center">
                <h2 className="text-3xl font-bold mb-2 pixel-font text-[var(--accent-primary)]">CHOOSE YOUR PATH</h2>
                <p className="text-[var(--text-secondary)]">Select a realm to begin your adventure.</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {courses.map(course => (
                    <div key={course.id} className="panel group hover:border-[var(--accent-secondary)] transition-all">
                        <div className="h-40 bg-[var(--bg-color)] mb-4 rounded border border-[var(--border-color)] flex items-center justify-center overflow-hidden relative">
                            <img
                                src={`${import.meta.env.BASE_URL}assets/headers/${course.slug === 'sql-fundamentals' ? 'sql_landscape.png' :
                                    course.slug === 'r-fundamentals' ? 'r_landscape.png' : 'python_landscape.png'
                                    }`}
                                alt={course.title}
                                className="w-full h-full object-cover pixel-art transition-transform duration-500 group-hover:scale-110"
                            />
                        </div>

                        <div className="flex justify-between items-start mb-2">
                            <h3 className="text-xl font-bold">{course.title}</h3>
                            <span className="text-xs px-2 py-1 rounded bg-[rgba(99,102,241,0.2)] text-[var(--accent-secondary)] border border-[rgba(99,102,241,0.3)]">
                                {course.difficulty}
                            </span>
                        </div>

                        <p className="text-sm text-[var(--text-secondary)] mb-4 h-10 overflow-hidden text-ellipsis">
                            {course.description}
                        </p>

                        <div className="flex items-center justify-between mt-auto">
                            <div className="text-xs text-[var(--text-secondary)]">
                                {course.chapters_count} Chapters
                            </div>

                            <Link to={`/course/${course.slug}`} className="btn-retro flex items-center gap-2 text-sm">
                                <Play className="w-4 h-4" /> START
                            </Link>
                        </div>
                    </div>
                ))}

                {/* Coming Soon Card */}
                <div className="panel border-dashed border-[var(--text-secondary)] opacity-50 flex flex-col items-center justify-center min-h-[300px]">
                    <Lock className="w-8 h-8 mb-2" />
                    <span className="pixel-font">LOCKED REGION</span>
                </div>
            </div>
        </div>
    );
};
