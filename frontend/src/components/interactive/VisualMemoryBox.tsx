import React from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface VisualMemoryBoxProps {
    name: string;
    type?: string;
}

export const VisualMemoryBox: React.FC<VisualMemoryBoxProps> = ({ name, type = 'auto' }) => {
    const { variables } = useInteractive();
    const value = variables[name];

    const displayType = type === 'auto' ? typeof value : type;
    const displayValue = value === undefined ? '?' : JSON.stringify(value);

    return (
        <div
            data-interaction-type="memory_box"
            data-component="VisualMemoryBox"
            className="inline-flex flex-col items-center mx-2 align-middle"
        >
            <div className="text-xs text-[var(--text-secondary)] font-mono mb-1">{name}</div>
            <div className="w-24 h-24 bg-[#1a1a2e] border-2 border-[var(--accent-secondary)] rounded flex flex-col items-center justify-center shadow-[0_0_15px_rgba(var(--accent-secondary-rgb),0.3)] relative overflow-hidden group transition-all hover:scale-105">
                <div className="text-2xl font-bold text-white z-10">{displayValue}</div>
                <div className="text-[10px] text-[var(--text-secondary)] mt-1 z-10 font-mono">type: {displayType}</div>

                {/* Background decorative effect */}
                <div className="absolute inset-0 opacity-10 bg-[radial-gradient(circle_at_center,_var(--accent-secondary),_transparent)]"></div>
            </div>
        </div>
    );
};
