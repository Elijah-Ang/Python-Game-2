import React, { useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';
import { VisualTable } from './VisualTable';

interface DataTransformFilter {
    id: string;
    label: string;
    rows: Record<string, any>[];
}

interface DataTransformAnimatorProps {
    title?: string;
    columns: string[];
    beforeRows: Record<string, any>[];
    filters: DataTransformFilter[];
    resultVar?: string;
}

export const DataTransformAnimator: React.FC<DataTransformAnimatorProps> = ({
    title = 'Transform the data',
    columns,
    beforeRows,
    filters,
    resultVar = 'rows_kept'
}) => {
    const { setVariable, recordDecision, recordConsequence } = useInteractive();
    const [activeFilter, setActiveFilter] = useState(filters[0]);

    React.useEffect(() => {
        if (filters[0]) {
            setVariable(resultVar, filters[0].rows.length);
        }
    }, [filters, resultVar, setVariable]);

    const handleFilterSelect = (filter: DataTransformFilter) => {
        setActiveFilter(filter);
        setVariable(resultVar, filter.rows.length);
        recordDecision('filter_select', { filter: filter.id });
        recordConsequence('table', { rows: filter.rows.length });
    };

    return (
        <div
            data-interaction-type="data_transform"
            data-component="DataTransformAnimator"
            className="my-4 p-4 bg-[var(--bg-panel)] rounded-lg border border-[var(--border-color)]"
        >
            <div className="text-sm font-medium text-[var(--accent-primary)] mb-2">{title}</div>
            <div className="flex flex-wrap gap-2 mb-3">
                {filters.map(filter => {
                    const isActive = activeFilter.id === filter.id;
                    return (
                        <button
                            key={filter.id}
                            onClick={() => handleFilterSelect(filter)}
                            className={`
                                px-3 py-1 rounded text-sm border transition-all
                                ${isActive
                                    ? 'bg-[var(--accent-secondary)] text-black border-[var(--accent-secondary)]'
                                    : 'bg-[#0d0d10] text-[var(--text-primary)] border-[var(--border-color)] hover:border-[var(--accent-primary)]'}
                            `}
                        >
                            {filter.label}
                        </button>
                    );
                })}
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div className="p-2 rounded border border-[var(--border-color)] bg-[#0d0d10]">
                    <div className="text-xs text-[var(--text-secondary)] mb-2">Before</div>
                    <VisualTable
                        data={beforeRows}
                        columns={columns}
                        allowSort={false}
                        allowFilter={false}
                        allowRowHighlight
                    />
                </div>
                <div className="p-2 rounded border border-[var(--border-color)] bg-[#0d0d10] animate-[pulse_1.2s_ease-in-out]">
                    <div className="text-xs text-[var(--text-secondary)] mb-2">
                        After ({activeFilter.rows.length} rows)
                    </div>
                    <VisualTable
                        data={activeFilter.rows}
                        columns={columns}
                        allowSort={false}
                        allowFilter={false}
                        allowRowHighlight
                    />
                </div>
            </div>
        </div>
    );
};
