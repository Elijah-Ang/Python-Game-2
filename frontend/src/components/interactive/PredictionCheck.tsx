import React, { useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface PredictionCheckProps {
    question: string;
    options: string[];
    correctIndex: number;
    explanation?: string;
    onCorrect?: () => void;
}

export const PredictionCheck: React.FC<PredictionCheckProps> = ({
    question,
    options,
    correctIndex,
    explanation,
    onCorrect
}) => {
    const { recordDecision, recordConsequence, recordEvent } = useInteractive();
    const [selectedIndex, setSelectedIndex] = useState<number | null>(null);
    const [revealed, setRevealed] = useState(false);

    const handleSelect = (idx: number) => {
        if (revealed) return;
        setSelectedIndex(idx);
        recordDecision('predict_select', { index: idx });
    };

    const handleCheck = () => {
        if (selectedIndex === null) return;
        setRevealed(true);
        recordConsequence('prediction', { index: selectedIndex, correct: selectedIndex === correctIndex });
        if (selectedIndex === correctIndex) {
            onCorrect?.();
            recordEvent('prediction_correct', { index: selectedIndex });
        }
    };

    const isCorrect = selectedIndex === correctIndex;

    return (
        <div
            data-interaction-type="prediction"
            data-component="PredictionCheck"
            className="my-4 p-4 bg-[var(--bg-panel)] rounded-lg border border-[var(--border-color)]"
        >
            <div className="text-sm font-medium text-[var(--accent-primary)] mb-3 flex items-center gap-2">
                🤔 Predict the output:
            </div>
            <div className="text-white mb-4">{question}</div>

            <div className="space-y-2 mb-4">
                {options.map((opt, idx) => {
                    let bgClass = 'bg-[#1a1a2e] hover:bg-[rgba(255,255,255,0.05)]';
                    let borderClass = 'border-[var(--border-color)]';

                    if (revealed) {
                        if (idx === correctIndex) {
                            bgClass = 'bg-[rgba(74,222,128,0.2)]';
                            borderClass = 'border-[var(--accent-success)]';
                        } else if (idx === selectedIndex) {
                            bgClass = 'bg-[rgba(239,68,68,0.2)]';
                            borderClass = 'border-[var(--accent-error)]';
                        }
                    } else if (idx === selectedIndex) {
                        borderClass = 'border-[var(--accent-secondary)]';
                    }

                    return (
                        <button
                            key={idx}
                            onClick={() => handleSelect(idx)}
                            disabled={revealed}
                            className={`
                                w-full text-left px-4 py-2 rounded border transition-all
                                font-mono text-sm
                                ${bgClass} ${borderClass}
                                ${revealed ? 'cursor-default' : 'cursor-pointer'}
                            `}
                        >
                            {opt}
                        </button>
                    );
                })}
            </div>

            {!revealed ? (
                <button
                    onClick={handleCheck}
                    disabled={selectedIndex === null}
                    className="px-4 py-2 bg-[var(--accent-secondary)] text-black rounded font-medium disabled:opacity-50 transition-all"
                >
                    Check My Prediction
                </button>
            ) : (
                <div className={`p-3 rounded ${isCorrect ? 'bg-[rgba(74,222,128,0.1)]' : 'bg-[rgba(239,68,68,0.1)]'}`}>
                    <div className={`font-medium ${isCorrect ? 'text-[var(--accent-success)]' : 'text-[var(--accent-error)]'}`}>
                        {isCorrect ? '✅ Correct!' : '❌ Not quite'}
                    </div>
                    {explanation && (
                        <div className="text-sm text-[var(--text-secondary)] mt-1">{explanation}</div>
                    )}
                </div>
            )}
        </div>
    );
};
