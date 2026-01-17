import React from 'react';

interface OutputDiffProps {
    expected: string;
    actual: string;
    title?: string;
}

export const OutputDiff: React.FC<OutputDiffProps> = ({
    expected,
    actual,
    title = 'Output Comparison'
}) => {
    const isMatch = expected.trim() === actual.trim();

    return (
        <div data-interaction-type="output_diff" data-component="OutputDiff" className="my-4">
            <div className="text-xs text-[var(--text-secondary)] mb-2">{title}</div>
            <div className="grid grid-cols-2 gap-2">
                <div className="p-3 bg-[#0d0d10] rounded border border-[var(--border-color)]">
                    <div className="text-xs text-[var(--text-secondary)] mb-1">Expected</div>
                    <pre className="text-sm text-[var(--accent-success)] font-mono whitespace-pre-wrap">
                        {expected || '(empty)'}
                    </pre>
                </div>
                <div className={`p-3 rounded border ${isMatch
                        ? 'bg-[rgba(74,222,128,0.1)] border-[var(--accent-success)]'
                        : 'bg-[rgba(239,68,68,0.1)] border-[var(--accent-error)]'
                    }`}>
                    <div className="text-xs text-[var(--text-secondary)] mb-1 flex items-center gap-2">
                        Actual
                        {isMatch ? (
                            <span className="text-[var(--accent-success)]">✓ Match</span>
                        ) : (
                            <span className="text-[var(--accent-error)]">✗ Mismatch</span>
                        )}
                    </div>
                    <pre className={`text-sm font-mono whitespace-pre-wrap ${isMatch ? 'text-[var(--accent-success)]' : 'text-[var(--accent-error)]'
                        }`}>
                        {actual || '(empty)'}
                    </pre>
                </div>
            </div>
        </div>
    );
};
