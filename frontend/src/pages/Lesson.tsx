import React, { useEffect, useState, useCallback, useRef } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import Editor from '@monaco-editor/react';
import { Play, Send, ChevronRight, FileCode, RotateCcw, Eye, EyeOff, Lightbulb, X, CheckCircle, AlertCircle } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';
import { InteractiveProvider, useInteractive } from '../context/InteractiveContext';
import { VariableSlider } from '../components/interactive/VariableSlider';
import { VisualMemoryBox } from '../components/interactive/VisualMemoryBox';
import { DraggableValueBox, ValueChip } from '../components/interactive/DraggableValueBox';
import { LiveCodeBlock } from '../components/interactive/LiveCodeBlock';
import { VisualTable } from '../components/interactive/VisualTable';
import { ParsonsPuzzle } from '../components/interactive/ParsonsPuzzle';
import { PredictionCheck } from '../components/interactive/PredictionCheck';
import { HintLadder } from '../components/interactive/HintLadder';
import { StateInspector } from '../components/interactive/StateInspector';
import { ResetStateButton } from '../components/interactive/ResetStateButton';
import { OutputDiff } from '../components/interactive/OutputDiff';
import { StepExecutor } from '../components/interactive/StepExecutor';
import { InteractionPlanRenderer } from '../components/interactive/InteractionPlanRenderer';
import { FillBlanks } from '../components/interactive/FillBlanks';
import confetti from 'canvas-confetti';
import { verifyCode, verifySql, verifyR } from '../utils/verifier';
import type { LessonInteractionPlan } from '../types/interaction';

interface LessonData {
    id: number;
    title: string;
    content: string;
    starter_code: string;
    solution_code: string;
    expected_output: string;
    chapter_id: number;
    concept_tags?: string[];
    interaction_plan?: LessonInteractionPlan;
    interaction_required?: boolean;
    expected_result?: string;
    send_to_editor_template?: string;
    interaction_confidence?: number;
    manual_review?: boolean;
}

interface VerifyResult {
    correct: boolean;
    feedback: string;
    suggestions: string[];
}

interface PyodideInterface {
    loadPackage: (packages: string | string[]) => Promise<void>;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    pyimport: (pkg: string) => any;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    runPythonAsync: (code: string) => Promise<any>;
    setStdout: (options: { batched: (msg: string) => void }) => void;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    globals: any;
}

interface WebRInterface {
    init: () => Promise<void>;
    installPackages: (packages: string[]) => Promise<void>;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    evalR: (code: string) => Promise<any>;
    FS: {
        readFile: (path: string) => Promise<Uint8Array>;
    };
}

const runWithTimeout = async <T,>(promise: Promise<T>, timeoutMs: number, timeoutMessage: string) => {
    let timeoutHandle: number | undefined;
    const timeoutPromise = new Promise<never>((_, reject) => {
        timeoutHandle = window.setTimeout(() => {
            reject(new Error(timeoutMessage));
        }, timeoutMs);
    });

    try {
        return await Promise.race([promise, timeoutPromise]);
    } finally {
        if (timeoutHandle) {
            window.clearTimeout(timeoutHandle);
        }
    }
};

declare global {
    interface Window {
        loadPyodide: () => Promise<PyodideInterface>;
    }
}

const LessonContent: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const navigate = useNavigate();
    const [lesson, setLesson] = useState<LessonData | null>(null);
    const [code, setCode] = useState("");
    const [output, setOutput] = useState("");
    const [error, setError] = useState<string | null>(null);
    const [graphOutput, setGraphOutput] = useState<string | null>(null);
    const [isRunning, setIsRunning] = useState(false);
    const [isVerifying, setIsVerifying] = useState(false);
    const [pyodide, setPyodide] = useState<PyodideInterface | null>(null);
    const [showSolution, setShowSolution] = useState(false);
    const [verifyResult, setVerifyResult] = useState<VerifyResult | null>(null);
    const [editorHeightPercent, setEditorHeightPercent] = useState(65);
    const [isDragging, setIsDragging] = useState(false);
    const [lessonOrder, setLessonOrder] = useState<number | null>(null);
    const [orderedLessonIds, setOrderedLessonIds] = useState<number[]>([]);
    const [webR, setWebR] = useState<WebRInterface | null>(null);
    const rightPanelRef = useRef<HTMLDivElement>(null);
    const [mobileTab, setMobileTab] = useState<'lesson' | 'code'>('lesson');
    const { decisionCount, consequenceCount, recordEvent, recordDecision, recordConsequence } = useInteractive();
    const lessonStartRef = useRef(Date.now());
    const [completionLogged, setCompletionLogged] = useState(false);

    // Load Lesson Data from static JSON
    useEffect(() => {
        const loadLessonData = async () => {
            try {
                // Fetch lesson content
                const lessonsRes = await fetch(`${import.meta.env.BASE_URL}data/lessons.json?t=${Date.now()}`);
                const lessonsData = await lessonsRes.json();
                const lessonData = lessonsData[id as string];

                if (lessonData) {
                    setLesson(lessonData);
                    // SQL lessons have IDs >= 1001 && < 2000
                    // R lessons have IDs >= 2000
                    const currentId = Number(id);
                    const isSql = currentId >= 1001 && currentId < 2000;
                    const isR = currentId >= 2000;

                    if (isSql) {
                        setCode("-- Write your SQL here\n\n");
                    } else if (isR) {
                        setCode("# Write your R code here\n\n");
                    } else {
                        setCode("# Write your code here\n\n");
                    }

                    setShowSolution(false);
                    setVerifyResult(null);
                    setOutput("");
                    setGraphOutput(null);

                    // Fetch course data to get the lesson order
                    let courseFile = `${import.meta.env.BASE_URL}data/course-python-basics.json`;
                    if (isSql) courseFile = `${import.meta.env.BASE_URL}data/course-sql-fundamentals.json`;
                    if (isR) courseFile = `${import.meta.env.BASE_URL}data/course-r-fundamentals.json`;
                    const courseRes = await fetch(`${courseFile}?t=${Date.now()}`);
                    const courseData = await courseRes.json();

                    // Build ordered list of lesson IDs from course structure
                    const orderedIds: number[] = [];
                    let currentOrder = 0;
                    let foundOrder: number | null = null;

                    for (const chapter of courseData.chapters) {
                        // Handle both concepts structure and flat lessons structure
                        // eslint-disable-next-line @typescript-eslint/no-explicit-any
                        let chapterLessons: any[] = [];
                        if (chapter.concepts) {
                            // New structure: extract lessons from concepts
                            for (const concept of chapter.concepts) {
                                chapterLessons = chapterLessons.concat(concept.lessons);
                            }
                        } else if (chapter.lessons) {
                            // Old structure: direct lessons array
                            chapterLessons = chapter.lessons;
                        }

                        // Note: R course uses local order per concept, Python uses global order.
                        // Don't sort here - use natural JSON order which already respects structure.
                        for (const lesson of chapterLessons) {
                            orderedIds.push(lesson.id);
                            currentOrder++;
                            if (lesson.id === Number(id)) {
                                foundOrder = currentOrder;
                            }
                        }
                    }

                    setOrderedLessonIds(orderedIds);
                    setLessonOrder(foundOrder);
                }
            } catch (err: unknown) {
                const msg = err instanceof Error ? err.message : String(err);
                console.error(err);
                setError(msg || "Failed to load lesson. Please try refreshing.");
            }
        };
        loadLessonData();
    }, [id]);

    useEffect(() => {
        lessonStartRef.current = Date.now();
        setCompletionLogged(false);
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

    // Load WebR for R lessons
    useEffect(() => {
        const initWebR = async () => {
            const currentId = Number(id);
            if (currentId >= 2000 && !webR) {
                try {
                    setOutput("⏳ Setting up R environment (downloading packages)...");
                    // Dynamic import from CDN
                    // @ts-expect-error WebR is loaded from CDN
                    const { WebR } = await import('https://webr.r-wasm.org/latest/webr.mjs');
                    const w = new WebR();
                    await w.init();

                    // Install and load common packages
                    console.log("Installing R packages...");
                    await w.installPackages(['ggplot2', 'dplyr', 'palmerpenguins']);
                    await w.evalR('library(ggplot2); library(dplyr); library(palmerpenguins); data(penguins)');

                    setWebR(w);
                    console.log("WebR Ready");
                    setOutput(""); // Clear "Setting up" message
                } catch (e: unknown) {
                    const msg = e instanceof Error ? e.message : String(e);
                    console.error("WebR init error:", e);
                    setOutput("⚠️ Error loading R environment: " + msg);
                }
            }
        };
        initWebR();
    }, [id, webR]);

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
        recordDecision('run_code', { language: 'python' });

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
            await runWithTimeout(pyodide.runPythonAsync(code), 5000, "Python execution timed out after 5 seconds.");

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
            recordConsequence('output', { language: 'python', status: 'success' });
        } catch (err: unknown) {
            resultOutput = "❌ Error:\n" + String(err);
            setOutput(resultOutput);
            recordConsequence('output', { language: 'python', status: 'error' });
        } finally {
            setIsRunning(false);
        }
        return resultOutput;
    };

    const runRCode = async (): Promise<string> => {
        if (!webR) {
            const msg = "⏳ Loading R engine...";
            setOutput(msg);
            return msg;
        }
        setIsRunning(true);
        setOutput("");
        setGraphOutput(null);
        recordDecision('run_code', { language: 'r' });

        let resultOutput = "";
        try {
            // Setup canvas for plot capture (WebR has built-in canvas support, but we need to hook it)
            // For now, capturing stdout

            // Capture output
            let outputBuffer = "";

            // Run code
            // We use options to capture stdout
            // const shelf = await webR.evalR(code); // Unused, shelf causes build error

            // Try to capture basic print output
            // WebR console output capture involves hooking the console or using capture.output
            // Simpler approach: Wrap user code in capture.output and return it

            try {
                // 1. Start PNG device
                await webR.evalR(`png("output.png", width=500, height=400, res=72)`);

                // 2. Run user code (capturing stdout)
                const captureCode = `paste(capture.output({
${code}
}), collapse="\\n")`;
                const outputResult = await runWithTimeout(webR.evalR(captureCode), 5000, "R execution timed out after 5 seconds.");
                outputBuffer = await outputResult.toString();

                // 3. Close device
                await webR.evalR("dev.off()");

            } catch (innerErr: unknown) {
                // Determine if error is from the code or the plotting
                const msg = innerErr instanceof Error ? innerErr.message : String(innerErr);
                outputBuffer = "Error: " + msg;
                // Try to close device just in case
                // Try to close device just in case
                try { await webR.evalR("dev.off()"); } catch { /* ignore */ }
            }

            // 4. Check for generated plot file
            try {
                const plotData = await webR.FS.readFile("output.png");
                if (plotData && plotData.length > 0) {
                    // Convert Uint8Array to base64
                    // eslint-disable-next-line @typescript-eslint/no-explicit-any
                    const blob = new Blob([plotData as any], { type: 'image/png' });
                    const reader = new FileReader();
                    reader.onloadend = () => {
                        // reader.result is "data:image/png;base64,..."
                        setGraphOutput(reader.result as string);
                    };
                    reader.readAsDataURL(blob);
                }
            } catch {
                // No plot generated (file not found), which is fine
            }

            // Clean up: Remove quotes "...", unescape newlines
            // Also strip common R output indices like [1] but keep relevant data

            // Handle plots? (Advanced WebR setup needed for canvas, for now text output)

            // Clean up: Remove quotes "...", unescape newlines
            // Also strip common R output indices like [1] but keep relevant data
            resultOutput = outputBuffer
                .replace(/^"|"$/g, '')
                .replace(/\\n/g, '\n')
                .replace(/^\[\d+\]\s+/gm, ''); // Remove [1] line prefixes

            if (!resultOutput.trim()) {
                resultOutput = "✓ Code executed successfully (no output)";
            }

            setOutput(resultOutput);
            recordConsequence('output', { language: 'r', status: resultOutput.startsWith('❌') ? 'error' : 'success' });
        } catch (err: unknown) {
            const msg = err instanceof Error ? err.message : String(err);
            resultOutput = "❌ Error:\n" + msg;
            setOutput(resultOutput);
            recordConsequence('output', { language: 'r', status: 'error' });
        } finally {
            setIsRunning(false);
        }
        return resultOutput;
    };

    const submitAnswer = async () => {
        const currentId = Number(id) || 1;
        const isSql = currentId >= 1001 && currentId < 2000;

        setIsVerifying(true);
        recordDecision('submit', { lessonId: currentId });

        let result;
        if (isSql) {
            // For SQL, compare user code against solution code
            result = verifySql(
                lesson?.solution_code || '',
                code
            );
        } else if (currentId >= 2000) {
            // For R, run code and compare output
            const executionOutput = await runRCode();
            result = verifyR(
                lesson?.expected_output || '',
                executionOutput,
                code,
                !!graphOutput
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
        recordConsequence('verification', { correct: result.correct });

        if (result.correct) {
            triggerConfetti();
            if (!completionLogged) {
                const elapsedMs = Date.now() - lessonStartRef.current;
                recordEvent('time_to_complete', {
                    lessonId: lesson?.id,
                    ms: elapsedMs,
                    seconds: Math.round(elapsedMs / 1000)
                });
                setCompletionLogged(true);
            }
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
        recordEvent('reset_count', { source: 'editor' });
    };

    const goToNext = () => {
        const currentId = Number(id);
        const isSql = currentId >= 1001 && currentId < 2000;
        const isR = currentId >= 2000;
        const slug = isR ? 'r-fundamentals' : (isSql ? 'sql-fundamentals' : 'python-basics');

        if (orderedLessonIds.length > 0) {
            const currentIndex = orderedLessonIds.indexOf(currentId);
            if (currentIndex !== -1 && currentIndex < orderedLessonIds.length - 1) {
                navigate(`/lesson/${orderedLessonIds[currentIndex + 1]}`);
            } else {
                // End of course
                navigate(`/course/${slug}`);
            }
        } else {
            // Fallback
            const nextId = currentId + 1;
            navigate(`/lesson/${nextId}`);
        }
    };

    const goToPrev = () => {
        const currentId = Number(id);
        const isSql = currentId >= 1001 && currentId < 2000;
        const isR = currentId >= 2000;
        const slug = isR ? 'r-fundamentals' : (isSql ? 'sql-fundamentals' : 'python-basics');

        if (orderedLessonIds.length > 0) {
            const currentIndex = orderedLessonIds.indexOf(currentId);
            if (currentIndex > 0) {
                navigate(`/lesson/${orderedLessonIds[currentIndex - 1]}`);
            } else {
                // Beginning of course
                navigate(`/course/${slug}`);
            }
        } else {
            // Fallback
            const prevId = currentId - 1;
            if (prevId > 0) {
                navigate(`/lesson/${prevId}`);
            }
        }
    };

    const handlePrimeCode = useCallback((snippet: string) => {
        setCode(snippet);
        setOutput("");
        setGraphOutput(null);
        setVerifyResult(null);
        setShowSolution(false);
        setMobileTab('code');
    }, [setCode, setGraphOutput, setMobileTab, setOutput, setShowSolution, setVerifyResult]);

    if (error) {
        return (
            <div className="h-screen bg-[var(--bg-color)] flex flex-col items-center justify-center p-4">
                <div className="text-[var(--accent-error)] mb-4 text-xl">⚠️ Error Loading Lesson</div>
                <div className="text-[var(--text-secondary)] mb-4 bg-[var(--bg-panel)] p-4 rounded font-mono text-sm border border-[var(--border-color)]">
                    {error}
                </div>
                <button
                    onClick={() => window.location.reload()}
                    className="px-4 py-2 bg-[var(--accent-primary)] text-white rounded hover:opacity-90 transition-colors"
                >
                    Retry Connection
                </button>
            </div>
        );
    }

    if (!lesson) {
        return (
            <div className="h-screen bg-[var(--bg-color)] flex items-center justify-center">
                <div className="animate-pulse text-[var(--text-secondary)]">Loading exercise...</div>
            </div>
        );
    }

    const currentExercise = Number(id) || 1;
    const isSqlLesson = currentExercise >= 1001 && currentExercise < 2000;
    const isRLesson = currentExercise >= 2000;
    const totalExercises = isRLesson ? 200 : (isSqlLesson ? 161 : 113); // TODO: Update R total

    // Determine display order
    let displayExercise = currentExercise;
    if (lessonOrder !== null) {
        displayExercise = lessonOrder;
    } else {
        if (isRLesson) displayExercise = currentExercise - 2000;
        else if (isSqlLesson) displayExercise = currentExercise - 1000;
    }

    const courseSlug = isRLesson ? 'r-fundamentals' : (isSqlLesson ? 'sql-fundamentals' : 'python-basics');
    const editorLanguage = isRLesson ? 'r' : (isSqlLesson ? 'sql' : 'python');
    const scriptFilename = isRLesson ? 'script.R' : (isSqlLesson ? 'query.sql' : 'script.py');
    const interactionRequired = lesson.interaction_required ?? true;
    const interactionLocked = interactionRequired && (decisionCount < 1 || consequenceCount < 1);
    const interactionPlan: LessonInteractionPlan = lesson.interaction_plan ? [...lesson.interaction_plan] : [];

    if (lesson.send_to_editor_template && !interactionPlan.some(item => item.type === 'send_to_editor')) {
        interactionPlan.push({
            type: 'send_to_editor',
            template: lesson.send_to_editor_template,
            templateId: 'lesson_template'
        });
    }

    return (
        <div className="h-screen flex flex-col bg-[var(--bg-color)] overflow-hidden">
                {/* Top Navigation Bar */}
                <div className="h-12 bg-[var(--bg-panel)] border-b border-[var(--border-color)] flex items-center px-3 md:px-4 gap-2 md:gap-4 shrink-0">
                    <Link to="/" className="flex items-center gap-2 hover:opacity-80">
                        <span className="text-lg">📊</span>
                        <span className="font-bold text-[var(--accent-primary)] pixel-font hidden sm:inline">DS Adventure</span>
                    </Link>

                    <span className="text-[var(--border-color)] hidden sm:inline">|</span>

                    <div className="flex items-center gap-2">
                        <span className="text-sm font-medium truncate max-w-[150px] md:max-w-none">{lesson.title}</span>
                    </div>

                    {/* Progress Bar - Hide on very small screens */}
                    <div className="flex-1 max-w-xs mx-2 md:mx-4 hidden sm:block">
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

                {/* Mobile Tab Bar - Only visible on small screens */}
                <div className="md:hidden flex border-b border-[var(--border-color)] bg-[var(--bg-panel)]">
                    <button
                        onClick={() => setMobileTab('lesson')}
                        className={`flex-1 py-3 text-sm font-medium text-center transition-colors ${mobileTab === 'lesson'
                            ? 'text-[var(--accent-primary)] border-b-2 border-[var(--accent-primary)] bg-[var(--bg-color)]'
                            : 'text-[var(--text-secondary)] hover:text-white'
                            }`}
                    >
                        📖 Lesson
                    </button>
                    <button
                        onClick={() => setMobileTab('code')}
                        className={`flex-1 py-3 text-sm font-medium text-center transition-colors ${mobileTab === 'code'
                            ? 'text-[var(--accent-warning)] border-b-2 border-[var(--accent-warning)] bg-[var(--bg-color)]'
                            : 'text-[var(--text-secondary)] hover:text-white'
                            }`}
                    >
                        💻 Code
                    </button>
                </div>

                {/* Main Content Area */}
                <div className="flex-1 flex flex-col md:flex-row overflow-hidden min-h-0">
                    {/* Left Panel: Instructions - Hidden on mobile when code tab active */}
                    <div className={`${mobileTab === 'lesson' ? 'flex' : 'hidden'
                        } md:flex w-full md:w-1/2 flex-col border-r border-[var(--border-color)] min-h-0`}>
                        <div className="flex-1 overflow-y-auto p-4 md:p-6 min-h-0">
                            {/* Exercise Number */}
                            <h1 className={`text-2xl font-bold mb-4 pixel-font ${lesson.id > 9999 ? 'pl-8 border-l-4 border-[var(--accent-secondary)]' : ''}`}>
                                {lesson.id > 9999 && <span className="text-sm font-normal text-[var(--accent-secondary)] block mb-1">REINFORCER</span>}
                                {String(displayExercise).padStart(2, '0')}. {lesson.title}
                            </h1>

                            {/* Lesson Content */}
                            <div className="prose prose-invert prose-sm max-w-none lesson-content">
                                <ReactMarkdown
                                    remarkPlugins={[remarkGfm]}
                                    rehypePlugins={[rehypeRaw]}
                                    components={{
                                        // @ts-ignore
                                        variableslider: VariableSlider,
                                        // @ts-ignore
                                        visualmemorybox: VisualMemoryBox,
                                        // @ts-ignore
                                        draggablevaluebox: DraggableValueBox,
                                        // @ts-ignore
                                        valuechip: ValueChip,
                                        // @ts-ignore
                                        livecodeblock: LiveCodeBlock,
                                        // @ts-ignore
                                        visualtable: VisualTable,
                                        // @ts-ignore
                                        parsonspuzzle: ParsonsPuzzle,
                                        // @ts-ignore
                                        predictioncheck: PredictionCheck,
                                        // @ts-ignore
                                        hintladder: HintLadder,
                                        // @ts-ignore
                                        stateinspector: StateInspector,
                                        // @ts-ignore
                                        resetstatebutton: ResetStateButton,
                                        // @ts-ignore
                                        outputdiff: OutputDiff,
                                        // @ts-ignore
                                        stepexecutor: StepExecutor,
                                        // @ts-ignore
                                        fillblanks: FillBlanks,
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
                                        thead: ({ children }) => <thead>{children}</thead>,
                                        tbody: ({ children }) => <tbody>{children}</tbody>,
                                        tr: ({ children }) => <tr>{children}</tr>,
                                        th: ({ children }) => <th className="border border-[var(--border-color)] px-2 py-1 bg-[var(--bg-panel)] text-left">{children}</th>,
                                        td: ({ children }) => <td className="border border-[var(--border-color)] px-2 py-1">{children}</td>,
                                    }}
                                >
                                    {lesson.content}
                                </ReactMarkdown>
                            </div>

                            {interactionPlan.length > 0 && (
                                <InteractionPlanRenderer
                                    plan={interactionPlan}
                                    onSendToEditor={handlePrimeCode}
                                    expectedOutput={lesson.expected_output}
                                />
                            )}

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

                        {/* Instructions Footer - Simplified on mobile */}
                        <div className="border-t border-[var(--border-color)] bg-[var(--bg-panel)] p-2 md:p-3">
                            <div className="flex items-center justify-between">
                                {/* Hide title section on mobile */}
                                <div className="hidden md:flex items-center gap-3">
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
                                {/* Mobile: Show exercise count inline */}
                                <span className="md:hidden text-xs text-[var(--text-secondary)]">
                                    {displayExercise} / {totalExercises}
                                </span>
                                <div className="flex items-center gap-2">
                                    <button
                                        onClick={goToPrev}
                                        disabled={currentExercise <= 1}
                                        className="px-3 md:px-4 py-1.5 md:py-2 bg-[var(--border-color)] rounded hover:bg-[rgba(255,255,255,0.1)] disabled:opacity-40 transition-colors text-sm"
                                    >
                                        Back
                                    </button>
                                    <button
                                        onClick={goToNext}
                                        className="px-3 md:px-4 py-1.5 md:py-2 bg-[var(--border-color)] rounded hover:bg-[rgba(255,255,255,0.1)] transition-colors text-sm"
                                    >
                                        Next
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Right Panel: Code Editor + Terminal - Hidden on mobile when lesson tab active */}
                    <div ref={rightPanelRef} className={`${mobileTab === 'code' ? 'flex' : 'hidden'
                        } md:flex w-full md:w-1/2 flex-col min-h-0`}>
                        {/* Editor Header - Rebuild Trigger */}
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
                                {/* Allow Run for Python and R (even if R uses simulation/verification for now) */}
                                {!isSqlLesson && (
                                    <button
                                        onClick={isRLesson ? runRCode : runCode}
                                        disabled={isRunning}
                                        className="px-4 py-1.5 bg-[var(--border-color)] rounded hover:bg-[rgba(255,255,255,0.1)] flex items-center gap-2 text-sm"
                                    >
                                        <Play className="w-4 h-4" />
                                        Run
                                    </button>
                                )}
                                <button
                                    onClick={submitAnswer}
                                    disabled={isRunning || isVerifying || interactionLocked}
                                    className="px-4 py-1.5 bg-[var(--accent-secondary)] text-white rounded hover:opacity-90 flex items-center gap-2 text-sm font-medium"
                                    title={interactionLocked ? 'Complete an interactive step to unlock submission' : 'Submit your answer'}
                                >
                                    <Send className="w-4 h-4" />
                                    {interactionLocked ? "Interact to Unlock" : (isVerifying ? "Checking..." : "Submit")}
                                </button>
                            </div>
                            {interactionLocked && (
                                <span className="text-xs text-[var(--accent-warning)]">
                                    Complete 1 interaction to unlock
                                </span>
                            )}
                        </div>

                        {/* Resizable Divider - Supports both mouse and touch */}
                        <div
                            className={`h-3 md:h-2 bg-[var(--border-color)] cursor-row-resize hover:bg-[var(--accent-secondary)] active:bg-[var(--accent-secondary)] transition-colors flex items-center justify-center ${isDragging ? 'bg-[var(--accent-secondary)]' : ''}`}
                            onMouseDown={(e) => {
                                e.preventDefault();
                                setIsDragging(true);
                                const startY = e.clientY;
                                const startPercent = editorHeightPercent;
                                const panel = rightPanelRef.current;
                                if (!panel) return;

                                const handleMouseMove = (moveEvent: MouseEvent) => {
                                    const panelRect = panel.getBoundingClientRect();
                                    const panelHeight = panelRect.height - 56 - 48;
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
                            onTouchStart={(e) => {
                                const touch = e.touches[0];
                                const startY = touch.clientY;
                                const startPercent = editorHeightPercent;
                                const panel = rightPanelRef.current;
                                if (!panel) return;

                                const handleTouchMove = (moveEvent: TouchEvent) => {
                                    const touch = moveEvent.touches[0];
                                    const panelRect = panel.getBoundingClientRect();
                                    const panelHeight = panelRect.height - 56 - 48;
                                    const deltaY = touch.clientY - startY;
                                    const deltaPercent = (deltaY / panelHeight) * 100;
                                    const newPercent = Math.min(85, Math.max(30, startPercent + deltaPercent));
                                    setEditorHeightPercent(newPercent);
                                };

                                const handleTouchEnd = () => {
                                    document.removeEventListener('touchmove', handleTouchMove);
                                    document.removeEventListener('touchend', handleTouchEnd);
                                };

                                document.addEventListener('touchmove', handleTouchMove, { passive: true });
                                document.addEventListener('touchend', handleTouchEnd);
                            }}
                            onDoubleClick={() => {
                                // Tap to cycle through presets: 50% -> 70% -> 40% -> 50%
                                if (editorHeightPercent < 45) setEditorHeightPercent(50);
                                else if (editorHeightPercent < 60) setEditorHeightPercent(70);
                                else setEditorHeightPercent(40);
                            }}
                        >
                            <div className="w-12 h-1 bg-[var(--text-secondary)] rounded opacity-50"></div>
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
                                        title="Dismiss"
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

export const Lesson: React.FC = () => {
    const { id } = useParams<{ id: string }>();

    return (
        <InteractiveProvider key={id}>
            <LessonContent />
        </InteractiveProvider>
    );
};
