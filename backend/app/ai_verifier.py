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


def is_error_output(output: str) -> bool:
    """Check if output contains Python errors."""
    error_indicators = [
        "Error:",
        "Traceback",
        "SyntaxError",
        "NameError",
        "TypeError",
        "ValueError",
        "IndexError",
        "KeyError",
        "AttributeError",
        "IndentationError",
        "ZeroDivisionError"
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
