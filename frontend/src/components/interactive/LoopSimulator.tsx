import React, { useEffect, useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';
import { Play, SkipForward, RotateCcw } from 'lucide-react';

interface LoopSimulatorProps {
    label?: string;
    iterations: number;
    startValue: number;
    stepValue: number;
    valueVar?: string;
    stepVar?: string;
}

export const LoopSimulator: React.FC<LoopSimulatorProps> = ({
    label = 'Loop simulator',
    iterations,
    startValue,
    stepValue,
    valueVar = 'loop_value',
    stepVar = 'loop_step'
}) => {
    const { setVariable, recordDecision, recordConsequence } = useInteractive();
    const [currentStep, setCurrentStep] = useState(0);
    const [isPlaying, setIsPlaying] = useState(false);
    const [value, setValue] = useState(startValue);

    useEffect(() => {
        setVariable(valueVar, value);
        setVariable(stepVar, currentStep);
    }, [currentStep, setVariable, stepVar, value, valueVar]);

    useEffect(() => {
        if (!isPlaying) return;
        if (currentStep >= iterations) {
            setIsPlaying(false);
            return;
        }
        const timer = window.setTimeout(() => {
            setCurrentStep((prev) => prev + 1);
            setValue((prev) => prev + stepValue);
            recordConsequence('state', { type: 'loop_step', step: currentStep + 1 });
        }, 600);
        return () => window.clearTimeout(timer);
    }, [currentStep, isPlaying, iterations, recordConsequence, stepValue]);

    const handleNext = () => {
        if (currentStep >= iterations) return;
        setCurrentStep((prev) => prev + 1);
        setValue((prev) => prev + stepValue);
        recordDecision('loop_step', { step: currentStep + 1 });
        recordConsequence('state', { type: 'loop_step', step: currentStep + 1 });
    };

    const handlePlay = () => {
        recordDecision('loop_play', { from: currentStep + 1 });
        setIsPlaying(true);
    };

    const handleReset = () => {
        setCurrentStep(0);
        setValue(startValue);
        setIsPlaying(false);
        recordDecision('loop_reset', {});
    };

    return (
        <div
            data-interaction-type="loop_simulator"
            data-component="LoopSimulator"
            className="my-4 rounded-lg overflow-hidden border border-[var(--border-color)] bg-[#0d0d10]"
        >
            <div className="p-3 border-b border-[var(--border-color)] flex items-center justify-between">
                <div>
                    <div className="text-sm font-semibold text-[var(--accent-secondary)]">{label}</div>
                    <div className="text-xs text-[var(--text-secondary)]">Each step adds {stepValue}.</div>
                </div>
                <div className="text-xs text-[var(--text-secondary)]">Step {currentStep}/{iterations}</div>
            </div>
            <div className="p-4 space-y-3">
                <div className="flex gap-2 flex-wrap">
                    {Array.from({ length: iterations }).map((_, idx) => (
                        <div
                            key={idx}
                            className={`w-6 h-6 rounded-full border text-xs flex items-center justify-center ${
                                idx < currentStep
                                    ? 'bg-[var(--accent-success)] text-black border-[var(--accent-success)]'
                                    : 'border-[var(--border-color)] text-[var(--text-secondary)]'
                            }`}
                        >
                            {idx + 1}
                        </div>
                    ))}
                </div>
                <div className="text-sm font-mono text-[var(--accent-warning)]">
                    value = {value}
                </div>
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
                    disabled={isPlaying || currentStep >= iterations}
                    className="p-2 rounded hover:bg-[rgba(255,255,255,0.1)] disabled:opacity-50"
                    title="Play"
                >
                    <Play className="w-4 h-4" />
                </button>
                <button
                    onClick={handleNext}
                    disabled={isPlaying || currentStep >= iterations}
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
