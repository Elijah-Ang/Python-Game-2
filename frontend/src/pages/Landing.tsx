import React from 'react';
import { Link } from 'react-router-dom';
import { BookOpen, BarChart3, Brain, Database } from 'lucide-react';

export const Landing: React.FC = () => {
    return (
        <div className="min-h-screen bg-[var(--bg-color)]">
            {/* Hero Section */}
            <section
                className="relative h-[70vh] flex items-center justify-center overflow-hidden"
                style={{
                    backgroundImage: `url(${import.meta.env.BASE_URL}hero_background.png)`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center bottom'
                }}
            >
                {/* Gradient overlay for text readability */}
                <div className="absolute inset-0 bg-gradient-to-t from-[var(--bg-color)] via-transparent to-transparent"></div>

                <div className="relative z-10 text-center px-4">
                    <p className="text-2xl md:text-3xl mb-2 tracking-widest text-white font-bold uppercase drop-shadow-[0_2px_4px_rgba(0,0,0,0.9)]">
                        Start Your
                    </p>
                    <h1 className="text-6xl md:text-8xl font-bold mb-6 pixel-font text-transparent bg-clip-text bg-gradient-to-b from-yellow-300 via-orange-400 to-orange-600 drop-shadow-[0_2px_4px_rgba(0,0,0,0.8)]">
                        Data Science<br />Adventure
                    </h1>
                    <p className="text-xl md:text-2xl text-white font-semibold mb-8 max-w-2xl mx-auto drop-shadow-[0_2px_4px_rgba(0,0,0,0.9)]">
                        The most fun and beginner-friendly way to learn to code for Data Science.
                    </p>
                    <Link
                        to="/catalog"
                        className="inline-block bg-yellow-400 hover:bg-yellow-300 text-black font-bold py-4 px-8 rounded-lg text-lg transition-all transform hover:scale-105 shadow-lg"
                    >
                        Get started
                    </Link>
                </div>

                {/* Mascot */}
                <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2 text-6xl opacity-90">
                    🐍
                </div>
            </section>

            {/* Features Section - Data Science Focused */}
            <section className="py-20 px-8 max-w-6xl mx-auto">
                <h2 className="text-4xl font-bold text-center mb-4">
                    From Zero to Data Scientist
                </h2>
                <p className="text-center text-[var(--text-secondary)] mb-16 max-w-2xl mx-auto">
                    Learn Python and Data Science concepts step by step with interactive exercises and clear explanations.
                </p>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    <div className="panel text-center p-6">
                        <div className="w-14 h-14 mx-auto mb-4 rounded-full bg-[rgba(99,102,241,0.2)] flex items-center justify-center">
                            <BookOpen className="w-7 h-7 text-[var(--accent-secondary)]" />
                        </div>
                        <h3 className="font-bold text-lg mb-2">Python Fundamentals</h3>
                        <p className="text-[var(--text-secondary)] text-sm">
                            Master variables, loops, functions, and data structures.
                        </p>
                    </div>

                    <div className="panel text-center p-6">
                        <div className="w-14 h-14 mx-auto mb-4 rounded-full bg-[rgba(59,130,246,0.2)] flex items-center justify-center">
                            <Database className="w-7 h-7 text-blue-400" />
                        </div>
                        <h3 className="font-bold text-lg mb-2">SQL Fundamentals</h3>
                        <p className="text-[var(--text-secondary)] text-sm">
                            Query databases, join tables, and analyze data with SQL.
                        </p>
                    </div>

                    <div className="panel text-center p-6">
                        <div className="w-14 h-14 mx-auto mb-4 rounded-full bg-[rgba(250,204,21,0.2)] flex items-center justify-center">
                            <BarChart3 className="w-7 h-7 text-[var(--accent-warning)]" />
                        </div>
                        <h3 className="font-bold text-lg mb-2">Data Analysis</h3>
                        <p className="text-[var(--text-secondary)] text-sm">
                            Learn Pandas, statistics, and visualization.
                        </p>
                    </div>

                    <div className="panel text-center p-6">
                        <div className="w-14 h-14 mx-auto mb-4 rounded-full bg-[rgba(74,222,128,0.2)] flex items-center justify-center">
                            <Brain className="w-7 h-7 text-[var(--accent-success)]" />
                        </div>
                        <h3 className="font-bold text-lg mb-2">Machine Learning</h3>
                        <p className="text-[var(--text-secondary)] text-sm">
                            Build predictive models with scikit-learn.
                        </p>
                    </div>
                </div>
            </section>

            {/* CTA Section */}
            <section className="py-16 text-center">
                <h3 className="text-2xl font-bold mb-4">Ready to begin your journey?</h3>
                <Link
                    to="/catalog"
                    className="btn-retro text-lg py-3 px-6"
                >
                    Start Learning 🚀
                </Link>
            </section>
        </div>
    );
};
