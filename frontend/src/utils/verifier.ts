// Verification logic for code exercises
// This runs entirely in the browser - no server needed!

interface VerifyResult {
    correct: boolean;
    feedback: string;
    suggestions: string[];
}

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
    const graphIndicators = ["[Graph:", "graph", "plot", "chart", "histogram", "scatter", "visualization"];
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

// Normalize output for comparison
function normalizeOutput(output: string): string {
    return output
        .replace("✓ Code executed successfully (no output)", "")
        .replace(/\s+/g, " ")
        .trim()
        .toLowerCase();
}

// Compare outputs
function compareOutputs(expected: string, actual: string): { match: boolean; percent: number } {
    const expectedNorm = normalizeOutput(expected);
    const actualNorm = normalizeOutput(actual);

    if (expectedNorm === actualNorm) return { match: true, percent: 100 };
    if (expectedNorm && actualNorm.includes(expectedNorm)) return { match: true, percent: 95 };

    const expectedParts = new Set(expectedNorm.split(" "));
    const actualParts = new Set(actualNorm.split(" "));

    if (expectedParts.size === 0) return { match: false, percent: 0 };

    let matchCount = 0;
    expectedParts.forEach(part => {
        if (actualParts.has(part)) matchCount++;
    });

    const percent = (matchCount / expectedParts.size) * 100;
    return { match: percent >= 90, percent };
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

    // Compare outputs
    const { match, percent } = compareOutputs(expectedOutput, actualOutput);

    if (match) {
        return {
            correct: true,
            feedback: "Perfect! Your output matches the expected result! 🎉",
            suggestions: []
        };
    } else if (percent >= 70) {
        return {
            correct: true,
            feedback: "Great job! Your output is close enough! 🎉",
            suggestions: []
        };
    } else if (percent >= 40) {
        return {
            correct: false,
            feedback: "Almost there! Your output is partially correct.",
            suggestions: ["Check the expected output and compare with yours"]
        };
    } else {
        return {
            correct: false,
            feedback: "Your output doesn't match the expected result.",
            suggestions: ["Compare your output with the expected output"]
        };
    }
}
