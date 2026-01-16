import React, { useMemo, useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface BlankOption {
    id: string;
    options: string[];
    correct: string;
}

interface FillBlanksProps {
    template: string;
    blanks: BlankOption[];
    onSolved?: () => void;
}

export const FillBlanks: React.FC<FillBlanksProps> = ({ template, blanks, onSolved }) => {
    const { recordDecision, recordConsequence } = useInteractive();
    const initialSelections = useMemo(() => {
        const selections: Record<string, string> = {};
        blanks.forEach(blank => {
            selections[blank.id] = '';
        });
        return selections;
    }, [blanks]);
    const [selections, setSelections] = useState<Record<string, string>>(initialSelections);
    const [isSolved, setIsSolved] = useState(false);

    const allFilled = blanks.every(blank => selections[blank.id]);
    const allCorrect = blanks.every(blank => selections[blank.id] === blank.correct);

    const handleSelect = (id: string, option: string) => {
        setSelections(prev => ({ ...prev, [id]: option }));
        recordDecision('fill_blank', { id, option });
        recordConsequence('state', { id, option });
    };

    if (allFilled && allCorrect && !isSolved) {
        setIsSolved(true);
        onSolved?.();
        recordConsequence('puzzle_solved', { type: 'fill_blanks' });
    }

    const renderedTemplate = template.split(/(\{\{.*?\}\})/g).map((chunk, idx) => {
        const match = chunk.match(/\{\{(.*?)\}\}/);
        if (!match) {
            return <span key={idx}>{chunk}</span>;
        }
        const blankId = match[1];
        const value = selections[blankId] || '____';
        const blankDef = blanks.find(blank => blank.id === blankId);
        const isCorrect = blankDef ? selections[blankId] === blankDef.correct : false;
        return (
            <span
                key={idx}
                className={`inline-flex items-center px-2 py-0.5 mx-1 rounded border text-sm font-mono ${
                    selections[blankId]
                        ? isCorrect
                            ? 'border-[var(--accent-success)] text-[var(--accent-success)]'
                            : 'border-[var(--accent-error)] text-[var(--accent-error)]'
                        : 'border-[var(--border-color)] text-[var(--text-secondary)]'
                }`}
            >
                {value}
            </span>
        );
    });

    return (
        <div className="my-4 p-4 bg-[var(--bg-panel)] rounded-lg border border-[var(--border-color)]">
            <div className="text-sm font-medium text-[var(--accent-primary)] mb-3">
                Fill the blanks
            </div>
            <div className="text-sm text-white leading-relaxed mb-3">{renderedTemplate}</div>
            <div className="space-y-3">
                {blanks.map(blank => (
                    <div key={blank.id}>
                        <div className="text-xs text-[var(--text-secondary)] mb-1">
                            Choose for {blank.id}
                        </div>
                        <div className="flex flex-wrap gap-2">
                            {blank.options.map(option => {
                                const isSelected = selections[blank.id] === option;
                                return (
                                    <button
                                        key={option}
                                        type="button"
                                        onClick={() => handleSelect(blank.id, option)}
                                        className={`
                                            px-2 py-1 rounded text-sm font-mono border transition-all
                                            ${isSelected
                                                ? 'bg-[var(--accent-secondary)] text-black border-[var(--accent-secondary)]'
                                                : 'bg-[#0d0d10] text-[var(--text-primary)] border-[var(--border-color)] hover:border-[var(--accent-primary)]'}
                                        `}
                                    >
                                        {option}
                                    </button>
                                );
                            })}
                        </div>
                    </div>
                ))}
            </div>
            {allFilled && (
                <div className={`mt-3 text-sm font-medium ${allCorrect ? 'text-[var(--accent-success)]' : 'text-[var(--accent-error)]'}`}>
                    {allCorrect ? '✅ Blanks solved' : '❌ Not quite — adjust the wrong choices'}
                </div>
            )}
        </div>
    );
};
