import React, { useMemo, useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface GraphManipulatorProps {
    title?: string;
    mode?: 'linear' | 'quadratic';
    slope?: number;
    intercept?: number;
    xMin?: number;
    xMax?: number;
    initialX?: number;
    xVar?: string;
    yVar?: string;
}

const clamp = (value: number, min: number, max: number) => Math.min(max, Math.max(min, value));

export const GraphManipulator: React.FC<GraphManipulatorProps> = ({
    title = 'Graph manipulator',
    mode = 'linear',
    slope = 1,
    intercept = 0,
    xMin = -5,
    xMax = 5,
    initialX = 1,
    xVar = 'graph_x',
    yVar = 'graph_y'
}) => {
    const { setVariable, recordDecision, recordConsequence } = useInteractive();
    const [xValue, setXValue] = useState(initialX);

    const yValue = useMemo(() => {
        if (mode === 'quadratic') {
            return slope * xValue * xValue + intercept;
        }
        return slope * xValue + intercept;
    }, [intercept, mode, slope, xValue]);

    const handleChange = (value: number) => {
        const clamped = clamp(value, xMin, xMax);
        setXValue(clamped);
        setVariable(xVar, clamped);
        setVariable(yVar, Number(yValue.toFixed(2)));
        recordDecision('graph_move', { x: clamped });
        recordConsequence('visual', { y: Number(yValue.toFixed(2)) });
    };

    React.useEffect(() => {
        setVariable(xVar, xValue);
        setVariable(yVar, Number(yValue.toFixed(2)));
    }, [setVariable, xValue, xVar, yValue, yVar]);

    const svgWidth = 240;
    const svgHeight = 160;
    const xScale = (xValue - xMin) / (xMax - xMin);
    const yNormalized = clamp((yValue - (xMin * slope + intercept)) / ((xMax * slope + intercept) - (xMin * slope + intercept)), 0, 1);

    return (
        <div
            data-interaction-type="graph_manipulator"
            data-component="GraphManipulator"
            className="my-4 p-4 bg-[var(--bg-panel)] rounded-lg border border-[var(--border-color)]"
        >
            <div className="text-sm font-medium text-[var(--accent-primary)] mb-2">{title}</div>
            <div className="flex flex-col md:flex-row gap-4 items-center">
                <div className="bg-[#0d0d10] border border-[var(--border-color)] rounded p-3">
                    <svg width={svgWidth} height={svgHeight} className="block">
                        <rect width={svgWidth} height={svgHeight} fill="#0d0d10" />
                        <line x1={20} y1={svgHeight - 20} x2={svgWidth - 10} y2={svgHeight - 20} stroke="#334155" />
                        <line x1={20} y1={10} x2={20} y2={svgHeight - 20} stroke="#334155" />
                        <circle
                            cx={20 + xScale * (svgWidth - 40)}
                            cy={10 + (1 - yNormalized) * (svgHeight - 40)}
                            r={6}
                            fill="#facc15"
                        />
                    </svg>
                </div>
                <div className="space-y-2 text-sm">
                    <div className="text-[var(--text-secondary)]">Drag with slider or keyboard</div>
                    <input
                        type="range"
                        min={xMin}
                        max={xMax}
                        value={xValue}
                        onChange={(e) => handleChange(Number(e.target.value))}
                        className="w-48 accent-[var(--accent-primary)]"
                    />
                    <div className="text-[var(--accent-warning)] font-mono">
                        x = {xValue}, y = {yValue.toFixed(2)}
                    </div>
                    <div className="text-xs text-[var(--text-secondary)]">
                        {mode === 'quadratic' ? `y = ${slope}x² + ${intercept}` : `y = ${slope}x + ${intercept}`}
                    </div>
                </div>
            </div>
        </div>
    );
};
