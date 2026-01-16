import React, { createContext, useContext, useState, type ReactNode } from 'react';

interface InteractiveContextType {
    variables: Record<string, any>;
    setVariable: (name: string, value: any) => void;
    resetVariables: () => void;
}

const InteractiveContext = createContext<InteractiveContextType | undefined>(undefined);

export const InteractiveProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
    const [variables, setVariables] = useState<Record<string, any>>({});

    const setVariable = (name: string, value: any) => {
        setVariables(prev => ({ ...prev, [name]: value }));
    };

    const resetVariables = () => {
        setVariables({});
    };

    return (
        <InteractiveContext.Provider value={{ variables, setVariable, resetVariables }}>
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
