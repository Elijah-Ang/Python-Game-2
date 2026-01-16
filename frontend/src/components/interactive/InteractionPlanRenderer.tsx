import React, { useMemo } from 'react';
import { VariableSlider } from './VariableSlider';
import { VisualMemoryBox } from './VisualMemoryBox';
import { DraggableValueBox, ValueChip } from './DraggableValueBox';
import { LiveCodeBlock } from './LiveCodeBlock';
import { VisualTable } from './VisualTable';
import { ParsonsPuzzle } from './ParsonsPuzzle';
import { PredictionCheck } from './PredictionCheck';
import { HintLadder } from './HintLadder';
import { StateInspector } from './StateInspector';
import { ResetStateButton } from './ResetStateButton';
import { OutputDiff } from './OutputDiff';
import { StepExecutor } from './StepExecutor';
import { FillBlanks } from './FillBlanks';
import { useInteractive } from '../../context/InteractiveContext';
import { resolveInteractionDataset } from '../../utils/interactionPlanDatasets';
import { renderTemplate } from '../../utils/interactionTemplate';
import type { LessonInteractionPlan } from '../../types/interaction';

interface InteractionPlanRendererProps {
    plan: LessonInteractionPlan;
    onSendToEditor: (code: string) => void;
    expectedOutput?: string;
}

const getStringValue = (value: unknown): string => {
    if (value === null || value === undefined) return '';
    return String(value);
};

export const InteractionPlanRenderer: React.FC<InteractionPlanRendererProps> = ({
    plan,
    onSendToEditor,
    expectedOutput
}) => {
    const { variables, recordDecision, recordConsequence } = useInteractive();

    const safePlan = plan || [];

    const renderedItems = useMemo(() => safePlan.map((item, index) => {
        const key = `${item.type}-${index}`;

        switch (item.type) {
            case 'prediction': {
                return (
                    <PredictionCheck
                        key={key}
                        question={item.question}
                        options={item.options}
                        correctIndex={item.correctIndex}
                        explanation={item.explanation}
                    />
                );
            }
            case 'hint_ladder': {
                return (
                    <HintLadder
                        key={key}
                        hints={item.hints}
                    />
                );
            }
            case 'variable_slider': {
                return (
                    <VariableSlider
                        key={key}
                        name={item.name}
                        min={item.min}
                        max={item.max}
                        initial={item.initial}
                        label={item.label}
                    />
                );
            }
            case 'memory_box': {
                return (
                    <div key={key} className="flex flex-wrap gap-3">
                        {item.names.map((name) => (
                            <VisualMemoryBox key={name} name={name} type={item.valueType} />
                        ))}
                    </div>
                );
            }
            case 'draggable_value': {
                return (
                    <div key={key} className="space-y-2">
                        {item.chips?.length ? (
                            <div className="flex flex-wrap gap-2">
                                {item.chips.map((chip) => (
                                    <ValueChip key={chip} value={chip} />
                                ))}
                            </div>
                        ) : null}
                        <DraggableValueBox
                            name={item.name}
                            acceptedValues={item.acceptedValues}
                            label={item.label}
                            type={item.valueType}
                            initial={item.initial}
                        />
                    </div>
                );
            }
            case 'visual_table': {
                const data = item.data ?? resolveInteractionDataset(item.dataRef);
                return (
                    <VisualTable
                        key={key}
                        data={data}
                        columns={item.columns}
                        title={item.title}
                        allowSort={item.allowSort}
                        allowFilter={item.allowFilter}
                        highlightColumn={item.highlightColumn}
                        allowReorder={item.allowReorder}
                        allowRowHighlight={item.allowRowHighlight}
                    />
                );
            }
            case 'live_code_block': {
                return (
                    <LiveCodeBlock
                        key={key}
                        initialcode={item.initialCode}
                        language={item.language}
                        highlightline={item.highlightLine}
                        variablename={item.variableName}
                    />
                );
            }
            case 'parsons_puzzle': {
                return (
                    <ParsonsPuzzle
                        key={key}
                        correctOrder={item.correctOrder}
                        scrambledOrder={item.scrambledOrder}
                    />
                );
            }
            case 'fill_blanks': {
                return (
                    <FillBlanks
                        key={key}
                        template={item.template}
                        blanks={item.blanks}
                    />
                );
            }
            case 'step_executor': {
                return (
                    <StepExecutor
                        key={key}
                        code={item.code}
                        steps={item.steps}
                    />
                );
            }
            case 'output_diff': {
                const expected = item.expected ?? expectedOutput ?? '';
                const actual = item.actual ?? getStringValue(variables[item.actualVar || ''] ?? '');
                return (
                    <OutputDiff
                        key={key}
                        expected={expected}
                        actual={actual}
                        title={item.title}
                    />
                );
            }
            case 'state_inspector': {
                return (
                    <StateInspector
                        key={key}
                        title={item.title}
                        showTypes={item.showTypes}
                        filter={item.filter}
                    />
                );
            }
            case 'reset_state': {
                return (
                    <ResetStateButton
                        key={key}
                        label={item.label}
                    />
                );
            }
            case 'send_to_editor': {
                const template = item.template;
                const interpolated = template
                    ? renderTemplate(template, variables)
                    : '';

                return (
                    <div
                        key={key}
                        className="my-4 p-4 bg-[var(--bg-panel)] rounded-lg border border-[var(--border-color)] flex flex-wrap items-center justify-between gap-3"
                    >
                        <div>
                            <div className="text-sm font-medium text-[var(--accent-secondary)]">
                                {item.label || 'Send to editor'}
                            </div>
                            <div className="text-xs text-[var(--text-secondary)]">
                                Use your current choices to generate the next code snippet.
                            </div>
                        </div>
                        <button
                            type="button"
                            onClick={() => {
                                onSendToEditor(interpolated);
                                recordDecision('send_to_editor', { template: item.templateId || 'inline' });
                                recordConsequence('editor', { filled: Boolean(interpolated) });
                            }}
                            className="px-3 py-2 bg-[var(--accent-secondary)] text-black rounded text-sm font-medium hover:opacity-90"
                        >
                            Send to editor
                        </button>
                    </div>
                );
            }
            default:
                return null;
        }
    }).filter(Boolean), [expectedOutput, onSendToEditor, recordConsequence, recordDecision, safePlan, variables]);

    if (!renderedItems.length) {
        return null;
    }

    return (
        <div className="mt-6 space-y-4">
            <div className="text-xs uppercase tracking-[0.25em] text-[var(--text-secondary)]">
                Interactive Plan
            </div>
            {renderedItems}
        </div>
    );
};
