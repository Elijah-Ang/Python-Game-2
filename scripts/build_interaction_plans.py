import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple


LESSONS_PATH = Path("frontend/public/data/lessons.json")

PYTHON_TAG_RULES = {
    "variables": ["variable", "assignment", "reassign", "swap", "naming"],
    "strings": ["string", "f-string", "concatenation", "format", "text", "replace", "split", "strip"],
    "numbers": ["number", "integer", "float", "math", "arithmetic", "operator", "modulo", "division", "multiply"],
    "booleans": ["boolean", "true", "false", "logical"],
    "conditionals": ["if", "elif", "else", "conditional", "comparison"],
    "loops": ["loop", "for", "while", "range", "iterate", "iteration"],
    "lists": ["list", "index", "append", "slice"],
    "dictionaries": ["dictionary", "dict", "key", "value", "map"],
    "sets": ["set", "unique"],
    "functions": ["function", "def", "return", "parameter", "argument"],
    "files": ["file", "csv", "read", "write", "open"],
    "classes": ["class", "object", "oop", "instance", "method"],
    "debugging": ["debug", "error", "traceback"],
    "projects": ["project", "challenge", "capstone", "boss"],
}

SQL_TAG_RULES = {
    "schema": ["database", "table", "row", "column", "schema", "primary key", "foreign key"],
    "select": ["select", "from", "projection"],
    "where": ["where", "filter", "predicate"],
    "order_by": ["order by", "sort"],
    "limit": ["limit", "top"],
    "join": ["join", "inner join", "left join", "right join", "full join"],
    "group_by": ["group by", "aggregate", "count", "sum", "avg", "min", "max", "having"],
    "mutations": ["insert", "update", "delete"],
    "subquery": ["subquery", "cte", "with"],
    "case": ["case", "when", "then"],
    "window": ["window", "over", "partition"],
}

R_TAG_RULES = {
    "visualization": ["ggplot", "geom", "plot", "chart", "graph"],
    "dataframe": ["data frame", "dataframe", "tibble"],
    "dplyr_filter": ["filter", "subset", "where"],
    "dplyr_select": ["select", "rename"],
    "dplyr_mutate": ["mutate", "transform"],
    "dplyr_group": ["group_by", "summarise", "summarize", "aggregate"],
    "vectors": ["vector", "c(", "seq", "sequence"],
    "functions": ["function", "apply", "map"],
    "control": ["if", "else", "loop", "for", "while"],
    "packages": ["library", "package", "install"],
}


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def count_code_blocks(content: str) -> int:
    return len(re.findall(r"```", content)) // 2


def infer_tags(text: str, title: str, rules: Dict[str, List[str]]) -> Tuple[List[str], float]:
    tags: List[str] = []
    scores: Dict[str, int] = {}
    for tag, keywords in rules.items():
        for keyword in keywords:
            if keyword in text:
                scores[tag] = scores.get(tag, 0) + 1
            if keyword in title:
                scores[tag] = scores.get(tag, 0) + 2

    if not scores:
        return ["general"], 0.55

    sorted_tags = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    tags = [tag for tag, _ in sorted_tags]
    top_score = sorted_tags[0][1]
    confidence = min(0.95, 0.6 + top_score * 0.08)
    return tags, confidence


def mutate_output(output: str) -> str:
    numeric_match = re.search(r"-?\d+(\.\d+)?", output)
    if numeric_match:
        number = numeric_match.group(0)
        try:
            value = float(number)
            mutated = value + 1
            if number.isdigit():
                mutated_str = str(int(mutated))
            else:
                mutated_str = str(mutated)
            return output.replace(number, mutated_str, 1)
        except ValueError:
            pass

    if "\n" in output:
        lines = output.splitlines()
        return "\n".join(lines[:-1]) or "No output"

    return f"{output} (different)"


def build_prediction(expected_output: str, fallback_question: str, fallback_options: List[str]) -> Dict[str, Any]:
    cleaned = (expected_output or "").strip()
    if cleaned and cleaned != "Run your code to see the output!":
        wrong_one = mutate_output(cleaned)
        wrong_two = mutate_output(wrong_one)
        options = [cleaned, wrong_one, wrong_two]
        unique_options = []
        for opt in options:
            if opt not in unique_options:
                unique_options.append(opt)
        while len(unique_options) < 3:
            unique_options.append(f"{cleaned} (alt)")
        return {
            "type": "prediction",
            "question": "Predict the output before you run it.",
            "options": unique_options[:3],
            "correctIndex": 0,
            "explanation": "Compare the output to the lesson target to confirm your reasoning."
        }

    return {
        "type": "prediction",
        "question": fallback_question,
        "options": fallback_options,
        "correctIndex": 0,
        "explanation": "Try the action, then compare the result with your prediction."
    }


def build_hints(solution_code: str, fallback: str) -> List[str]:
    cleaned = (solution_code or "").strip()
    if cleaned:
        lines = [line for line in cleaned.splitlines() if line.strip()]
        line_one = lines[0] if lines else fallback
        line_two = lines[1] if len(lines) > 1 else line_one
        preview = "\n".join(lines[:4])
        return [
            f"Focus on the line that sets up the key value: {line_one}",
            f"Next, make sure you include: {line_two}",
            f"One working solution starts like:\n{preview}"
        ]
    return [
        fallback,
        "Try updating one line at a time and re-check the output.",
        "Use the lesson instructions as a template for the correct structure."
    ]


def python_plan(tag: str, lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan: List[Dict[str, Any]] = []
    prediction = build_prediction(
        lesson.get("expected_output", ""),
        "What will this snippet print?",
        ["It prints a value", "It errors", "It prints nothing"]
    )
    plan.append(prediction)

    template = lesson.get("starter_code") or "value = 0\nprint(value)"

    if tag in ("variables", "numbers", "booleans"):
        plan.extend([
            {
                "type": "variable_slider",
                "name": "py_value",
                "min": 0,
                "max": 20,
                "initial": 7,
                "label": "Choose a value"
            },
            {
                "type": "memory_box",
                "names": ["py_value"],
                "valueType": "number"
            }
        ])
        template = "score = {{py_value}}\nprint(score)"
    elif tag == "strings":
        plan.extend([
            {
                "type": "draggable_value",
                "name": "py_text",
                "acceptedValues": ["data", "python", "science"],
                "chips": ["data", "python", "science"],
                "label": "Drop a word into the variable",
                "valueType": "string",
                "initial": "data"
            },
            {
                "type": "memory_box",
                "names": ["py_text"],
                "valueType": "string"
            }
        ])
        template = 'word = "{{py_text}}"\nprint(word)'
    elif tag == "loops":
        plan.extend([
            {
                "type": "variable_slider",
                "name": "py_loops",
                "min": 2,
                "max": 6,
                "initial": 3,
                "label": "Loop count"
            },
            {
                "type": "step_executor",
                "code": "total = 0\nfor i in range(3):\n    total += i\nprint(total)",
                "steps": [
                    {"line": 1, "description": "Start total at 0", "stateChanges": {"total": 0}},
                    {"line": 2, "description": "Loop over range", "stateChanges": {"i": 0}},
                    {"line": 3, "description": "Add i to total", "stateChanges": {"total": 0}},
                    {"line": 2, "description": "Next i value", "stateChanges": {"i": 1}},
                    {"line": 3, "description": "Add i to total", "stateChanges": {"total": 1}},
                ]
            }
        ])
        template = "total = 0\nfor i in range({{py_loops}}):\n    total += i\nprint(total)"
    elif tag == "conditionals":
        plan.extend([
            {
                "type": "draggable_value",
                "name": "py_flag",
                "acceptedValues": ["True", "False"],
                "chips": ["True", "False"],
                "label": "Choose a condition result",
                "valueType": "boolean",
                "initial": "True"
            },
            {
                "type": "fill_blanks",
                "template": "if {{condition}}:\n    print(\"Yes\")\nelse:\n    print(\"No\")",
                "blanks": [
                    {
                        "id": "condition",
                        "options": ["x > 3", "x < 3", "x == 3"],
                        "correct": "x > 3"
                    }
                ]
            }
        ])
        template = "flag = {{py_flag}}\nif flag:\n    print(\"Yes\")\nelse:\n    print(\"No\")"
    elif tag in ("lists", "dictionaries", "sets"):
        plan.append({
            "type": "visual_table",
            "title": "Preview the collection",
            "dataRef": "python_scores",
            "columns": ["name", "score", "bonus"],
            "allowSort": True,
            "allowFilter": True,
            "allowRowHighlight": True,
            "highlightColumn": "score"
        })
        template = "scores = [12, 18, 24, 15]\nprint(scores)"
    else:
        plan.append({
            "type": "live_code_block",
            "initialCode": lesson.get("starter_code") or "# Try editing this line\nvalue = 3\nprint(value)",
            "language": "python",
            "highlightLine": 2
        })

    hints = build_hints(lesson.get("solution_code", ""), "Look at the variable names in the prompt.")
    plan.append({"type": "hint_ladder", "hints": hints})
    plan.append({"type": "send_to_editor", "template": template, "templateId": "python_template"})
    plan.append({"type": "reset_state", "label": "Reset interactions"})
    return plan, template


def sql_plan(tag: str, lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan: List[Dict[str, Any]] = []
    prediction = build_prediction(
        lesson.get("expected_output", ""),
        "What will the query return?",
        ["Rows of data", "An error", "An empty result"]
    )
    plan.append(prediction)

    template = "SELECT * FROM employees;"

    if tag in ("schema", "select"):
        plan.extend([
            {
                "type": "draggable_value",
                "name": "sql_columns",
                "acceptedValues": ["*", "name, department", "name"],
                "chips": ["*", "name, department", "name"],
                "label": "Choose columns",
                "valueType": "string",
                "initial": "*"
            },
            {
                "type": "visual_table",
                "title": "Sample table",
                "dataRef": "sql_employees",
                "columns": ["id", "name", "department", "salary"],
                "allowSort": True,
                "allowFilter": True,
                "allowRowHighlight": True,
                "highlightColumn": "salary"
            },
            {
                "type": "fill_blanks",
                "template": "SELECT {{columns}} FROM employees;",
                "blanks": [
                    {
                        "id": "columns",
                        "options": ["*", "name, department", "name"],
                        "correct": "*"
                    }
                ]
            }
        ])
        template = "SELECT {{sql_columns}} FROM employees;"
    elif tag == "where":
        plan.extend([
            {
                "type": "draggable_value",
                "name": "sql_department",
                "acceptedValues": ["Sales", "Marketing", "Engineering"],
                "chips": ["Sales", "Marketing", "Engineering"],
                "label": "Filter by department",
                "valueType": "string",
                "initial": "Sales"
            },
            {
                "type": "visual_table",
                "title": "Employees (filter in query)",
                "dataRef": "sql_employees",
                "columns": ["id", "name", "department", "salary"],
                "allowSort": True,
                "allowFilter": True,
                "allowRowHighlight": True,
                "highlightColumn": "department"
            }
        ])
        template = "SELECT * FROM employees WHERE department = '{{sql_department}}';"
    elif tag in ("order_by", "limit"):
        plan.extend([
            {
                "type": "variable_slider",
                "name": "sql_limit",
                "min": 1,
                "max": 5,
                "initial": 3,
                "label": "Row limit"
            },
            {
                "type": "visual_table",
                "title": "Orders preview",
                "dataRef": "sql_orders",
                "columns": ["order_id", "customer", "status", "spend"],
                "allowSort": True,
                "allowFilter": True,
                "allowRowHighlight": True,
                "highlightColumn": "spend"
            }
        ])
        template = "SELECT * FROM orders ORDER BY spend DESC LIMIT {{sql_limit}};"
    elif tag == "join":
        plan.extend([
            {
                "type": "draggable_value",
                "name": "sql_join",
                "acceptedValues": ["JOIN", "LEFT JOIN", "RIGHT JOIN"],
                "chips": ["JOIN", "LEFT JOIN", "RIGHT JOIN"],
                "label": "Pick a join type",
                "valueType": "string",
                "initial": "JOIN"
            },
            {
                "type": "fill_blanks",
                "template": "SELECT * FROM orders {{join_type}} customers ON orders.customer_id = customers.id;",
                "blanks": [
                    {
                        "id": "join_type",
                        "options": ["JOIN", "LEFT JOIN", "RIGHT JOIN"],
                        "correct": "JOIN"
                    }
                ]
            },
            {
                "type": "live_code_block",
                "initialCode": "SELECT orders.id, customers.name\nFROM orders\nJOIN customers ON orders.customer_id = customers.id;",
                "language": "sql",
                "highlightLine": 3
            }
        ])
        template = "SELECT orders.id, customers.name\nFROM orders\n{{sql_join}} customers ON orders.customer_id = customers.id;"
    elif tag == "group_by":
        plan.extend([
            {
                "type": "draggable_value",
                "name": "sql_agg",
                "acceptedValues": ["SUM", "AVG", "COUNT"],
                "chips": ["SUM", "AVG", "COUNT"],
                "label": "Pick an aggregate",
                "valueType": "string",
                "initial": "AVG"
            },
            {
                "type": "fill_blanks",
                "template": "SELECT department, {{agg}}(salary) FROM employees GROUP BY department;",
                "blanks": [
                    {
                        "id": "agg",
                        "options": ["SUM", "AVG", "COUNT"],
                        "correct": "AVG"
                    }
                ]
            },
            {
                "type": "visual_table",
                "title": "Employees table",
                "dataRef": "sql_employees",
                "columns": ["department", "salary"],
                "allowSort": True,
                "allowFilter": False,
                "allowRowHighlight": True,
                "highlightColumn": "department"
            }
        ])
        template = "SELECT department, {{sql_agg}}(salary) FROM employees GROUP BY department;"
    else:
        plan.append({
            "type": "visual_table",
            "title": "Orders preview",
            "dataRef": "sql_orders",
            "columns": ["order_id", "customer", "status", "spend"],
            "allowSort": True,
            "allowFilter": True,
            "allowRowHighlight": True,
            "highlightColumn": "status"
        })

    hints = build_hints(lesson.get("solution_code", ""), "Focus on the clause named in the lesson title.")
    plan.append({"type": "hint_ladder", "hints": hints})
    plan.append({"type": "send_to_editor", "template": template, "templateId": "sql_template"})
    plan.append({"type": "reset_state", "label": "Reset interactions"})
    return plan, template


def r_plan(tag: str, lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan: List[Dict[str, Any]] = []
    prediction = build_prediction(
        lesson.get("expected_output", ""),
        "What will this R code output?",
        ["A tibble/plot", "An error", "No output"]
    )
    plan.append(prediction)

    template = "summary(data)"

    if tag == "visualization":
        plan.extend([
            {
                "type": "draggable_value",
                "name": "r_geom",
                "acceptedValues": ["geom_point()", "geom_bar()", "geom_line()"],
                "chips": ["geom_point()", "geom_bar()", "geom_line()"],
                "label": "Choose a geom layer",
                "valueType": "string",
                "initial": "geom_point()"
            },
            {
                "type": "visual_table",
                "title": "Penguin sample",
                "dataRef": "r_penguins",
                "columns": ["species", "island", "bill_length", "body_mass"],
                "allowSort": True,
                "allowFilter": True,
                "allowRowHighlight": True,
                "highlightColumn": "body_mass"
            },
            {
                "type": "live_code_block",
                "initialCode": "ggplot(penguins, aes(x = bill_length, y = body_mass)) +\n  geom_point()",
                "language": "r",
                "highlightLine": 2
            }
        ])
        template = "ggplot(penguins, aes(x = bill_length, y = body_mass)) + {{r_geom}}"
    elif tag in ("dplyr_filter", "dplyr_select", "dplyr_mutate"):
        plan.extend([
            {
                "type": "draggable_value",
                "name": "r_threshold",
                "acceptedValues": [3400, 3800, 4200],
                "chips": [3400, 3800, 4200],
                "label": "Body mass threshold",
                "valueType": "number",
                "initial": 3400
            },
            {
                "type": "visual_table",
                "title": "Penguin preview",
                "dataRef": "r_penguins",
                "columns": ["species", "island", "bill_length", "body_mass"],
                "allowSort": True,
                "allowFilter": True,
                "allowRowHighlight": True,
                "highlightColumn": "body_mass"
            }
        ])
        template = "filtered <- penguins[penguins$body_mass >= {{r_threshold}}, ]\nhead(filtered, 3)"
    elif tag == "vectors":
        plan.extend([
            {
                "type": "variable_slider",
                "name": "r_index",
                "min": 1,
                "max": 4,
                "initial": 2,
                "label": "Vector index"
            },
            {
                "type": "visual_table",
                "title": "Vector values",
                "dataRef": "r_vectors",
                "columns": ["index", "value"],
                "allowSort": False,
                "allowFilter": False,
                "allowRowHighlight": True,
                "highlightColumn": "value"
            }
        ])
        template = "values <- c(10, 14, 22, 5)\nvalues[{{r_index}}]"
    else:
        plan.append({
            "type": "live_code_block",
            "initialCode": lesson.get("starter_code") or "# Edit this line\nx <- 2\nx * 3",
            "language": "r",
            "highlightLine": 2
        })

    hints = build_hints(lesson.get("solution_code", ""), "Focus on the function used in the lesson title.")
    plan.append({"type": "hint_ladder", "hints": hints})
    plan.append({"type": "send_to_editor", "template": template, "templateId": "r_template"})
    plan.append({"type": "reset_state", "label": "Reset interactions"})
    return plan, template


def build_plan(curriculum: str, tag: str, lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    if curriculum == "python":
        return python_plan(tag, lesson)
    if curriculum == "sql":
        return sql_plan(tag, lesson)
    return r_plan(tag, lesson)


def main() -> None:
    if not LESSONS_PATH.exists():
        raise SystemExit(f"Missing lessons file at {LESSONS_PATH}")

    lessons = json.loads(LESSONS_PATH.read_text())
    updated = {}
    manual_review_ids = []

    for lesson_id, lesson in lessons.items():
        lesson_id_int = int(lesson_id)
        if lesson_id_int >= 2000:
            curriculum = "r"
            rules = R_TAG_RULES
        elif 1000 < lesson_id_int < 2000:
            curriculum = "sql"
            rules = SQL_TAG_RULES
        else:
            curriculum = "python"
            rules = PYTHON_TAG_RULES

        text = normalize_text(f"{lesson.get('title', '')} {lesson.get('content', '')} {lesson.get('chapter_title', '')}")
        title_text = normalize_text(lesson.get("title", ""))
        tags, confidence = infer_tags(text, title_text, rules)
        primary_tag = tags[0]

        plan, template = build_plan(curriculum, primary_tag, lesson)

        code_blocks = count_code_blocks(lesson.get("content", ""))
        is_project = any(keyword in title_text for keyword in ("project", "capstone", "challenge", "boss"))
        manual_review = confidence < 0.7 or code_blocks > 3 or is_project or len(tags) > 3

        lesson["concept_tags"] = tags
        lesson["interaction_plan"] = plan
        lesson["interaction_required"] = True
        lesson["send_to_editor_template"] = template
        lesson["interaction_confidence"] = round(confidence, 2)
        lesson["manual_review"] = manual_review

        if manual_review:
            manual_review_ids.append(lesson_id)

        updated[lesson_id] = lesson

    LESSONS_PATH.write_text(json.dumps(updated, indent=2))

    report_path = Path("scripts/interaction_plan_report.json")
    report = {
        "total_lessons": len(updated),
        "manual_review_count": len(manual_review_ids),
        "manual_review_ids": manual_review_ids[:200]
    }
    report_path.write_text(json.dumps(report, indent=2))
    print(f"Updated {len(updated)} lessons. Manual review: {len(manual_review_ids)}.")


if __name__ == "__main__":
    main()
