import React, { useMemo, useEffect, useRef } from 'react';
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
import { TokenSlotPuzzle } from './TokenSlotPuzzle';
import { LoopSimulator } from './LoopSimulator';
import { ConditionalPath } from './ConditionalPath';
import { DataTransformAnimator } from './DataTransformAnimator';
import { JoinVisualizer } from './JoinVisualizer';
import { DebugQuest } from './DebugQuest';
import { GraphManipulator } from './GraphManipulator';
import { MemoryMachine } from './MemoryMachine';
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
    const sendToEditorItems = useMemo(
        () => safePlan.filter((item) => item.type === 'send_to_editor'),
        [safePlan]
    );
    const lastSentRef = useRef<string | null>(null);

    useEffect(() => {
        const item = sendToEditorItems[0];
        if (!item) {
            return;
        }

        const template = item.template ? renderTemplate(item.template, variables) : '';
        if (!template) {
            return;
        }

        const templateId = item.templateId || 'inline';
        const signature = `${templateId}::${template}`;
        if (signature === lastSentRef.current) {
            return;
        }

        onSendToEditor(template);
        recordDecision('send_to_editor_auto', { template: templateId });
        recordConsequence('editor', { filled: true, source: 'auto' });
        lastSentRef.current = signature;
    }, [sendToEditorItems, variables, onSendToEditor, recordDecision, recordConsequence]);

    const renderedItems = useMemo(() => safePlan
        .filter((item) => item.type !== 'send_to_editor')
        .map((item, index) => {
        const key = `${item.type}-${index}`;
        const wrap = (node: React.ReactNode) => (
            <div key={key} data-interaction-type={item.type}>
                {node}
            </div>
        );

        switch (item.type) {
            case 'prediction': {
                return wrap(
                    <PredictionCheck
                        question={item.question}
                        options={item.options}
                        correctIndex={item.correctIndex}
                        explanation={item.explanation}
                    />
                );
            }
            case 'hint_ladder': {
                return wrap(
                    <HintLadder
                        hints={item.hints}
                    />
                );
            }
            case 'variable_slider': {
                return wrap(
                    <VariableSlider
                        name={item.name}
                        min={item.min}
                        max={item.max}
                        initial={item.initial}
                        label={item.label}
                    />
                );
            }
            case 'memory_box': {
                return wrap(
                    <div className="flex flex-wrap gap-3">
                        {item.names.map((name) => (
                            <VisualMemoryBox key={name} name={name} type={item.valueType} />
                        ))}
                    </div>
                );
            }
            case 'draggable_value': {
                return wrap(
                    <div className="space-y-2">
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
                return wrap(
                    <VisualTable
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
                return wrap(
                    <LiveCodeBlock
                        initialcode={item.initialCode}
                        language={item.language}
                        highlightline={item.highlightLine}
                        variablename={item.variableName}
                    />
                );
            }
            case 'parsons_puzzle': {
                return wrap(
                    <ParsonsPuzzle
                        correctOrder={item.correctOrder}
                        scrambledOrder={item.scrambledOrder}
                    />
                );
            }
            case 'fill_blanks': {
                return wrap(
                    <FillBlanks
                        template={item.template}
                        blanks={item.blanks}
                    />
                );
            }
            case 'token_slot': {
                return wrap(
                    <TokenSlotPuzzle
                        template={item.template}
                        slots={item.slots}
                    />
                );
            }
            case 'loop_simulator': {
                return wrap(
                    <LoopSimulator
                        label={item.label}
                        iterations={item.iterations}
                        startValue={item.startValue}
                        stepValue={item.stepValue}
                        valueVar={item.valueVar}
                        stepVar={item.stepVar}
                    />
                );
            }
            case 'conditional_path': {
                return wrap(
                    <ConditionalPath
                        prompt={item.prompt}
                        choices={item.choices}
                        trueLabel={item.trueLabel}
                        falseLabel={item.falseLabel}
                        resultVar={item.resultVar}
                    />
                );
            }
            case 'data_transform': {
                return wrap(
                    <DataTransformAnimator
                        title={item.title}
                        columns={item.columns}
                        beforeRows={item.beforeRows}
                        filters={item.filters}
                        resultVar={item.resultVar}
                    />
                );
            }
            case 'join_visualizer': {
                return wrap(
                    <JoinVisualizer
                        leftTitle={item.leftTitle}
                        rightTitle={item.rightTitle}
                        leftRows={item.leftRows}
                        rightRows={item.rightRows}
                        leftKey={item.leftKey}
                        rightKey={item.rightKey}
                        joinTypes={item.joinTypes}
                        resultVar={item.resultVar}
                        joinVar={item.joinVar}
                    />
                );
            }
            case 'debug_quest': {
                return wrap(
                    <DebugQuest
                        title={item.title}
                        snippet={item.snippet}
                        bugLine={item.bugLine}
                        options={item.options}
                        solvedVar={item.solvedVar}
                    />
                );
            }
            case 'graph_manipulator': {
                return wrap(
                    <GraphManipulator
                        title={item.title}
                        mode={item.mode}
                        slope={item.slope}
                        intercept={item.intercept}
                        xMin={item.xMin}
                        xMax={item.xMax}
                        initialX={item.initialX}
                        xVar={item.xVar}
                        yVar={item.yVar}
                    />
                );
            }
            case 'memory_machine': {
                return wrap(
                    <MemoryMachine
                        title={item.title}
                        slots={item.slots}
                        steps={item.steps}
                    />
                );
            }
            case 'step_executor': {
                return wrap(
                    <StepExecutor
                        code={item.code}
                        steps={item.steps}
                    />
                );
            }
            case 'output_diff': {
                const expected = item.expected ?? expectedOutput ?? '';
                const actual = item.actual ?? getStringValue(variables[item.actualVar || ''] ?? '');
                return wrap(
                    <OutputDiff
                        expected={expected}
                        actual={actual}
                        title={item.title}
                    />
                );
            }
            case 'state_inspector': {
                return wrap(
                    <StateInspector
                        title={item.title}
                        showTypes={item.showTypes}
                        filter={item.filter}
                    />
                );
            }
            case 'reset_state': {
                return wrap(
                    <ResetStateButton
                        label={item.label}
                    />
                );
            }
            default:
                return null;
        }
    }).filter(Boolean), [expectedOutput, recordDecision, recordConsequence, safePlan, variables]);

    if (!renderedItems.length) {
        return null;
    }

    return (
        <div data-component="InteractionPlanRenderer" data-layout="interaction-plan" className="mt-6 space-y-4">
            <div className="text-xs uppercase tracking-[0.25em] text-[var(--text-secondary)]">
                Interactive Plan
            </div>
            {renderedItems}
        </div>
    );
};
