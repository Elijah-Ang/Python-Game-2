import React, { useState, type DragEvent } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface DraggableValueBoxProps {
    name: string;
    acceptedValues: (string | number)[];
    label?: string;
    type?: string;
    onValueChange?: (value: string | number) => void;
    initial?: string | number;
}

export const DraggableValueBox: React.FC<DraggableValueBoxProps> = ({
    name,
    acceptedValues,
    label,
    type = 'auto',
    onValueChange,
    initial
}) => {
    const { variables, setVariable, selectedValue, setSelectedValue, recordDecision, recordConsequence } = useInteractive();
    const currentValue = variables[name];
    const [isDragOver, setIsDragOver] = useState(false);

    const applyValue = (value: string | number, source: 'drag' | 'click' | 'keyboard' | 'init') => {
        if (!acceptedValues.includes(value)) return;
        setVariable(name, value);
        onValueChange?.(value);
        if (source !== 'init') {
            recordDecision('value_select', { name, value, source });
        }
        recordConsequence('state', { control: 'draggable', name, value });
    };

    React.useEffect(() => {
        if (currentValue === undefined && initial !== undefined) {
            applyValue(initial, 'init');
        }
    }, [currentValue, initial]);

    const handleDrop = (e: DragEvent<HTMLDivElement>) => {
        e.preventDefault();
        setIsDragOver(false);
        const droppedValue = e.dataTransfer.getData('text/plain');

        // Try to parse as number if it looks like one
        const parsedValue = !isNaN(Number(droppedValue)) ? Number(droppedValue) : droppedValue;

        applyValue(parsedValue, 'drag');
        setSelectedValue(null);
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
                onClick={() => {
                    if (selectedValue !== null) {
                        applyValue(selectedValue, 'click');
                        setSelectedValue(null);
                    }
                }}
                onKeyDown={(e) => {
                    if ((e.key === 'Enter' || e.key === ' ') && selectedValue !== null) {
                        e.preventDefault();
                        applyValue(selectedValue, 'keyboard');
                        setSelectedValue(null);
                    }
                }}
                role="button"
                tabIndex={0}
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
            {selectedValue !== null && (
                <div className="mt-2 text-[10px] text-[var(--text-secondary)] font-mono">
                    Selected: {JSON.stringify(selectedValue)} — click or press Enter to place
                </div>
            )}
        </div>
    );
};

// Value chip that can be dragged
interface ValueChipProps {
    value: string | number;
    onSelect?: (value: string | number) => void;
}

export const ValueChip: React.FC<ValueChipProps> = ({ value, onSelect }) => {
    const { selectedValue, setSelectedValue, recordDecision, recordConsequence } = useInteractive();
    const handleDragStart = (e: DragEvent<HTMLSpanElement>) => {
        e.dataTransfer.setData('text/plain', String(value));
        e.dataTransfer.effectAllowed = 'copy';
    };

    const isNumber = typeof value === 'number';
    const isSelected = selectedValue === value;

    return (
        <span
            draggable
            onDragStart={handleDragStart}
            onClick={() => {
                setSelectedValue(value);
                onSelect?.(value);
                recordDecision('value_select', { value, source: 'click_chip' });
                recordConsequence('state', { control: 'chip', value });
            }}
            onKeyDown={(e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    setSelectedValue(value);
                    onSelect?.(value);
                    recordDecision('value_select', { value, source: 'keyboard_chip' });
                    recordConsequence('state', { control: 'chip', value });
                }
            }}
            tabIndex={0}
            role="button"
            className={`
                inline-block px-3 py-1.5 rounded-full cursor-grab active:cursor-grabbing
                font-mono text-sm font-bold select-none
                transition-all hover:scale-105 hover:shadow-lg
                ${isSelected ? 'ring-2 ring-[var(--accent-success)]' : ''}
                ${isNumber
                    ? 'bg-[var(--accent-secondary)] text-black'
                    : 'bg-[var(--accent-warning)] text-black'}
            `}
        >
            {JSON.stringify(value)}
        </span>
    );
};
