import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { VariableSlider } from './VariableSlider';
import { VisualTable } from './VisualTable';
import { DraggableValueBox, ValueChip } from './DraggableValueBox';
import { LiveCodeBlock } from './LiveCodeBlock';
import { ParsonsPuzzle } from './ParsonsPuzzle';
import { PredictionCheck } from './PredictionCheck';
import { StepExecutor } from './StepExecutor';
import { OutputDiff } from './OutputDiff';
import { StateInspector } from './StateInspector';
import { ResetStateButton } from './ResetStateButton';
import { INTERACTION_BLUEPRINTS, type CurriculumMode } from '../../utils/interactionLabConfig';
import { useInteractive } from '../../context/InteractiveContext';
import { Play, Send } from 'lucide-react';

interface InteractionLabProps {
    mode: CurriculumMode;
    onPrimeCode: (code: string) => void;
    expectedOutput?: string;
    lessonTitle: string;
}

export const InteractionLab: React.FC<InteractionLabProps> = ({
    mode,
    onPrimeCode,
    expectedOutput,
    lessonTitle
}) => {
    const blueprint = INTERACTION_BLUEPRINTS[mode];
    const { variables, setVariable } = useInteractive();
    const sliderName = `${mode}-lab-slider`;
    const filterName = `${mode}-lab-filter`;

    const [loopBound, setLoopBound] = useState<number>(blueprint.slider.initial);
    const [filterValue, setFilterValue] = useState<string | number>(blueprint.filter.defaultValue);
    const [puzzleSolved, setPuzzleSolved] = useState(false);
    const [predictionSolved, setPredictionSolved] = useState(false);
    const [generatedCode, setGeneratedCode] = useState(() =>
        blueprint.buildCode(blueprint.slider.initial, blueprint.filter.defaultValue)
    );

    const applyFilter = useCallback((row: Record<string, any>, value: string | number) => {
        if (!blueprint.table.filterKey) return true;

        if (typeof blueprint.table.filterKey === 'function') {
            return blueprint.table.filterKey(row, value);
        }

        const target = row[blueprint.table.filterKey];
        if (typeof value === 'number') {
            return Number(target) >= Number(value);
        }
        return String(target).toLowerCase() === String(value).toLowerCase();
    }, [blueprint.table.filterKey]);

    const filteredRows = useMemo(() => {
        const filtered = blueprint.table.rows.filter((row) => applyFilter(row, filterValue));
        return filtered.slice(0, loopBound);
    }, [applyFilter, blueprint.table.rows, filterValue, loopBound]);

    const baselineRows = useMemo(() => {
        const base = blueprint.table.rows.filter((row) => applyFilter(row, blueprint.filter.defaultValue));
        return base.slice(0, blueprint.slider.initial);
    }, [applyFilter, blueprint.filter.defaultValue, blueprint.slider.initial, blueprint.table.rows]);

    const expectedText = expectedOutput && expectedOutput.trim() && expectedOutput !== 'Run your code to see the output!'
        ? expectedOutput
        : blueprint.buildOutcome(baselineRows, blueprint.filter.defaultValue, blueprint.slider.initial);
    const actualText = blueprint.buildOutcome(filteredRows, filterValue, loopBound);

    const metrics = useMemo(() => {
        if (blueprint.metrics) {
            return blueprint.metrics(filteredRows, filterValue, loopBound);
        }
        return [
            { label: 'Loops', value: loopBound, max: blueprint.slider.max, accent: 'secondary' as const },
            { label: 'Rows kept', value: filteredRows.length, max: blueprint.table.rows.length, accent: 'warning' as const }
        ];
    }, [blueprint, filteredRows, filterValue, loopBound]);

    const readyToSend = puzzleSolved || predictionSolved;

    useEffect(() => {
        setLoopBound(blueprint.slider.initial);
        setFilterValue(blueprint.filter.defaultValue);
        setPuzzleSolved(false);
        setPredictionSolved(false);
        const baseCode = blueprint.buildCode(blueprint.slider.initial, blueprint.filter.defaultValue);
        setGeneratedCode(baseCode);
        setVariable(sliderName, blueprint.slider.initial);
        setVariable(filterName, blueprint.filter.defaultValue);
    }, [blueprint, filterName, sliderName, setVariable]);

    useEffect(() => {
        const ctxFilter = variables[filterName];
        if (ctxFilter !== undefined && ctxFilter !== filterValue) {
            setFilterValue(ctxFilter);
        }
    }, [filterName, filterValue, variables]);

    useEffect(() => {
        setGeneratedCode(blueprint.buildCode(loopBound, filterValue));
    }, [blueprint, filterValue, loopBound]);

    useEffect(() => {
        setVariable(`${mode}-lab-kept`, filteredRows.length);
        setVariable(`${mode}-lab-outcome`, actualText);
    }, [actualText, filteredRows.length, mode, setVariable]);

    const handlePrimeCode = () => {
        onPrimeCode(generatedCode);
    };

    const handleResetLab = () => {
        setLoopBound(blueprint.slider.initial);
        setFilterValue(blueprint.filter.defaultValue);
        setPuzzleSolved(false);
        setPredictionSolved(false);
        const baseCode = blueprint.buildCode(blueprint.slider.initial, blueprint.filter.defaultValue);
        setGeneratedCode(baseCode);
        setVariable(sliderName, blueprint.slider.initial);
        setVariable(filterName, blueprint.filter.defaultValue);
    };

    const accentToColor = (accent?: string) => {
        switch (accent) {
            case 'secondary': return 'bg-[var(--accent-secondary)]';
            case 'warning': return 'bg-[var(--accent-warning)]';
            case 'success': return 'bg-[var(--accent-success)]';
            default: return 'bg-[var(--accent-primary)]';
        }
    };

    return (
        <div className="mt-6 p-4 md:p-5 bg-[var(--bg-panel)] rounded-lg border border-[var(--accent-secondary)] shadow-[0_0_0_1px_rgba(99,102,241,0.3)] space-y-4">
            <div className="flex flex-wrap items-start gap-3 justify-between">
                <div>
                    <div className="text-xs uppercase tracking-[0.08em] text-[var(--text-secondary)]">Hands-on lab</div>
                    <div className="text-lg font-semibold text-[var(--accent-primary)]">
                        Drag, tweak, and watch {mode.toUpperCase()} react
                    </div>
                    <div className="text-xs text-[var(--text-secondary)]">
                        Interactive companion for “{lessonTitle}” — move sliders, drag chips, and force the output to move.
                    </div>
                </div>
                <div className="flex items-center gap-2">
                    <ResetStateButton label="Reset lab" onReset={handleResetLab} />
                    <button
                        onClick={handlePrimeCode}
                        disabled={!readyToSend}
                        className={`
                            px-3 py-2 rounded text-sm font-medium flex items-center gap-2 transition-all
                            ${readyToSend
                                ? 'bg-[var(--accent-secondary)] text-black hover:opacity-90'
                                : 'bg-[var(--border-color)] text-[var(--text-secondary)] cursor-not-allowed'}
                        `}
                        title={readyToSend ? 'Send this generated snippet into the main editor' : 'Solve the puzzle or prediction first'}
                    >
                        <Send className="w-4 h-4" />
                        Send to editor
                    </button>
                </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                <div className="p-3 rounded-lg border border-[var(--border-color)] bg-[#0d0d10] space-y-3">
                    <div className="flex items-center justify-between gap-2">
                        <div>
                            <div className="text-sm font-semibold text-[var(--accent-secondary)]">{blueprint.slider.label}</div>
                            {blueprint.slider.helper && <div className="text-xs text-[var(--text-secondary)]">{blueprint.slider.helper}</div>}
                        </div>
                        <div className="text-xs text-[var(--text-secondary)] bg-[var(--bg-panel)] px-2 py-1 rounded">
                            {loopBound} steps
                        </div>
                    </div>
                    <VariableSlider
                        name={sliderName}
                        min={blueprint.slider.min}
                        max={blueprint.slider.max}
                        initial={blueprint.slider.initial}
                        label="Loop/sample size"
                        onValueChange={setLoopBound}
                    />
                    <div className="space-y-2">
                        {metrics.map((metric) => {
                            const pct = metric.max ? Math.min(100, (metric.value / metric.max) * 100) : 100;
                            return (
                                <div key={metric.label}>
                                    <div className="flex justify-between text-xs text-[var(--text-secondary)] mb-1">
                                        <span>{metric.label}</span>
                                        <span className="text-[var(--text-primary)]">{metric.value}{metric.max ? ` / ${metric.max}` : ''}</span>
                                    </div>
                                    <div className="h-2 bg-[var(--border-color)] rounded-full overflow-hidden">
                                        <div
                                            className={`h-full ${accentToColor(metric.accent)}`}
                                            style={{ width: `${pct}%` }}
                                        />
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                </div>

                <div className="p-3 rounded-lg border border-[var(--border-color)] bg-[#0a0a0c] space-y-2">
                    <div className="flex items-center justify-between">
                        <div>
                            <div className="text-sm font-semibold text-[var(--accent-secondary)]">Tactile filter</div>
                            <div className="text-xs text-[var(--text-secondary)]">{blueprint.filter.helper}</div>
                        </div>
                        <div className="flex gap-2 flex-wrap justify-end">
                            {blueprint.filter.chips.map((chip) => (
                                <ValueChip key={chip} value={chip} />
                            ))}
                        </div>
                    </div>
                    <DraggableValueBox
                        name={filterName}
                        acceptedValues={blueprint.filter.chips}
                        label={blueprint.filter.label}
                        type={typeof blueprint.filter.defaultValue}
                        onValueChange={setFilterValue}
                    />
                    <div className="text-xs text-[var(--text-secondary)]">
                        Drag a chip into the slot above. Every change re-filters the dataset below in real time.
                    </div>
                </div>

                <div className="p-3 rounded-lg border border-[var(--border-color)] bg-[#0d0d10]">
                    <div className="flex items-center justify-between mb-2">
                        <div>
                            <div className="text-sm font-semibold text-[var(--accent-secondary)]">Live dataset</div>
                            <div className="text-xs text-[var(--text-secondary)]">Drag columns, toggle fields, and click rows to spotlight them.</div>
                        </div>
                        <div className="text-xs text-[var(--text-secondary)] px-2 py-1 bg-[var(--bg-panel)] rounded">
                            Showing {filteredRows.length}/{blueprint.table.rows.length}
                        </div>
                    </div>
                    <VisualTable
                        data={filteredRows}
                        columns={blueprint.table.columns}
                        allowSort
                        allowFilter={blueprint.table.allowFilter}
                        highlightColumn={blueprint.table.highlightColumn}
                        allowReorder
                        allowRowHighlight
                    />
                </div>

                <div className="p-3 rounded-lg border border-[var(--border-color)] bg-[#0a0a0c] space-y-3">
                    <div className="flex items-center justify-between">
                        <div>
                            <div className="text-sm font-semibold text-[var(--accent-secondary)]">Predict & prove</div>
                            <div className="text-xs text-[var(--text-secondary)]">You unlock the editor once you nail one of these.</div>
                        </div>
                        <div className="text-xs text-[var(--text-secondary)]">
                            {readyToSend ? 'Unlocked' : 'Solve to unlock'}
                        </div>
                    </div>
                    <PredictionCheck
                        question={blueprint.prediction.question}
                        options={blueprint.prediction.options}
                        correctIndex={blueprint.prediction.correctIndex}
                        explanation={blueprint.prediction.explanation}
                        onCorrect={() => setPredictionSolved(true)}
                    />
                    <ParsonsPuzzle
                        correctOrder={blueprint.puzzle}
                        onSolved={() => setPuzzleSolved(true)}
                    />
                </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                <div className="p-3 rounded-lg border border-[var(--border-color)] bg-[#0d0d10] space-y-2">
                    <div className="flex items-center justify-between">
                        <div>
                            <div className="text-sm font-semibold text-[var(--accent-secondary)]">Animate each step</div>
                            <div className="text-xs text-[var(--text-secondary)]">See how state changes per line before you run it for real.</div>
                        </div>
                        <Play className="w-4 h-4 text-[var(--accent-secondary)]" />
                    </div>
                    <StepExecutor
                        code={blueprint.steps.code}
                        steps={blueprint.steps.steps}
                        key={`${mode}-steps`}
                    />
                </div>

                <div className="p-3 rounded-lg border border-[var(--border-color)] bg-[#0a0a0c] space-y-3">
                    <div className="flex items-center justify-between">
                        <div>
                            <div className="text-sm font-semibold text-[var(--accent-secondary)]">Edit a single line</div>
                            <div className="text-xs text-[var(--text-secondary)]">
                                Try to break it or fix it — your tweaks can be pushed into the main editor.
                            </div>
                        </div>
                    </div>
                    <LiveCodeBlock
                        initialcode={generatedCode}
                        language={blueprint.liveCode.language}
                        highlightline={blueprint.liveCode.highlightLine}
                    />
                    {blueprint.liveCode.note && (
                        <div className="text-xs text-[var(--text-secondary)]">{blueprint.liveCode.note}</div>
                    )}
                    <div className="text-xs text-[var(--text-secondary)]">
                        Tip: intentionally make a mistake to see how the preview reacts, then send the fixed version.
                    </div>
                </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                <div className="p-3 rounded-lg border border-[var(--border-color)] bg-[#0d0d10] space-y-2">
                    <div className="flex items-center justify-between">
                        <div>
                            <div className="text-sm font-semibold text-[var(--accent-secondary)]">Instant feedback</div>
                            <div className="text-xs text-[var(--text-secondary)]">Output updates as you drag and slide.</div>
                        </div>
                    </div>
                    <OutputDiff
                        title="Baseline vs current"
                        expected={expectedText}
                        actual={actualText}
                    />
                </div>

                <div className="p-3 rounded-lg border border-[var(--border-color)] bg-[#0a0a0c] space-y-3">
                    <div className="flex items-center justify-between">
                        <div>
                            <div className="text-sm font-semibold text-[var(--accent-secondary)]">Lab state</div>
                            <div className="text-xs text-[var(--text-secondary)]">Everything you touch is tracked and resettable.</div>
                        </div>
                    </div>
                    <StateInspector
                        title="Live lab variables"
                        filter={[sliderName, filterName, `${mode}-lab-kept`]}
                    />
                    <div className="text-xs text-[var(--text-secondary)]">
                        Keep iterating — you can drag, run, and retry without losing your place.
                    </div>
                </div>
            </div>
        </div>
    );
};
