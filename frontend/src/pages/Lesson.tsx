import React, { useEffect, useState, useCallback, useRef } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import Editor from '@monaco-editor/react';
import { Play, Send, ChevronRight, FileCode, RotateCcw, Eye, EyeOff, Lightbulb, X, CheckCircle, AlertCircle } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import confetti from 'canvas-confetti';
import { verifyCode, verifySql } from '../utils/verifier';

interface LessonData {
    id: number;
    title: string;
    content: string;
    starter_code: string;
    solution_code: string;
    expected_output: string;
    chapter_id: number;
}

interface VerifyResult {
    correct: boolean;
    feedback: string;
    suggestions: string[];
}

declare global {
    interface Window {
        loadPyodide: any;
    }
}

export const Lesson: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const navigate = useNavigate();
    const [lesson, setLesson] = useState<LessonData | null>(null);
    const [code, setCode] = useState("");
    const [output, setOutput] = useState("");
    const [graphOutput, setGraphOutput] = useState<string | null>(null);
    const [isRunning, setIsRunning] = useState(false);
    const [isVerifying, setIsVerifying] = useState(false);
    const [pyodide, setPyodide] = useState<any>(null);
    const [showSolution, setShowSolution] = useState(false);
    const [verifyResult, setVerifyResult] = useState<VerifyResult | null>(null);
    const [editorHeightPercent, setEditorHeightPercent] = useState(65);
    const [isDragging, setIsDragging] = useState(false);
    const rightPanelRef = useRef<HTMLDivElement>(null);

    // Load Lesson Data from static JSON
    useEffect(() => {
        fetch('/data/lessons.json')
            .then(res => res.json())
            .then(data => {
                const lessonData = data[id as string];
                if (lessonData) {
                    setLesson(lessonData);
                    // SQL lessons have IDs >= 1001
                    const isSql = Number(id) >= 1001;
                    setCode(isSql ? "-- Write your SQL here\n\n" : "# Write your code here\n\n");
                    setShowSolution(false);
                    setVerifyResult(null);
                    setOutput("");
                    setGraphOutput(null);
                }
            })
            .catch(err => console.error(err));
    }, [id]);

    // Load Pyodide with matplotlib support
    useEffect(() => {
        const initPyodide = async () => {
            if (window.loadPyodide && !pyodide) {
                try {
                    const py = await window.loadPyodide();
                    // Load essential packages
                    await py.loadPackage(['numpy', 'micropip']);
                    const micropip = py.pyimport("micropip");
                    await micropip.install("matplotlib");
                    setPyodide(py);
                    console.log("Pyodide Ready with matplotlib");
                } catch (e) {
                    console.error("Pyodide init error:", e);
                    // Try without matplotlib
                    const py = await window.loadPyodide();
                    setPyodide(py);
                }
            }
        };
        initPyodide();
    }, [pyodide]);

    const triggerConfetti = useCallback(() => {
        confetti({
            particleCount: 100,
            spread: 70,
            origin: { y: 0.6 }
        });
        // Second burst
        setTimeout(() => {
            confetti({
                particleCount: 50,
                angle: 60,
                spread: 55,
                origin: { x: 0 }
            });
            confetti({
                particleCount: 50,
                angle: 120,
                spread: 55,
                origin: { x: 1 }
            });
        }, 250);
    }, []);

    const runCode = async (): Promise<string> => {
        if (!pyodide) {
            const msg = "⏳ Loading Python engine...";
            setOutput(msg);
            return msg;
        }
        setIsRunning(true);
        setOutput("");
        setGraphOutput(null);

        let resultOutput = "";
        try {
            let outputBuffer = "";
            pyodide.setStdout({ batched: (msg: string) => { outputBuffer += msg + "\n"; } });

            // Setup matplotlib to capture figures
            const setupCode = `
import sys
import io
import base64

# Override plt.show to capture figure
_captured_figures = []

def _capture_show():
    import matplotlib.pyplot as plt
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor='#1a1a2e')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    _captured_figures.append(img_base64)
    plt.close()

# Try to patch matplotlib if available
try:
    import matplotlib.pyplot as plt
    plt.style.use('dark_background')
    plt.show = _capture_show
except:
    pass
`;
            await pyodide.runPythonAsync(setupCode);
            await pyodide.runPythonAsync(code);

            // Check for captured figures
            const figures = pyodide.globals.get('_captured_figures');
            if (figures && figures.length > 0) {
                const figArray = figures.toJs();
                if (figArray.length > 0) {
                    setGraphOutput(`data:image/png;base64,${figArray[figArray.length - 1]}`);
                }
            }

            resultOutput = outputBuffer || "✓ Code executed successfully (no output)";
            setOutput(resultOutput);
        } catch (err: any) {
            resultOutput = "❌ Error:\n" + err.toString();
            setOutput(resultOutput);
        } finally {
            setIsRunning(false);
        }
        return resultOutput;
    };

    // For SQL lessons, we can't run in browser - just verify against expected output
    const runSqlCode = (): string => {
        const msg = "\u2139\ufe0f SQL queries are verified by comparing your query structure to the expected solution.\n\nClick 'Submit' to check your answer!";
        setOutput(msg);
        return msg;
    };

    const submitAnswer = async () => {
        const currentId = Number(id) || 1;
        const isSql = currentId >= 1001;

        setIsVerifying(true);

        let result;
        if (isSql) {
            // For SQL, compare user code against solution code
            result = verifySql(
                lesson?.solution_code || '',
                code
            );
        } else {
            // For Python, run code and compare output
            const executionOutput = await runCode();
            result = verifyCode(
                lesson?.expected_output || '',
                executionOutput,
                code
            );
        }

        setVerifyResult(result);

        if (result.correct) {
            triggerConfetti();
        }

        setIsVerifying(false);
    };

    const toggleSolution = () => {
        setShowSolution(!showSolution);
    };

    const resetCode = () => {
        // Reset to the lesson's starter code, not generic text
        setCode(lesson?.starter_code || "# Write your code here\n\n");
        setShowSolution(false);
        setVerifyResult(null);
        setOutput("");
        setGraphOutput(null);
    };

    const goToNext = () => {
        const currentId = Number(id);
        const isSql = currentId >= 1001;
        const nextId = currentId + 1;

        if (isSql) {
            // SQL lessons: 1001-1098 currently implemented
            if (nextId <= 1098) {
                navigate(`/lesson/${nextId}`);
            } else {
                navigate('/course/sql-fundamentals');
            }
        } else {
            // Python lessons: 1-144
            if (nextId <= 144) {
                navigate(`/lesson/${nextId}`);
            } else {
                navigate('/course/python-basics');
            }
        }
    };

    const goToPrev = () => {
        const prevId = Number(id) - 1;
        if (prevId > 0) {
            navigate(`/lesson/${prevId}`);
        }
    };

    if (!lesson) {
        return (
            <div className="h-screen bg-[var(--bg-color)] flex items-center justify-center">
                <div className="animate-pulse text-[var(--text-secondary)]">Loading exercise...</div>
            </div>
        );
    }

    const currentExercise = Number(id) || 1;
    const isSqlLesson = currentExercise >= 1001;
    const totalExercises = isSqlLesson ? 161 : 113;
    const displayExercise = isSqlLesson ? currentExercise - 1000 : currentExercise;
    const courseSlug = isSqlLesson ? 'sql-fundamentals' : 'python-basics';
    const courseName = isSqlLesson ? 'SQL' : 'Python';
    const editorLanguage = isSqlLesson ? 'sql' : 'python';
    const scriptFilename = isSqlLesson ? 'query.sql' : 'script.py';

    return (
        <div className="h-screen flex flex-col bg-[var(--bg-color)] overflow-hidden">
            {/* Top Navigation Bar */}
            <div className="h-12 bg-[var(--bg-panel)] border-b border-[var(--border-color)] flex items-center px-4 gap-4 shrink-0">
                <Link to="/" className="flex items-center gap-2 hover:opacity-80">
                    <span className="text-lg">📊</span>
                    <span className="font-bold text-[var(--accent-primary)] pixel-font">DS Adventure</span>
                </Link>

                <span className="text-[var(--border-color)]">|</span>

                <div className="flex items-center gap-2">
                    <span className="text-sm font-medium">{courseName} / {lesson.title}</span>
                </div>

                {/* Progress Bar */}
                <div className="flex-1 max-w-xs mx-4">
                    <div className="h-2 bg-[var(--border-color)] rounded-full overflow-hidden">
                        <div
                            className="h-full bg-[var(--accent-secondary)] transition-all"
                            style={{ width: `${(displayExercise / totalExercises) * 100}%` }}
                        ></div>
                    </div>
                </div>
                <span className="text-xs text-[var(--text-secondary)]">
                    {Math.round((displayExercise / totalExercises) * 100)}%
                </span>

                {/* Right side */}
                <div className="ml-auto flex items-center gap-4 text-xs text-[var(--text-secondary)]">
                    <Link to={`/course/${courseSlug}`} className="hover:text-white">← Back to course</Link>
                </div>
            </div>

            {/* Main Content Area */}
            <div className="flex-1 flex overflow-hidden">
                {/* Left Panel: Instructions */}
                <div className="w-1/2 flex flex-col border-r border-[var(--border-color)]">
                    <div className="flex-1 overflow-y-auto p-6">
                        {/* Exercise Number */}
                        <h1 className="text-2xl font-bold mb-4 pixel-font">
                            {String(displayExercise).padStart(2, '0')}. {lesson.title}
                        </h1>

                        {/* Lesson Content */}
                        <div className="prose prose-invert prose-sm max-w-none lesson-content">
                            <ReactMarkdown
                                remarkPlugins={[remarkGfm]}
                                components={{
                                    h1: ({ children }) => <h1 className="text-xl font-bold mt-6 mb-3 text-[var(--accent-primary)]">{children}</h1>,
                                    h2: ({ children }) => <h2 className="text-lg font-bold mt-5 mb-2">{children}</h2>,
                                    h3: ({ children }) => <h3 className="text-md font-bold mt-4 mb-2">{children}</h3>,
                                    p: ({ children }) => <p className="mb-3 leading-relaxed">{children}</p>,
                                    ul: ({ children }) => <ul className="list-disc list-inside mb-3 space-y-1">{children}</ul>,
                                    ol: ({ children }) => <ol className="list-decimal list-inside mb-3 space-y-1">{children}</ol>,
                                    code: ({ className, children }) => {
                                        const isBlock = className?.includes('language-');
                                        return isBlock ? (
                                            <pre className="bg-[#0d0d10] p-3 rounded text-sm overflow-x-auto my-3">
                                                <code className="text-[var(--accent-success)]">{children}</code>
                                            </pre>
                                        ) : (
                                            <code className="bg-[#0d0d10] px-1.5 py-0.5 rounded text-[var(--accent-warning)] text-sm">{children}</code>
                                        );
                                    },
                                    strong: ({ children }) => <strong className="text-[var(--accent-warning)] font-bold">{children}</strong>,
                                    a: ({ href, children }) => <a href={href} className="text-[var(--accent-secondary)] underline hover:opacity-80">{children}</a>,
                                    table: ({ children }) => <table className="w-full border-collapse my-3 text-sm">{children}</table>,
                                    th: ({ children }) => <th className="border border-[var(--border-color)] px-2 py-1 bg-[var(--bg-panel)]">{children}</th>,
                                    td: ({ children }) => <td className="border border-[var(--border-color)] px-2 py-1">{children}</td>,
                                }}
                            >
                                {lesson.content}
                            </ReactMarkdown>
                        </div>

                        {/* Expected Output Section */}
                        {lesson.expected_output && lesson.expected_output !== "Run your code to see the output!" && (
                            <div className="mt-6 p-3 bg-[var(--bg-panel)] rounded border border-[var(--border-color)]">
                                <div className="text-sm font-medium text-[var(--accent-secondary)] mb-2 flex items-center gap-2">
                                    <Lightbulb className="w-4 h-4" />
                                    Expected Output:
                                </div>
                                <pre className="bg-[#0d0d10] p-3 rounded text-sm text-[var(--accent-success)] overflow-x-auto">
                                    {lesson.expected_output}
                                </pre>
                            </div>
                        )}

                        {/* Solution Section (Collapsible) */}
                        {lesson.solution_code && (
                            <div className="mt-4">
                                <button
                                    onClick={toggleSolution}
                                    className="flex items-center gap-2 text-sm text-[var(--accent-warning)] hover:opacity-80"
                                >
                                    {showSolution ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                                    {showSolution ? "Hide Solution" : "Show Solution"}
                                </button>
                                {showSolution && (
                                    <pre className="mt-2 bg-[#1a1a2e] p-3 rounded text-sm text-[var(--text-secondary)] overflow-x-auto border border-[var(--accent-warning)] border-opacity-30">
                                        <code>{lesson.solution_code}</code>
                                    </pre>
                                )}
                            </div>
                        )}
                    </div>

                    {/* Instructions Footer */}
                    <div className="border-t border-[var(--border-color)] bg-[var(--bg-panel)] p-3">
                        <div className="flex items-center justify-between">
                            <div className="flex items-center gap-3">
                                <div className="w-8 h-8 bg-[var(--border-color)] rounded flex items-center justify-center">
                                    📝
                                </div>
                                <div>
                                    <div className="text-sm font-medium">{lesson.title}</div>
                                    <div className="text-xs text-[var(--text-secondary)]">
                                        Exercise {displayExercise} / {totalExercises}
                                    </div>
                                </div>
                            </div>
                            <div className="flex items-center gap-2">
                                <button
                                    onClick={goToPrev}
                                    disabled={currentExercise <= 1}
                                    className="px-4 py-2 bg-[var(--border-color)] rounded hover:bg-[rgba(255,255,255,0.1)] disabled:opacity-40 transition-colors"
                                >
                                    Back
                                </button>
                                <button
                                    onClick={goToNext}
                                    className="px-4 py-2 bg-[var(--border-color)] rounded hover:bg-[rgba(255,255,255,0.1)] transition-colors"
                                >
                                    Next
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Right Panel: Code Editor + Terminal */}
                <div ref={rightPanelRef} className="w-1/2 flex flex-col">
                    {/* Editor Header */}
                    <div className="h-10 bg-[var(--bg-panel)] border-b border-[var(--border-color)] flex items-center px-2 justify-between">
                        <div className="flex items-center">
                            <div className="px-3 py-1.5 bg-[var(--bg-color)] border-t-2 border-t-[var(--accent-warning)] text-sm flex items-center gap-2">
                                <FileCode className="w-4 h-4 text-[var(--accent-warning)]" />
                                <span>{scriptFilename}</span>
                            </div>
                        </div>
                    </div>

                    {/* Code Editor */}
                    <div style={{ height: `${editorHeightPercent}%` }} className="min-h-0">
                        <Editor
                            height="100%"
                            language={editorLanguage}
                            theme="vs-dark"
                            value={code}
                            onChange={(val) => setCode(val || "")}
                            options={{
                                minimap: { enabled: false },
                                fontSize: 14,
                                fontFamily: "'Fira Code', 'Monaco', monospace",
                                lineNumbers: 'on',
                                scrollBeyondLastLine: false,
                                padding: { top: 16 },
                            }}
                        />
                    </div>

                    {/* Editor Toolbar */}
                    <div className="h-12 bg-[var(--bg-panel)] border-t border-b border-[var(--border-color)] flex items-center px-4 justify-between">
                        <div className="flex items-center gap-2">
                            <button
                                onClick={resetCode}
                                className="w-8 h-8 flex items-center justify-center rounded hover:bg-[rgba(255,255,255,0.1)]"
                                title="Reset Code"
                            >
                                <RotateCcw className="w-4 h-4" />
                            </button>

                        </div>
                        <div className="flex items-center gap-2">
                            {/* Only show Run button for Python lessons */}
                            {!isSqlLesson && (
                                <button
                                    onClick={runCode}
                                    disabled={isRunning}
                                    className="px-4 py-1.5 bg-[var(--border-color)] rounded hover:bg-[rgba(255,255,255,0.1)] flex items-center gap-2 text-sm"
                                >
                                    <Play className="w-4 h-4" />
                                    Run
                                </button>
                            )}
                            <button
                                onClick={submitAnswer}
                                disabled={isRunning || isVerifying}
                                className="px-4 py-1.5 bg-[var(--accent-secondary)] text-white rounded hover:opacity-90 flex items-center gap-2 text-sm font-medium"
                            >
                                <Send className="w-4 h-4" />
                                {isVerifying ? "Checking..." : "Submit"}
                            </button>
                        </div>
                    </div>

                    {/* Resizable Divider */}
                    <div
                        className={`h-2 bg-[var(--border-color)] cursor-row-resize hover:bg-[var(--accent-secondary)] transition-colors flex items-center justify-center ${isDragging ? 'bg-[var(--accent-secondary)]' : ''}`}
                        onMouseDown={(e) => {
                            e.preventDefault();
                            setIsDragging(true);
                            const startY = e.clientY;
                            const startPercent = editorHeightPercent;
                            const panel = rightPanelRef.current;
                            if (!panel) return;

                            const handleMouseMove = (moveEvent: MouseEvent) => {
                                const panelRect = panel.getBoundingClientRect();
                                const panelHeight = panelRect.height - 56 - 48; // Subtract header and toolbar heights
                                const deltaY = moveEvent.clientY - startY;
                                const deltaPercent = (deltaY / panelHeight) * 100;
                                const newPercent = Math.min(85, Math.max(30, startPercent + deltaPercent));
                                setEditorHeightPercent(newPercent);
                            };

                            const handleMouseUp = () => {
                                setIsDragging(false);
                                document.removeEventListener('mousemove', handleMouseMove);
                                document.removeEventListener('mouseup', handleMouseUp);
                            };

                            document.addEventListener('mousemove', handleMouseMove);
                            document.addEventListener('mouseup', handleMouseUp);
                        }}
                    >
                        <div className="w-8 h-1 bg-[var(--text-secondary)] rounded opacity-50"></div>
                    </div>

                    {/* Terminal / Output */}
                    <div style={{ height: `${100 - editorHeightPercent - 10}%` }} className="bg-[#0a0a0c] flex flex-col min-h-0">
                        <div className="px-4 py-2 text-xs text-[var(--text-secondary)] border-b border-[var(--border-color)] flex items-center justify-between">
                            <span>Output</span>
                            {graphOutput && <span className="text-[var(--accent-success)]">📊 Graph rendered</span>}
                        </div>
                        <div className="flex-1 p-4 font-mono text-sm overflow-auto">
                            {graphOutput ? (
                                <div className="flex flex-col gap-2">
                                    <img src={graphOutput} alt="Plot output" className="max-w-full h-auto rounded" />
                                    {output && <pre className="text-[var(--accent-success)]">{output}</pre>}
                                </div>
                            ) : output ? (
                                <pre className={`whitespace-pre-wrap ${output.includes('Error') ? 'text-[var(--accent-error)]' : 'text-[var(--accent-success)]'}`}>{output}</pre>
                            ) : (
                                <span className="text-[var(--text-secondary)] opacity-50">▌ {isSqlLesson ? 'Click Submit to verify your query' : 'Click Run to execute your code'}</span>
                            )}
                        </div>
                    </div>

                    {/* Verification Result */}
                    {verifyResult && (
                        <div className={`p-4 border-t-2 ${verifyResult.correct ? 'border-[var(--accent-success)] bg-[rgba(74,222,128,0.1)]' : 'border-[var(--accent-error)] bg-[rgba(239,68,68,0.1)]'}`}>
                            <div className="flex items-start gap-3">
                                {verifyResult.correct ? (
                                    <CheckCircle className="w-6 h-6 text-[var(--accent-success)] shrink-0" />
                                ) : (
                                    <AlertCircle className="w-6 h-6 text-[var(--accent-error)] shrink-0" />
                                )}
                                <div className="flex-1">
                                    <p className={`font-medium ${verifyResult.correct ? 'text-[var(--accent-success)]' : 'text-[var(--accent-error)]'}`}>
                                        {verifyResult.correct ? "🎉 Correct!" : "Not quite right"}
                                    </p>
                                    <p className="text-sm text-[var(--text-secondary)] mt-1">{verifyResult.feedback}</p>
                                    {verifyResult.suggestions.length > 0 && (
                                        <ul className="mt-2 text-sm text-[var(--text-secondary)]">
                                            {verifyResult.suggestions.map((s, i) => (
                                                <li key={i} className="flex items-center gap-2">
                                                    <span>💡</span> {s}
                                                </li>
                                            ))}
                                        </ul>
                                    )}
                                </div>
                                {verifyResult.correct && (
                                    <button
                                        onClick={goToNext}
                                        className="px-4 py-2 bg-[var(--accent-success)] text-black rounded font-medium flex items-center gap-1"
                                    >
                                        Next <ChevronRight className="w-4 h-4" />
                                    </button>
                                )}
                                <button
                                    onClick={() => setVerifyResult(null)}
                                    className="p-1 hover:bg-[rgba(255,255,255,0.1)] rounded"
                                >
                                    <X className="w-4 h-4" />
                                </button>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};
