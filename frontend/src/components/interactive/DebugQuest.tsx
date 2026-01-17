import React, { useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface DebugOption {
    label: string;
    fix: string;
    correct: boolean;
}

interface DebugQuestProps {
    title?: string;
    snippet: string;
    bugLine: number;
    options: DebugOption[];
    solvedVar?: string;
}

export const DebugQuest: React.FC<DebugQuestProps> = ({
    title = 'Debug quest',
    snippet,
    bugLine,
    options,
    solvedVar = 'debug_solved'
}) => {
    const { setVariable, recordDecision, recordConsequence } = useInteractive();
    const [selected, setSelected] = useState<DebugOption | null>(null);
    const [isSolved, setIsSolved] = useState(false);
    const lines = snippet.split('\n');

    const handleSelect = (option: DebugOption) => {
        setSelected(option);
        recordDecision('debug_choice', { fix: option.fix });
        recordConsequence('state', { correct: option.correct });
        if (option.correct && !isSolved) {
            setIsSolved(true);
            setVariable(solvedVar, true);
        }
    };

    return (
        <div
            data-interaction-type="debug_quest"
            data-component="DebugQuest"
            className="my-4 p-4 bg-[var(--bg-panel)] rounded-lg border border-[var(--border-color)]"
        >
            <div className="text-sm font-medium text-[var(--accent-primary)] mb-3">{title}</div>
            <div className="bg-[#0d0d10] rounded border border-[var(--border-color)] p-3 font-mono text-sm mb-3">
                {lines.map((line, idx) => (
                    <div
                        key={idx}
                        className={`flex ${idx + 1 === bugLine ? 'bg-[rgba(var(--accent-error-rgb),0.2)] -mx-3 px-3' : ''}`}
                    >
                        <span className="w-6 text-[var(--text-secondary)] opacity-50 select-none">
                            {idx + 1}
                        </span>
                        <span className={idx + 1 === bugLine ? 'text-[var(--accent-error)]' : 'text-[var(--accent-success)]'}>
                            {line || ' '}
                        </span>
                    </div>
                ))}
            </div>
            <div className="space-y-2">
                {options.map(option => {
                    const isSelected = selected?.fix === option.fix;
                    const isCorrect = isSelected && option.correct;
                    return (
                        <button
                            key={option.fix}
                            onClick={() => handleSelect(option)}
                            className={`
                                w-full text-left px-3 py-2 rounded border transition-all text-sm font-mono
                                ${isSelected
                                    ? isCorrect
                                        ? 'bg-[rgba(74,222,128,0.2)] border-[var(--accent-success)]'
                                        : 'bg-[rgba(239,68,68,0.2)] border-[var(--accent-error)]'
                                    : 'bg-[#0d0d10] border-[var(--border-color)] hover:border-[var(--accent-primary)]'}
                            `}
                        >
                            {option.label}
                        </button>
                    );
                })}
            </div>
            {selected && (
                <div className={`mt-3 text-sm font-medium ${selected.correct ? 'text-[var(--accent-success)]' : 'text-[var(--accent-error)]'}`}>
                    {selected.correct ? '✅ Bug fixed' : '❌ That fix breaks the logic'}
                </div>
            )}
        </div>
    );
};
