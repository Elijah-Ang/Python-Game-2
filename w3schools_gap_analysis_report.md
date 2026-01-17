# W3Schools Gap Analysis (Reference Benchmark)

This report maps W3Schools topics to existing lessons. No new chapters or W3Schools-labeled sections are proposed.

Impact rubric:
- impact_score = (category_weight 1-5) * 10 + status_weight (Missing=20, Partial=10, Covered=0)
- size S/M/L indicates expected effort per lesson update
- risk indicates likelihood of unintended pacing or conceptual regression

Legend:
- Covered: A strong direct match exists in current lessons.
- Partially Covered: Some overlap exists, but the topic needs reinforcement or a missing sub-concept.
- Missing: No clear lesson covers this topic; suggest insertion point.

## Top 20 Highest-Impact Upgrades (Python + SQL)
1. PY-009 | Variable Names | impact=75 | size=M | risk=low | target=39, 1, 2
2. PY-075 | Shorthand If | impact=73 | size=M | risk=low | target=23, 22, 24
3. PY-076 | Nested If | impact=73 | size=M | risk=low | target=23, 175, 22
4. SQL-004 | SQL Select Distinct | impact=70 | size=S | risk=low | target=1035, 1131, 1010
5. SQL-014 | SQL Select Top | impact=70 | size=S | risk=low | target=1131, 1010, 1200
6. SQL-037 | SQL Select Into | impact=70 | size=S | risk=low | target=1131, 1010, 1200
7. PY-010 | Assign Multiple Values | impact=65 | size=M | risk=low | target=15, 33, 135
8. PY-012 | Global Variables | impact=65 | size=M | risk=low | target=2, 3, 4
9. SQL-029 | SQL Full Join | impact=65 | size=L | risk=med | target=1049, 1044, 1046
10. SQL-064 | ADD CONSTRAINT | impact=65 | size=M | risk=med | target=1237, 1120, 1118
11. SQL-076 | CREATE INDEX | impact=65 | size=M | risk=med | target=1238, 1126, 1128
12. SQL-077 | CREATE OR REPLACE VIEW | impact=65 | size=M | risk=low | target=1144, 1199, 1145
13. SQL-079 | CREATE UNIQUE INDEX | impact=65 | size=M | risk=med | target=1238, 1120, 1126
14. SQL-086 | DROP CONSTRAINT | impact=65 | size=M | risk=med | target=1237, 1120, 1118
15. SQL-089 | DROP INDEX | impact=65 | size=M | risk=med | target=1238, 1126, 1128
16. PY-079 | Python While Loops | impact=64 | size=M | risk=low | target=19, 13, 20
17. PY-080 | Python For Loops | impact=64 | size=M | risk=low | target=13, 19, 20
18. PY-100 | Python String Formatting | impact=64 | size=M | risk=low | target=6, 54, 122
19. PY-192 | Python Built-in Functions | impact=64 | size=M | risk=low | target=31, 37, 128
20. SQL-015 | SQL Aggregate Functions | impact=64 | size=M | risk=low | target=1179, 1162, 1163

## Python Topic Coverage

- gap_id: PY-001
  topic: Python Intro
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-002
  topic: Python Get Started
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-003
  topic: Python Syntax
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Syntax rules are a major source of early errors; clarity here reduces confusion later.
  proposed_changes: Add a short “indentation + statement boundaries” callout and a common mistake example.

- gap_id: PY-004
  topic: Statements
  status: Covered
  covered_by: 22 (If Statements)
  insert_target: N/A
  why_it_matters: Syntax rules are a major source of early errors; clarity here reduces confusion later.
  proposed_changes: Add a short “indentation + statement boundaries” callout and a common mistake example.

- gap_id: PY-005
  topic: Python Output
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Printing output is the first feedback loop learners rely on.
  proposed_changes: Add a small exercise that prints mixed types and explains newline behavior.

- gap_id: PY-006
  topic: Print Numbers
  status: Missing
  covered_by: 9 (Numbers: Integers and Floats), 155 (Number Sequences)
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Printing output is the first feedback loop learners rely on.
  proposed_changes: Add a small exercise that prints mixed types and explains newline behavior.

- gap_id: PY-007
  topic: Python Comments
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Comments teach reading and maintainability early.
  proposed_changes: Add a brief example showing inline vs block comments and when to use each.

- gap_id: PY-008
  topic: Python Variables
  status: Covered
  covered_by: 2 (Naming Variables), 3 (Reassigning Variables), 4 (Multiple Variables)
  insert_target: N/A
  why_it_matters: Variables underpin all later work; naming and scope errors are common.
  proposed_changes: Add naming rules, a “rename safely” example, and a scope pitfall note.

- gap_id: PY-009
  topic: Variable Names
  status: Missing
  covered_by: 39 (Variable Scope), 1 (What is a Variable?), 2 (Naming Variables)
  insert_target: 4 (Functions)
  why_it_matters: Variables underpin all later work; naming and scope errors are common.
  proposed_changes: Add naming rules, a “rename safely” example, and a scope pitfall note.

- gap_id: PY-010
  topic: Assign Multiple Values
  status: Partially Covered
  covered_by: 15 (Accumulating Values), 33 (Return Values), 135 (Counting Missing Values)
  insert_target: N/A
  why_it_matters: Variables underpin all later work; naming and scope errors are common.
  proposed_changes: Add naming rules, a “rename safely” example, and a scope pitfall note.

- gap_id: PY-011
  topic: Output Variables
  status: Partially Covered
  covered_by: 2 (Naming Variables), 3 (Reassigning Variables), 4 (Multiple Variables)
  insert_target: N/A
  why_it_matters: Printing output is the first feedback loop learners rely on.
  proposed_changes: Add a small exercise that prints mixed types and explains newline behavior.

- gap_id: PY-012
  topic: Global Variables
  status: Partially Covered
  covered_by: 2 (Naming Variables), 3 (Reassigning Variables), 4 (Multiple Variables)
  insert_target: N/A
  why_it_matters: Variables underpin all later work; naming and scope errors are common.
  proposed_changes: Add naming rules, a “rename safely” example, and a scope pitfall note.

- gap_id: PY-013
  topic: Python Data Types
  status: Partially Covered
  covered_by: 149 (Converting Between Types), 169 (Data Transformer), 52 (CSV Data)
  insert_target: N/A
  why_it_matters: Type confusion causes subtle bugs and misunderstandings about operations.
  proposed_changes: Add casting examples and a “type mismatch” pitfall exercise.

- gap_id: PY-014
  topic: Python bytes
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Type confusion causes subtle bugs and misunderstandings about operations.
  proposed_changes: Add casting examples and a “type mismatch” pitfall exercise.

- gap_id: PY-015
  topic: Python bytearray
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Type confusion causes subtle bugs and misunderstandings about operations.
  proposed_changes: Add casting examples and a “type mismatch” pitfall exercise.

- gap_id: PY-016
  topic: Python memoryview
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-017
  topic: Python Numbers
  status: Covered
  covered_by: 9 (Numbers: Integers and Floats), 155 (Number Sequences)
  insert_target: N/A
  why_it_matters: Type confusion causes subtle bugs and misunderstandings about operations.
  proposed_changes: Add casting examples and a “type mismatch” pitfall exercise.

- gap_id: PY-018
  topic: Python Primitive Types
  status: Partially Covered
  covered_by: 149 (Converting Between Types), 123 (Type Conversion), 152 (Complex Type Conversion)
  insert_target: N/A
  why_it_matters: Type confusion causes subtle bugs and misunderstandings about operations.
  proposed_changes: Add casting examples and a “type mismatch” pitfall exercise.

- gap_id: PY-019
  topic: Python Casting
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Type confusion causes subtle bugs and misunderstandings about operations.
  proposed_changes: Add casting examples and a “type mismatch” pitfall exercise.

- gap_id: PY-020
  topic: Python Strings
  status: Covered
  covered_by: 142 (Splitting Strings), 5 (What are Strings?), 7 (F-Strings (Formatted Strings))
  insert_target: N/A
  why_it_matters: String operations show indexing and immutability early.
  proposed_changes: Add slicing and formatting examples plus a short transformation exercise.

- gap_id: PY-021
  topic: Slicing Strings
  status: Partially Covered
  covered_by: 142 (Splitting Strings), 5 (What are Strings?), 7 (F-Strings (Formatted Strings))
  insert_target: N/A
  why_it_matters: String operations show indexing and immutability early.
  proposed_changes: Add slicing and formatting examples plus a short transformation exercise.

- gap_id: PY-022
  topic: Modify Strings
  status: Partially Covered
  covered_by: 142 (Splitting Strings), 5 (What are Strings?), 7 (F-Strings (Formatted Strings))
  insert_target: N/A
  why_it_matters: String operations show indexing and immutability early.
  proposed_changes: Add slicing and formatting examples plus a short transformation exercise.

- gap_id: PY-023
  topic: Concatenate Strings
  status: Partially Covered
  covered_by: 142 (Splitting Strings), 5 (What are Strings?), 7 (F-Strings (Formatted Strings))
  insert_target: N/A
  why_it_matters: String operations show indexing and immutability early.
  proposed_changes: Add slicing and formatting examples plus a short transformation exercise.

- gap_id: PY-024
  topic: Format Strings
  status: Partially Covered
  covered_by: 142 (Splitting Strings), 5 (What are Strings?), 7 (F-Strings (Formatted Strings))
  insert_target: N/A
  why_it_matters: String operations show indexing and immutability early.
  proposed_changes: Add slicing and formatting examples plus a short transformation exercise.

- gap_id: PY-025
  topic: Escape Characters
  status: Partially Covered
  covered_by: 153 (Counting Characters)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-026
  topic: String Methods
  status: Covered
  covered_by: 8 (String Methods), 42 (List Methods), 45 (Dictionary Methods)
  insert_target: N/A
  why_it_matters: String operations show indexing and immutability early.
  proposed_changes: Add slicing and formatting examples plus a short transformation exercise.

- gap_id: PY-027
  topic: Python Booleans
  status: Covered
  covered_by: 12 (Booleans and Type Conversion), 116 (Boolean Indexing)
  insert_target: N/A
  why_it_matters: Booleans drive conditionals; weak understanding breaks branching.
  proposed_changes: Add a truth-table mini example and a comparison pitfall.

- gap_id: PY-028
  topic: Python Operators
  status: Covered
  covered_by: 25 (Comparison Operators), 30 (Ternary Operator)
  insert_target: N/A
  why_it_matters: Operator precedence and comparisons are a frequent error source.
  proposed_changes: Add a precedence example and a “parentheses fix” exercise.

- gap_id: PY-029
  topic: Arithmetic Operators
  status: Partially Covered
  covered_by: 25 (Comparison Operators), 30 (Ternary Operator), 127 (Array Arithmetic)
  insert_target: N/A
  why_it_matters: Operator precedence and comparisons are a frequent error source.
  proposed_changes: Add a precedence example and a “parentheses fix” exercise.

- gap_id: PY-030
  topic: Assignment Operators
  status: Partially Covered
  covered_by: 25 (Comparison Operators), 11 (Compound Assignment), 30 (Ternary Operator)
  insert_target: N/A
  why_it_matters: Operator precedence and comparisons are a frequent error source.
  proposed_changes: Add a precedence example and a “parentheses fix” exercise.

- gap_id: PY-031
  topic: Comparison Operators
  status: Covered
  covered_by: 25 (Comparison Operators), 30 (Ternary Operator), 192 (Array Comparison)
  insert_target: N/A
  why_it_matters: Operator precedence and comparisons are a frequent error source.
  proposed_changes: Add a precedence example and a “parentheses fix” exercise.

- gap_id: PY-032
  topic: Logical Operators
  status: Partially Covered
  covered_by: 25 (Comparison Operators), 26 (Logical AND), 27 (Logical OR)
  insert_target: N/A
  why_it_matters: Operator precedence and comparisons are a frequent error source.
  proposed_changes: Add a precedence example and a “parentheses fix” exercise.

- gap_id: PY-033
  topic: Identity Operators
  status: Partially Covered
  covered_by: 25 (Comparison Operators), 30 (Ternary Operator)
  insert_target: N/A
  why_it_matters: Operator precedence and comparisons are a frequent error source.
  proposed_changes: Add a precedence example and a “parentheses fix” exercise.

- gap_id: PY-034
  topic: Membership Operators
  status: Partially Covered
  covered_by: 25 (Comparison Operators), 30 (Ternary Operator)
  insert_target: N/A
  why_it_matters: Operator precedence and comparisons are a frequent error source.
  proposed_changes: Add a precedence example and a “parentheses fix” exercise.

- gap_id: PY-035
  topic: Bitwise Operators
  status: Partially Covered
  covered_by: 25 (Comparison Operators), 30 (Ternary Operator)
  insert_target: N/A
  why_it_matters: Operator precedence and comparisons are a frequent error source.
  proposed_changes: Add a precedence example and a “parentheses fix” exercise.

- gap_id: PY-036
  topic: Operator Precedence
  status: Missing
  covered_by: 30 (Ternary Operator), 25 (Comparison Operators)
  insert_target: 3 (Logic & Control Flow)
  why_it_matters: Operator precedence and comparisons are a frequent error source.
  proposed_changes: Add a precedence example and a “parentheses fix” exercise.

- gap_id: PY-037
  topic: Python Lists
  status: Covered
  covered_by: 41 (Lists Basics), 43 (List Slicing), 172 (List Deduplication)
  insert_target: N/A
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-038
  topic: Access List Items
  status: Missing
  covered_by: 171 (Top N Items), 41 (Lists Basics), 43 (List Slicing)
  insert_target: 7 (Data Structures)
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-039
  topic: Change List Items
  status: Missing
  covered_by: 171 (Top N Items), 41 (Lists Basics), 43 (List Slicing)
  insert_target: 7 (Data Structures)
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-040
  topic: Add List Items
  status: Missing
  covered_by: 171 (Top N Items), 41 (Lists Basics), 43 (List Slicing)
  insert_target: 7 (Data Structures)
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-041
  topic: Remove List Items
  status: Missing
  covered_by: 171 (Top N Items), 41 (Lists Basics), 43 (List Slicing)
  insert_target: 7 (Data Structures)
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-042
  topic: Loop Lists
  status: Partially Covered
  covered_by: 41 (Lists Basics), 13 (For Loop Basics), 19 (While Loop Basics)
  insert_target: N/A
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-043
  topic: List Comprehension
  status: Covered
  covered_by: 48 (List Comprehension), 41 (Lists Basics), 43 (List Slicing)
  insert_target: N/A
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-044
  topic: Sort Lists
  status: Partially Covered
  covered_by: 41 (Lists Basics), 43 (List Slicing), 172 (List Deduplication)
  insert_target: N/A
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-045
  topic: Copy Lists
  status: Partially Covered
  covered_by: 41 (Lists Basics), 43 (List Slicing), 172 (List Deduplication)
  insert_target: N/A
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-046
  topic: Join Lists
  status: Partially Covered
  covered_by: 41 (Lists Basics), 43 (List Slicing), 172 (List Deduplication)
  insert_target: N/A
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-047
  topic: List Methods
  status: Covered
  covered_by: 42 (List Methods), 8 (String Methods), 45 (Dictionary Methods)
  insert_target: N/A
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-048
  topic: Python Tuples
  status: Covered
  covered_by: 46 (Tuples)
  insert_target: N/A
  why_it_matters: Immutable sequences appear in unpacking and function returns.
  proposed_changes: Add unpacking example and a “why tuples” contrast note.

- gap_id: PY-049
  topic: Access Tuples
  status: Covered
  covered_by: 46 (Tuples)
  insert_target: N/A
  why_it_matters: Immutable sequences appear in unpacking and function returns.
  proposed_changes: Add unpacking example and a “why tuples” contrast note.

- gap_id: PY-050
  topic: Update Tuples
  status: Covered
  covered_by: 46 (Tuples)
  insert_target: N/A
  why_it_matters: Immutable sequences appear in unpacking and function returns.
  proposed_changes: Add unpacking example and a “why tuples” contrast note.

- gap_id: PY-051
  topic: Unpack Tuples
  status: Covered
  covered_by: 46 (Tuples)
  insert_target: N/A
  why_it_matters: Immutable sequences appear in unpacking and function returns.
  proposed_changes: Add unpacking example and a “why tuples” contrast note.

- gap_id: PY-052
  topic: Loop Tuples
  status: Covered
  covered_by: 46 (Tuples), 13 (For Loop Basics), 19 (While Loop Basics)
  insert_target: N/A
  why_it_matters: Immutable sequences appear in unpacking and function returns.
  proposed_changes: Add unpacking example and a “why tuples” contrast note.

- gap_id: PY-053
  topic: Join Tuples
  status: Covered
  covered_by: 46 (Tuples)
  insert_target: N/A
  why_it_matters: Immutable sequences appear in unpacking and function returns.
  proposed_changes: Add unpacking example and a “why tuples” contrast note.

- gap_id: PY-054
  topic: Tuple Methods
  status: Partially Covered
  covered_by: 8 (String Methods), 42 (List Methods), 45 (Dictionary Methods)
  insert_target: N/A
  why_it_matters: Immutable sequences appear in unpacking and function returns.
  proposed_changes: Add unpacking example and a “why tuples” contrast note.

- gap_id: PY-055
  topic: Python Sets
  status: Covered
  covered_by: 47 (Sets)
  insert_target: N/A
  why_it_matters: Sets teach uniqueness and membership efficiently.
  proposed_changes: Add membership checks and a “dedupe” example.

- gap_id: PY-056
  topic: Access Set Items
  status: Missing
  covered_by: 171 (Top N Items), 47 (Sets)
  insert_target: 7 (Data Structures)
  why_it_matters: Sets teach uniqueness and membership efficiently.
  proposed_changes: Add membership checks and a “dedupe” example.

- gap_id: PY-057
  topic: Add Set Items
  status: Missing
  covered_by: 171 (Top N Items), 47 (Sets)
  insert_target: 7 (Data Structures)
  why_it_matters: Sets teach uniqueness and membership efficiently.
  proposed_changes: Add membership checks and a “dedupe” example.

- gap_id: PY-058
  topic: Remove Set Items
  status: Missing
  covered_by: 171 (Top N Items), 47 (Sets), 92 (Remove Duplicates)
  insert_target: 7 (Data Structures)
  why_it_matters: Sets teach uniqueness and membership efficiently.
  proposed_changes: Add membership checks and a “dedupe” example.

- gap_id: PY-059
  topic: Loop Sets
  status: Covered
  covered_by: 47 (Sets), 13 (For Loop Basics), 19 (While Loop Basics)
  insert_target: N/A
  why_it_matters: Sets teach uniqueness and membership efficiently.
  proposed_changes: Add membership checks and a “dedupe” example.

- gap_id: PY-060
  topic: Join Sets
  status: Covered
  covered_by: 47 (Sets)
  insert_target: N/A
  why_it_matters: Sets teach uniqueness and membership efficiently.
  proposed_changes: Add membership checks and a “dedupe” example.

- gap_id: PY-061
  topic: Frozenset
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-062
  topic: Set Methods
  status: Partially Covered
  covered_by: 8 (String Methods), 42 (List Methods), 45 (Dictionary Methods)
  insert_target: N/A
  why_it_matters: Sets teach uniqueness and membership efficiently.
  proposed_changes: Add membership checks and a “dedupe” example.

- gap_id: PY-063
  topic: Python Dictionaries
  status: Covered
  covered_by: 44 (Dictionaries), 174 (Merge Dictionaries)
  insert_target: N/A
  why_it_matters: Dictionaries are used everywhere; key errors are common.
  proposed_changes: Add get() vs [] and a missing-key pitfall.

- gap_id: PY-064
  topic: Access Items
  status: Partially Covered
  covered_by: 171 (Top N Items)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-065
  topic: Change Items
  status: Partially Covered
  covered_by: 171 (Top N Items)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-066
  topic: Add Items
  status: Partially Covered
  covered_by: 171 (Top N Items)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-067
  topic: Remove Items
  status: Partially Covered
  covered_by: 171 (Top N Items), 92 (Remove Duplicates)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-068
  topic: Loop Dictionaries
  status: Covered
  covered_by: 44 (Dictionaries), 174 (Merge Dictionaries), 13 (For Loop Basics)
  insert_target: N/A
  why_it_matters: Dictionaries are used everywhere; key errors are common.
  proposed_changes: Add get() vs [] and a missing-key pitfall.

- gap_id: PY-069
  topic: Copy Dictionaries
  status: Covered
  covered_by: 44 (Dictionaries), 174 (Merge Dictionaries)
  insert_target: N/A
  why_it_matters: Dictionaries are used everywhere; key errors are common.
  proposed_changes: Add get() vs [] and a missing-key pitfall.

- gap_id: PY-070
  topic: Nested Dictionaries
  status: Covered
  covered_by: 44 (Dictionaries), 174 (Merge Dictionaries), 175 (Nested Lookup)
  insert_target: N/A
  why_it_matters: Dictionaries are used everywhere; key errors are common.
  proposed_changes: Add get() vs [] and a missing-key pitfall.

- gap_id: PY-071
  topic: Dictionary Methods
  status: Covered
  covered_by: 45 (Dictionary Methods), 8 (String Methods), 42 (List Methods)
  insert_target: N/A
  why_it_matters: Dictionaries are used everywhere; key errors are common.
  proposed_changes: Add get() vs [] and a missing-key pitfall.

- gap_id: PY-072
  topic: Python If...Else
  status: Covered
  covered_by: 23 (If-Else), 24 (If-Elif-Else), 22 (If Statements)
  insert_target: N/A
  why_it_matters: Branching is a core reasoning skill for programs.
  proposed_changes: Add a multi-branch example and a “boundary case” exercise.

- gap_id: PY-073
  topic: Python Elif
  status: Covered
  covered_by: 24 (If-Elif-Else)
  insert_target: N/A
  why_it_matters: Branching is a core reasoning skill for programs.
  proposed_changes: Add a multi-branch example and a “boundary case” exercise.

- gap_id: PY-074
  topic: Python Else
  status: Covered
  covered_by: 23 (If-Else), 24 (If-Elif-Else)
  insert_target: N/A
  why_it_matters: Branching is a core reasoning skill for programs.
  proposed_changes: Add a multi-branch example and a “boundary case” exercise.

- gap_id: PY-075
  topic: Shorthand If
  status: Missing
  covered_by: 23 (If-Else), 22 (If Statements), 24 (If-Elif-Else)
  insert_target: 3 (Logic & Control Flow)
  why_it_matters: Branching is a core reasoning skill for programs.
  proposed_changes: Add a multi-branch example and a “boundary case” exercise.

- gap_id: PY-076
  topic: Nested If
  status: Missing
  covered_by: 23 (If-Else), 175 (Nested Lookup), 22 (If Statements)
  insert_target: 3 (Logic & Control Flow)
  why_it_matters: Branching is a core reasoning skill for programs.
  proposed_changes: Add a multi-branch example and a “boundary case” exercise.

- gap_id: PY-077
  topic: Pass Statement
  status: Missing
  covered_by: 22 (If Statements)
  insert_target: 3 (Logic & Control Flow)
  why_it_matters: Syntax rules are a major source of early errors; clarity here reduces confusion later.
  proposed_changes: Add a short “indentation + statement boundaries” callout and a common mistake example.

- gap_id: PY-078
  topic: Python Match
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-079
  topic: Python While Loops
  status: Partially Covered
  covered_by: 19 (While Loop Basics), 13 (For Loop Basics), 20 (Loop Control: break)
  insert_target: N/A
  why_it_matters: Loop control and range boundaries are high-friction for beginners.
  proposed_changes: Add an off-by-one example and a small accumulator exercise.

- gap_id: PY-080
  topic: Python For Loops
  status: Partially Covered
  covered_by: 13 (For Loop Basics), 19 (While Loop Basics), 20 (Loop Control: break)
  insert_target: N/A
  why_it_matters: Loop control and range boundaries are high-friction for beginners.
  proposed_changes: Add an off-by-one example and a small accumulator exercise.

- gap_id: PY-081
  topic: Python Data Processing
  status: Covered
  covered_by: 158 (Data Processing Loop), 169 (Data Transformer), 52 (CSV Data)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-082
  topic: Python Functions
  status: Covered
  covered_by: 31 (Defining Functions), 37 (Lambda Functions), 128 (Universal Functions (ufuncs))
  insert_target: N/A
  why_it_matters: Functions enable reuse; parameter/return confusion is common.
  proposed_changes: Add an input/output tracing example and a “return vs print” exercise.

- gap_id: PY-083
  topic: Python Arguments
  status: Covered
  covered_by: 36 (Keyword Arguments)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-084
  topic: Python *args / **kwargs
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-085
  topic: Python Scope
  status: Covered
  covered_by: 39 (Variable Scope)
  insert_target: N/A
  why_it_matters: Functions enable reuse; parameter/return confusion is common.
  proposed_changes: Add an input/output tracing example and a “return vs print” exercise.

- gap_id: PY-086
  topic: Python Decorators
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-087
  topic: Python Lambda
  status: Covered
  covered_by: 37 (Lambda Functions)
  insert_target: N/A
  why_it_matters: Functions enable reuse; parameter/return confusion is common.
  proposed_changes: Add an input/output tracing example and a “return vs print” exercise.

- gap_id: PY-088
  topic: Python Recursion
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-089
  topic: Python Generators
  status: Missing
  covered_by: 188 (Combinations Generator)
  insert_target: 9 (Modules & Packages)
  why_it_matters: Iteration protocol explains for-loops and generators.
  proposed_changes: Add iterator example with iter()/next().

- gap_id: PY-090
  topic: Python Range
  status: Covered
  covered_by: 16 (Using range()), 98 (Range), 18 (range() with Step)
  insert_target: N/A
  why_it_matters: Loop control and range boundaries are high-friction for beginners.
  proposed_changes: Add an off-by-one example and a small accumulator exercise.

- gap_id: PY-091
  topic: Python Arrays
  status: Covered
  covered_by: 189 (Custom Arrays), 125 (Creating Special Arrays), 190 (Array Reshaping)
  insert_target: N/A
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-092
  topic: Python Iterators
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Iteration protocol explains for-loops and generators.
  proposed_changes: Add iterator example with iter()/next().

- gap_id: PY-093
  topic: Python Modules
  status: Covered
  covered_by: 59 (Importing Modules), 61 (Random Module), 62 (Datetime Module)
  insert_target: N/A
  why_it_matters: Imports and packages unlock real workflows.
  proposed_changes: Add a tiny “import + call” exercise and clarify pip vs import.

- gap_id: PY-094
  topic: Python Dates
  status: Covered
  covered_by: 143 (Converting Dates)
  insert_target: N/A
  why_it_matters: Dates/times are common in real data tasks.
  proposed_changes: Add basic datetime parsing example.

- gap_id: PY-095
  topic: Python Math
  status: Covered
  covered_by: 10 (Math Operations), 183 (Math Utilities), 191 (Element-wise Math)
  insert_target: N/A
  why_it_matters: Math utilities are used across problem solving.
  proposed_changes: Add a brief import + function example.

- gap_id: PY-096
  topic: Python JSON
  status: Covered
  covered_by: 53 (JSON Basics), 179 (JSON Navigator)
  insert_target: N/A
  why_it_matters: JSON is the most common data interchange format.
  proposed_changes: Add load/dump example and a nested object exercise.

- gap_id: PY-097
  topic: Python RegEx
  status: Covered
  covered_by: 224 (Regex Cleanup)
  insert_target: N/A
  why_it_matters: Pattern matching is powerful but error-prone.
  proposed_changes: Add a simple search vs match contrast.

- gap_id: PY-098
  topic: Python PIP
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Imports and packages unlock real workflows.
  proposed_changes: Add a tiny “import + call” exercise and clarify pip vs import.

- gap_id: PY-099
  topic: Python Try...Except
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Error handling builds resilience and debugging skills.
  proposed_changes: Add try/except structure + common errors exercise.

- gap_id: PY-100
  topic: Python String Formatting
  status: Missing
  covered_by: 6 (String Concatenation), 54 (String Processing), 122 (String Cleanup)
  insert_target: 8 (File Handling)
  why_it_matters: String operations show indexing and immutability early.
  proposed_changes: Add slicing and formatting examples plus a short transformation exercise.

- gap_id: PY-101
  topic: Python None
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-102
  topic: Python User Input
  status: Covered
  covered_by: 151 (Parsing User Input), 157 (Input Validation)
  insert_target: N/A
  why_it_matters: Input enables interactive scripts and reinforces types.
  proposed_changes: Add input() + type casting exercise.

- gap_id: PY-103
  topic: Python VirtualEnv
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-104
  topic: Python OOP
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-105
  topic: Python Classes/Objects
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: OOP is conceptually dense; learners often mix up class vs instance state.
  proposed_changes: Add a state diagram example and a “class vs instance” pitfall.

- gap_id: PY-106
  topic: Python __init__ Method
  status: Missing
  covered_by: 8 (String Methods), 42 (List Methods), 45 (Dictionary Methods)
  insert_target: 7 (Data Structures)
  why_it_matters: OOP is conceptually dense; learners often mix up class vs instance state.
  proposed_changes: Add a state diagram example and a “class vs instance” pitfall.

- gap_id: PY-107
  topic: Python self Parameter
  status: Missing
  covered_by: 32 (Function Parameters), 34 (Multiple Parameters), 35 (Default Parameters)
  insert_target: 4 (Functions)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-108
  topic: Python Class Properties
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: OOP is conceptually dense; learners often mix up class vs instance state.
  proposed_changes: Add a state diagram example and a “class vs instance” pitfall.

- gap_id: PY-109
  topic: Python Class Methods
  status: Partially Covered
  covered_by: 8 (String Methods), 42 (List Methods), 45 (Dictionary Methods)
  insert_target: N/A
  why_it_matters: OOP is conceptually dense; learners often mix up class vs instance state.
  proposed_changes: Add a state diagram example and a “class vs instance” pitfall.

- gap_id: PY-110
  topic: Python Inheritance
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: OOP is conceptually dense; learners often mix up class vs instance state.
  proposed_changes: Add a state diagram example and a “class vs instance” pitfall.

- gap_id: PY-111
  topic: Python Polymorphism
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-112
  topic: Python Encapsulation
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-113
  topic: Python Inner Classes
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: OOP is conceptually dense; learners often mix up class vs instance state.
  proposed_changes: Add a state diagram example and a “class vs instance” pitfall.

- gap_id: PY-114
  topic: Python File Handling
  status: Missing
  covered_by: 227 (Error Handling), 75 (Handling Missing Data), 119 (Handling Missing Data)
  insert_target: 10 (Pandas & Data Wrangling)
  why_it_matters: File I/O is required for practical scripting.
  proposed_changes: Add a read/write example and a path handling note.

- gap_id: PY-115
  topic: Python Read Files
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: File I/O is required for practical scripting.
  proposed_changes: Add a read/write example and a path handling note.

- gap_id: PY-116
  topic: Python Write/Create Files
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: File I/O is required for practical scripting.
  proposed_changes: Add a read/write example and a path handling note.

- gap_id: PY-117
  topic: Python Delete Files
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: File I/O is required for practical scripting.
  proposed_changes: Add a read/write example and a path handling note.

- gap_id: PY-118
  topic: Getting Started
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-119
  topic: Mean Median Mode
  status: Covered
  covered_by: 96 (Median), 97 (Mode), 138 (Filling with Median)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-120
  topic: Standard Deviation
  status: Covered
  covered_by: 100 (Standard Deviation), 134 (Variance and Standard Deviation)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-121
  topic: Percentile
  status: Covered
  covered_by: 101 (Percentiles), 133 (Percentiles and Quartiles)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-122
  topic: Data Distribution
  status: Missing
  covered_by: 169 (Data Transformer), 52 (CSV Data), 55 (Data Parsing)
  insert_target: 101 (Final Boss: Data Scientist)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-123
  topic: Normal Data Distribution
  status: Missing
  covered_by: 169 (Data Transformer), 52 (CSV Data), 55 (Data Parsing)
  insert_target: 101 (Final Boss: Data Scientist)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-124
  topic: Scatter Plot
  status: Covered
  covered_by: 79 (Scatter Plot), 77 (Line Plot), 207 (Density Plot)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-125
  topic: Linear Regression
  status: Covered
  covered_by: 105 (Linear Regression), 86 (Linear Search), 237 (Evaluating Regression Models)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-126
  topic: Polynomial Regression
  status: Missing
  covered_by: 105 (Linear Regression), 237 (Evaluating Regression Models)
  insert_target: 14 (Machine Learning Intro)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-127
  topic: Multiple Regression
  status: Missing
  covered_by: 105 (Linear Regression), 4 (Multiple Variables), 34 (Multiple Parameters)
  insert_target: 11 (Data Visualization)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-128
  topic: Scale
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-129
  topic: Train/Test
  status: Covered
  covered_by: 104 (Train/Test Split)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-130
  topic: Decision Tree
  status: Covered
  covered_by: 108 (Decision Tree), 162 (Nested Decision Tree)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-131
  topic: Confusion Matrix
  status: Covered
  covered_by: 111 (Confusion Matrix), 195 (Matrix Operations)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-132
  topic: Hierarchical Clustering
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-133
  topic: Logistic Regression
  status: Missing
  covered_by: 105 (Linear Regression), 237 (Evaluating Regression Models)
  insert_target: 14 (Machine Learning Intro)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-134
  topic: Grid Search
  status: Missing
  covered_by: 57 (Search in Text), 86 (Linear Search), 87 (Binary Search)
  insert_target: 12 (Algorithms)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-135
  topic: Categorical Data
  status: Missing
  covered_by: 169 (Data Transformer), 52 (CSV Data), 55 (Data Parsing)
  insert_target: 101 (Final Boss: Data Scientist)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-136
  topic: K-means
  status: Missing
  covered_by: 95 (Mean (Average)), 228 (Weighted Mean), 107 (K-Nearest Neighbors)
  insert_target: 13 (Statistics)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-137
  topic: Bootstrap Aggregation
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-138
  topic: Cross Validation
  status: Covered
  covered_by: 110 (Cross Validation), 157 (Input Validation)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-139
  topic: AUC - ROC Curve
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-140
  topic: K-nearest neighbors
  status: Covered
  covered_by: 107 (K-Nearest Neighbors)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-141
  topic: Python DSA
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-142
  topic: Lists and Arrays
  status: Partially Covered
  covered_by: 41 (Lists Basics), 189 (Custom Arrays), 125 (Creating Special Arrays)
  insert_target: N/A
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-143
  topic: Stacks
  status: Missing
  covered_by: 113 (💀 FINAL BOSS: Full Stack Data Scientist)
  insert_target: 101 (Final Boss: Data Scientist)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-144
  topic: Queues
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-145
  topic: Linked Lists
  status: Partially Covered
  covered_by: 41 (Lists Basics), 43 (List Slicing), 172 (List Deduplication)
  insert_target: N/A
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-146
  topic: Hash Tables
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-147
  topic: Trees
  status: Missing
  covered_by: 108 (Decision Tree), 162 (Nested Decision Tree)
  insert_target: 3 (Logic & Control Flow)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-148
  topic: Binary Trees
  status: Missing
  covered_by: 87 (Binary Search), 108 (Decision Tree), 162 (Nested Decision Tree)
  insert_target: 12 (Algorithms)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-149
  topic: Binary Search Trees
  status: Covered
  covered_by: 87 (Binary Search), 57 (Search in Text), 86 (Linear Search)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-150
  topic: AVL Trees
  status: Missing
  covered_by: 108 (Decision Tree), 162 (Nested Decision Tree)
  insert_target: 3 (Logic & Control Flow)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-151
  topic: Graphs
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-152
  topic: Linear Search
  status: Covered
  covered_by: 86 (Linear Search), 57 (Search in Text), 87 (Binary Search)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-153
  topic: Binary Search
  status: Covered
  covered_by: 87 (Binary Search), 57 (Search in Text), 86 (Linear Search)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-154
  topic: Bubble Sort
  status: Covered
  covered_by: 88 (Bubble Sort), 214 (Selection Sort), 215 (Insertion Sort)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-155
  topic: Selection Sort
  status: Covered
  covered_by: 214 (Selection Sort), 199 (Column Selection), 88 (Bubble Sort)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-156
  topic: Insertion Sort
  status: Covered
  covered_by: 215 (Insertion Sort), 88 (Bubble Sort), 214 (Selection Sort)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-157
  topic: Quick Sort
  status: Covered
  covered_by: 217 (Quick Sort), 88 (Bubble Sort), 214 (Selection Sort)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-158
  topic: Counting Sort
  status: Missing
  covered_by: 88 (Bubble Sort), 214 (Selection Sort), 215 (Insertion Sort)
  insert_target: 12 (Algorithms)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-159
  topic: Radix Sort
  status: Missing
  covered_by: 88 (Bubble Sort), 214 (Selection Sort), 215 (Insertion Sort)
  insert_target: 12 (Algorithms)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-160
  topic: Merge Sort
  status: Covered
  covered_by: 216 (Merge Sort), 88 (Bubble Sort), 214 (Selection Sort)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-161
  topic: MySQL Get Started
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-162
  topic: MySQL Create Database
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-163
  topic: MySQL Create Table
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-164
  topic: MySQL Insert
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-165
  topic: MySQL Select
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-166
  topic: MySQL Where
  status: Missing
  covered_by: 130 (np.where() Conditional Selection)
  insert_target: 95 (NumPy Fundamentals)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-167
  topic: MySQL Order By
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-168
  topic: MySQL Delete
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-169
  topic: MySQL Drop Table
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-170
  topic: MySQL Update
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-171
  topic: MySQL Limit
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-172
  topic: MySQL Join
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-173
  topic: MongoDB Get Started
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-174
  topic: MongoDB Create DB
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-175
  topic: MongoDB Collection
  status: Missing
  covered_by: 63 (Collections Module)
  insert_target: 9 (Modules & Packages)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-176
  topic: MongoDB Insert
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-177
  topic: MongoDB Find
  status: Missing
  covered_by: 89 (Find Maximum)
  insert_target: 12 (Algorithms)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-178
  topic: MongoDB Query
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-179
  topic: MongoDB Sort
  status: Missing
  covered_by: 88 (Bubble Sort), 214 (Selection Sort), 215 (Insertion Sort)
  insert_target: 12 (Algorithms)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-180
  topic: MongoDB Delete
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-181
  topic: MongoDB Drop Collection
  status: Missing
  covered_by: 63 (Collections Module)
  insert_target: 9 (Modules & Packages)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-182
  topic: MongoDB Update
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-183
  topic: MongoDB Limit
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-184
  topic: Python as Aspect Oriented
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-185
  topic: Python Database
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-186
  topic: Python Web Applications
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-187
  topic: Python Workflows
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-188
  topic: Python Maths & Science
  status: Missing
  covered_by: 10 (Math Operations), 183 (Math Utilities), 191 (Element-wise Math)
  insert_target: 9 (Modules & Packages)
  why_it_matters: Math utilities are used across problem solving.
  proposed_changes: Add a brief import + function example.

- gap_id: PY-189
  topic: Python Regular Expressions
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-190
  topic: Python Unit Testing
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-191
  topic: Python Overview
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-192
  topic: Python Built-in Functions
  status: Partially Covered
  covered_by: 31 (Defining Functions), 37 (Lambda Functions), 128 (Universal Functions (ufuncs))
  insert_target: N/A
  why_it_matters: Functions enable reuse; parameter/return confusion is common.
  proposed_changes: Add an input/output tracing example and a “return vs print” exercise.

- gap_id: PY-193
  topic: Python File Methods
  status: Partially Covered
  covered_by: 8 (String Methods), 42 (List Methods), 45 (Dictionary Methods)
  insert_target: N/A
  why_it_matters: File I/O is required for practical scripting.
  proposed_changes: Add a read/write example and a path handling note.

- gap_id: PY-194
  topic: Python Keywords
  status: Missing
  covered_by: 36 (Keyword Arguments)
  insert_target: 4 (Functions)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-195
  topic: Python Exceptions
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Error handling builds resilience and debugging skills.
  proposed_changes: Add try/except structure + common errors exercise.

- gap_id: PY-196
  topic: Python Glossary
  status: Missing
  covered_by: None
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: PY-197
  topic: Built-in Modules
  status: Partially Covered
  covered_by: 59 (Importing Modules), 61 (Random Module), 62 (Datetime Module)
  insert_target: N/A
  why_it_matters: Imports and packages unlock real workflows.
  proposed_changes: Add a tiny “import + call” exercise and clarify pip vs import.

- gap_id: PY-198
  topic: Remove List Duplicates
  status: Covered
  covered_by: 92 (Remove Duplicates), 121 (Removing Duplicates), 140 (Duplicates in Specific Columns)
  insert_target: N/A
  why_it_matters: Lists are core data structures; mutation and indexing must be clear.
  proposed_changes: Add before/after mutation examples and a small list update exercise.

- gap_id: PY-199
  topic: Reverse a String
  status: Missing
  covered_by: 6 (String Concatenation), 54 (String Processing), 122 (String Cleanup)
  insert_target: 12 (Algorithms)
  why_it_matters: String operations show indexing and immutability early.
  proposed_changes: Add slicing and formatting examples plus a short transformation exercise.

- gap_id: PY-200
  topic: Add Two Numbers
  status: Missing
  covered_by: 9 (Numbers: Integers and Floats), 93 (Two Sum), 155 (Number Sequences)
  insert_target: 1 (Variables, Types & Memory)
  why_it_matters: Type confusion causes subtle bugs and misunderstandings about operations.
  proposed_changes: Add casting examples and a “type mismatch” pitfall exercise.

## SQL Topic Coverage

- gap_id: SQL-001
  topic: SQL Intro
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-002
  topic: SQL Syntax
  status: Covered
  covered_by: 1066 (Basic CTE Syntax)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-003
  topic: SQL Select
  status: Covered
  covered_by: 1131 (Avoiding SELECT *), 1010 (Your First SELECT), 1200 (SELECT Subqueries)
  insert_target: N/A
  why_it_matters: SELECT is the backbone of querying.
  proposed_changes: Add a focused example with column selection and aliasing.

- gap_id: SQL-004
  topic: SQL Select Distinct
  status: Missing
  covered_by: 1035 (COUNT DISTINCT), 1131 (Avoiding SELECT *), 1010 (Your First SELECT)
  insert_target: 203 (Aggregations & Grouping)
  why_it_matters: SELECT is the backbone of querying.
  proposed_changes: Add a focused example with column selection and aliasing.

- gap_id: SQL-005
  topic: SQL Where
  status: Covered
  covered_by: 1016 (WHERE Basics), 1056 (Subquery in WHERE), 1042 (WHERE vs HAVING)
  insert_target: N/A
  why_it_matters: Filtering rows correctly is foundational for all analysis.
  proposed_changes: Add a multi-condition example and a “common filter mistakes” note.

- gap_id: SQL-006
  topic: SQL Order By
  status: Covered
  covered_by: 1021 (ORDER BY Sorting), 1244 (Join Order), 1009 (Query Execution Order)
  insert_target: N/A
  why_it_matters: Sorting and limiting results are common in real queries.
  proposed_changes: Add an ORDER BY + LIMIT example and a stable ordering note.

- gap_id: SQL-007
  topic: SQL And
  status: Covered
  covered_by: 1038 (MIN and MAX), 1064 (INTERSECT and EXCEPT), 1079 (RANK and DENSE_RANK)
  insert_target: N/A
  why_it_matters: Filtering rows correctly is foundational for all analysis.
  proposed_changes: Add a multi-condition example and a “common filter mistakes” note.

- gap_id: SQL-008
  topic: SQL Or
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: Filtering rows correctly is foundational for all analysis.
  proposed_changes: Add a multi-condition example and a “common filter mistakes” note.

- gap_id: SQL-009
  topic: SQL Not
  status: Covered
  covered_by: 1059 (NOT EXISTS), 1028 (IS NULL and IS NOT NULL), 1197 (NOT EXISTS Pattern)
  insert_target: N/A
  why_it_matters: Filtering rows correctly is foundational for all analysis.
  proposed_changes: Add a multi-condition example and a “common filter mistakes” note.

- gap_id: SQL-010
  topic: SQL Insert Into
  status: Partially Covered
  covered_by: 1132 (INSERT Basics), 1134 (INSERT from SELECT), 1133 (INSERT Multiple Rows)
  insert_target: N/A
  why_it_matters: DML is essential for data maintenance.
  proposed_changes: Add a multi-row INSERT example.

- gap_id: SQL-011
  topic: SQL Null Values
  status: Partially Covered
  covered_by: 1249 (Default Values), 1007 (NULL Basics), 1027 (Understanding NULL)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-012
  topic: SQL Update
  status: Covered
  covered_by: 1135 (UPDATE Basics), 1250 (Conditional Update), 1251 (Batch Update)
  insert_target: N/A
  why_it_matters: Unsafe updates are a common production mistake.
  proposed_changes: Add a “missing WHERE” caution and a targeted update exercise.

- gap_id: SQL-013
  topic: SQL Delete
  status: Covered
  covered_by: 1137 (DELETE Basics), 1138 (DELETE with Conditions)
  insert_target: N/A
  why_it_matters: Deletes are dangerous without filters.
  proposed_changes: Add a “confirm rows first” tip and a safe delete exercise.

- gap_id: SQL-014
  topic: SQL Select Top
  status: Missing
  covered_by: 1131 (Avoiding SELECT *), 1010 (Your First SELECT), 1200 (SELECT Subqueries)
  insert_target: 212 (Mutations & Transactions)
  why_it_matters: SELECT is the backbone of querying.
  proposed_changes: Add a focused example with column selection and aliasing.

- gap_id: SQL-015
  topic: SQL Aggregate Functions
  status: Partially Covered
  covered_by: 1179 (String Functions), 1162 (Quiz: Window Functions I), 1163 (Quiz: Window Functions II)
  insert_target: N/A
  why_it_matters: Aggregations are core to analytics queries.
  proposed_changes: Add a simple group/aggregate example and a grouping pitfall.

- gap_id: SQL-016
  topic: SQL Min and Max
  status: Covered
  covered_by: 1038 (MIN and MAX), 1064 (INTERSECT and EXCEPT), 1079 (RANK and DENSE_RANK)
  insert_target: N/A
  why_it_matters: Filtering rows correctly is foundational for all analysis.
  proposed_changes: Add a multi-condition example and a “common filter mistakes” note.

- gap_id: SQL-017
  topic: SQL Count
  status: Covered
  covered_by: 1034 (COUNT Function), 1035 (COUNT DISTINCT), 1184 (Conditional COUNT)
  insert_target: N/A
  why_it_matters: Aggregations are core to analytics queries.
  proposed_changes: Add a simple group/aggregate example and a grouping pitfall.

- gap_id: SQL-018
  topic: SQL Sum
  status: Covered
  covered_by: 1036 (SUM Function), 1214 (Cumulative Sum), 1185 (NULL-aware SUM)
  insert_target: N/A
  why_it_matters: Aggregations are core to analytics queries.
  proposed_changes: Add a simple group/aggregate example and a grouping pitfall.

- gap_id: SQL-019
  topic: SQL Avg
  status: Covered
  covered_by: 1037 (AVG Function)
  insert_target: N/A
  why_it_matters: Aggregations are core to analytics queries.
  proposed_changes: Add a simple group/aggregate example and a grouping pitfall.

- gap_id: SQL-020
  topic: SQL Like
  status: Covered
  covered_by: 1020 (LIKE Pattern Matching)
  insert_target: N/A
  why_it_matters: Filtering rows correctly is foundational for all analysis.
  proposed_changes: Add a multi-condition example and a “common filter mistakes” note.

- gap_id: SQL-021
  topic: SQL Wildcards
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-022
  topic: SQL In
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: Filtering rows correctly is foundational for all analysis.
  proposed_changes: Add a multi-condition example and a “common filter mistakes” note.

- gap_id: SQL-023
  topic: SQL Between
  status: Covered
  covered_by: 1019 (BETWEEN Operator)
  insert_target: N/A
  why_it_matters: Filtering rows correctly is foundational for all analysis.
  proposed_changes: Add a multi-condition example and a “common filter mistakes” note.

- gap_id: SQL-024
  topic: SQL Aliases
  status: Covered
  covered_by: 1014 (Table Aliases), 1013 (Column Aliases with AS)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-025
  topic: SQL Joins
  status: Covered
  covered_by: 1053 (Self Joins), 1043 (Why We Need Joins), 1052 (Duplicate Rows in Joins)
  insert_target: N/A
  why_it_matters: Joins are the core relational skill; errors are frequent.
  proposed_changes: Add a join diagram explanation and a “missing matches” pitfall.

- gap_id: SQL-026
  topic: SQL Inner Join
  status: Covered
  covered_by: 1044 (INNER JOIN Basics), 1045 (INNER JOIN Multiple Tables), 1046 (LEFT JOIN Basics)
  insert_target: N/A
  why_it_matters: Joins are the core relational skill; errors are frequent.
  proposed_changes: Add a join diagram explanation and a “missing matches” pitfall.

- gap_id: SQL-027
  topic: SQL Left Join
  status: Covered
  covered_by: 1046 (LEFT JOIN Basics), 1047 (LEFT JOIN for Missing Data), 1044 (INNER JOIN Basics)
  insert_target: N/A
  why_it_matters: Joins are the core relational skill; errors are frequent.
  proposed_changes: Add a join diagram explanation and a “missing matches” pitfall.

- gap_id: SQL-028
  topic: SQL Right Join
  status: Covered
  covered_by: 1048 (RIGHT JOIN), 1044 (INNER JOIN Basics), 1046 (LEFT JOIN Basics)
  insert_target: N/A
  why_it_matters: Joins are the core relational skill; errors are frequent.
  proposed_changes: Add a join diagram explanation and a “missing matches” pitfall.

- gap_id: SQL-029
  topic: SQL Full Join
  status: Partially Covered
  covered_by: 1049 (FULL OUTER JOIN), 1044 (INNER JOIN Basics), 1046 (LEFT JOIN Basics)
  insert_target: N/A
  why_it_matters: Joins are the core relational skill; errors are frequent.
  proposed_changes: Add a join diagram explanation and a “missing matches” pitfall.

- gap_id: SQL-030
  topic: SQL Self Join
  status: Covered
  covered_by: 1053 (Self Joins), 1044 (INNER JOIN Basics), 1191 (Self-Referential)
  insert_target: N/A
  why_it_matters: Joins are the core relational skill; errors are frequent.
  proposed_changes: Add a join diagram explanation and a “missing matches” pitfall.

- gap_id: SQL-031
  topic: SQL Union
  status: Covered
  covered_by: 1062 (UNION Operator), 1063 (UNION ALL), 1202 (Union Dedup)
  insert_target: N/A
  why_it_matters: UNION/INTERSECT/EXCEPT broaden query composition.
  proposed_changes: Add a UNION example and a column compatibility note.

- gap_id: SQL-032
  topic: SQL Union All
  status: Covered
  covered_by: 1063 (UNION ALL), 1062 (UNION Operator), 1202 (Union Dedup)
  insert_target: N/A
  why_it_matters: UNION/INTERSECT/EXCEPT broaden query composition.
  proposed_changes: Add a UNION example and a column compatibility note.

- gap_id: SQL-033
  topic: SQL Group By
  status: Covered
  covered_by: 1039 (GROUP BY Basics), 1210 (Window vs GROUP BY), 1040 (GROUP BY Multiple Columns)
  insert_target: N/A
  why_it_matters: Aggregations are core to analytics queries.
  proposed_changes: Add a simple group/aggregate example and a grouping pitfall.

- gap_id: SQL-034
  topic: SQL Having
  status: Covered
  covered_by: 1041 (HAVING Clause), 1042 (WHERE vs HAVING)
  insert_target: N/A
  why_it_matters: HAVING is often confused with WHERE.
  proposed_changes: Add a side-by-side WHERE vs HAVING example.

- gap_id: SQL-035
  topic: SQL Exists
  status: Covered
  covered_by: 1058 (EXISTS Operator), 1059 (NOT EXISTS), 1196 (Double EXISTS)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-036
  topic: SQL Any, All
  status: Missing
  covered_by: 1063 (UNION ALL), 1012 (SELECT All Columns)
  insert_target: 205 (Subqueries & Set Operations)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-037
  topic: SQL Select Into
  status: Missing
  covered_by: 1131 (Avoiding SELECT *), 1010 (Your First SELECT), 1200 (SELECT Subqueries)
  insert_target: 212 (Mutations & Transactions)
  why_it_matters: SELECT is the backbone of querying.
  proposed_changes: Add a focused example with column selection and aliasing.

- gap_id: SQL-038
  topic: SQL Insert Into Select
  status: Partially Covered
  covered_by: 1134 (INSERT from SELECT), 1132 (INSERT Basics), 1131 (Avoiding SELECT *)
  insert_target: N/A
  why_it_matters: SELECT is the backbone of querying.
  proposed_changes: Add a focused example with column selection and aliasing.

- gap_id: SQL-039
  topic: SQL Case
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: CASE adds conditional logic inside SQL.
  proposed_changes: Add a CASE-based categorization example.

- gap_id: SQL-040
  topic: SQL Null Functions
  status: Partially Covered
  covered_by: 1179 (String Functions), 1162 (Quiz: Window Functions I), 1163 (Quiz: Window Functions II)
  insert_target: N/A
  why_it_matters: Built-in SQL functions are used constantly.
  proposed_changes: Add 2-3 function examples and a quick exercise.

- gap_id: SQL-041
  topic: SQL Stored Procedures
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: Procedures are common in production systems.
  proposed_changes: Add a short explanation and a placeholder example.

- gap_id: SQL-042
  topic: SQL Comments
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-043
  topic: SQL Operators
  status: Covered
  covered_by: 1017 (Comparison Operators), 1018 (IN Operator), 1019 (BETWEEN Operator)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-044
  topic: SQL Create DB
  status: Missing
  covered_by: 1153 (Cloud vs Traditional DB)
  insert_target: 214 (Cloud Warehouse Features)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-045
  topic: SQL Drop DB
  status: Missing
  covered_by: 1153 (Cloud vs Traditional DB)
  insert_target: 214 (Cloud Warehouse Features)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-046
  topic: SQL Backup DB
  status: Missing
  covered_by: 1153 (Cloud vs Traditional DB)
  insert_target: 214 (Cloud Warehouse Features)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-047
  topic: SQL Create Table
  status: Missing
  covered_by: 1239 (Table Design), 1156 (Table Partitioning), 1014 (Table Aliases)
  insert_target: 204 (Joins Like a Pro)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-048
  topic: SQL Drop Table
  status: Missing
  covered_by: 1239 (Table Design), 1156 (Table Partitioning), 1014 (Table Aliases)
  insert_target: 204 (Joins Like a Pro)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-049
  topic: SQL Alter Table
  status: Missing
  covered_by: 1239 (Table Design), 1156 (Table Partitioning), 1014 (Table Aliases)
  insert_target: 204 (Joins Like a Pro)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-050
  topic: SQL Constraints
  status: Covered
  covered_by: 1120 (Unique Constraints), 1118 (Primary Key Constraints), 1119 (Foreign Key Constraints)
  insert_target: N/A
  why_it_matters: Constraints enforce data integrity and prevent bad data.
  proposed_changes: Add PRIMARY KEY and FOREIGN KEY examples with a why note.

- gap_id: SQL-051
  topic: SQL Not Null
  status: Partially Covered
  covered_by: 1007 (NULL Basics), 1028 (IS NULL and IS NOT NULL), 1027 (Understanding NULL)
  insert_target: N/A
  why_it_matters: Filtering rows correctly is foundational for all analysis.
  proposed_changes: Add a multi-condition example and a “common filter mistakes” note.

- gap_id: SQL-052
  topic: SQL Unique
  status: Covered
  covered_by: 1120 (Unique Constraints)
  insert_target: N/A
  why_it_matters: Constraints enforce data integrity and prevent bad data.
  proposed_changes: Add PRIMARY KEY and FOREIGN KEY examples with a why note.

- gap_id: SQL-053
  topic: SQL Primary Key
  status: Covered
  covered_by: 1003 (Primary Keys), 1118 (Primary Key Constraints), 1157 (Clustering Keys)
  insert_target: N/A
  why_it_matters: Constraints enforce data integrity and prevent bad data.
  proposed_changes: Add PRIMARY KEY and FOREIGN KEY examples with a why note.

- gap_id: SQL-054
  topic: SQL Foreign Key
  status: Covered
  covered_by: 1119 (Foreign Key Constraints), 1004 (Foreign Keys & Relationships), 1003 (Primary Keys)
  insert_target: N/A
  why_it_matters: Constraints enforce data integrity and prevent bad data.
  proposed_changes: Add PRIMARY KEY and FOREIGN KEY examples with a why note.

- gap_id: SQL-055
  topic: SQL Check
  status: Covered
  covered_by: 1232 (Completeness Check), 1233 (Consistency Check), 1108 (Data Quality Checks)
  insert_target: N/A
  why_it_matters: Constraints enforce data integrity and prevent bad data.
  proposed_changes: Add PRIMARY KEY and FOREIGN KEY examples with a why note.

- gap_id: SQL-056
  topic: SQL Default
  status: Covered
  covered_by: 1249 (Default Values)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-057
  topic: SQL Index
  status: Covered
  covered_by: 1238 (Index Creation), 1126 (Index Trade-offs), 1128 (Sequential vs Index Scan)
  insert_target: N/A
  why_it_matters: Indexes explain performance tradeoffs.
  proposed_changes: Add a short “when to index” example and caution.

- gap_id: SQL-058
  topic: SQL Auto Increment
  status: Missing
  covered_by: 1262 (Auto-Scaling & Elasticity)
  insert_target: 214 (Cloud Warehouse Features)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-059
  topic: SQL Dates
  status: Missing
  covered_by: 1180 (Date Formatting), 1086 (Date Truncation), 1219 (Date Range)
  insert_target: 201 (SELECT Basics)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-060
  topic: SQL Views
  status: Covered
  covered_by: 1199 (Inline Views), 1145 (Updatable Views), 1146 (Materialized Views)
  insert_target: N/A
  why_it_matters: Views encapsulate complex queries for reuse.
  proposed_changes: Add a CREATE VIEW example and a simple use case.

- gap_id: SQL-061
  topic: SQL Injection
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-062
  topic: SQL Data Types
  status: Partially Covered
  covered_by: 1022 (Integer Types), 1024 (Text Types), 1245 (Scan Types)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-063
  topic: ADD
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-064
  topic: ADD CONSTRAINT
  status: Missing
  covered_by: 1237 (Constraint Testing), 1120 (Unique Constraints), 1118 (Primary Key Constraints)
  insert_target: 210 (Database Design Essentials)
  why_it_matters: Constraints enforce data integrity and prevent bad data.
  proposed_changes: Add PRIMARY KEY and FOREIGN KEY examples with a why note.

- gap_id: SQL-065
  topic: ALL
  status: Covered
  covered_by: 1063 (UNION ALL), 1012 (SELECT All Columns)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-066
  topic: ALTER
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-067
  topic: ALTER COLUMN
  status: Missing
  covered_by: 1241 (Audit Columns), 1011 (Selecting Multiple Columns), 1012 (SELECT All Columns)
  insert_target: 203 (Aggregations & Grouping)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-068
  topic: ANY
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-069
  topic: AS
  status: Covered
  covered_by: 1013 (Column Aliases with AS)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-070
  topic: ASC
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-071
  topic: BACKUP DATABASE
  status: Missing
  covered_by: 1001 (What is a Database?)
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-072
  topic: COLUMN
  status: Covered
  covered_by: 1241 (Audit Columns), 1011 (Selecting Multiple Columns), 1012 (SELECT All Columns)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-073
  topic: CONSTRAINT
  status: Covered
  covered_by: 1237 (Constraint Testing), 1120 (Unique Constraints), 1118 (Primary Key Constraints)
  insert_target: N/A
  why_it_matters: Constraints enforce data integrity and prevent bad data.
  proposed_changes: Add PRIMARY KEY and FOREIGN KEY examples with a why note.

- gap_id: SQL-074
  topic: CREATE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-075
  topic: CREATE DATABASE
  status: Missing
  covered_by: 1001 (What is a Database?)
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-076
  topic: CREATE INDEX
  status: Missing
  covered_by: 1238 (Index Creation), 1126 (Index Trade-offs), 1128 (Sequential vs Index Scan)
  insert_target: 210 (Database Design Essentials)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-077
  topic: CREATE OR REPLACE VIEW
  status: Missing
  covered_by: 1144 (View Basics), 1199 (Inline Views), 1145 (Updatable Views)
  insert_target: 212 (Mutations & Transactions)
  why_it_matters: Filtering rows correctly is foundational for all analysis.
  proposed_changes: Add a multi-condition example and a “common filter mistakes” note.

- gap_id: SQL-078
  topic: CREATE PROCEDURE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-079
  topic: CREATE UNIQUE INDEX
  status: Missing
  covered_by: 1238 (Index Creation), 1120 (Unique Constraints), 1126 (Index Trade-offs)
  insert_target: 210 (Database Design Essentials)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-080
  topic: CREATE VIEW
  status: Partially Covered
  covered_by: 1144 (View Basics), 1199 (Inline Views), 1145 (Updatable Views)
  insert_target: N/A
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-081
  topic: DATABASE
  status: Covered
  covered_by: 1001 (What is a Database?)
  insert_target: N/A
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-082
  topic: DESC
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-083
  topic: DISTINCT
  status: Covered
  covered_by: 1035 (COUNT DISTINCT)
  insert_target: N/A
  why_it_matters: DISTINCT prevents accidental double counting.
  proposed_changes: Add a duplicate-removal example and a warning about DISTINCT + aggregates.

- gap_id: SQL-084
  topic: DROP
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-085
  topic: DROP COLUMN
  status: Missing
  covered_by: 1241 (Audit Columns), 1011 (Selecting Multiple Columns), 1012 (SELECT All Columns)
  insert_target: 203 (Aggregations & Grouping)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-086
  topic: DROP CONSTRAINT
  status: Missing
  covered_by: 1237 (Constraint Testing), 1120 (Unique Constraints), 1118 (Primary Key Constraints)
  insert_target: 210 (Database Design Essentials)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-087
  topic: DROP DATABASE
  status: Missing
  covered_by: 1001 (What is a Database?)
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-088
  topic: DROP DEFAULT
  status: Missing
  covered_by: 1249 (Default Values)
  insert_target: 212 (Mutations & Transactions)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-089
  topic: DROP INDEX
  status: Missing
  covered_by: 1238 (Index Creation), 1126 (Index Trade-offs), 1128 (Sequential vs Index Scan)
  insert_target: 210 (Database Design Essentials)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-090
  topic: DROP VIEW
  status: Partially Covered
  covered_by: 1144 (View Basics), 1199 (Inline Views), 1145 (Updatable Views)
  insert_target: N/A
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-091
  topic: EXEC
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-092
  topic: FROM
  status: Covered
  covered_by: 1134 (INSERT from SELECT)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-093
  topic: FULL OUTER JOIN
  status: Covered
  covered_by: 1049 (FULL OUTER JOIN), 1193 (Outer Join Uses), 1044 (INNER JOIN Basics)
  insert_target: N/A
  why_it_matters: Joins are the core relational skill; errors are frequent.
  proposed_changes: Add a join diagram explanation and a “missing matches” pitfall.

- gap_id: SQL-094
  topic: IS NULL
  status: Partially Covered
  covered_by: 1007 (NULL Basics), 1028 (IS NULL and IS NOT NULL), 1005 (SQL is Declarative)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-095
  topic: IS NOT NULL
  status: Covered
  covered_by: 1028 (IS NULL and IS NOT NULL), 1007 (NULL Basics), 1005 (SQL is Declarative)
  insert_target: N/A
  why_it_matters: Filtering rows correctly is foundational for all analysis.
  proposed_changes: Add a multi-condition example and a “common filter mistakes” note.

- gap_id: SQL-096
  topic: JOIN
  status: Covered
  covered_by: 1044 (INNER JOIN Basics), 1046 (LEFT JOIN Basics), 1048 (RIGHT JOIN)
  insert_target: N/A
  why_it_matters: Joins are the core relational skill; errors are frequent.
  proposed_changes: Add a join diagram explanation and a “missing matches” pitfall.

- gap_id: SQL-097
  topic: LIMIT
  status: Covered
  covered_by: 1015 (LIMIT Clause)
  insert_target: N/A
  why_it_matters: Sorting and limiting results are common in real queries.
  proposed_changes: Add an ORDER BY + LIMIT example and a stable ordering note.

- gap_id: SQL-098
  topic: OUTER JOIN
  status: Covered
  covered_by: 1049 (FULL OUTER JOIN), 1193 (Outer Join Uses), 1044 (INNER JOIN Basics)
  insert_target: N/A
  why_it_matters: Joins are the core relational skill; errors are frequent.
  proposed_changes: Add a join diagram explanation and a “missing matches” pitfall.

- gap_id: SQL-099
  topic: PROCEDURE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: Procedures are common in production systems.
  proposed_changes: Add a short explanation and a placeholder example.

- gap_id: SQL-100
  topic: ROWNUM
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-101
  topic: SET
  status: Covered
  covered_by: 1006 (Result Sets), 1168 (Quiz: Set Operations I), 1169 (Quiz: Set Operations II)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-102
  topic: TABLE
  status: Covered
  covered_by: 1239 (Table Design), 1156 (Table Partitioning), 1014 (Table Aliases)
  insert_target: N/A
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-103
  topic: TOP
  status: Covered
  covered_by: 1211 (Top N per Group)
  insert_target: N/A
  why_it_matters: Sorting and limiting results are common in real queries.
  proposed_changes: Add an ORDER BY + LIMIT example and a stable ordering note.

- gap_id: SQL-104
  topic: TRUNCATE TABLE
  status: Missing
  covered_by: 1239 (Table Design), 1156 (Table Partitioning), 1014 (Table Aliases)
  insert_target: 204 (Joins Like a Pro)
  why_it_matters: DDL defines structure and constraints; it is required for schema work.
  proposed_changes: Add a CREATE TABLE example with constraints and data types.

- gap_id: SQL-105
  topic: VALUES
  status: Covered
  covered_by: 1249 (Default Values), 1194 (Multi-value IN), 1084 (FIRST_VALUE and LAST_VALUE)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-106
  topic: VIEW
  status: Covered
  covered_by: 1144 (View Basics), 1199 (Inline Views), 1145 (Updatable Views)
  insert_target: N/A
  why_it_matters: Views encapsulate complex queries for reuse.
  proposed_changes: Add a CREATE VIEW example and a simple use case.

- gap_id: SQL-107
  topic: MySQL Functions
  status: Partially Covered
  covered_by: 1179 (String Functions), 1162 (Quiz: Window Functions I), 1163 (Quiz: Window Functions II)
  insert_target: N/A
  why_it_matters: Built-in SQL functions are used constantly.
  proposed_changes: Add 2-3 function examples and a quick exercise.

- gap_id: SQL-108
  topic: ASCII
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-109
  topic: CHAR_LENGTH
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-110
  topic: CHARACTER_LENGTH
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-111
  topic: CONCAT
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-112
  topic: CONCAT_WS
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-113
  topic: FIELD
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-114
  topic: FIND_IN_SET
  status: Missing
  covered_by: 1203 (Intersection Find), 1006 (Result Sets), 1168 (Quiz: Set Operations I)
  insert_target: 205 (Subqueries & Set Operations)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-115
  topic: FORMAT
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-116
  topic: INSERT
  status: Covered
  covered_by: 1132 (INSERT Basics), 1134 (INSERT from SELECT), 1133 (INSERT Multiple Rows)
  insert_target: N/A
  why_it_matters: DML is essential for data maintenance.
  proposed_changes: Add a multi-row INSERT example.

- gap_id: SQL-117
  topic: INSTR
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-118
  topic: LCASE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-119
  topic: LEFT
  status: Covered
  covered_by: 1046 (LEFT JOIN Basics), 1047 (LEFT JOIN for Missing Data)
  insert_target: N/A
  why_it_matters: Joins are the core relational skill; errors are frequent.
  proposed_changes: Add a join diagram explanation and a “missing matches” pitfall.

- gap_id: SQL-120
  topic: LENGTH
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-121
  topic: LOCATE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-122
  topic: LOWER
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-123
  topic: LPAD
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-124
  topic: LTRIM
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-125
  topic: MID
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-126
  topic: POSITION
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-127
  topic: REPEAT
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-128
  topic: REPLACE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-129
  topic: REVERSE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-130
  topic: RIGHT
  status: Covered
  covered_by: 1048 (RIGHT JOIN), 1264 (Choose the Right Warehouse)
  insert_target: N/A
  why_it_matters: Joins are the core relational skill; errors are frequent.
  proposed_changes: Add a join diagram explanation and a “missing matches” pitfall.

- gap_id: SQL-131
  topic: RPAD
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-132
  topic: RTRIM
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-133
  topic: SPACE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-134
  topic: STRCMP
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-135
  topic: SUBSTR
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-136
  topic: SUBSTRING
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-137
  topic: SUBSTRING_INDEX
  status: Missing
  covered_by: 1238 (Index Creation), 1126 (Index Trade-offs), 1128 (Sequential vs Index Scan)
  insert_target: 210 (Database Design Essentials)
  why_it_matters: Indexes explain performance tradeoffs.
  proposed_changes: Add a short “when to index” example and caution.

- gap_id: SQL-138
  topic: TRIM
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-139
  topic: UCASE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-140
  topic: UPPER
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-141
  topic: ABS
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-142
  topic: ACOS
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-143
  topic: ASIN
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-144
  topic: ATAN
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-145
  topic: ATAN2
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-146
  topic: CEIL
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-147
  topic: CEILING
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-148
  topic: COS
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-149
  topic: COT
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-150
  topic: DEGREES
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-151
  topic: DIV
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-152
  topic: EXP
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-153
  topic: FLOOR
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-154
  topic: GREATEST
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-155
  topic: LEAST
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-156
  topic: LN
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-157
  topic: LOG
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-158
  topic: LOG10
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-159
  topic: LOG2
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-160
  topic: MAX
  status: Covered
  covered_by: 1038 (MIN and MAX)
  insert_target: N/A
  why_it_matters: Aggregations are core to analytics queries.
  proposed_changes: Add a simple group/aggregate example and a grouping pitfall.

- gap_id: SQL-161
  topic: MIN
  status: Covered
  covered_by: 1038 (MIN and MAX)
  insert_target: N/A
  why_it_matters: Aggregations are core to analytics queries.
  proposed_changes: Add a simple group/aggregate example and a grouping pitfall.

- gap_id: SQL-162
  topic: MOD
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-163
  topic: PI
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-164
  topic: POW
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-165
  topic: POWER
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-166
  topic: RADIANS
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-167
  topic: RAND
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-168
  topic: ROUND
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-169
  topic: SIGN
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-170
  topic: SIN
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-171
  topic: SQRT
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-172
  topic: TAN
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-173
  topic: TRUNCATE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-174
  topic: ADDDATE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-175
  topic: ADDTIME
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-176
  topic: CURDATE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-177
  topic: CURRENT_DATE
  status: Missing
  covered_by: 1180 (Date Formatting), 1086 (Date Truncation), 1219 (Date Range)
  insert_target: 201 (SELECT Basics)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-178
  topic: CURRENT_TIME
  status: Missing
  covered_by: 1171 (Quiz: Date/Time I), 1172 (Quiz: Date/Time II), 1173 (Quiz: Date/Time III)
  insert_target: 201 (SELECT Basics)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-179
  topic: CURRENT_TIMESTAMP
  status: Missing
  covered_by: 1025 (Date and Timestamp Types)
  insert_target: 202 (Data Types, NULLs & Calculations)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-180
  topic: CURTIME
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-181
  topic: DATE
  status: Covered
  covered_by: 1180 (Date Formatting), 1086 (Date Truncation), 1219 (Date Range)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-182
  topic: DATEDIFF
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-183
  topic: DATE_ADD
  status: Missing
  covered_by: 1180 (Date Formatting), 1086 (Date Truncation), 1219 (Date Range)
  insert_target: 201 (SELECT Basics)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-184
  topic: DATE_FORMAT
  status: Covered
  covered_by: 1180 (Date Formatting), 1086 (Date Truncation), 1219 (Date Range)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-185
  topic: DATE_SUB
  status: Missing
  covered_by: 1180 (Date Formatting), 1086 (Date Truncation), 1219 (Date Range)
  insert_target: 201 (SELECT Basics)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-186
  topic: DAY
  status: Covered
  covered_by: 1221 (Business Days)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-187
  topic: DAYNAME
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-188
  topic: DAYOFMONTH
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-189
  topic: DAYOFWEEK
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-190
  topic: DAYOFYEAR
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-191
  topic: EXTRACT
  status: Covered
  covered_by: 1090 (EXTRACT Function)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-192
  topic: FROM_DAYS
  status: Partially Covered
  covered_by: 1221 (Business Days), 1134 (INSERT from SELECT)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-193
  topic: HOUR
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-194
  topic: LAST_DAY
  status: Missing
  covered_by: 1221 (Business Days), 1084 (FIRST_VALUE and LAST_VALUE), 1101 (Keeping First/Last Record)
  insert_target: 208 (Time-Series SQL)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-195
  topic: LOCALTIME
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-196
  topic: LOCALTIMESTAMP
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-197
  topic: MAKEDATE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-198
  topic: MAKETIME
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-199
  topic: MICROSECOND
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-200
  topic: MINUTE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-201
  topic: MONTH
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-202
  topic: MONTHNAME
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-203
  topic: NOW
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-204
  topic: PERIOD_ADD
  status: Missing
  covered_by: 1217 (Period Comparison), 1218 (Period Grouping), 1088 (Grouping by Time Periods)
  insert_target: 208 (Time-Series SQL)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-205
  topic: PERIOD_DIFF
  status: Missing
  covered_by: 1217 (Period Comparison), 1218 (Period Grouping), 1088 (Grouping by Time Periods)
  insert_target: 208 (Time-Series SQL)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-206
  topic: QUARTER
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-207
  topic: SECOND
  status: Covered
  covered_by: 1114 (Second and Third Normal Form)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-208
  topic: SEC_TO_TIME
  status: Missing
  covered_by: 1171 (Quiz: Date/Time I), 1172 (Quiz: Date/Time II), 1173 (Quiz: Date/Time III)
  insert_target: 201 (SELECT Basics)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-209
  topic: STR_TO_DATE
  status: Missing
  covered_by: 1180 (Date Formatting), 1086 (Date Truncation), 1219 (Date Range)
  insert_target: 201 (SELECT Basics)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-210
  topic: SUBDATE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-211
  topic: SUBTIME
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-212
  topic: SYSDATE
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-213
  topic: TIME
  status: Covered
  covered_by: 1171 (Quiz: Date/Time I), 1172 (Quiz: Date/Time II), 1173 (Quiz: Date/Time III)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-214
  topic: TIME_FORMAT
  status: Missing
  covered_by: 1171 (Quiz: Date/Time I), 1172 (Quiz: Date/Time II), 1173 (Quiz: Date/Time III)
  insert_target: 201 (SELECT Basics)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-215
  topic: TIME_TO_SEC
  status: Missing
  covered_by: 1171 (Quiz: Date/Time I), 1172 (Quiz: Date/Time II), 1173 (Quiz: Date/Time III)
  insert_target: 201 (SELECT Basics)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-216
  topic: TIMEDIFF
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-217
  topic: TIMESTAMP
  status: Covered
  covered_by: 1025 (Date and Timestamp Types)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-218
  topic: TO_DAYS
  status: Partially Covered
  covered_by: 1221 (Business Days)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-219
  topic: WEEK
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-220
  topic: WEEKDAY
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-221
  topic: WEEKOFYEAR
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-222
  topic: YEAR
  status: Covered
  covered_by: 1097 (Year-over-Year Comparisons)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-223
  topic: YEARWEEK
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-224
  topic: BIN
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-225
  topic: BINARY
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-226
  topic: CAST
  status: Covered
  covered_by: 1032 (CAST and Type Conversion)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-227
  topic: COALESCE
  status: Covered
  covered_by: 1030 (COALESCE Function)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-228
  topic: CONNECTION_ID
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-229
  topic: CONV
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-230
  topic: CONVERT
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-231
  topic: CURRENT_USER
  status: Missing
  covered_by: 1223 (First-Time Users), 1106 (Active User Definitions)
  insert_target: 208 (Time-Series SQL)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-232
  topic: IF
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-233
  topic: IFNULL
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-234
  topic: ISNULL
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-235
  topic: LAST_INSERT_ID
  status: Missing
  covered_by: 1132 (INSERT Basics), 1134 (INSERT from SELECT), 1084 (FIRST_VALUE and LAST_VALUE)
  insert_target: 212 (Mutations & Transactions)
  why_it_matters: DML is essential for data maintenance.
  proposed_changes: Add a multi-row INSERT example.

- gap_id: SQL-236
  topic: NULLIF
  status: Covered
  covered_by: 1031 (NULLIF Function), 1033 (Safe Division with NULLIF)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-237
  topic: SESSION_USER
  status: Missing
  covered_by: 1093 (Session Analysis), 1223 (First-Time Users), 1106 (Active User Definitions)
  insert_target: 208 (Time-Series SQL)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-238
  topic: SYSTEM_USER
  status: Missing
  covered_by: 1223 (First-Time Users), 1106 (Active User Definitions)
  insert_target: 208 (Time-Series SQL)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-239
  topic: USER
  status: Covered
  covered_by: 1223 (First-Time Users), 1106 (Active User Definitions)
  insert_target: N/A
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-240
  topic: VERSION
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-241
  topic: MS Access Functions
  status: Partially Covered
  covered_by: 1179 (String Functions), 1162 (Quiz: Window Functions I), 1163 (Quiz: Window Functions II)
  insert_target: N/A
  why_it_matters: Built-in SQL functions are used constantly.
  proposed_changes: Add 2-3 function examples and a quick exercise.

- gap_id: SQL-242
  topic: SQL Quick Ref
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-243
  topic: SQL Editor
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

- gap_id: SQL-244
  topic: Try it Yourself &raquo;
  status: Missing
  covered_by: None
  insert_target: 200 (Setup & Mental Model)
  why_it_matters: This topic appears in W3Schools and should be addressed for completeness.
  proposed_changes: Add a short example and one targeted exercise aligned to the topic.

## Rules For Applying Upgrades
- Prefer merging into existing lessons before adding new lessons.
- New chapters are allowed only when a topic is completely missing, too large to insert into one chapter, and requires multiple lessons.
- Do not create W3Schools-labeled sections.
- Every change must reference the gap_id it addresses.
- Provide per-lesson diff summaries and a small changelog per batch.