import React, { useEffect } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface VariableSliderProps {
    name: string;
    min: number | string;
    max: number | string;
    initial?: number | string;
    label?: string;
}

export const VariableSlider: React.FC<VariableSliderProps> = ({ name, min, max, initial, label }) => {
    const { variables, setVariable } = useInteractive();
    const minVal = Number(min);
    const maxVal = Number(max);
    const initialVal = initial !== undefined ? Number(initial) : minVal;

    const value = variables[name] ?? initialVal;

    // Set initial value on mount if not set
    useEffect(() => {
        if (variables[name] === undefined) {
            setVariable(name, initialVal);
        }
    }, [name, initialVal, setVariable, variables]);

    return (
        <div className="my-4 p-4 bg-[var(--bg-panel)] rounded border border-[var(--border-color)]">
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
                onChange={(e) => setVariable(name, Number(e.target.value))}
                className="w-full accent-[var(--accent-primary)] cursor-pointer"
            />
        </div>
    );
};
