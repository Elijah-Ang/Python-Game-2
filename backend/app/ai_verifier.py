"""
Output-Based Code Verification Service
Compares user's output to expected output without AI.
"""
import re
from typing import Tuple


def verify_code(
    expected_output: str,
    actual_output: str,
    user_code: str
) -> dict:
    """
    Verify user's code by comparing actual output to expected output.
    
    Returns:
        {
            "correct": bool,
            "feedback": str,
            "suggestions": list[str]
        }
    """
    
    # Check for errors first
    if is_error_output(actual_output):
        error_type = extract_error_type(actual_output)
        return {
            "correct": False,
            "feedback": f"Your code has an error: {error_type}",
            "suggestions": get_error_suggestions(error_type, actual_output)
        }
    
    # Check if code is too short (not attempted)
    if len(user_code.strip()) < 10:
        return {
            "correct": False,
            "feedback": "It looks like you haven't written any code yet!",
            "suggestions": ["Read the instructions on the left", "Write code to solve the task"]
        }
    
    # Special handling for graph/visualization exercises
    if is_graph_exercise(expected_output):
        graph_result = validate_graph_code(user_code, actual_output)
        if graph_result:
            return graph_result
    
    # No expected output defined - just check if code ran successfully
    if not expected_output or expected_output == "Run your code to see the output!":
        if actual_output and not is_error_output(actual_output):
            return {
                "correct": True,
                "feedback": "Your code ran successfully! 🎉",
                "suggestions": []
            }
        return {
            "correct": False,
            "feedback": "Your code didn't produce any output.",
            "suggestions": ["Make sure to use print() to display results"]
        }
    
    # Compare outputs
    match_result, match_percent = compare_outputs(expected_output, actual_output)
    
    if match_result:
        return {
            "correct": True,
            "feedback": "Perfect! Your output matches the expected result! 🎉",
            "suggestions": []
        }
    elif match_percent >= 70:
        return {
            "correct": True,
            "feedback": "Great job! Your output is close enough! 🎉",
            "suggestions": []
        }
    elif match_percent >= 40:
        return {
            "correct": False,
            "feedback": "Almost there! Your output is partially correct.",
            "suggestions": [
                "Check the expected output and compare with yours",
                "Make sure all required values are printed"
            ]
        }
    else:
        return {
            "correct": False,
            "feedback": "Your output doesn't match the expected result.",
            "suggestions": [
                "Compare your output with the expected output",
                "Make sure you're printing the right values"
            ]
        }


def is_graph_exercise(expected_output: str) -> bool:
    """Check if this is a graph/visualization exercise."""
    if not expected_output:
        return False
    graph_indicators = [
        "[Graph:",
        "graph",
        "plot",
        "chart",
        "histogram",
        "scatter",
        "visualization"
    ]
    return any(indicator.lower() in expected_output.lower() for indicator in graph_indicators)


def validate_graph_code(user_code: str, actual_output: str) -> dict:
    """
    Validate that graph code actually creates a proper visualization.
    Returns None if valid (continue normal flow), or error dict if invalid.
    """
    import re
    
    code_lower = user_code.lower()
    
    # Must import matplotlib
    has_matplotlib_import = "import matplotlib" in code_lower or "from matplotlib" in code_lower
    if not has_matplotlib_import:
        return {
            "correct": False,
            "feedback": "You need to import matplotlib to create graphs.",
            "suggestions": ["Add: import matplotlib.pyplot as plt"]
        }
    
    # Define all valid plotting function patterns (including ax1, ax2, axes[0], etc.)
    plotting_patterns = [
        r'plt\.(plot|bar|scatter|hist|pie|barh|subplot)\s*\(',
        r'ax\d*\.(plot|bar|scatter|hist|pie|barh)\s*\(',  # ax, ax1, ax2, etc.
        r'axes?\[\d+\]\.(plot|bar|scatter|hist|pie|barh)\s*\(',  # ax[0], axes[0], etc.
        r'axes?\[\d+,\s*\d+\]\.(plot|bar|scatter|hist|pie|barh)\s*\(',  # axes[0, 1]
    ]
    
    # Check if ANY plotting function is called with actual data
    plot_calls_with_data = []
    for pattern in plotting_patterns:
        matches = re.findall(pattern + r'[^)]+', user_code)
        plot_calls_with_data.extend(matches)
    
    # Also check for simple calls like plt.plot([1,2,3])
    simple_patterns = [
        r'plt\.(plot|bar|scatter|hist|pie|barh)\s*\([^\)]+\)',
        r'ax\d*\.(plot|bar|scatter|hist|pie|barh)\s*\([^\)]+\)',
    ]
    
    has_plot_with_data = False
    for pattern in simple_patterns:
        if re.search(pattern, user_code):
            has_plot_with_data = True
            break
    
    if not has_plot_with_data:
        # Check if they just created subplots without plotting
        if "subplots" in user_code.lower():
            return {
                "correct": False,
                "feedback": "You created subplots, but didn't plot any data on them!",
                "suggestions": [
                    "Use ax1.plot([1, 2, 3]) or ax1.bar(['A', 'B'], [5, 8]) to add data",
                    "Each subplot needs its own plot call with data"
                ]
            }
        return {
            "correct": False,
            "feedback": "You need to create a plot with actual data.",
            "suggestions": [
                "Use plt.plot(), plt.bar(), plt.scatter(), or other plotting functions",
                "Make sure to pass data to your plotting function"
            ]
        }
    
    # Check for plt.show() - required to display the graph
    has_show = "plt.show()" in user_code or ".show()" in user_code
    if not has_show:
        return {
            "correct": False,
            "feedback": "Don't forget to display your graph!",
            "suggestions": ["Add plt.show() at the end to display your plot"]
        }
    
    # All checks passed - graph code is valid
    return None


def is_error_output(output: str) -> bool:
    """Check if output contains Python errors."""
    if not output:
        return False
    
    error_indicators = [
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
        "StopIteration",
        "RecursionError"
    ]
    return any(indicator in output for indicator in error_indicators)


def extract_error_type(output: str) -> str:
    """Extract the type of error from output."""
    error_types = [
        "SyntaxError", "NameError", "TypeError", "ValueError",
        "IndexError", "KeyError", "AttributeError", "IndentationError",
        "ZeroDivisionError", "FileNotFoundError", "ImportError"
    ]
    for error in error_types:
        if error in output:
            return error
    return "Unknown Error"


def get_error_suggestions(error_type: str, output: str) -> list:
    """Get helpful suggestions based on error type."""
    suggestions = {
        "SyntaxError": ["Check for missing colons, parentheses, or quotes", "Make sure indentation is correct"],
        "NameError": ["Check if the variable is defined before use", "Watch for typos in variable names"],
        "TypeError": ["Make sure you're using the right data types", "Check function arguments"],
        "ValueError": ["Check the value you're passing", "Make sure data format is correct"],
        "IndexError": ["Check list/string index bounds", "Remember indices start at 0"],
        "KeyError": ["Check if the key exists in the dictionary", "Watch for typos in key names"],
        "IndentationError": ["Check your indentation", "Use consistent spaces (4 per level)"],
        "ZeroDivisionError": ["Don't divide by zero!", "Add a check before dividing"],
    }
    return suggestions.get(error_type, ["Review the error message carefully"])


def normalize_output(output: str) -> str:
    """Normalize output for comparison."""
    # Remove common prefixes
    output = output.replace("✓ Code executed successfully (no output)", "").strip()
    
    # Normalize whitespace
    output = re.sub(r'\s+', ' ', output).strip()
    
    # Normalize case for comparison
    return output.lower()


def compare_outputs(expected: str, actual: str) -> Tuple[bool, float]:
    """
    Compare expected and actual output.
    Returns (is_match, match_percentage).
    """
    expected_norm = normalize_output(expected)
    actual_norm = normalize_output(actual)
    
    # Exact match
    if expected_norm == actual_norm:
        return True, 100.0
    
    # Check if expected is contained in actual (user might print extra)
    if expected_norm in actual_norm:
        return True, 95.0
    
    # Check if all key parts of expected are in actual
    expected_parts = set(expected_norm.split())
    actual_parts = set(actual_norm.split())
    
    if not expected_parts:
        return False, 0.0
    
    matching_parts = expected_parts.intersection(actual_parts)
    match_percent = (len(matching_parts) / len(expected_parts)) * 100
    
    # Check for key numeric values
    expected_numbers = set(re.findall(r'\d+\.?\d*', expected_norm))
    actual_numbers = set(re.findall(r'\d+\.?\d*', actual_norm))
    
    if expected_numbers and expected_numbers.issubset(actual_numbers):
        match_percent = max(match_percent, 80.0)
    
    return match_percent >= 90, match_percent
