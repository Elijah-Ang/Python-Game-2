import React, { useState, type DragEvent } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface DraggableValueBoxProps {
    name: string;
    acceptedValues: (string | number)[];
    label?: string;
    type?: string;
    onValueChange?: (value: string | number) => void;
}

export const DraggableValueBox: React.FC<DraggableValueBoxProps> = ({
    name,
    acceptedValues,
    label,
    type = 'auto',
    onValueChange
}) => {
    const { variables, setVariable } = useInteractive();
    const currentValue = variables[name];
    const [isDragOver, setIsDragOver] = useState(false);

    const handleDrop = (e: DragEvent<HTMLDivElement>) => {
        e.preventDefault();
        setIsDragOver(false);
        const droppedValue = e.dataTransfer.getData('text/plain');

        // Try to parse as number if it looks like one
        const parsedValue = !isNaN(Number(droppedValue)) ? Number(droppedValue) : droppedValue;

        if (acceptedValues.includes(parsedValue)) {
            setVariable(name, parsedValue);
            onValueChange?.(parsedValue);
        }
    };

    const handleDragOver = (e: DragEvent<HTMLDivElement>) => {
        e.preventDefault();
        setIsDragOver(true);
    };

    const handleDragLeave = () => {
        setIsDragOver(false);
    };

    const displayType = type === 'auto' ? typeof currentValue : type;
    const displayValue = currentValue === undefined ? '?' : JSON.stringify(currentValue);

    return (
        <div className="flex flex-col items-center my-4">
            <div className="text-xs text-[var(--text-secondary)] font-mono mb-2">{label || name}</div>
            <div
                onDrop={handleDrop}
                onDragOver={handleDragOver}
                onDragLeave={handleDragLeave}
                className={`
                    w-28 h-28 rounded-lg border-2 border-dashed
                    flex flex-col items-center justify-center
                    transition-all cursor-pointer
                    ${isDragOver
                        ? 'border-[var(--accent-success)] bg-[rgba(74,222,128,0.1)] scale-105'
                        : 'border-[var(--accent-secondary)] bg-[#1a1a2e]'}
                    ${currentValue !== undefined ? 'border-solid' : ''}
                    hover:border-[var(--accent-primary)]
                `}
            >
                {currentValue !== undefined ? (
                    <>
                        <div className="text-2xl font-bold text-white">{displayValue}</div>
                        <div className="text-[10px] text-[var(--text-secondary)] mt-1 font-mono">
                            type: {displayType}
                        </div>
                    </>
                ) : (
                    <div className="text-sm text-[var(--text-secondary)] text-center px-2">
                        Drop a value here
                    </div>
                )}
            </div>
        </div>
    );
};

// Value chip that can be dragged
interface ValueChipProps {
    value: string | number;
}

export const ValueChip: React.FC<ValueChipProps> = ({ value }) => {
    const handleDragStart = (e: DragEvent<HTMLSpanElement>) => {
        e.dataTransfer.setData('text/plain', String(value));
        e.dataTransfer.effectAllowed = 'copy';
    };

    const isNumber = typeof value === 'number';

    return (
        <span
            draggable
            onDragStart={handleDragStart}
            className={`
                inline-block px-3 py-1.5 rounded-full cursor-grab active:cursor-grabbing
                font-mono text-sm font-bold select-none
                transition-all hover:scale-105 hover:shadow-lg
                ${isNumber
                    ? 'bg-[var(--accent-secondary)] text-black'
                    : 'bg-[var(--accent-warning)] text-black'}
            `}
        >
            {JSON.stringify(value)}
        </span>
    );
};
