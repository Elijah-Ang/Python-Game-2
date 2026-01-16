import React, { useState } from 'react';

interface ParsonsPuzzleProps {
    correctOrder: string[];
    scrambledOrder?: string[];
    onSolved?: () => void;
}

export const ParsonsPuzzle: React.FC<ParsonsPuzzleProps> = ({
    correctOrder,
    scrambledOrder,
    onSolved
}) => {
    // Scramble if not provided
    const initialOrder = scrambledOrder || [...correctOrder].sort(() => Math.random() - 0.5);
    const [lines, setLines] = useState<string[]>(initialOrder);
    const [draggedIdx, setDraggedIdx] = useState<number | null>(null);
    const [isSolved, setIsSolved] = useState(false);

    const handleDragStart = (idx: number) => {
        setDraggedIdx(idx);
    };

    const handleDragOver = (e: React.DragEvent, idx: number) => {
        e.preventDefault();
        if (draggedIdx === null || draggedIdx === idx) return;

        const newLines = [...lines];
        const [removed] = newLines.splice(draggedIdx, 1);
        newLines.splice(idx, 0, removed);
        setLines(newLines);
        setDraggedIdx(idx);
    };

    const handleDragEnd = () => {
        setDraggedIdx(null);

        // Check if solved
        const isCorrect = lines.every((line, idx) => line === correctOrder[idx]);
        if (isCorrect && !isSolved) {
            setIsSolved(true);
            onSolved?.();
        }
    };

    return (
        <div className="my-4">
            <div className="text-sm text-[var(--text-secondary)] mb-2">
                🧩 Drag to arrange the code in the correct order:
            </div>
            <div className="space-y-1">
                {lines.map((line, idx) => {
                    return (
                        <div
                            key={`${line}-${idx}`}
                            draggable
                            onDragStart={() => handleDragStart(idx)}
                            onDragOver={(e) => handleDragOver(e, idx)}
                            onDragEnd={handleDragEnd}
                            className={`
                                px-3 py-2 rounded font-mono text-sm cursor-grab active:cursor-grabbing
                                transition-all select-none
                                ${draggedIdx === idx ? 'opacity-50 scale-95' : ''}
                                ${isSolved
                                    ? 'bg-[rgba(74,222,128,0.2)] border border-[var(--accent-success)]'
                                    : 'bg-[#0d0d10] border border-[var(--border-color)] hover:border-[var(--accent-primary)]'}
                            `}
                        >
                            <span className="text-[var(--text-secondary)] mr-2">{idx + 1}.</span>
                            <span className={isSolved ? 'text-[var(--accent-success)]' : 'text-white'}>{line}</span>
                        </div>
                    );
                })}
            </div>
            {isSolved && (
                <div className="mt-3 text-[var(--accent-success)] font-medium flex items-center gap-2">
                    ✅ Correct! The code is in the right order.
                </div>
            )}
        </div>
    );
};
