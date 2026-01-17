import React, { useMemo, useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';
import { VisualTable } from './VisualTable';

interface JoinVisualizerProps {
    leftTitle?: string;
    rightTitle?: string;
    leftRows: Record<string, any>[];
    rightRows: Record<string, any>[];
    leftKey: string;
    rightKey: string;
    joinTypes: string[];
    resultVar?: string;
    joinVar?: string;
}

const joinData = (
    leftRows: Record<string, any>[],
    rightRows: Record<string, any>[],
    leftKey: string,
    rightKey: string,
    joinType: string
) => {
    const rightIndex = new Map(rightRows.map(row => [row[rightKey], row]));
    const results: Record<string, any>[] = [];

    leftRows.forEach((left) => {
        const match = rightIndex.get(left[leftKey]);
        if (match) {
            results.push({ ...left, ...match });
        } else if (joinType === 'LEFT JOIN') {
            results.push({ ...left });
        }
    });

    if (joinType === 'RIGHT JOIN') {
        const leftIndex = new Map(leftRows.map(row => [row[leftKey], row]));
        rightRows.forEach((right) => {
            const match = leftIndex.get(right[rightKey]);
            if (match) {
                if (!results.find(row => row[leftKey] === right[rightKey])) {
                    results.push({ ...match, ...right });
                }
            } else {
                results.push({ ...right });
            }
        });
    }

    return results;
};

export const JoinVisualizer: React.FC<JoinVisualizerProps> = ({
    leftTitle = 'Left table',
    rightTitle = 'Right table',
    leftRows,
    rightRows,
    leftKey,
    rightKey,
    joinTypes,
    resultVar = 'join_rows',
    joinVar = 'join_type'
}) => {
    const { setVariable, recordDecision, recordConsequence } = useInteractive();
    const [joinType, setJoinType] = useState(joinTypes[0]);

    const resultRows = useMemo(() => joinData(leftRows, rightRows, leftKey, rightKey, joinType), [
        joinType,
        leftRows,
        leftKey,
        rightRows,
        rightKey
    ]);

    const handleSelect = (type: string) => {
        setJoinType(type);
        setVariable(joinVar, type);
        setVariable(resultVar, resultRows.length);
        recordDecision('join_select', { joinType: type });
        recordConsequence('table', { rows: resultRows.length });
    };

    React.useEffect(() => {
        setVariable(joinVar, joinType);
        setVariable(resultVar, resultRows.length);
    }, [joinType, joinVar, resultRows.length, resultVar, setVariable]);

    const outputColumns = useMemo(() => {
        const columns = new Set<string>();
        leftRows.forEach(row => Object.keys(row).forEach(key => columns.add(key)));
        rightRows.forEach(row => Object.keys(row).forEach(key => columns.add(key)));
        return Array.from(columns);
    }, [leftRows, rightRows]);

    return (
        <div
            data-interaction-type="join_visualizer"
            data-component="JoinVisualizer"
            className="my-4 p-4 bg-[var(--bg-panel)] rounded-lg border border-[var(--border-color)]"
        >
            <div className="text-sm font-medium text-[var(--accent-primary)] mb-3">Join visualizer</div>
            <div className="flex flex-wrap gap-2 mb-4">
                {joinTypes.map((type) => (
                    <button
                        key={type}
                        onClick={() => handleSelect(type)}
                        className={`
                            px-3 py-1 rounded text-sm border transition-all
                            ${joinType === type
                                ? 'bg-[var(--accent-secondary)] text-black border-[var(--accent-secondary)]'
                                : 'bg-[#0d0d10] text-[var(--text-primary)] border-[var(--border-color)] hover:border-[var(--accent-primary)]'}
                        `}
                    >
                        {type}
                    </button>
                ))}
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                <div className="p-2 rounded border border-[var(--border-color)] bg-[#0d0d10]">
                    <div className="text-xs text-[var(--text-secondary)] mb-2">{leftTitle}</div>
                    <VisualTable
                        data={leftRows}
                        columns={Object.keys(leftRows[0] || {})}
                        allowSort={false}
                        allowFilter={false}
                    />
                </div>
                <div className="p-2 rounded border border-[var(--border-color)] bg-[#0d0d10]">
                    <div className="text-xs text-[var(--text-secondary)] mb-2">{rightTitle}</div>
                    <VisualTable
                        data={rightRows}
                        columns={Object.keys(rightRows[0] || {})}
                        allowSort={false}
                        allowFilter={false}
                    />
                </div>
                <div className="p-2 rounded border border-[var(--border-color)] bg-[#0d0d10]">
                    <div className="text-xs text-[var(--text-secondary)] mb-2">Result ({resultRows.length} rows)</div>
                    <VisualTable
                        data={resultRows}
                        columns={outputColumns}
                        allowSort={false}
                        allowFilter={false}
                    />
                </div>
            </div>
        </div>
    );
};
