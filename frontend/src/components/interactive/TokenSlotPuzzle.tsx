import React, { useMemo, useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface TokenSlotOption {
    id: string;
    label?: string;
    options: string[];
    correct: string;
}

interface TokenSlotPuzzleProps {
    template: string;
    slots: TokenSlotOption[];
    onSolved?: () => void;
}

export const TokenSlotPuzzle: React.FC<TokenSlotPuzzleProps> = ({ template, slots, onSolved }) => {
    const { setVariable, recordDecision, recordConsequence } = useInteractive();
    const initialSelections = useMemo(() => {
        const selections: Record<string, string> = {};
        slots.forEach(slot => {
            selections[slot.id] = '';
        });
        return selections;
    }, [slots]);
    const [selections, setSelections] = useState<Record<string, string>>(initialSelections);
    const [isSolved, setIsSolved] = useState(false);

    const handleSelect = (slotId: string, option: string) => {
        setSelections(prev => ({ ...prev, [slotId]: option }));
        setVariable(slotId, option);
        recordDecision('token_slot', { slotId, option });
        recordConsequence('state', { slotId, option });
    };

    const allFilled = slots.every(slot => selections[slot.id]);
    const allCorrect = slots.every(slot => selections[slot.id] === slot.correct);

    if (allFilled && allCorrect && !isSolved) {
        setIsSolved(true);
        recordConsequence('puzzle_solved', { type: 'token_slot' });
        onSolved?.();
    }

    const renderedTemplate = template.split(/(\{\{.*?\}\})/g).map((chunk, idx) => {
        const match = chunk.match(/\{\{(.*?)\}\}/);
        if (!match) {
            return <span key={idx}>{chunk}</span>;
        }
        const slotId = match[1];
        const value = selections[slotId] || '____';
        const slotDef = slots.find(slot => slot.id === slotId);
        const isCorrect = slotDef ? selections[slotId] === slotDef.correct : false;
        return (
            <span
                key={idx}
                className={`inline-flex items-center px-2 py-0.5 mx-1 rounded border text-sm font-mono ${
                    selections[slotId]
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
        <div
            data-interaction-type="token_slot"
            data-component="TokenSlotPuzzle"
            className="my-4 p-4 bg-[var(--bg-panel)] rounded-lg border border-[var(--border-color)]"
        >
            <div className="text-sm font-medium text-[var(--accent-primary)] mb-3">
                Slot the right tokens
            </div>
            <div className="text-sm text-white leading-relaxed mb-4">{renderedTemplate}</div>
            <div className="space-y-3">
                {slots.map(slot => (
                    <div key={slot.id}>
                        <div className="text-xs text-[var(--text-secondary)] mb-1">
                            {slot.label || slot.id}
                        </div>
                        <div className="flex flex-wrap gap-2">
                            {slot.options.map(option => {
                                const isSelected = selections[slot.id] === option;
                                return (
                                    <button
                                        key={option}
                                        type="button"
                                        onClick={() => handleSelect(slot.id, option)}
                                        onKeyDown={(e) => {
                                            if (e.key === 'Enter' || e.key === ' ') {
                                                e.preventDefault();
                                                handleSelect(slot.id, option);
                                            }
                                        }}
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
                    {allCorrect ? '✅ Tokens placed correctly' : '❌ Adjust the wrong tokens'}
                </div>
            )}
        </div>
    );
};
