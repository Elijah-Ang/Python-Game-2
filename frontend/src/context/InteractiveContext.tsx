import React, { createContext, useContext, useState, useCallback, type ReactNode } from 'react';

type TelemetryEventName =
    | 'decision_made'
    | 'consequence_shown'
    | 'prediction_correct'
    | 'hint_used'
    | 'reset_count'
    | 'time_to_complete';

interface TelemetryEvent {
    name: TelemetryEventName;
    timestamp: number;
    meta?: Record<string, any>;
}

interface InteractiveContextType {
    variables: Record<string, any>;
    setVariable: (name: string, value: any) => void;
    resetVariables: () => void;
    selectedValue: string | number | null;
    setSelectedValue: (value: string | number | null) => void;
    events: TelemetryEvent[];
    decisionCount: number;
    consequenceCount: number;
    recordEvent: (name: TelemetryEventName, meta?: Record<string, any>) => void;
    recordDecision: (type: string, meta?: Record<string, any>) => void;
    recordConsequence: (type: string, meta?: Record<string, any>) => void;
    resetInteractions: () => void;
}

const InteractiveContext = createContext<InteractiveContextType | undefined>(undefined);

export const InteractiveProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
    const [variables, setVariables] = useState<Record<string, any>>({});
    const [selectedValue, setSelectedValue] = useState<string | number | null>(null);
    const [events, setEvents] = useState<TelemetryEvent[]>([]);
    const [decisionCount, setDecisionCount] = useState(0);
    const [consequenceCount, setConsequenceCount] = useState(0);

    const setVariable = (name: string, value: any) => {
        setVariables(prev => ({ ...prev, [name]: value }));
    };

    const resetVariables = () => {
        setVariables({});
        setSelectedValue(null);
    };

    const recordEvent = useCallback((name: TelemetryEventName, meta?: Record<string, any>) => {
        const event = { name, timestamp: Date.now(), meta };
        setEvents(prev => [...prev, event]);
        if (name === 'decision_made') {
            setDecisionCount(prev => prev + 1);
        }
        if (name === 'consequence_shown') {
            setConsequenceCount(prev => prev + 1);
        }
        if (typeof window !== 'undefined') {
            // eslint-disable-next-line no-console
            console.log('[telemetry]', name, meta || {});
        }
    }, []);

    const recordDecision = useCallback((type: string, meta?: Record<string, any>) => {
        recordEvent('decision_made', { type, ...meta });
    }, [recordEvent]);

    const recordConsequence = useCallback((type: string, meta?: Record<string, any>) => {
        recordEvent('consequence_shown', { type, ...meta });
    }, [recordEvent]);

    const resetInteractions = () => {
        setEvents([]);
        setDecisionCount(0);
        setConsequenceCount(0);
    };

    return (
        <InteractiveContext.Provider
            value={{
                variables,
                setVariable,
                resetVariables,
                selectedValue,
                setSelectedValue,
                events,
                decisionCount,
                consequenceCount,
                recordEvent,
                recordDecision,
                recordConsequence,
                resetInteractions
            }}
        >
            {children}
        </InteractiveContext.Provider>
    );
};

export const useInteractive = () => {
    const context = useContext(InteractiveContext);
    if (!context) {
        throw new Error('useInteractive must be used within an InteractiveProvider');
    }
    return context;
};
