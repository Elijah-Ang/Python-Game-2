import React, { useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface ConditionalChoice {
    label: string;
    outcome: string;
}

interface ConditionalPathProps {
    prompt: string;
    choices: ConditionalChoice[];
    trueLabel: string;
    falseLabel: string;
    resultVar?: string;
}

export const ConditionalPath: React.FC<ConditionalPathProps> = ({
    prompt,
    choices,
    trueLabel,
    falseLabel,
    resultVar = 'condition_result'
}) => {
    const { setVariable, recordDecision, recordConsequence } = useInteractive();
    const [selected, setSelected] = useState<ConditionalChoice | null>(null);

    const handleSelect = (choice: ConditionalChoice) => {
        setSelected(choice);
        setVariable(resultVar, choice.outcome);
        recordDecision('conditional_pick', { choice: choice.label, outcome: choice.outcome });
        recordConsequence('state', { type: 'conditional', outcome: choice.outcome });
    };

    return (
        <div
            data-interaction-type="conditional_path"
            data-component="ConditionalPath"
            className="my-4 p-4 bg-[var(--bg-panel)] rounded-lg border border-[var(--border-color)]"
        >
            <div className="text-sm font-medium text-[var(--accent-primary)] mb-3">
                {prompt}
            </div>
            <div className="flex flex-wrap gap-2 mb-4">
                {choices.map(choice => {
                    const isSelected = selected?.label === choice.label;
                    return (
                        <button
                            key={choice.label}
                            onClick={() => handleSelect(choice)}
                            onKeyDown={(e) => {
                                if (e.key === 'Enter' || e.key === ' ') {
                                    e.preventDefault();
                                    handleSelect(choice);
                                }
                            }}
                            className={`
                                px-3 py-1 rounded text-sm border transition-all
                                ${isSelected
                                    ? 'bg-[var(--accent-secondary)] text-black border-[var(--accent-secondary)]'
                                    : 'bg-[#0d0d10] text-[var(--text-primary)] border-[var(--border-color)] hover:border-[var(--accent-primary)]'}
                            `}
                        >
                            {choice.label}
                        </button>
                    );
                })}
            </div>
            <div className="grid grid-cols-2 gap-3">
                <div
                    className={`p-3 rounded border ${selected?.outcome === 'true'
                        ? 'border-[var(--accent-success)] bg-[rgba(74,222,128,0.15)]'
                        : 'border-[var(--border-color)] bg-[#0d0d10]'}`}
                >
                    <div className="text-xs text-[var(--text-secondary)] mb-1">TRUE path</div>
                    <div className="text-sm text-white">{trueLabel}</div>
                </div>
                <div
                    className={`p-3 rounded border ${selected?.outcome === 'false'
                        ? 'border-[var(--accent-warning)] bg-[rgba(250,204,21,0.12)]'
                        : 'border-[var(--border-color)] bg-[#0d0d10]'}`}
                >
                    <div className="text-xs text-[var(--text-secondary)] mb-1">FALSE path</div>
                    <div className="text-sm text-white">{falseLabel}</div>
                </div>
            </div>
            {selected && (
                <div className="mt-3 text-sm text-[var(--text-secondary)]">
                    Condition evaluated to <span className="text-white">{selected.outcome}</span>
                </div>
            )}
        </div>
    );
};
