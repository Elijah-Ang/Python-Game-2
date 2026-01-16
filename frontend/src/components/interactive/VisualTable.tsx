import React, { useState } from 'react';

interface VisualTableProps {
    data: Record<string, any>[];
    columns: string[];
    title?: string;
    allowSort?: boolean;
    allowFilter?: boolean;
    highlightColumn?: string;
}

export const VisualTable: React.FC<VisualTableProps> = ({
    data,
    columns,
    title,
    allowSort = true,
    allowFilter = false,
    highlightColumn
}) => {
    const [sortColumn, setSortColumn] = useState<string | null>(null);
    const [sortAsc, setSortAsc] = useState(true);
    const [visibleColumns, setVisibleColumns] = useState<Set<string>>(new Set(columns));
    const [filterValue, setFilterValue] = useState('');

    const handleSort = (col: string) => {
        if (!allowSort) return;
        if (sortColumn === col) {
            setSortAsc(!sortAsc);
        } else {
            setSortColumn(col);
            setSortAsc(true);
        }
    };

    const toggleColumn = (col: string) => {
        const newVisible = new Set(visibleColumns);
        if (newVisible.has(col)) {
            if (newVisible.size > 1) newVisible.delete(col);
        } else {
            newVisible.add(col);
        }
        setVisibleColumns(newVisible);
    };

    let displayData = [...data];

    // Apply filter
    if (filterValue) {
        displayData = displayData.filter(row =>
            Object.values(row).some(v =>
                String(v).toLowerCase().includes(filterValue.toLowerCase())
            )
        );
    }

    // Apply sort
    if (sortColumn) {
        displayData.sort((a, b) => {
            const aVal = a[sortColumn];
            const bVal = b[sortColumn];
            const cmp = aVal < bVal ? -1 : aVal > bVal ? 1 : 0;
            return sortAsc ? cmp : -cmp;
        });
    }

    const visibleCols = columns.filter(c => visibleColumns.has(c));

    return (
        <div className="my-4">
            {title && <div className="text-sm font-medium text-[var(--accent-secondary)] mb-2">{title}</div>}

            {/* Column toggles */}
            <div className="flex flex-wrap gap-2 mb-2">
                {columns.map(col => (
                    <button
                        key={col}
                        onClick={() => toggleColumn(col)}
                        className={`
                            px-2 py-0.5 text-xs rounded transition-all
                            ${visibleColumns.has(col)
                                ? 'bg-[var(--accent-secondary)] text-black'
                                : 'bg-[var(--bg-panel)] text-[var(--text-secondary)]'}
                        `}
                    >
                        {col}
                    </button>
                ))}
            </div>

            {/* Filter */}
            {allowFilter && (
                <input
                    type="text"
                    placeholder="Filter rows..."
                    value={filterValue}
                    onChange={(e) => setFilterValue(e.target.value)}
                    className="w-full mb-2 px-2 py-1 text-sm bg-[var(--bg-panel)] border border-[var(--border-color)] rounded text-white"
                />
            )}

            {/* Table */}
            <div className="overflow-x-auto">
                <table className="w-full border-collapse text-sm">
                    <thead>
                        <tr>
                            {visibleCols.map(col => (
                                <th
                                    key={col}
                                    onClick={() => handleSort(col)}
                                    className={`
                                        border border-[var(--border-color)] px-2 py-1 text-left
                                        ${allowSort ? 'cursor-pointer hover:bg-[var(--bg-panel)]' : ''}
                                        ${col === highlightColumn ? 'bg-[rgba(var(--accent-warning-rgb),0.2)]' : 'bg-[var(--bg-panel)]'}
                                    `}
                                >
                                    {col}
                                    {sortColumn === col && (
                                        <span className="ml-1">{sortAsc ? '↑' : '↓'}</span>
                                    )}
                                </th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {displayData.map((row, idx) => (
                            <tr key={idx} className="hover:bg-[rgba(255,255,255,0.02)]">
                                {visibleCols.map(col => (
                                    <td
                                        key={col}
                                        className={`
                                            border border-[var(--border-color)] px-2 py-1
                                            ${col === highlightColumn ? 'bg-[rgba(var(--accent-warning-rgb),0.1)]' : ''}
                                        `}
                                    >
                                        {String(row[col])}
                                    </td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <div className="text-xs text-[var(--text-secondary)] mt-1">
                Showing {displayData.length} of {data.length} rows
            </div>
        </div>
    );
};
