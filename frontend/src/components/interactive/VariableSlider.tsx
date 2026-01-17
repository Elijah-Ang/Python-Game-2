import React, { useEffect } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface VariableSliderProps {
    name: string;
    min: number | string;
    max: number | string;
    initial?: number | string;
    label?: string;
    onValueChange?: (value: number) => void;
}

export const VariableSlider: React.FC<VariableSliderProps> = ({ name, min, max, initial, label, onValueChange }) => {
    const { variables, setVariable, recordDecision, recordConsequence } = useInteractive();
    const minVal = Number(min);
    const maxVal = Number(max);
    const initialVal = initial !== undefined ? Number(initial) : minVal;

    const value = variables[name] ?? initialVal;

    // Set initial value on mount if not set
    useEffect(() => {
        if (variables[name] === undefined) {
            setVariable(name, initialVal);
            onValueChange?.(initialVal);
            recordConsequence('state', { control: 'slider', name, value: initialVal });
        }
    }, [name, initialVal, onValueChange, recordConsequence, setVariable, variables]);

    return (
        <div
            data-interaction-type="variable_slider"
            data-component="VariableSlider"
            className="my-4 p-4 bg-[var(--bg-panel)] rounded border border-[var(--border-color)]"
        >
            <div className="flex justify-between mb-2">
                <label className="text-sm font-medium text-[var(--accent-primary)] font-mono">
                    {label || name} = <span className="text-[var(--accent-warning)]">{value}</span>
                </label>
            </div>
            <input
                type="range"
                min={minVal}
                max={maxVal}
                value={value}
                onChange={(e) => {
                    const newValue = Number(e.target.value);
                    setVariable(name, newValue);
                    onValueChange?.(newValue);
                    recordDecision('slider', { name, value: newValue });
                    recordConsequence('state', { control: 'slider', name, value: newValue });
                }}
                className="w-full accent-[var(--accent-primary)] cursor-pointer"
            />
        </div>
    );
};
