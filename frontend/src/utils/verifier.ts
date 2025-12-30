// Verification logic for code exercises
// This runs entirely in the browser - no server needed!

interface VerifyResult {
    correct: boolean;
    feedback: string;
    suggestions: string[];
    expectedVsActual?: { expected: string; actual: string };
}

// ============ SQL VERIFICATION ============

// Normalize SQL query for comparison
function normalizeSql(sql: string): string {
    return sql
        // Remove comments
        .replace(/--.*$/gm, '')
        .replace(/\/\*[\s\S]*?\*\//g, '')
        // Normalize whitespace
        .replace(/\s+/g, ' ')
        .trim()
        // Remove trailing semicolons
        .replace(/;+$/, '')
        // Lowercase for comparison (SQL keywords are case-insensitive)
        .toLowerCase()
        // Normalize quotes
        .replace(/"/g, "'");
}

// Extract SQL keywords and structure
function extractSqlStructure(sql: string): {
    hasSelect: boolean;
    columns: string[];
    hasFrom: boolean;
    tables: string[];
    hasWhere: boolean;
    hasJoin: boolean;
    hasGroupBy: boolean;
    hasOrderBy: boolean;
} {
    const normalized = normalizeSql(sql);

    return {
        hasSelect: /\bselect\b/i.test(sql),
        columns: extractBetween(normalized, 'select', 'from').split(',').map(c => c.trim()).filter(Boolean),
        hasFrom: /\bfrom\b/i.test(sql),
        tables: extractAfter(normalized, 'from').split(/\bjoin\b|\bwhere\b|\bgroup by\b|\border by\b|\blimit\b/)[0]?.split(',').map(t => t.trim()).filter(Boolean) || [],
        hasWhere: /\bwhere\b/i.test(sql),
        hasJoin: /\bjoin\b/i.test(sql),
        hasGroupBy: /\bgroup\s+by\b/i.test(sql),
        hasOrderBy: /\border\s+by\b/i.test(sql),
    };
}

function extractBetween(str: string, start: string, end: string): string {
    const startIdx = str.indexOf(start);
    const endIdx = str.indexOf(end);
    if (startIdx === -1 || endIdx === -1) return '';
    return str.slice(startIdx + start.length, endIdx).trim();
}

function extractAfter(str: string, keyword: string): string {
    const idx = str.indexOf(keyword);
    if (idx === -1) return '';
    return str.slice(idx + keyword.length).trim();
}

// Main SQL verification function
export function verifySql(
    solutionCode: string,
    userCode: string
): VerifyResult {
    // Basic checks
    if (!userCode || userCode.trim().length < 5 || userCode.trim() === '-- Write your SQL here') {
        return {
            correct: false,
            feedback: "Please write your SQL query!",
            suggestions: ["Read the instructions and write your query in the editor"]
        };
    }

    const normalizedUser = normalizeSql(userCode);
    const normalizedSolution = normalizeSql(solutionCode);

    // Exact match (normalized)
    if (normalizedUser === normalizedSolution) {
        return {
            correct: true,
            feedback: "Perfect! Your SQL query is correct! 🎉",
            suggestions: []
        };
    }

    // Check SQL structure
    const userStructure = extractSqlStructure(userCode);
    const solutionStructure = extractSqlStructure(solutionCode);

    // Missing SELECT
    if (solutionStructure.hasSelect && !userStructure.hasSelect) {
        return {
            correct: false,
            feedback: "Your query needs a SELECT statement.",
            suggestions: ["Start with: SELECT column_names", "Use SELECT * to select all columns"]
        };
    }

    // Missing FROM
    if (solutionStructure.hasFrom && !userStructure.hasFrom) {
        return {
            correct: false,
            feedback: "Your query needs a FROM clause.",
            suggestions: ["Add: FROM table_name", "Specify which table to query"]
        };
    }

    // Check if columns match (for SELECT queries)
    if (solutionStructure.hasSelect && userStructure.hasSelect) {
        const solutionCols = new Set(solutionStructure.columns);
        const userCols = new Set(userStructure.columns);

        // Check for SELECT *
        if (solutionCols.has('*') && !userCols.has('*')) {
            if (!arraysMatch(Array.from(solutionCols), Array.from(userCols))) {
                return {
                    correct: false,
                    feedback: "Check your column selection.",
                    suggestions: ["The expected query uses SELECT *"]
                };
            }
        }
    }

    // Check table names
    if (solutionStructure.tables.length > 0 && userStructure.tables.length > 0) {
        const solutionTable = solutionStructure.tables[0];
        const userTable = userStructure.tables[0];
        if (solutionTable !== userTable) {
            return {
                correct: false,
                feedback: "Check your table name.",
                suggestions: [`The query should use the '${solutionTable}' table`]
            };
        }
    }

    // Missing WHERE when needed
    if (solutionStructure.hasWhere && !userStructure.hasWhere) {
        return {
            correct: false,
            feedback: "Your query needs a WHERE clause to filter results.",
            suggestions: ["Add: WHERE condition", "Example: WHERE salary > 50000"]
        };
    }

    // Check for common SQL syntax issues
    if (!userCode.toLowerCase().includes('select') && !userCode.toLowerCase().includes('insert') &&
        !userCode.toLowerCase().includes('update') && !userCode.toLowerCase().includes('delete')) {
        return {
            correct: false,
            feedback: "That doesn't look like a valid SQL query.",
            suggestions: ["SQL queries usually start with SELECT, INSERT, UPDATE, or DELETE"]
        };
    }

    // Close but not exact - provide helpful feedback
    return {
        correct: false,
        feedback: "Your query is close but doesn't match the expected solution.",
        suggestions: [
            "Check your syntax carefully",
            "Compare with the expected query structure"
        ],
        expectedVsActual: { expected: solutionCode, actual: userCode }
    };
}

function arraysMatch(a: string[], b: string[]): boolean {
    if (a.length !== b.length) return false;
    const setA = new Set(a);
    return b.every(item => setA.has(item));
}

// ============ PYTHON VERIFICATION ============


// Check if output contains errors
function isErrorOutput(output: string): boolean {
    if (!output) return false;
    const errorIndicators = [
        "Error:",
        "Error\n",
        "❌",
        "Traceback",
        "SyntaxError",
        "NameError",
        "TypeError",
        "ValueError",
        "IndexError",
        "KeyError",
        "AttributeError",
        "IndentationError",
        "ZeroDivisionError",
        "PythonError",
        "ModuleNotFoundError",
        "ImportError",
        "RuntimeError",
    ];
    return errorIndicators.some(indicator => output.includes(indicator));
}

// Extract error type from output
function extractErrorType(output: string): string {
    const errorTypes = [
        "SyntaxError", "NameError", "TypeError", "ValueError",
        "IndexError", "KeyError", "AttributeError", "IndentationError",
        "ZeroDivisionError", "FileNotFoundError", "ImportError"
    ];
    for (const error of errorTypes) {
        if (output.includes(error)) return error;
    }
    return "Unknown Error";
}

// Get suggestions based on error type
function getErrorSuggestions(errorType: string): string[] {
    const suggestions: Record<string, string[]> = {
        "SyntaxError": ["Check for missing colons, parentheses, or quotes", "Make sure indentation is correct"],
        "NameError": ["Check if the variable is defined before use", "Watch for typos in variable names"],
        "TypeError": ["Make sure you're using the right data types", "Check function arguments"],
        "ValueError": ["Check the value you're passing", "Make sure data format is correct"],
        "IndexError": ["Check list/string index bounds", "Remember indices start at 0"],
        "KeyError": ["Check if the key exists in the dictionary", "Watch for typos in key names"],
        "IndentationError": ["Check your indentation", "Use consistent spaces (4 per level)"],
        "ZeroDivisionError": ["Don't divide by zero!", "Add a check before dividing"],
    };
    return suggestions[errorType] || ["Review the error message carefully"];
}

// Check if this is a graph exercise
function isGraphExercise(expectedOutput: string): boolean {
    if (!expectedOutput) return false;
    const graphIndicators = ["[Graph:", "graph", "plot", "chart", "histogram", "scatter", "visualization", "subplot"];
    return graphIndicators.some(indicator => expectedOutput.toLowerCase().includes(indicator.toLowerCase()));
}

// Validate graph code
function validateGraphCode(userCode: string): VerifyResult | null {
    const codeLower = userCode.toLowerCase();

    // Must import matplotlib
    if (!codeLower.includes("import matplotlib") && !codeLower.includes("from matplotlib")) {
        return {
            correct: false,
            feedback: "You need to import matplotlib to create graphs.",
            suggestions: ["Add: import matplotlib.pyplot as plt"]
        };
    }

    // Must have plotting function with data
    const plotPatterns = [
        /plt\.(plot|bar|scatter|hist|pie|barh)\s*\([^)]+\)/,
        /ax\d*\.(plot|bar|scatter|hist|pie|barh)\s*\([^)]+\)/,
        /axes\[\d+\]\.(plot|bar|scatter|hist|pie|barh)\s*\([^)]+\)/,
    ];

    const hasPlotWithData = plotPatterns.some(pattern => pattern.test(userCode));

    if (!hasPlotWithData) {
        if (userCode.toLowerCase().includes("subplots")) {
            return {
                correct: false,
                feedback: "You created subplots, but didn't plot any data on them!",
                suggestions: ["Use ax1.plot([1, 2, 3]) or ax1.bar(['A', 'B'], [5, 8]) to add data"]
            };
        }
        return {
            correct: false,
            feedback: "You need to create a plot with actual data.",
            suggestions: ["Use plt.plot(), plt.bar(), plt.scatter(), or other plotting functions"]
        };
    }

    // Must have plt.show()
    if (!userCode.includes("plt.show()") && !userCode.includes(".show()")) {
        return {
            correct: false,
            feedback: "Don't forget to display your graph!",
            suggestions: ["Add plt.show() at the end to display your plot"]
        };
    }

    return null; // Valid graph code
}

// Normalize output for comparison - STRICTER version
function normalizeOutput(output: string): string {
    return output
        .replace("✓ Code executed successfully (no output)", "")
        .trim();
}

// Compare outputs - STRICTER matching
function compareOutputs(expected: string, actual: string): { match: boolean; percent: number; exactMatch: boolean } {
    const expectedNorm = normalizeOutput(expected);
    const actualNorm = normalizeOutput(actual);

    // Exact match check (case-sensitive)
    if (expectedNorm === actualNorm) {
        return { match: true, percent: 100, exactMatch: true };
    }

    // Case-insensitive exact match
    if (expectedNorm.toLowerCase() === actualNorm.toLowerCase()) {
        return { match: true, percent: 99, exactMatch: false };
    }

    // Check if expected is contained in actual (with some tolerance)
    if (expectedNorm && actualNorm.includes(expectedNorm)) {
        return { match: true, percent: 95, exactMatch: false };
    }

    // Word-based comparison for partial matching
    const expectedParts = new Set(expectedNorm.toLowerCase().split(/\s+/));
    const actualParts = new Set(actualNorm.toLowerCase().split(/\s+/));

    if (expectedParts.size === 0) return { match: false, percent: 0, exactMatch: false };

    let matchCount = 0;
    expectedParts.forEach(part => {
        if (actualParts.has(part)) matchCount++;
    });

    const percent = (matchCount / expectedParts.size) * 100;
    // STRICTER: Only accept if >= 90% match (was 70%)
    return { match: percent >= 90, percent, exactMatch: false };
}

// Generate detailed comparison feedback
function generateComparisonFeedback(expected: string, actual: string): string[] {
    const suggestions: string[] = [];

    // Check for common issues
    if (expected.includes("*") && actual.includes("+")) {
        suggestions.push("Hint: The exercise asks for multiplication (*), not addition (+)");
    }
    if (expected.includes("/") && actual.includes("-")) {
        suggestions.push("Hint: The exercise asks for division (/), not subtraction (-)");
    }
    if (expected.toLowerCase() !== expected && actual.toLowerCase() === actual) {
        suggestions.push("Hint: Check your capitalization");
    }
    if (expected.includes('"') || expected.includes("'")) {
        if (!actual.includes(expected.split(/["']/)[1])) {
            suggestions.push("Hint: Check your string output matches exactly");
        }
    }

    return suggestions;
}

// Main verification function
export function verifyCode(
    expectedOutput: string,
    actualOutput: string,
    userCode: string
): VerifyResult {
    // Check for errors first
    if (isErrorOutput(actualOutput)) {
        const errorType = extractErrorType(actualOutput);
        return {
            correct: false,
            feedback: `Your code has an error: ${errorType}`,
            suggestions: getErrorSuggestions(errorType)
        };
    }

    // Check if code is too short
    if (userCode.trim().length < 10) {
        return {
            correct: false,
            feedback: "It looks like you haven't written any code yet!",
            suggestions: ["Read the instructions on the left", "Write code to solve the task"]
        };
    }

    // Special handling for graph exercises
    if (isGraphExercise(expectedOutput)) {
        const graphResult = validateGraphCode(userCode);
        if (graphResult) return graphResult;

        // Graph code is valid
        return {
            correct: true,
            feedback: "Great job! Your graph looks good! 🎉",
            suggestions: []
        };
    }

    // No expected output - just check if code ran
    if (!expectedOutput || expectedOutput === "Run your code to see the output!") {
        if (actualOutput && !isErrorOutput(actualOutput)) {
            return {
                correct: true,
                feedback: "Your code ran successfully! 🎉",
                suggestions: []
            };
        }
        return {
            correct: false,
            feedback: "Your code didn't produce any output.",
            suggestions: ["Make sure to use print() to display results"]
        };
    }

    // Compare outputs with STRICTER matching
    const { match, percent, exactMatch } = compareOutputs(expectedOutput, actualOutput);

    if (exactMatch) {
        return {
            correct: true,
            feedback: "Perfect! Your output matches exactly! 🎉",
            suggestions: []
        };
    } else if (match) {
        return {
            correct: true,
            feedback: "Great job! Your output is correct! 🎉",
            suggestions: []
        };
    } else if (percent >= 70) {
        // Still not good enough - give specific feedback
        const detailedSuggestions = generateComparisonFeedback(expectedOutput, actualOutput);
        return {
            correct: false,
            feedback: "Almost there! Your output is close but not quite right.",
            suggestions: detailedSuggestions.length > 0
                ? detailedSuggestions
                : ["Compare your output carefully with the expected output"],
            expectedVsActual: { expected: expectedOutput, actual: actualOutput }
        };
    } else if (percent >= 40) {
        return {
            correct: false,
            feedback: "Your output is partially correct but needs work.",
            suggestions: [
                "Compare each line with the expected output",
                ...generateComparisonFeedback(expectedOutput, actualOutput)
            ],
            expectedVsActual: { expected: expectedOutput, actual: actualOutput }
        };
    } else {
        return {
            correct: false,
            feedback: "Your output doesn't match the expected result.",
            suggestions: [
                "Read the instructions carefully",
                "Make sure you're using the correct values and operations",
                ...generateComparisonFeedback(expectedOutput, actualOutput)
            ],
            expectedVsActual: { expected: expectedOutput, actual: actualOutput }
        };
    }
}
