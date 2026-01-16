import React, { useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';
import { Play, SkipForward, RotateCcw } from 'lucide-react';

interface StepExecutorProps {
    code: string;
    steps: {
        line: number;
        description: string;
        stateChanges?: Record<string, any>;
    }[];
    language?: 'python' | 'r';
}

export const StepExecutor: React.FC<StepExecutorProps> = ({
    code,
    steps
}) => {
    const { setVariable, recordDecision, recordConsequence } = useInteractive();
    const [currentStep, setCurrentStep] = useState(-1); // -1 = not started
    const [isPlaying, setIsPlaying] = useState(false);

    const lines = code.split('\n');

    const executeStep = (stepIndex: number) => {
        if (stepIndex >= 0 && stepIndex < steps.length) {
            const step = steps[stepIndex];
            if (step.stateChanges) {
                Object.entries(step.stateChanges).forEach(([key, value]) => {
                    setVariable(key, value);
                });
            }
            recordConsequence('state', { type: 'step', step: stepIndex + 1 });
        }
    };

    const handleNext = () => {
        if (currentStep < steps.length - 1) {
            const nextStep = currentStep + 1;
            setCurrentStep(nextStep);
            recordDecision('step_next', { step: nextStep + 1 });
            executeStep(nextStep);
        }
    };

    const handlePlay = async () => {
        setIsPlaying(true);
        recordDecision('step_play', { from: currentStep + 1 });
        for (let i = currentStep + 1; i < steps.length; i++) {
            setCurrentStep(i);
            executeStep(i);
            await new Promise(r => setTimeout(r, 800));
        }
        setIsPlaying(false);
    };

    const handleReset = () => {
        setCurrentStep(-1);
        setIsPlaying(false);
        recordDecision('step_reset', { step: 0 });
    };

    const currentLineNumber = currentStep >= 0 ? steps[currentStep]?.line : null;

    return (
        <div className="my-4 rounded-lg overflow-hidden border border-[var(--border-color)]">
            {/* Code Display */}
            <div className="bg-[#0d0d10] p-3 font-mono text-sm">
                {lines.map((line, idx) => {
                    const lineNum = idx + 1;
                    const isActive = lineNum === currentLineNumber;
                    const isPast = currentStep >= 0 && steps.slice(0, currentStep + 1).some(s => s.line === lineNum);

                    return (
                        <div
                            key={idx}
                            className={`flex transition-all ${isActive
                                ? 'bg-[rgba(var(--accent-warning-rgb),0.3)] -mx-3 px-3'
                                : isPast
                                    ? 'opacity-50'
                                    : ''
                                }`}
                        >
                            <span className="w-6 text-[var(--text-secondary)] opacity-50 select-none">
                                {lineNum}
                            </span>
                            <span className={isActive ? 'text-[var(--accent-warning)]' : 'text-[var(--accent-success)]'}>
                                {line || ' '}
                            </span>
                            {isActive && (
                                <span className="ml-2 text-[var(--accent-warning)] animate-pulse">◀</span>
                            )}
                        </div>
                    );
                })}
            </div>

            {/* Step Description */}
            {currentStep >= 0 && (
                <div className="bg-[var(--bg-panel)] border-t border-[var(--border-color)] p-3">
                    <div className="text-sm text-[var(--accent-secondary)]">
                        Step {currentStep + 1}/{steps.length}:
                    </div>
                    <div className="text-white">{steps[currentStep]?.description}</div>
                </div>
            )}

            {/* Controls */}
            <div className="bg-[var(--bg-panel)] border-t border-[var(--border-color)] p-2 flex items-center gap-2">
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
                    title="Play All"
                >
                    <Play className="w-4 h-4" />
                </button>
                <button
                    onClick={handleNext}
                    disabled={isPlaying || currentStep >= steps.length - 1}
                    className="px-3 py-1 rounded bg-[var(--accent-secondary)] text-black text-sm font-medium disabled:opacity-50"
                >
                    <span className="flex items-center gap-1">
                        Next Step <SkipForward className="w-3 h-3" />
                    </span>
                </button>
                <div className="ml-auto text-xs text-[var(--text-secondary)]">
                    {currentStep < 0 ? 'Ready' : `${currentStep + 1}/${steps.length}`}
                </div>
            </div>
        </div>
    );
};
