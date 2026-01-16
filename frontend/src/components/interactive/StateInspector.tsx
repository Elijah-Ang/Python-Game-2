import React from 'react';
import { useInteractive } from '../../context/InteractiveContext';

interface StateInspectorProps {
    title?: string;
    showTypes?: boolean;
    filter?: string[]; // Only show these variable names
}

export const StateInspector: React.FC<StateInspectorProps> = ({
    title = 'Environment',
    showTypes = true,
    filter
}) => {
    const { variables } = useInteractive();

    const displayVars = filter
        ? Object.entries(variables).filter(([k]) => filter.includes(k))
        : Object.entries(variables);

    if (displayVars.length === 0) {
        return (
            <div className="my-4 p-4 bg-[#1a1a2e] rounded-lg border border-[var(--border-color)]">
                <div className="text-xs text-[var(--text-secondary)] mb-2">{title}</div>
                <div className="text-sm text-[var(--text-secondary)] italic">No variables yet</div>
            </div>
        );
    }

    const getTypeColor = (value: any): string => {
        const type = typeof value;
        switch (type) {
            case 'number': return 'text-[var(--accent-secondary)]';
            case 'string': return 'text-[var(--accent-warning)]';
            case 'boolean': return 'text-[var(--accent-primary)]';
            default: return 'text-[var(--text-secondary)]';
        }
    };

    const getTypeLabel = (value: any): string => {
        if (Array.isArray(value)) return 'list';
        if (value === null) return 'null';
        return typeof value;
    };

    return (
        <div className="my-4 p-4 bg-[#1a1a2e] rounded-lg border border-[var(--border-color)]">
            <div className="text-xs text-[var(--text-secondary)] mb-3 flex items-center gap-2">
                📋 {title}
            </div>
            <div className="font-mono text-sm space-y-2">
                {displayVars.map(([name, value]) => (
                    <div key={name} className="flex items-center gap-3 p-2 bg-[#0d0d10] rounded">
                        <span className="text-[var(--accent-primary)] min-w-[80px]">{name}</span>
                        <span className="text-[var(--border-color)]">=</span>
                        <span className={getTypeColor(value)}>
                            {JSON.stringify(value)}
                        </span>
                        {showTypes && (
                            <span className="ml-auto text-xs text-[var(--text-secondary)] bg-[var(--bg-panel)] px-2 py-0.5 rounded">
                                {getTypeLabel(value)}
                            </span>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
};
