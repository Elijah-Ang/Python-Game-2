export type CurriculumMode = 'python' | 'sql' | 'r';

interface Metric {
    label: string;
    value: number;
    max?: number;
    accent?: 'primary' | 'secondary' | 'warning' | 'success';
}

interface SliderConfig {
    label: string;
    min: number;
    max: number;
    initial: number;
    helper?: string;
}

interface FilterConfig {
    label: string;
    name: string;
    defaultValue: string | number;
    chips: (string | number)[];
    helper?: string;
}

interface TableConfig {
    columns: string[];
    rows: Record<string, any>[];
    allowFilter?: boolean;
    highlightColumn?: string;
    filterKey?: string | ((row: Record<string, any>, value: string | number) => boolean);
}

interface LiveCodeConfig {
    initial: string;
    language: 'python' | 'sql' | 'r';
    highlightLine?: number;
    note?: string;
}

interface PredictionConfig {
    question: string;
    options: string[];
    correctIndex: number;
    explanation: string;
}

interface StepConfig {
    code: string;
    steps: {
        line: number;
        description: string;
        stateChanges?: Record<string, any>;
    }[];
}

export interface InteractionBlueprint {
    label: string;
    slider: SliderConfig;
    filter: FilterConfig;
    table: TableConfig;
    liveCode: LiveCodeConfig;
    puzzle: string[];
    prediction: PredictionConfig;
    steps: StepConfig;
    buildOutcome: (rows: Record<string, any>[], filterValue: string | number, loopBound: number) => string;
    buildCode: (loopBound: number, filterValue: string | number) => string;
    metrics?: (rows: Record<string, any>[], filterValue: string | number, loopBound: number) => Metric[];
}

const pythonRows = [
    { task: 'Sensor warmup', points: 24, mistakes: 1, speed: 'slow' },
    { task: 'Mini-quiz', points: 36, mistakes: 0, speed: 'fast' },
    { task: 'Refactor loop', points: 44, mistakes: 2, speed: 'medium' },
    { task: 'Plot check', points: 58, mistakes: 1, speed: 'fast' },
    { task: 'Data clean', points: 33, mistakes: 2, speed: 'medium' },
    { task: 'Debug script', points: 47, mistakes: 3, speed: 'slow' }
];

const simulatePythonScore = (rows: typeof pythonRows, loopBound: number): number => {
    if (rows.length === 0) return 0;
    let total = 0;
    for (let i = 0; i < loopBound; i++) {
        const row = rows[i % rows.length];
        total += row.points - row.mistakes * 2 + i;
    }
    return total;
};

const sqlRows = [
    { order: 501, city: 'Austin', status: 'shipped', spend: 120.5, items: 3 },
    { order: 502, city: 'Denver', status: 'processing', spend: 88.2, items: 2 },
    { order: 503, city: 'Austin', status: 'cancelled', spend: 0, items: 0 },
    { order: 504, city: 'Seattle', status: 'shipped', spend: 142.0, items: 4 },
    { order: 505, city: 'Miami', status: 'processing', spend: 64.0, items: 1 },
    { order: 506, city: 'Seattle', status: 'shipped', spend: 220.0, items: 5 },
    { order: 507, city: 'Chicago', status: 'processing', spend: 71.0, items: 2 }
];

const rRows = [
    { id: 1, species: 'Adelie', island: 'Torgersen', bill_length: 38.9, body_mass: 3600 },
    { id: 2, species: 'Chinstrap', island: 'Dream', bill_length: 46.5, body_mass: 4050 },
    { id: 3, species: 'Gentoo', island: 'Biscoe', bill_length: 50.1, body_mass: 5000 },
    { id: 4, species: 'Adelie', island: 'Dream', bill_length: 37.2, body_mass: 3400 },
    { id: 5, species: 'Gentoo', island: 'Biscoe', bill_length: 48.8, body_mass: 4800 },
    { id: 6, species: 'Chinstrap', island: 'Dream', bill_length: 42.0, body_mass: 3900 }
];

export const INTERACTION_BLUEPRINTS: Record<CurriculumMode, InteractionBlueprint> = {
    python: {
        label: 'Python sandbox',
        slider: {
            label: 'Loop bound & preview size',
            min: 2,
            max: 7,
            initial: 4,
            helper: 'Slide to change how many passes your loop makes.'
        },
        filter: {
            label: 'Minimum points to keep a task',
            name: 'python-filter',
            defaultValue: 35,
            chips: [25, 35, 45, 55],
            helper: 'Drag a value to change which rows survive.'
        },
        table: {
            columns: ['task', 'points', 'mistakes', 'speed'],
            rows: pythonRows,
            allowFilter: true,
            highlightColumn: 'points',
            filterKey: 'points'
        },
        liveCode: {
            initial: [
                'scores = [24, 36, 44, 58, 33, 47]',
                'minimum = 35  # drag to change',
                'trimmed = []',
                '',
                'for score in scores:',
                '    if score >= minimum:',
                '        trimmed.append(score)',
                '',
                'total = 0',
                'for step in range(4):',
                '    total += trimmed[step % len(trimmed)]',
                'print(total)'
            ].join('\n'),
            language: 'python',
            highlightLine: 10,
            note: 'Tweak the loop bound line and re-run.'
        },
        puzzle: [
            'values = [2, 4, 6]',
            'total = 0',
            'for value in values:',
            '    total += value',
            'print(total)'
        ],
        prediction: {
            question: 'Drag minimum to 45 and set the loop bound to 5. How many tasks stay in play?',
            options: ['All 6 tasks loop', '2 tasks remain and repeat', 'Nothing runs because the filter is empty'],
            correctIndex: 1,
            explanation: 'Only scores 58 and 47 are >= 45, so they repeat through the five-step loop.'
        },
        steps: {
            code: [
                'scores = [24, 36, 44, 58]',
                'filtered = []',
                'for score in scores:',
                '    if score >= 35:',
                '        filtered.append(score)',
                'total = sum(filtered)',
                'print(total)'
            ].join('\n'),
            steps: [
                { line: 1, description: 'Prepare a small list of scores', stateChanges: { py_scores: [24, 36, 44, 58] } },
                { line: 2, description: 'Start with an empty bucket', stateChanges: { py_filtered: [] } },
                { line: 3, description: 'Walk the list', stateChanges: { py_iterating: true } },
                { line: 4, description: 'Keep only scores >= 35', stateChanges: { py_filtered: [36, 44, 58] } },
                { line: 6, description: 'Sum the kept values', stateChanges: { py_total: 138 } }
            ]
        },
        buildOutcome: (rows, filterValue, loopBound) => {
            if (rows.length === 0) {
                return `No tasks meet the ${filterValue}+ threshold. Lower the drag value or widen the loop.`;
            }
            const total = simulatePythonScore(rows as typeof pythonRows, loopBound);
            return `Loop x${loopBound} with min ${filterValue}: ${rows.length} tasks keep running, projected score ${total}.`;
        },
        buildCode: (loopBound, filterValue) => {
            return [
                'tasks = [24, 36, 44, 58, 33, 47]',
                `minimum = ${filterValue}`,
                'kept = []',
                '',
                'for task in tasks:',
                '    if task >= minimum:',
                '        kept.append(task)',
                '    if len(kept) == 0:',
                '        break',
                '',
                `score = 0`,
                `for step in range(${loopBound}):`,
                '    score += kept[step % len(kept)]',
                'print(score)'
            ].join('\n');
        },
        metrics: (rows, _filterValue, loopBound) => {
            const total = simulatePythonScore(rows as typeof pythonRows, loopBound);
            return [
                { label: 'Loop count', value: loopBound, max: 7, accent: 'secondary' },
                { label: 'Tasks kept', value: rows.length, max: pythonRows.length, accent: 'warning' },
                { label: 'Sim score', value: total, max: 400, accent: 'primary' }
            ];
        }
    },
    sql: {
        label: 'SQL sand table',
        slider: {
            label: 'LIMIT (rows surfaced)',
            min: 2,
            max: 6,
            initial: 4,
            helper: 'Slide to preview more or fewer rows.'
        },
        filter: {
            label: 'Order status to focus',
            name: 'sql-filter',
            defaultValue: 'shipped',
            chips: ['shipped', 'processing', 'cancelled'],
            helper: 'Drag a status chip into the drop zone.'
        },
        table: {
            columns: ['order', 'city', 'status', 'spend', 'items'],
            rows: sqlRows,
            allowFilter: true,
            highlightColumn: 'spend',
            filterKey: 'status'
        },
        liveCode: {
            initial: [
                'SELECT city, spend, status',
                'FROM orders',
                "WHERE status = 'shipped'",
                'ORDER BY spend DESC',
                'LIMIT 4;'
            ].join('\n'),
            language: 'sql',
            highlightLine: 3,
            note: 'Edit the WHERE or LIMIT line, then submit below.'
        },
        puzzle: [
            'SELECT city, spend',
            'FROM orders',
            "WHERE status = 'shipped'",
            'ORDER BY spend DESC',
            'LIMIT 3;'
        ],
        prediction: {
            question: 'Drag status to processing and set LIMIT to 2. Which city shows up first?',
            options: ['Austin', 'Denver', 'Chicago'],
            correctIndex: 1,
            explanation: 'Denver has the highest spend among the first two processing orders.'
        },
        steps: {
            code: [
                'WITH filtered AS (',
                "  SELECT city, spend, status FROM orders WHERE status = 'shipped'",
                ')',
                'SELECT city, SUM(spend) AS total',
                'FROM filtered',
                'GROUP BY city',
                'ORDER BY total DESC;'
            ].join('\n'),
            steps: [
                { line: 1, description: 'Create a staging set for the chosen status', stateChanges: { sql_stage: 'status filtered' } },
                { line: 4, description: 'Aggregate spend per city', stateChanges: { sql_agg: 'city totals ready' } },
                { line: 6, description: 'Sort highest to lowest spend', stateChanges: { sql_sorted: true } }
            ]
        },
        buildOutcome: (rows, filterValue, loopBound) => {
            if (rows.length === 0) {
                return `No ${filterValue} orders visible. Try a different status or widen LIMIT ${loopBound}.`;
            }
            const totalSpend = rows.reduce((sum, r) => sum + Number(r.spend || 0), 0);
            const avgItems = rows.length ? rows.reduce((sum, r) => sum + Number(r.items || 0), 0) / rows.length : 0;
            const citySpread = new Set(rows.map(r => r.city)).size;
            return `Previewing ${rows.length} ${filterValue} orders • $${totalSpend.toFixed(2)} total • ${avgItems.toFixed(1)} avg items • ${citySpread} cities.`;
        },
        buildCode: (loopBound, filterValue) => {
            return [
                'SELECT city, spend, status',
                'FROM orders',
                `WHERE status = '${filterValue}'`,
                'ORDER BY spend DESC',
                `LIMIT ${loopBound};`
            ].join('\n');
        },
        metrics: (rows, _filterValue, loopBound) => {
            const spend = rows.reduce((sum, r) => sum + Number(r.spend || 0), 0);
            return [
                { label: 'LIMIT', value: loopBound, max: 6, accent: 'secondary' },
                { label: 'Rows kept', value: rows.length, max: sqlRows.length, accent: 'warning' },
                { label: 'Spend total', value: Number(spend.toFixed(2)), max: 600, accent: 'primary' }
            ];
        }
    },
    r: {
        label: 'R sketch pad',
        slider: {
            label: 'Sample size (head)',
            min: 3,
            max: 7,
            initial: 4,
            helper: 'Slide to change how many rows you sample.'
        },
        filter: {
            label: 'Minimum body mass (g)',
            name: 'r-filter',
            defaultValue: 3600,
            chips: [3400, 3800, 4200, 4600],
            helper: 'Drag a mass threshold to see penguins drop or stay.'
        },
        table: {
            columns: ['species', 'island', 'bill_length', 'body_mass'],
            rows: rRows,
            allowFilter: true,
            highlightColumn: 'body_mass',
            filterKey: 'body_mass'
        },
        liveCode: {
            initial: [
                'penguins <- data.frame(',
                '  species = c("Adelie","Chinstrap","Gentoo","Adelie"),',
                '  body_mass = c(3600, 3800, 5000, 3450)',
                ')',
                '',
                'threshold <- 3600',
                'sampled <- head(penguins[penguins$body_mass >= threshold, ], 4)',
                'mean(sampled$body_mass)'
            ].join('\n'),
            language: 'r',
            highlightLine: 7,
            note: 'Nudge the threshold line to see downstream changes.'
        },
        puzzle: [
            'penguins <- read.csv("data.csv")',
            'filtered <- subset(penguins, body_mass >= 3600)',
            'head(filtered, 3)',
            'mean(filtered$body_mass)'
        ],
        prediction: {
            question: 'If the threshold is 4200 and sample size is 3, what happens to the average mass?',
            options: ['It increases', 'It decreases', 'It stays identical'],
            correctIndex: 0,
            explanation: 'Dropping lighter birds pushes the mean up.'
        },
        steps: {
            code: [
                'penguins <- data.frame(body_mass = c(3600, 4050, 5000, 3400))',
                'heavy <- penguins[penguins$body_mass >= 3600, ]',
                'preview <- head(heavy, 2)',
                'mean(preview$body_mass)'
            ].join('\n'),
            steps: [
                { line: 1, description: 'Load a small penguin sample', stateChanges: { r_rows: [3600, 4050, 5000, 3400] } },
                { line: 2, description: 'Filter by mass', stateChanges: { r_filtered: [3600, 4050, 5000] } },
                { line: 3, description: 'Take the head() slice', stateChanges: { r_preview: [3600, 4050] } },
                { line: 4, description: 'Calculate the mean', stateChanges: { r_mean: 3825 } }
            ]
        },
        buildOutcome: (rows, filterValue, loopBound) => {
            if (rows.length === 0) {
                return `No penguins above ${filterValue}g. Lower the drag value or widen the sample.`;
            }
            const masses = rows.map(r => Number(r.body_mass || 0));
            const meanMass = masses.reduce((sum, m) => sum + m, 0) / masses.length;
            const median = masses.slice().sort((a, b) => a - b)[Math.floor(masses.length / 2)];
            return `Sampling ${Math.min(loopBound, rows.length)} rows ≥ ${filterValue}g → mean ${meanMass.toFixed(1)}g, median ${median}g.`;
        },
        buildCode: (loopBound, filterValue) => {
            return [
                'penguins <- data.frame(',
                '  species = c("Adelie","Chinstrap","Gentoo","Adelie","Gentoo","Chinstrap"),',
                '  body_mass = c(3600, 4050, 5000, 3400, 4800, 3900)',
                ')',
                `filtered <- penguins[penguins$body_mass >= ${filterValue}, ]`,
                `head(filtered, ${loopBound})`,
                'mean(filtered$body_mass)'
            ].join('\n');
        },
        metrics: (rows, _filterValue, loopBound) => {
            const masses = rows.map(r => Number(r.body_mass || 0));
            const meanMass = masses.length ? masses.reduce((sum, m) => sum + m, 0) / masses.length : 0;
            return [
                { label: 'Sample size', value: loopBound, max: 7, accent: 'secondary' },
                { label: 'Rows kept', value: rows.length, max: rRows.length, accent: 'warning' },
                { label: 'Mean mass', value: Number(meanMass.toFixed(1)), max: 5200, accent: 'primary' }
            ];
        }
    }
};
