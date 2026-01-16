import React, { useState, useEffect, useCallback } from 'react';
import { useInteractive } from '../../context/InteractiveContext';
import { Play } from 'lucide-react';

interface LiveCodeBlockProps {
    initialcode?: string;  // lowercase for HTML attribute compatibility
    language?: string;
    variablename?: string;
    highlightline?: string | number;
}

export const LiveCodeBlock: React.FC<LiveCodeBlockProps> = ({
    initialcode = '# Write code here',
    language = 'python',
    variablename,
    highlightline
}) => {
    const { setVariable, recordDecision, recordConsequence } = useInteractive();
    const [code, setCode] = useState(initialcode || '# Write code here');
    const [output, setOutput] = useState<string>('');
    const [isRunning, setIsRunning] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [hasRun, setHasRun] = useState(false);

    const highlightNum = typeof highlightline === 'string' ? parseInt(highlightline, 10) : highlightline;

    const runCode = useCallback(async () => {
        const lang = (language || 'python').toLowerCase();

        if (lang === 'sql') {
            setOutput('📊 SQL preview mode - submit in the code editor below');
            setHasRun(true);
            return;
        }

        if (lang === 'r') {
            setOutput('📈 R preview mode - submit in the code editor below');
            setHasRun(true);
            return;
        }

        if (lang !== 'python') {
            setOutput(`(${lang} not supported for live execution)`);
            setHasRun(true);
            return;
        }

        setIsRunning(true);
        setError(null);
        recordDecision('run_preview', { language: lang });

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
                recordConsequence('output', { type: 'preview', language: lang });

                if (variablename) {
                    setVariable(variablename, result);
                }
            } else {
                setOutput('⏳ Python engine loading...');
            }
        } catch (err) {
            const msg = err instanceof Error ? err.message : String(err);
            setError(msg);
            setOutput('');
            recordConsequence('output', { type: 'preview', status: 'error' });
        } finally {
            setIsRunning(false);
            setHasRun(true);
        }
    }, [code, language, variablename, setVariable]);

    // Reset code when initialcode changes (new lesson)
    useEffect(() => {
        setCode(initialcode || '# Write code here');
        setOutput('');
        setError(null);
        setHasRun(false);
    }, [initialcode]);

    const lines = (code || '').split('\n');

    return (
        <div className="my-4 rounded-lg overflow-hidden border border-[var(--border-color)]">
            {/* Code editor */}
            <div className="bg-[#0d0d10] p-3">
                <div className="font-mono text-sm">
                    {lines.map((line, idx) => (
                        <div
                            key={idx}
                            className={`flex ${highlightNum === idx + 1 ? 'bg-[rgba(var(--accent-warning-rgb),0.2)] -mx-3 px-3' : ''}`}
                        >
                            <span className="w-6 text-[var(--text-secondary)] opacity-50 select-none">
                                {idx + 1}
                            </span>
                            {highlightNum === idx + 1 ? (
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
                                <span className="text-[var(--accent-success)]">{line || ' '}</span>
                            )}
                        </div>
                    ))}
                </div>
            </div>

            {/* Run button + Output */}
            <div className="bg-[#0a0a0c] border-t border-[var(--border-color)] p-3">
                <div className="flex items-center gap-2 mb-2">
                    <button
                        onClick={runCode}
                        disabled={isRunning}
                        className="px-3 py-1 text-sm rounded bg-[var(--accent-secondary)] text-black font-medium flex items-center gap-1 hover:opacity-90 disabled:opacity-50"
                    >
                        <Play className="w-3 h-3" />
                        {isRunning ? 'Running...' : 'Run'}
                    </button>
                    <span className="text-xs text-[var(--text-secondary)]">
                        {hasRun ? 'Output:' : 'Click Run to execute'}
                    </span>
                </div>
                {hasRun && (
                    <pre className={`font-mono text-sm ${error ? 'text-[var(--accent-error)]' : 'text-[var(--accent-success)]'}`}>
                        {error || output || '(no output)'}
                    </pre>
                )}
            </div>
        </div>
    );
};
