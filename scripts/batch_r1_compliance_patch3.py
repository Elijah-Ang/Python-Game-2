"""
Batch R-1 Compliance Patch 3 - Aggressive markdown fencing fix
"""

import json
import re

with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

BATCH_R1 = {
    2002: [20021, 20022, 20023, 20024],
    2003: [20031, 20032, 20033, 20034],
    2001: [20011, 20012, 20013, 20014],
    2201: [22011, 22012, 22013, 22014],
    2030: [20301, 20302, 20303, 20304],
    2050: [20501, 20502, 20503, 20504],
    2500: [25001, 25002, 25003, 25004],
    2010: [20101, 20102, 20103, 20104],
    2040: [20401, 20402, 20403, 20404],
    2023: [20231, 20232, 20233, 20234],
    2021: [20211, 20212, 20213, 20214],
    2121: [21211, 21212, 21213, 21214],
}

def fix_markdown_fencing(content):
    """Aggressively fix markdown fencing issues."""
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check if this line opens a code block
        if stripped.startswith('```') and not stripped == '```' and not in_code_block:
            in_code_block = True
            fixed_lines.append(line)
            continue
        
        # If we're in a code block and see a markdown header (## or #)
        # that's not part of an R comment, we need to close the block first
        if in_code_block:
            # Check for markdown headers that shouldn't be in code
            if stripped.startswith('## ') or (stripped.startswith('# ') and not stripped.startswith('# ') and len(stripped) > 2 and stripped[2].isupper()):
                # This looks like a markdown header, close code block first
                fixed_lines.append('```')
                fixed_lines.append('')
                fixed_lines.append(line)
                in_code_block = False
                continue
            # Check for closing fence
            elif stripped == '```':
                in_code_block = False
                fixed_lines.append(line)
                continue
        
        fixed_lines.append(line)
    
    # Close any unclosed block
    if in_code_block:
        fixed_lines.append('```')
    
    return '\n'.join(fixed_lines)

# The real issue is that the Example section content runs into prose.
# Let me check a few lessons to understand the pattern

print("Checking 20021...")
content = lessons["20021"]["content"]
lines = content.split('\n')
for i, line in enumerate(lines[8:18], start=9):
    print(f"{i}: {line[:60]}")

# The issue: the detector thinks the comment "# This creates..." is a header
# Let me recheck the logic - R comments start with # but headers have ## or # Title
