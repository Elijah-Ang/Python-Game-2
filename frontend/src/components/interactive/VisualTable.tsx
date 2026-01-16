import React, { useEffect, useState } from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface VisualTableProps {
    data: Record<string, any>[];
    columns: string[];
    title?: string;
    allowSort?: boolean;
    allowFilter?: boolean;
    highlightColumn?: string;
    allowReorder?: boolean;
    allowRowHighlight?: boolean;
    onRowHighlight?: (row: Record<string, any> | null) => void;
}

export const VisualTable: React.FC<VisualTableProps> = ({
    data,
    columns,
    title,
    allowSort = true,
    allowFilter = false,
    highlightColumn,
    allowReorder = false,
    allowRowHighlight = false,
    onRowHighlight
}) => {
    const { recordDecision, recordConsequence } = useInteractive();
    const [sortColumn, setSortColumn] = useState<string | null>(null);
    const [sortAsc, setSortAsc] = useState(true);
    const [visibleColumns, setVisibleColumns] = useState<Set<string>>(new Set(columns));
    const [filterValue, setFilterValue] = useState('');
    const [columnOrder, setColumnOrder] = useState<string[]>(columns);
    const [draggedColumn, setDraggedColumn] = useState<string | null>(null);
    const [highlightedRow, setHighlightedRow] = useState<number | null>(null);

    useEffect(() => {
        setColumnOrder(columns);
        setVisibleColumns(new Set(columns));
        setHighlightedRow(null);
    }, [columns]);

    const handleSort = (col: string) => {
        if (!allowSort) return;
        if (sortColumn === col) {
            setSortAsc(!sortAsc);
        } else {
            setSortColumn(col);
            setSortAsc(true);
        }
        recordDecision('sort', { column: col });
        recordConsequence('table', { column: col });
    };

    const toggleColumn = (col: string) => {
        const newVisible = new Set(visibleColumns);
        if (newVisible.has(col)) {
            if (newVisible.size > 1) newVisible.delete(col);
        } else {
            newVisible.add(col);
        }
        setVisibleColumns(newVisible);
        recordDecision('toggle_column', { column: col });
        recordConsequence('table', { column: col });
    };

    const handleColumnDragStart = (col: string) => {
        if (!allowReorder) return;
        setDraggedColumn(col);
        recordDecision('reorder_start', { column: col });
    };

    const handleColumnDragEnter = (targetCol: string) => {
        if (!allowReorder || !draggedColumn || draggedColumn === targetCol) return;
        const currentIdx = columnOrder.indexOf(draggedColumn);
        const targetIdx = columnOrder.indexOf(targetCol);
        if (currentIdx === -1 || targetIdx === -1) return;

        const newOrder = [...columnOrder];
        newOrder.splice(currentIdx, 1);
        newOrder.splice(targetIdx, 0, draggedColumn);
        setColumnOrder(newOrder);
        recordConsequence('table', { order: newOrder });
    };

    const handleColumnDragEnd = () => {
        setDraggedColumn(null);
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

    const handleRowHighlight = (idx: number) => {
        if (!allowRowHighlight) return;
        const newIdx = highlightedRow === idx ? null : idx;
        setHighlightedRow(newIdx);
        onRowHighlight?.(newIdx === null ? null : displayData[idx]);
        recordDecision('row_highlight', { rowIndex: idx });
        recordConsequence('table', { rowIndex: idx });
    };

    const visibleCols = columnOrder.filter(c => visibleColumns.has(c));

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

            {allowReorder && (
                <div className="flex flex-wrap items-center gap-2 mb-2 text-xs text-[var(--text-secondary)]">
                    <span className="uppercase tracking-wide">Drag to reorder:</span>
                    {columnOrder.map(col => (
                        <span
                            key={col}
                            draggable
                            onDragStart={() => handleColumnDragStart(col)}
                            onDragEnter={() => handleColumnDragEnter(col)}
                            onDragEnd={handleColumnDragEnd}
                            onDragOver={(e) => e.preventDefault()}
                            className={`
                                px-2 py-1 rounded border text-[var(--text-primary)] transition-all cursor-grab active:cursor-grabbing
                                ${draggedColumn === col ? 'border-[var(--accent-secondary)] bg-[rgba(var(--accent-secondary-rgb),0.2)]' : 'border-[var(--border-color)] bg-[var(--bg-panel)]'}
                            `}
                        >
                            {col}
                        </span>
                    ))}
                </div>
            )}

            {/* Filter */}
            {allowFilter && (
                <input
                    type="text"
                    placeholder="Filter rows..."
                    value={filterValue}
                    onChange={(e) => {
                        const nextValue = e.target.value;
                        setFilterValue(nextValue);
                        recordDecision('filter', { value: nextValue });
                        recordConsequence('table', { filter: nextValue });
                    }}
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
                            <tr
                                key={idx}
                                onClick={() => handleRowHighlight(idx)}
                                className={`
                                    hover:bg-[rgba(255,255,255,0.02)]
                                    ${allowRowHighlight ? 'cursor-pointer' : ''}
                                    ${allowRowHighlight && highlightedRow === idx
                                        ? 'bg-[rgba(var(--accent-secondary-rgb),0.12)] border border-[var(--accent-secondary)]'
                                        : ''}
                                `}
                            >
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
