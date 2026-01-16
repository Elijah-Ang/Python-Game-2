export type InteractionPlanItem =
    | {
        type: 'prediction';
        question: string;
        options: string[];
        correctIndex: number;
        explanation?: string;
    }
    | {
        type: 'hint_ladder';
        hints: [string, string, string];
    }
    | {
        type: 'variable_slider';
        name: string;
        min: number | string;
        max: number | string;
        initial?: number | string;
        label?: string;
    }
    | {
        type: 'memory_box';
        names: string[];
        valueType?: string;
    }
    | {
        type: 'draggable_value';
        name: string;
        acceptedValues: (string | number)[];
        chips?: (string | number)[];
        label?: string;
        valueType?: string;
        initial?: string | number;
    }
    | {
        type: 'visual_table';
        columns: string[];
        data?: Record<string, any>[];
        dataRef?: string;
        title?: string;
        allowSort?: boolean;
        allowFilter?: boolean;
        allowReorder?: boolean;
        allowRowHighlight?: boolean;
        highlightColumn?: string;
    }
    | {
        type: 'live_code_block';
        initialCode: string;
        language?: string;
        highlightLine?: number;
        variableName?: string;
    }
    | {
        type: 'parsons_puzzle';
        correctOrder: string[];
        scrambledOrder?: string[];
    }
    | {
        type: 'fill_blanks';
        template: string;
        blanks: {
            id: string;
            options: string[];
            correct: string;
        }[];
    }
    | {
        type: 'step_executor';
        code: string;
        steps: {
            line: number;
            description: string;
            stateChanges?: Record<string, any>;
        }[];
    }
    | {
        type: 'output_diff';
        expected?: string;
        actual?: string;
        actualVar?: string;
        title?: string;
    }
    | {
        type: 'state_inspector';
        title?: string;
        showTypes?: boolean;
        filter?: string[];
    }
    | {
        type: 'reset_state';
        label?: string;
    }
    | {
        type: 'send_to_editor';
        template?: string;
        templateId?: string;
        label?: string;
    };

export type LessonInteractionPlan = InteractionPlanItem[];
