import React from 'react';
import { useInteractive } from '../../context/InteractiveContext';
import { RotateCcw } from 'lucide-react';

interface ResetStateButtonProps {
    label?: string;
    onReset?: () => void;
}

export const ResetStateButton: React.FC<ResetStateButtonProps> = ({
    label = 'Reset',
    onReset
}) => {
    const { resetVariables, resetInteractions, recordEvent } = useInteractive();

    const handleReset = () => {
        resetVariables();
        resetInteractions();
        recordEvent('reset_count', { source: 'interaction' });
        onReset?.();
    };

    return (
        <button
            onClick={handleReset}
            className="inline-flex items-center gap-2 px-3 py-1.5 text-sm rounded
                       bg-[var(--bg-panel)] border border-[var(--border-color)]
                       hover:border-[var(--accent-error)] hover:text-[var(--accent-error)]
                       transition-all"
        >
            <RotateCcw className="w-3 h-3" />
            {label}
        </button>
    );
};
