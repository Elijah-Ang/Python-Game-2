import React, { useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface HintLadderProps {
    hints: [string, string, string]; // Exactly 3 tiers
    onHintUsed?: (level: number) => void;
}

export const HintLadder: React.FC<HintLadderProps> = ({ hints, onHintUsed }) => {
    const { recordEvent } = useInteractive();
    const [revealedLevel, setRevealedLevel] = useState(0); // 0 = none, 1-3 = hint level

    const handleReveal = () => {
        if (revealedLevel < 3) {
            const newLevel = revealedLevel + 1;
            setRevealedLevel(newLevel);
            onHintUsed?.(newLevel);
            recordEvent('hint_used', { level: newLevel });
        }
    };

    const hintLabels = ['💡 Nudge', '🔍 Guidance', '📖 Solution'];
    const hintColors = [
        'border-[var(--accent-warning)]',
        'border-[var(--accent-secondary)]',
        'border-[var(--accent-success)]'
    ];

    return (
        <div className="my-4">
            <div className="flex items-center gap-2 mb-2">
                <span className="text-sm text-[var(--text-secondary)]">Need help?</span>
                {revealedLevel < 3 && (
                    <button
                        onClick={handleReveal}
                        className="text-sm px-3 py-1 rounded bg-[var(--bg-panel)] border border-[var(--border-color)] hover:border-[var(--accent-warning)] transition-all"
                    >
                        {hintLabels[revealedLevel]}
                    </button>
                )}
                <div className="flex gap-1 ml-auto">
                    {[1, 2, 3].map(level => (
                        <div
                            key={level}
                            className={`w-2 h-2 rounded-full transition-all ${level <= revealedLevel
                                    ? 'bg-[var(--accent-warning)]'
                                    : 'bg-[var(--border-color)]'
                                }`}
                        />
                    ))}
                </div>
            </div>

            {revealedLevel > 0 && (
                <div className="space-y-2">
                    {hints.slice(0, revealedLevel).map((hint, idx) => (
                        <div
                            key={idx}
                            className={`p-3 rounded bg-[#1a1a2e] border-l-2 ${hintColors[idx]} text-sm`}
                        >
                            <span className="text-[var(--text-secondary)]">{hintLabels[idx]}:</span>{' '}
                            <span className="text-white">{hint}</span>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};
