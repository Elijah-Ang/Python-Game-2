import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import { BookOpen } from 'lucide-react';

export const Layout: React.FC = () => {
    return (
        <div className="flex flex-col min-h-screen">
            {/* Header */}
            <header className="border-b border-[var(--border-color)] bg-[var(--bg-panel)] p-4 flex items-center justify-between">
                <Link to="/" className="flex items-center gap-2 hover:opacity-80">
                    <span className="text-2xl">📊</span>
                    <h1 className="text-xl font-bold tracking-wider pixel-font text-[var(--accent-primary)]">
                        Data Science Adventure
                    </h1>
                </Link>

                <nav className="flex items-center gap-6 text-sm font-medium">
                    <Link to="/course/python-basics" className="hover:text-[var(--accent-secondary)] flex items-center gap-1 transition-colors">
                        <BookOpen className="w-4 h-4" /> Courses
                    </Link>
                </nav>
            </header>

            {/* Main Content */}
            <main className="flex-1 overflow-auto bg-[var(--bg-color)]">
                <Outlet />
            </main>
        </div>
    );
};
