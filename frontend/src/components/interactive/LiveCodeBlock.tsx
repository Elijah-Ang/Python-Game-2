import React, { useState, useEffect, useCallback } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface LiveCodeBlockProps {
    initialCode: string;
    language: 'python' | 'sql' | 'r';
    variableName?: string; // If set, stores result in context
    highlightLine?: number; // Line to highlight for editing
}

export const LiveCodeBlock: React.FC<LiveCodeBlockProps> = ({
    initialCode,
    language,
    variableName,
    highlightLine
}) => {
    const { setVariable } = useInteractive();
    const [code, setCode] = useState(initialCode);
    const [output, setOutput] = useState<string>('');
    const [isRunning, setIsRunning] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const runCode = useCallback(async () => {
        if (language !== 'python') {
            setOutput('(Live execution only available for Python)');
            return;
        }

        setIsRunning(true);
        setError(null);

        try {
            // @ts-ignore - Pyodide is loaded globally
            if (window.pyodide) {
                let outputBuffer = '';
                // @ts-ignore
                window.pyodide.setStdout({
                    batched: (msg: string) => { outputBuffer += msg + '\n'; }
                });

                // @ts-ignore
                await window.pyodide.runPythonAsync(code);

                const result = outputBuffer.trim() || '(no output)';
                setOutput(result);

                if (variableName) {
                    setVariable(variableName, result);
                }
            } else {
                setOutput('⏳ Python engine loading...');
            }
        } catch (err) {
            const msg = err instanceof Error ? err.message : String(err);
            setError(msg);
            setOutput('');
        } finally {
            setIsRunning(false);
        }
    }, [code, language, variableName, setVariable]);

    // Auto-run on code change (debounced)
    useEffect(() => {
        const timer = setTimeout(() => {
            runCode();
        }, 500);
        return () => clearTimeout(timer);
    }, [code, runCode]);

    const lines = code.split('\n');

    return (
        <div className="my-4 rounded-lg overflow-hidden border border-[var(--border-color)]">
            {/* Code editor */}
            <div className="bg-[#0d0d10] p-3">
                <div className="font-mono text-sm">
                    {lines.map((line, idx) => (
                        <div
                            key={idx}
                            className={`flex ${highlightLine === idx + 1 ? 'bg-[rgba(var(--accent-warning-rgb),0.2)] -mx-3 px-3' : ''}`}
                        >
                            <span className="w-6 text-[var(--text-secondary)] opacity-50 select-none">
                                {idx + 1}
                            </span>
                            {highlightLine === idx + 1 ? (
                                <input
                                    type="text"
                                    value={line}
                                    onChange={(e) => {
                                        const newLines = [...lines];
                                        newLines[idx] = e.target.value;
                                        setCode(newLines.join('\n'));
                                    }}
                                    className="flex-1 bg-transparent text-[var(--accent-success)] outline-none border-b border-[var(--accent-warning)]"
                                />
                            ) : (
                                <span className="text-[var(--accent-success)]">{line}</span>
                            )}
                        </div>
                    ))}
                </div>
            </div>

            {/* Output */}
            <div className="bg-[#0a0a0c] border-t border-[var(--border-color)] p-3">
                <div className="text-xs text-[var(--text-secondary)] mb-1 flex items-center gap-2">
                    Output
                    {isRunning && <span className="animate-pulse">⏳</span>}
                </div>
                <pre className={`font-mono text-sm ${error ? 'text-[var(--accent-error)]' : 'text-[var(--accent-success)]'}`}>
                    {error || output || '(waiting...)'}
                </pre>
            </div>
        </div>
    );
};
