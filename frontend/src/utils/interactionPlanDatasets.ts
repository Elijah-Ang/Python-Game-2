const DATASETS: Record<string, Record<string, any>[]> = {
    python_scores: [
        { name: 'alpha', score: 12, bonus: 3 },
        { name: 'beta', score: 18, bonus: 0 },
        { name: 'gamma', score: 24, bonus: 4 },
        { name: 'delta', score: 15, bonus: 2 }
    ],
    python_strings: [
        { word: 'data', length: 4 },
        { word: 'science', length: 7 },
        { word: 'python', length: 6 },
        { word: 'loop', length: 4 }
    ],
    sql_orders: [
        { order_id: 1201, customer: 'Avery', status: 'shipped', spend: 84.5 },
        { order_id: 1202, customer: 'Blake', status: 'processing', spend: 32.0 },
        { order_id: 1203, customer: 'Casey', status: 'shipped', spend: 140.0 },
        { order_id: 1204, customer: 'Drew', status: 'cancelled', spend: 0.0 },
        { order_id: 1205, customer: 'Emery', status: 'processing', spend: 64.2 }
    ],
    sql_employees: [
        { id: 1, name: 'Alice', department: 'Sales', salary: 75000 },
        { id: 2, name: 'Bob', department: 'Marketing', salary: 90000 },
        { id: 3, name: 'Charlie', department: 'Sales', salary: 72000 },
        { id: 4, name: 'Drew', department: 'Engineering', salary: 105000 }
    ],
    r_penguins: [
        { species: 'Adelie', island: 'Torgersen', bill_length: 38.9, body_mass: 3600 },
        { species: 'Chinstrap', island: 'Dream', bill_length: 46.5, body_mass: 4050 },
        { species: 'Gentoo', island: 'Biscoe', bill_length: 50.1, body_mass: 5000 },
        { species: 'Adelie', island: 'Dream', bill_length: 37.2, body_mass: 3400 }
    ],
    r_vectors: [
        { index: 1, value: 10 },
        { index: 2, value: 14 },
        { index: 3, value: 22 },
        { index: 4, value: 5 }
    ]
};

export const resolveInteractionDataset = (name?: string): Record<string, any>[] => {
    if (!name) return [];
    return DATASETS[name] ? [...DATASETS[name]] : [];
};
