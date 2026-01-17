import React, { useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';
import { Play, SkipForward, RotateCcw } from 'lucide-react';

interface MemoryStep {
    label: string;
    slot: string;
    value: string | number;
}

interface MemoryMachineProps {
    title?: string;
    slots: string[];
    steps: MemoryStep[];
}

export const MemoryMachine: React.FC<MemoryMachineProps> = ({
    title = 'Memory machine',
    slots,
    steps
}) => {
    const { setVariable, recordDecision, recordConsequence } = useInteractive();
    const [currentStep, setCurrentStep] = useState(-1);
    const [memory, setMemory] = useState<Record<string, string | number>>({});
    const [isPlaying, setIsPlaying] = useState(false);

    const applyStep = (index: number) => {
        const step = steps[index];
        if (!step) return;
        setMemory(prev => ({ ...prev, [step.slot]: step.value }));
        setVariable(step.slot, step.value);
        recordConsequence('state', { slot: step.slot, value: step.value });
    };

    const handleNext = () => {
        if (currentStep >= steps.length - 1) return;
        const nextIndex = currentStep + 1;
        setCurrentStep(nextIndex);
        recordDecision('memory_step', { step: nextIndex + 1 });
        applyStep(nextIndex);
    };

    const handlePlay = async () => {
        setIsPlaying(true);
        recordDecision('memory_play', {});
        for (let i = currentStep + 1; i < steps.length; i++) {
            setCurrentStep(i);
            applyStep(i);
            // eslint-disable-next-line no-await-in-loop
            await new Promise(resolve => setTimeout(resolve, 600));
        }
        setIsPlaying(false);
    };

    const handleReset = () => {
        setCurrentStep(-1);
        setMemory({});
        setIsPlaying(false);
        recordDecision('memory_reset', {});
    };

    return (
        <div
            data-interaction-type="memory_machine"
            data-component="MemoryMachine"
            className="my-4 rounded-lg border border-[var(--border-color)] bg-[#0d0d10]"
        >
            <div className="p-3 border-b border-[var(--border-color)] flex items-center justify-between">
                <div>
                    <div className="text-sm font-semibold text-[var(--accent-secondary)]">{title}</div>
                    <div className="text-xs text-[var(--text-secondary)]">Step through each assignment.</div>
                </div>
                <div className="text-xs text-[var(--text-secondary)]">
                    {currentStep + 1}/{steps.length}
                </div>
            </div>
            <div className="p-4 grid grid-cols-2 gap-3">
                {slots.map(slot => (
                    <div
                        key={slot}
                        className={`p-3 rounded border ${
                            memory[slot] !== undefined
                                ? 'border-[var(--accent-success)] bg-[rgba(74,222,128,0.1)]'
                                : 'border-[var(--border-color)] bg-[#0a0a0c]'
                        }`}
                    >
                        <div className="text-xs text-[var(--text-secondary)] mb-1">{slot}</div>
                        <div className="text-sm font-mono text-white">
                            {memory[slot] !== undefined ? JSON.stringify(memory[slot]) : 'empty'}
                        </div>
                    </div>
                ))}
            </div>
            <div className="p-2 border-t border-[var(--border-color)] flex items-center gap-2">
                <button
                    onClick={handleReset}
                    className="p-2 rounded hover:bg-[rgba(255,255,255,0.1)]"
                    title="Reset"
                >
                    <RotateCcw className="w-4 h-4" />
                </button>
                <button
                    onClick={handlePlay}
                    disabled={isPlaying || currentStep >= steps.length - 1}
                    className="p-2 rounded hover:bg-[rgba(255,255,255,0.1)] disabled:opacity-50"
                    title="Play"
                >
                    <Play className="w-4 h-4" />
                </button>
                <button
                    onClick={handleNext}
                    disabled={isPlaying || currentStep >= steps.length - 1}
                    className="px-3 py-1 rounded bg-[var(--accent-secondary)] text-black text-sm font-medium disabled:opacity-50"
                >
                    <span className="flex items-center gap-1">
                        Next <SkipForward className="w-3 h-3" />
                    </span>
                </button>
            </div>
        </div>
    );
};
