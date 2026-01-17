import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

LESSONS_PATH = Path("frontend/public/data/lessons.json")
COURSE_PATHS = {
    "python": Path("frontend/public/data/course-python-basics.json"),
    "sql": Path("frontend/public/data/course-sql-fundamentals.json"),
    "r": Path("frontend/public/data/course-r-fundamentals.json"),
}

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

DEFAULT_LEFT_TABLE = [
    {"id": 1, "name": "Alice", "dept_id": 10},
    {"id": 2, "name": "Bob", "dept_id": 20},
    {"id": 3, "name": "Charlie", "dept_id": 10},
]

DEFAULT_RIGHT_TABLE = [
    {"dept_id": 10, "department": "Sales"},
    {"dept_id": 20, "department": "Marketing"},
    {"dept_id": 30, "department": "Engineering"},
]


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def count_code_blocks(content: str) -> int:
    return len(re.findall(r"```", content)) // 2


def infer_tags(text: str, title: str, rules: Dict[str, List[str]]) -> Tuple[List[str], float]:
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


def build_hints(solution_code: str, fallback: str) -> List[str]:
    cleaned = (solution_code or "").strip()
    if cleaned:
        lines = [line for line in cleaned.splitlines() if line.strip()]
        line_one = lines[0] if lines else fallback
        line_two = lines[1] if len(lines) > 1 else line_one
        preview = "\n".join(lines[:4])
        return [
            f"Look at the line that sets the key value: {line_one}",
            f"Then make sure you include: {line_two}",
            f"One working solution starts like:\n{preview}"
        ]
    return [
        fallback,
        "Try updating one line at a time and re-check the output.",
        "Use the lesson instructions as a template for the correct structure."
    ]


def extract_variables(starter_code: str, max_vars: int = 2) -> List[str]:
    variables = []
    for line in (starter_code or "").splitlines():
        match = re.match(r"\s*([a-zA-Z_]\w*)\s*=", line)
        if match:
            variables.append(match.group(1))
        if len(variables) >= max_vars:
            break
    defaults = ["value", "result", "total", "count"]
    if not variables:
        variables = defaults[:max_vars]
    if len(variables) < max_vars:
        variables.extend(defaults[len(variables):max_vars])
    return variables[:max_vars]


def extract_sql_table(solution_code: str) -> str:
    match = re.search(r"from\s+([a-zA-Z_]\w*)", (solution_code or "").lower())
    return match.group(1) if match else "employees"


def load_course_order(path: Path) -> List[int]:
    if not path.exists():
        return []
    data = json.loads(path.read_text())
    order: List[int] = []
    for chapter in data.get("chapters", []):
        if "concepts" in chapter:
            for concept in chapter.get("concepts", []):
                for lesson in concept.get("lessons", []):
                    order.append(lesson["id"])
        else:
            for lesson in chapter.get("lessons", []):
                order.append(lesson["id"])
    return order


def build_hint_item(lesson: Dict[str, Any]) -> Dict[str, Any]:
    hints = build_hints(lesson.get("solution_code", ""), "Review the key line in the prompt.")
    return {"type": "hint_ladder", "hints": hints}


def build_send_item(template: str, template_id: str) -> Dict[str, Any]:
    return {"type": "send_to_editor", "template": template, "templateId": template_id}


def build_reset_item() -> Dict[str, Any]:
    return {"type": "reset_state", "label": "Reset interactions"}


def recipe_py_var_memory(lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    var_one, var_two = extract_variables(lesson.get("starter_code", ""), 2)
    plan = [
        {
            "type": "memory_machine",
            "title": "Assign the variables",
            "slots": [var_one, var_two],
            "steps": [
                {"label": f"Set {var_one}", "slot": var_one, "value": 5},
                {"label": f"Set {var_two}", "slot": var_two, "value": 12},
            ],
        },
        {"type": "state_inspector", "title": "Variables right now", "filter": [var_one, var_two]},
    ]
    template = f"{var_one} = {{{{{var_one}}}}}\n{var_two} = {{{{{var_two}}}}}\nprint({var_one})"
    return plan, template


def recipe_py_var_token(lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    var_name = extract_variables(lesson.get("starter_code", ""), 1)[0]
    plan = [
        {
            "type": "token_slot",
            "template": f"{var_name} = {{{{{var_name}}}}}\nprint({var_name})",
            "slots": [
                {
                    "id": var_name,
                    "label": "Pick a starter value",
                    "options": ["2", "7", "15"],
                    "correct": "7",
                }
            ],
        },
        {"type": "memory_box", "names": [var_name]},
    ]
    template = f"{var_name} = {{{{{var_name}}}}}\nprint({var_name})"
    return plan, template


def recipe_py_var_fill(lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    var_name = extract_variables(lesson.get("starter_code", ""), 1)[0]
    plan = [
        {
            "type": "fill_blanks",
            "template": f"{var_name} = {{value}}\nprint({var_name})",
            "blanks": [
                {"id": "value", "options": ["3", "6", "9"], "correct": "6"}
            ],
        },
        {"type": "memory_box", "names": [var_name]},
    ]
    template = f"{var_name} = {{value}}\nprint({var_name})"
    return plan, template


def recipe_py_var_debug(lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    var_name = extract_variables(lesson.get("starter_code", ""), 1)[0]
    snippet = f"{var_name} == 5\nprint({var_name})"
    plan = [
        {
            "type": "debug_quest",
            "title": "Fix the assignment bug",
            "snippet": snippet,
            "bugLine": 1,
            "options": [
                {"label": f"Use '=' to assign {var_name}", "fix": f"{var_name} = 5", "correct": True},
                {"label": "Wrap the value in quotes", "fix": f"{var_name} = \"5\"", "correct": False},
                {"label": "Move print to line 1", "fix": f"print({var_name})", "correct": False},
            ],
        },
    ]
    template = f"{var_name} = 5\nprint({var_name})"
    return plan, template


def recipe_py_string_token(lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    var_name = extract_variables(lesson.get("starter_code", ""), 1)[0]
    plan = [
        {
            "type": "draggable_value",
            "name": var_name,
            "acceptedValues": ["\"data\"", "\"python\"", "\"science\""],
            "chips": ["\"data\"", "\"python\"", "\"science\""],
            "label": f"Drop a value into {var_name}",
            "valueType": "string",
            "initial": "\"python\"",
        },
        {"type": "memory_box", "names": [var_name], "valueType": "string"},
    ]
    template = f"{var_name} = {{{{{var_name}}}}}\nprint({var_name})"
    return plan, template


def recipe_py_string_debug(lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    snippet = "first = \"Hello\"\nsecond = \"World\"\nprint(first + second)"
    plan = [
        {
            "type": "debug_quest",
            "title": "Fix the missing space",
            "snippet": snippet,
            "bugLine": 3,
            "options": [
                {"label": "Add a space between words", "fix": "print(first + \" \" + second)", "correct": True},
                {"label": "Swap the order", "fix": "print(second + first)", "correct": False},
                {"label": "Remove the plus", "fix": "print(first second)", "correct": False},
            ],
        }
    ]
    template = "first = \"Hello\"\nsecond = \"World\"\nprint(first + \" \" + second)"
    return plan, template


def recipe_py_string_memory(lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    var_name = extract_variables(lesson.get("starter_code", ""), 1)[0]
    plan = [
        {
            "type": "memory_machine",
            "title": "Load the message",
            "slots": [var_name],
            "steps": [
                {"label": f"Set {var_name}", "slot": var_name, "value": "Hello"},
                {"label": "Swap to goodbye", "slot": var_name, "value": "Goodbye"},
            ],
        }
    ]
    template = f"{var_name} = \"Hello\"\nprint({var_name})"
    return plan, template


def recipe_py_number_graph(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "graph_manipulator",
            "title": "Move x to see y",
            "mode": "linear",
            "slope": 2,
            "intercept": 1,
            "xMin": -3,
            "xMax": 6,
            "initialX": 2,
            "xVar": "graph_x",
            "yVar": "graph_y",
        },
        {"type": "output_diff", "actualVar": "graph_y", "title": "Current y value"},
    ]
    template = "x = {{graph_x}}\ny = 2 * x + 1\nprint(y)"
    return plan, template


def recipe_py_number_loop(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "loop_simulator",
            "label": "Watch the counter climb",
            "iterations": 5,
            "startValue": 0,
            "stepValue": 3,
            "valueVar": "loop_value",
            "stepVar": "loop_step",
        }
    ]
    template = "total = 0\nfor i in range({{loop_step}}):\n    total += 3\nprint(total)"
    return plan, template


def recipe_py_number_token(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "token_slot",
            "template": "result = 8 {{operator}} 4\nprint(result)",
            "slots": [
                {
                    "id": "operator",
                    "label": "Pick the operator",
                    "options": ["+", "-", "*"],
                    "correct": "*",
                }
            ],
        },
    ]
    template = "result = 8 {{operator}} 4\nprint(result)"
    return plan, template


def recipe_py_conditional_path(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "conditional_path",
            "prompt": "Choose a condition outcome",
            "choices": [
                {"label": "score > 10", "outcome": "True"},
                {"label": "score < 3", "outcome": "False"},
            ],
            "trueLabel": "Print: high score!",
            "falseLabel": "Print: try again",
            "resultVar": "condition_result",
        },
    ]
    template = "score = 11\nif {{condition_result}}:\n    print(\"high score!\")\nelse:\n    print(\"try again\")"
    return plan, template


def recipe_py_loop_step(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "step_executor",
            "code": "total = 0\nfor i in range(3):\n    total += i\nprint(total)",
            "steps": [
                {"line": 1, "description": "Start total at 0", "stateChanges": {"total": 0}},
                {"line": 2, "description": "Enter loop", "stateChanges": {"i": 0}},
                {"line": 3, "description": "Add i", "stateChanges": {"total": 0}},
                {"line": 2, "description": "Next i", "stateChanges": {"i": 1}},
                {"line": 3, "description": "Add i", "stateChanges": {"total": 1}},
            ],
        }
    ]
    template = "total = 0\nfor i in range(3):\n    total += i\nprint(total)"
    return plan, template


def recipe_py_loop_memory(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "memory_machine",
            "title": "Loop state tracker",
            "slots": ["i", "total"],
            "steps": [
                {"label": "Start loop", "slot": "i", "value": 0},
                {"label": "Add to total", "slot": "total", "value": 0},
                {"label": "Next i", "slot": "i", "value": 1},
            ],
        }
    ]
    template = "total = 0\nfor i in range(2):\n    total += i\nprint(total)"
    return plan, template


def recipe_py_collection_table(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "visual_table",
            "title": "Collection preview",
            "dataRef": "python_scores",
            "columns": ["name", "score", "bonus"],
            "allowSort": True,
            "allowFilter": True,
            "allowRowHighlight": True,
            "highlightColumn": "score",
        }
    ]
    template = "scores = [12, 18, 24, 15]\nprint(scores[0])"
    return plan, template


def recipe_py_collection_transform(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "data_transform",
            "title": "Filter the list",
            "columns": ["name", "score", "bonus"],
            "beforeRows": [
                {"name": "alpha", "score": 12, "bonus": 3},
                {"name": "beta", "score": 18, "bonus": 0},
                {"name": "gamma", "score": 24, "bonus": 4},
            ],
            "filters": [
                {"id": "keep_high", "label": "score >= 18", "rows": [
                    {"name": "beta", "score": 18, "bonus": 0},
                    {"name": "gamma", "score": 24, "bonus": 4},
                ]},
                {"id": "keep_bonus", "label": "bonus > 0", "rows": [
                    {"name": "alpha", "score": 12, "bonus": 3},
                    {"name": "gamma", "score": 24, "bonus": 4},
                ]},
            ],
            "resultVar": "rows_kept",
        }
    ]
    template = "scores = [12, 18, 24]\nfiltered = [s for s in scores if s >= 18]\nprint(filtered)"
    return plan, template


def recipe_py_collection_debug(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    snippet = "scores = [12, 18, 24]\nprint(scores[3])"
    plan = [
        {
            "type": "debug_quest",
            "title": "Fix the index error",
            "snippet": snippet,
            "bugLine": 2,
            "options": [
                {"label": "Use index 2", "fix": "print(scores[2])", "correct": True},
                {"label": "Add quotes", "fix": "print(\"scores[3]\")", "correct": False},
                {"label": "Swap brackets", "fix": "print(scores(3))", "correct": False},
            ],
        }
    ]
    template = "scores = [12, 18, 24]\nprint(scores[2])"
    return plan, template


def recipe_py_general_live(lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    starter = lesson.get("starter_code") or "# Edit this line\nvalue = 3\nprint(value)"
    plan = [{"type": "live_code_block", "initialCode": starter, "language": "python", "highlightLine": 2}]
    template = starter
    return plan, template


def recipe_sql_schema_table(lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    table = extract_sql_table(lesson.get("solution_code", ""))
    plan = [
        {
            "type": "visual_table",
            "title": f"{table.title()} table",
            "dataRef": "sql_employees",
            "columns": ["id", "name", "department", "salary"],
            "allowSort": True,
            "allowFilter": True,
            "allowRowHighlight": True,
            "highlightColumn": "department",
        }
    ]
    template = f"SELECT * FROM {table};"
    return plan, template


def recipe_sql_schema_token(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "token_slot",
            "template": "SELECT {{columns}} FROM employees;",
            "slots": [
                {"id": "columns", "label": "Select columns", "options": ["*", "name, department", "name"], "correct": "*"}
            ],
        }
    ]
    template = "SELECT {{columns}} FROM employees;"
    return plan, template


def recipe_sql_schema_transform(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "data_transform",
            "title": "Highlight primary keys",
            "columns": ["id", "name", "department"],
            "beforeRows": [
                {"id": 1, "name": "Alice", "department": "Sales"},
                {"id": 2, "name": "Bob", "department": "Marketing"},
                {"id": 3, "name": "Charlie", "department": "Sales"},
            ],
            "filters": [
                {"id": "pk", "label": "id is unique", "rows": [
                    {"id": 1, "name": "Alice", "department": "Sales"},
                    {"id": 2, "name": "Bob", "department": "Marketing"},
                    {"id": 3, "name": "Charlie", "department": "Sales"},
                ]},
                {"id": "dup", "label": "duplicate id", "rows": [
                    {"id": 1, "name": "Alice", "department": "Sales"},
                    {"id": 1, "name": "Bob", "department": "Marketing"},
                ]},
            ],
        }
    ]
    template = "SELECT id, name FROM employees;"
    return plan, template


def recipe_sql_schema_debug(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    snippet = "SELECT id name FROM employees;"
    plan = [
        {
            "type": "debug_quest",
            "title": "Fix the missing comma",
            "snippet": snippet,
            "bugLine": 1,
            "options": [
                {"label": "Add comma between columns", "fix": "SELECT id, name FROM employees;", "correct": True},
                {"label": "Wrap table in quotes", "fix": "SELECT id name FROM \"employees\";", "correct": False},
                {"label": "Remove SELECT", "fix": "id, name FROM employees;", "correct": False},
            ],
        }
    ]
    template = "SELECT id, name FROM employees;"
    return plan, template


def recipe_sql_schema_join(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "join_visualizer",
            "leftTitle": "Orders",
            "rightTitle": "Customers",
            "leftRows": [
                {"order_id": 1, "customer_id": 10},
                {"order_id": 2, "customer_id": 20},
                {"order_id": 3, "customer_id": 10},
            ],
            "rightRows": [
                {"customer_id": 10, "name": "Avery"},
                {"customer_id": 20, "name": "Blake"},
            ],
            "leftKey": "customer_id",
            "rightKey": "customer_id",
            "joinTypes": ["JOIN", "LEFT JOIN"],
            "joinVar": "join_type",
            "resultVar": "join_rows",
        }
    ]
    template = "SELECT * FROM orders {{join_type}} customers ON orders.customer_id = customers.customer_id;"
    return plan, template


def recipe_sql_where_filter(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "data_transform",
            "title": "Filter by department",
            "columns": ["id", "name", "department", "salary"],
            "beforeRows": [
                {"id": 1, "name": "Alice", "department": "Sales", "salary": 75000},
                {"id": 2, "name": "Bob", "department": "Marketing", "salary": 90000},
                {"id": 3, "name": "Charlie", "department": "Sales", "salary": 72000},
            ],
            "filters": [
                {"id": "sales", "label": "department = 'Sales'", "rows": [
                    {"id": 1, "name": "Alice", "department": "Sales", "salary": 75000},
                    {"id": 3, "name": "Charlie", "department": "Sales", "salary": 72000},
                ]},
                {"id": "high", "label": "salary > 80000", "rows": [
                    {"id": 2, "name": "Bob", "department": "Marketing", "salary": 90000},
                ]},
            ],
        }
    ]
    template = "SELECT * FROM employees WHERE department = 'Sales';"
    return plan, template


def recipe_sql_where_token(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "token_slot",
            "template": "SELECT * FROM employees WHERE department = {{dept}};",
            "slots": [
                {"id": "dept", "label": "Pick a department", "options": ["'Sales'", "'Marketing'", "'Engineering'"], "correct": "'Sales'"}
            ],
        }
    ]
    template = "SELECT * FROM employees WHERE department = {{dept}};"
    return plan, template


def recipe_sql_where_debug(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    snippet = "SELECT * FROM employees WHERE salary > 50000"
    plan = [
        {
            "type": "debug_quest",
            "title": "Fix the missing semicolon",
            "snippet": snippet,
            "bugLine": 1,
            "options": [
                {"label": "Add a semicolon", "fix": "SELECT * FROM employees WHERE salary > 50000;", "correct": True},
                {"label": "Remove WHERE", "fix": "SELECT * FROM employees;", "correct": False},
                {"label": "Use commas", "fix": "SELECT * FROM employees, salary > 50000;", "correct": False},
            ],
        }
    ]
    template = "SELECT * FROM employees WHERE salary > 50000;"
    return plan, template


def recipe_sql_order_slider(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "variable_slider",
            "name": "sql_limit",
            "min": 1,
            "max": 5,
            "initial": 3,
            "label": "Limit results",
        },
        {
            "type": "visual_table",
            "title": "Orders",
            "dataRef": "sql_orders",
            "columns": ["order_id", "customer", "status", "spend"],
            "allowSort": True,
            "allowFilter": True,
            "allowRowHighlight": True,
            "highlightColumn": "spend",
        },
    ]
    template = "SELECT * FROM orders ORDER BY spend DESC LIMIT {{sql_limit}};"
    return plan, template


def recipe_sql_join_visual(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "join_visualizer",
            "leftTitle": "Employees",
            "rightTitle": "Departments",
            "leftRows": DEFAULT_LEFT_TABLE,
            "rightRows": DEFAULT_RIGHT_TABLE,
            "leftKey": "dept_id",
            "rightKey": "dept_id",
            "joinTypes": ["JOIN", "LEFT JOIN", "RIGHT JOIN"],
            "joinVar": "join_type",
            "resultVar": "join_rows",
        }
    ]
    template = "SELECT * FROM employees {{join_type}} departments ON employees.dept_id = departments.dept_id;"
    return plan, template


def recipe_sql_group_agg(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "token_slot",
            "template": "SELECT department, {{agg}}(salary) FROM employees GROUP BY department;",
            "slots": [
                {"id": "agg", "label": "Pick aggregate", "options": ["AVG", "SUM", "COUNT"], "correct": "AVG"}
            ],
        },
        {
            "type": "visual_table",
            "title": "Employees",
            "dataRef": "sql_employees",
            "columns": ["department", "salary"],
            "allowSort": True,
            "allowFilter": False,
        },
    ]
    template = "SELECT department, {{agg}}(salary) FROM employees GROUP BY department;"
    return plan, template


def recipe_sql_group_transform(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "data_transform",
            "title": "Group by department",
            "columns": ["department", "salary"],
            "beforeRows": [
                {"department": "Sales", "salary": 75000},
                {"department": "Sales", "salary": 72000},
                {"department": "Marketing", "salary": 90000},
            ],
            "filters": [
                {"id": "avg", "label": "AVG salary", "rows": [
                    {"department": "Sales", "salary": 73500},
                    {"department": "Marketing", "salary": 90000},
                ]},
                {"id": "count", "label": "COUNT rows", "rows": [
                    {"department": "Sales", "salary": 2},
                    {"department": "Marketing", "salary": 1},
                ]},
            ],
        }
    ]
    template = "SELECT department, AVG(salary) FROM employees GROUP BY department;"
    return plan, template


def recipe_sql_general_live(lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    starter = lesson.get("starter_code") or "SELECT * FROM employees;"
    plan = [{"type": "live_code_block", "initialCode": starter, "language": "sql", "highlightLine": 1}]
    template = starter
    return plan, template


def recipe_r_plot_toggle(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "draggable_value",
            "name": "r_geom",
            "acceptedValues": ["geom_point()", "geom_bar()", "geom_line()"],
            "chips": ["geom_point()", "geom_bar()", "geom_line()"],
            "label": "Pick a geom",
            "valueType": "string",
            "initial": "geom_point()",
        },
        {
            "type": "visual_table",
            "title": "Penguins",
            "dataRef": "r_penguins",
            "columns": ["species", "island", "bill_length", "body_mass"],
            "allowSort": True,
            "allowFilter": True,
            "allowRowHighlight": True,
            "highlightColumn": "body_mass",
        },
    ]
    template = "ggplot(penguins, aes(x = bill_length, y = body_mass)) + {{r_geom}}"
    return plan, template


def recipe_r_plot_debug(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    snippet = "ggplot(penguins, aes(x = bill_length, y = body_mass)) +\n  geom_point"
    plan = [
        {
            "type": "debug_quest",
            "title": "Fix the missing parentheses",
            "snippet": snippet,
            "bugLine": 2,
            "options": [
                {"label": "Use geom_point()", "fix": "geom_point()", "correct": True},
                {"label": "Replace with geom_bar()", "fix": "geom_bar()", "correct": False},
                {"label": "Remove the plus", "fix": "ggplot(penguins)", "correct": False},
            ],
        }
    ]
    template = "ggplot(penguins, aes(x = bill_length, y = body_mass)) + geom_point()"
    return plan, template


def recipe_r_plot_token(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "token_slot",
            "template": "ggplot(penguins, aes(x = {{xvar}}, y = {{yvar}})) + geom_point()",
            "slots": [
                {"id": "xvar", "label": "Pick x axis", "options": ["bill_length", "body_mass"], "correct": "bill_length"},
                {"id": "yvar", "label": "Pick y axis", "options": ["body_mass", "bill_length"], "correct": "body_mass"},
            ],
        }
    ]
    template = "ggplot(penguins, aes(x = {{xvar}}, y = {{yvar}})) + geom_point()"
    return plan, template


def recipe_r_filter_transform(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "data_transform",
            "title": "Filter penguins by mass",
            "columns": ["species", "body_mass"],
            "beforeRows": [
                {"species": "Adelie", "body_mass": 3600},
                {"species": "Chinstrap", "body_mass": 4050},
                {"species": "Gentoo", "body_mass": 5000},
            ],
            "filters": [
                {"id": "heavy", "label": ">= 4000", "rows": [
                    {"species": "Chinstrap", "body_mass": 4050},
                    {"species": "Gentoo", "body_mass": 5000},
                ]},
                {"id": "light", "label": "< 4000", "rows": [
                    {"species": "Adelie", "body_mass": 3600},
                ]},
            ],
            "resultVar": "rows_kept",
        }
    ]
    template = "filtered <- penguins[penguins$body_mass >= 4000, ]\nhead(filtered, 3)"
    return plan, template


def recipe_r_filter_token(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "token_slot",
            "template": "filtered <- penguins[penguins$body_mass {{op}} {{threshold}}, ]",
            "slots": [
                {"id": "op", "label": "Pick operator", "options": [">=", "<", ">"], "correct": ">="},
                {"id": "threshold", "label": "Pick threshold", "options": ["3800", "4200", "4600"], "correct": "4200"},
            ],
        }
    ]
    template = "filtered <- penguins[penguins$body_mass {{op}} {{threshold}}, ]"
    return plan, template


def recipe_r_vector_graph(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "graph_manipulator",
            "title": "Index the vector",
            "mode": "linear",
            "slope": 1,
            "intercept": 0,
            "xMin": 1,
            "xMax": 4,
            "initialX": 2,
            "xVar": "vector_index",
            "yVar": "vector_value",
        }
    ]
    template = "values <- c(10, 14, 22, 5)\nvalues[{{vector_index}}]"
    return plan, template


def recipe_r_vector_token(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "token_slot",
            "template": "values <- c(10, 14, 22, 5)\nvalues[{{index}}]",
            "slots": [
                {"id": "index", "label": "Pick index", "options": ["1", "2", "3", "4"], "correct": "2"},
            ],
        }
    ]
    template = "values <- c(10, 14, 22, 5)\nvalues[{{index}}]"
    return plan, template


def recipe_r_vector_loop(_: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    plan = [
        {
            "type": "loop_simulator",
            "label": "Step through the vector",
            "iterations": 4,
            "startValue": 0,
            "stepValue": 1,
            "valueVar": "vector_step",
            "stepVar": "vector_index",
        }
    ]
    template = "values <- c(10, 14, 22, 5)\nvalues[{{vector_index}}]"
    return plan, template


def recipe_r_general_live(lesson: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], str]:
    starter = lesson.get("starter_code") or "x <- 2\nx * 3"
    plan = [{"type": "live_code_block", "initialCode": starter, "language": "r", "highlightLine": 1}]
    template = starter
    return plan, template


RECIPE_BUILDERS = {
    "py_var_memory": recipe_py_var_memory,
    "py_var_token": recipe_py_var_token,
    "py_var_fill": recipe_py_var_fill,
    "py_var_debug": recipe_py_var_debug,
    "py_string_token": recipe_py_string_token,
    "py_string_debug": recipe_py_string_debug,
    "py_string_memory": recipe_py_string_memory,
    "py_number_graph": recipe_py_number_graph,
    "py_number_loop": recipe_py_number_loop,
    "py_number_token": recipe_py_number_token,
    "py_conditional_path": recipe_py_conditional_path,
    "py_loop_step": recipe_py_loop_step,
    "py_loop_memory": recipe_py_loop_memory,
    "py_collection_table": recipe_py_collection_table,
    "py_collection_transform": recipe_py_collection_transform,
    "py_collection_debug": recipe_py_collection_debug,
    "py_general_live": recipe_py_general_live,
    "sql_schema_table": recipe_sql_schema_table,
    "sql_schema_token": recipe_sql_schema_token,
    "sql_schema_transform": recipe_sql_schema_transform,
    "sql_schema_debug": recipe_sql_schema_debug,
    "sql_schema_join": recipe_sql_schema_join,
    "sql_where_filter": recipe_sql_where_filter,
    "sql_where_token": recipe_sql_where_token,
    "sql_where_debug": recipe_sql_where_debug,
    "sql_order_slider": recipe_sql_order_slider,
    "sql_join_visual": recipe_sql_join_visual,
    "sql_group_agg": recipe_sql_group_agg,
    "sql_group_transform": recipe_sql_group_transform,
    "sql_general_live": recipe_sql_general_live,
    "r_plot_toggle": recipe_r_plot_toggle,
    "r_plot_debug": recipe_r_plot_debug,
    "r_plot_token": recipe_r_plot_token,
    "r_filter_transform": recipe_r_filter_transform,
    "r_filter_token": recipe_r_filter_token,
    "r_vector_graph": recipe_r_vector_graph,
    "r_vector_token": recipe_r_vector_token,
    "r_vector_loop": recipe_r_vector_loop,
    "r_general_live": recipe_r_general_live,
}

RECIPE_OPTIONS = {
    "python": {
        "variables": ["py_var_memory", "py_var_token", "py_var_fill", "py_var_debug", "py_general_live"],
        "strings": ["py_string_token", "py_string_debug", "py_string_memory", "py_general_live"],
        "numbers": ["py_number_graph", "py_number_loop", "py_number_token", "py_general_live"],
        "conditionals": ["py_conditional_path", "py_var_debug", "py_var_token", "py_general_live"],
        "loops": ["py_loop_step", "py_loop_memory", "py_number_loop", "py_general_live"],
        "lists": ["py_collection_table", "py_collection_transform", "py_collection_debug", "py_general_live"],
        "dictionaries": ["py_collection_table", "py_collection_transform", "py_collection_debug", "py_general_live"],
        "sets": ["py_collection_table", "py_collection_transform", "py_collection_debug", "py_general_live"],
        "functions": ["py_var_debug", "py_string_token", "py_general_live", "py_var_token"],
        "debugging": ["py_var_debug", "py_collection_debug", "py_general_live", "py_var_token"],
        "general": ["py_var_token", "py_string_token", "py_general_live", "py_number_token"],
    },
    "sql": {
        "schema": ["sql_schema_table", "sql_schema_token", "sql_schema_transform", "sql_schema_debug", "sql_schema_join", "sql_general_live"],
        "select": ["sql_schema_token", "sql_schema_table", "sql_order_slider", "sql_schema_debug", "sql_general_live"],
        "where": ["sql_where_filter", "sql_where_token", "sql_where_debug", "sql_order_slider", "sql_general_live"],
        "order_by": ["sql_order_slider", "sql_schema_table", "sql_general_live", "sql_schema_token", "sql_schema_debug"],
        "limit": ["sql_order_slider", "sql_where_filter", "sql_schema_table", "sql_general_live", "sql_where_debug"],
        "join": ["sql_join_visual", "sql_schema_join", "sql_schema_transform", "sql_general_live", "sql_schema_table"],
        "group_by": ["sql_group_agg", "sql_group_transform", "sql_schema_table", "sql_where_filter", "sql_general_live"],
        "general": ["sql_schema_table", "sql_where_token", "sql_general_live", "sql_order_slider", "sql_schema_debug"],
    },
    "r": {
        "visualization": ["r_plot_toggle", "r_plot_token", "r_plot_debug", "r_general_live", "r_vector_graph"],
        "dplyr_filter": ["r_filter_transform", "r_filter_token", "r_plot_toggle", "r_general_live", "r_vector_graph"],
        "dplyr_select": ["r_filter_transform", "r_filter_token", "r_general_live", "r_plot_toggle", "r_vector_graph"],
        "dplyr_mutate": ["r_filter_transform", "r_filter_token", "r_general_live", "r_plot_toggle", "r_vector_graph"],
        "vectors": ["r_vector_graph", "r_vector_token", "r_vector_loop", "r_general_live", "r_filter_transform"],
        "dataframe": ["r_filter_transform", "r_filter_token", "r_plot_toggle", "r_general_live", "r_vector_graph"],
        "general": ["r_general_live", "r_plot_toggle", "r_plot_token", "r_vector_graph", "r_filter_transform"],
    },
}

RECIPE_POOLS = {
    "python": [key for key in RECIPE_BUILDERS.keys() if key.startswith("py_")],
    "sql": [key for key in RECIPE_BUILDERS.keys() if key.startswith("sql_")],
    "r": [key for key in RECIPE_BUILDERS.keys() if key.startswith("r_")],
}


def select_recipe(
    candidates: List[str],
    recent: List[str],
    chapter_id: int,
    chapter_totals: Dict[int, int],
    chapter_recipe_counts: Dict[int, Dict[str, int]],
    pool: List[str],
) -> str:
    def score_list(recipe_list: List[str]) -> List[Tuple[float, int, str]]:
        scored_local = []
        for recipe_id in recipe_list:
            consecutive_violation = len(recent) >= 2 and recent[-1] == recent[-2] == recipe_id
            count = chapter_recipe_counts.get(chapter_id, {}).get(recipe_id, 0)
            total = chapter_totals.get(chapter_id, 1)
            freq_violation = total >= 4 and (count + 1) / total > 0.25
            score = (2 if consecutive_violation else 0) + (1 if freq_violation else 0) + (count * 0.01)
            scored_local.append((score, count, recipe_id))
        return scored_local

    scored = score_list(candidates)
    if scored and all(score >= 1 for score, _, _ in scored) and pool:
        scored = score_list(pool)

    scored.sort(key=lambda item: (item[0], item[1]))
    return scored[0][2] if scored else candidates[0]


def build_plan(curriculum: str, tag: str, lesson: Dict[str, Any], recipe_id: str) -> Tuple[List[Dict[str, Any]], str]:
    builder = RECIPE_BUILDERS.get(recipe_id)
    if not builder:
        fallback_id = RECIPE_OPTIONS[curriculum]["general"][0]
        builder = RECIPE_BUILDERS[fallback_id]
        recipe_id = fallback_id
    plan, template = builder(lesson)
    plan.append(build_hint_item(lesson))
    plan.append(build_send_item(template, recipe_id))
    plan.append(build_reset_item())
    return plan, template


def main() -> None:
    if not LESSONS_PATH.exists():
        raise SystemExit(f"Missing lessons file at {LESSONS_PATH}")

    lessons = json.loads(LESSONS_PATH.read_text())
    course_order = {key: load_course_order(path) for key, path in COURSE_PATHS.items()}

    chapter_totals_by_curriculum: Dict[str, Dict[int, int]] = {"python": {}, "sql": {}, "r": {}}
    for lesson_key, lesson in lessons.items():
        chapter_id = int(lesson.get("chapter_id", 0))
        if not chapter_id:
            continue
        lesson_id = int(lesson_key)
        if lesson_id >= 2000:
            curriculum_key = "r"
        elif 1000 < lesson_id < 2000:
            curriculum_key = "sql"
        else:
            curriculum_key = "python"
        totals = chapter_totals_by_curriculum[curriculum_key]
        totals[chapter_id] = totals.get(chapter_id, 0) + 1

    manual_review_ids = []

    processed_ids = set()

    for curriculum, ordered_ids in course_order.items():
        recent_recipes: List[str] = []
        chapter_recipe_counts: Dict[int, Dict[str, int]] = {}
        rules = PYTHON_TAG_RULES if curriculum == "python" else SQL_TAG_RULES if curriculum == "sql" else R_TAG_RULES

        for lesson_id in ordered_ids:
            lesson = lessons.get(str(lesson_id))
            if not lesson:
                continue
            lesson["id"] = lesson_id

            text = normalize_text(f"{lesson.get('title', '')} {lesson.get('content', '')} {lesson.get('chapter_title', '')}")
            title_text = normalize_text(lesson.get("title", ""))
            tags, confidence = infer_tags(text, title_text, rules)
            primary_tag = tags[0]

            candidates = RECIPE_OPTIONS[curriculum].get(primary_tag, RECIPE_OPTIONS[curriculum]["general"])
            chapter_id = int(lesson.get("chapter_id", 0))
            recipe_id = select_recipe(
                candidates,
                recent_recipes,
                chapter_id,
                chapter_totals_by_curriculum[curriculum],
                chapter_recipe_counts,
                RECIPE_POOLS[curriculum],
            )
            plan, template = build_plan(curriculum, primary_tag, lesson, recipe_id)

            code_blocks = count_code_blocks(lesson.get("content", ""))
            is_project = any(keyword in title_text for keyword in ("project", "capstone", "challenge", "boss"))
            manual_review = confidence < 0.7 or code_blocks > 3 or is_project or len(tags) > 3

            lesson["concept_tags"] = tags
            lesson["interaction_plan"] = plan
            lesson["interaction_required"] = True
            lesson["send_to_editor_template"] = template
            lesson["interaction_recipe_id"] = recipe_id
            lesson["interaction_confidence"] = round(confidence, 2)
            lesson["manual_review"] = manual_review
            lesson["prediction_justification"] = None

            if manual_review:
                manual_review_ids.append(lesson_id)

            chapter_recipe_counts.setdefault(chapter_id, {})
            chapter_recipe_counts[chapter_id][recipe_id] = chapter_recipe_counts[chapter_id].get(recipe_id, 0) + 1
            recent_recipes.append(recipe_id)
            if len(recent_recipes) > 2:
                recent_recipes.pop(0)

            processed_ids.add(lesson_id)

    remaining_ids = sorted([int(key) for key in lessons.keys() if int(key) not in processed_ids])
    for lesson_id in remaining_ids:
        lesson = lessons.get(str(lesson_id))
        if not lesson:
            continue
        lesson["id"] = lesson_id

        if lesson_id >= 2000:
            curriculum = "r"
            rules = R_TAG_RULES
        elif 1000 < lesson_id < 2000:
            curriculum = "sql"
            rules = SQL_TAG_RULES
        else:
            curriculum = "python"
            rules = PYTHON_TAG_RULES

        text = normalize_text(f"{lesson.get('title', '')} {lesson.get('content', '')} {lesson.get('chapter_title', '')}")
        title_text = normalize_text(lesson.get("title", ""))
        tags, confidence = infer_tags(text, title_text, rules)
        primary_tag = tags[0]

        candidates = RECIPE_OPTIONS[curriculum].get(primary_tag, RECIPE_OPTIONS[curriculum]["general"])
        recipe_id = candidates[0]
        plan, template = build_plan(curriculum, primary_tag, lesson, recipe_id)

        code_blocks = count_code_blocks(lesson.get("content", ""))
        is_project = any(keyword in title_text for keyword in ("project", "capstone", "challenge", "boss"))
        manual_review = confidence < 0.7 or code_blocks > 3 or is_project or len(tags) > 3

        lesson["concept_tags"] = tags
        lesson["interaction_plan"] = plan
        lesson["interaction_required"] = True
        lesson["send_to_editor_template"] = template
        lesson["interaction_recipe_id"] = recipe_id
        lesson["interaction_confidence"] = round(confidence, 2)
        lesson["manual_review"] = manual_review
        lesson["prediction_justification"] = None

        if manual_review:
            manual_review_ids.append(lesson_id)

    LESSONS_PATH.write_text(json.dumps(lessons, indent=2))

    report_path = Path("scripts/interaction_plan_report.json")
    report = {
        "total_lessons": len(lessons),
        "manual_review_count": len(manual_review_ids),
        "manual_review_ids": manual_review_ids[:200]
    }
    report_path.write_text(json.dumps(report, indent=2))
    print(f"Updated {len(lessons)} lessons. Manual review: {len(manual_review_ids)}.")


if __name__ == "__main__":
    main()
