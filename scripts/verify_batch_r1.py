"""
Final verification with improved token extractor
"""

import json
import re

# Load lessons
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

R_FUNCTIONS = {
    'print', 'c', 'length', 'mean', 'sum', 'max', 'min', 'range', 'names',
    'library', 'ggplot', 'aes', 'geom_point', 'geom_histogram', 'theme_minimal',
    'theme_bw', 'theme_classic', 'theme_dark', 'filter', 'select', 'mutate',
    'arrange', 'desc', 'if_else', 'case_when', 'pivot_longer', 'pivot_wider',
}

KNOWN_DATASETS = {'penguins', 'mpg', 'diamonds', 'table4a', 'flights', 'starwars'}

REQUIRED_HEADERS = [
    "What You'll Learn", "Why This Matters", "Example", "Your Task",
    "Expected Output", "Common Mistake", "No Hidden Prerequisites"
]

def extract_tokens(text):
    tokens = set()
    func_matches = re.findall(r'\b([a-z_][a-z0-9_]*)\s*\(', text, re.IGNORECASE)
    for f in func_matches:
        if f.lower() in R_FUNCTIONS:
            tokens.add(f.lower() + '()')
    for ds in KNOWN_DATASETS:
        if re.search(rf'\b{ds}\b', text, re.IGNORECASE):
            tokens.add(ds)
    if '%>%' in text:
        tokens.add('%>%')
    if '<-' in text:
        tokens.add('<-')
    if '$' in text:
        tokens.add('$')
    return tokens

def check_headers(content):
    missing = []
    for h in REQUIRED_HEADERS:
        if h not in content:
            missing.append(h)
    return missing

def has_pipe_bridge(content):
    """Check if content has pipe micro-bridge."""
    return '💡' in content and '%>%' in content

def detect_role(title):
    title_lower = title.lower()
    if 'analogy' in title_lower:
        return 'recognition'
    elif 'variation' in title_lower:
        return 'modification'
    elif 'fix' in title_lower:
        return 'mistake'
    elif 'challenge' in title_lower:
        return 'applied'
    return 'unknown'

print("=" * 140)
print("BATCH R-1 VERIFICATION TABLE (Compliance Patch 2)")
print("=" * 140)
print(f"{'ID':<8} {'concept':<8} {'role':<12} {'tokens':<55} {'headers':<10} {'pipe_bridge'}")
print("-" * 140)

all_pass = True
for concept_id, reinforcer_ids in BATCH_R1.items():
    for r_id in reinforcer_ids:
        r = lessons.get(str(r_id), {})
        title = r.get('title', '')
        content = r.get('content', '')
        
        role = detect_role(title)
        tokens = extract_tokens(content)
        missing = check_headers(content)
        has_bridge = has_pipe_bridge(content) if '%>%' in content else 'N/A'
        
        tokens_str = ', '.join(sorted(tokens)[:6])
        headers_str = 'OK' if not missing else f'MISS:{len(missing)}'
        bridge_str = '✅' if has_bridge == True else ('N/A' if has_bridge == 'N/A' else '❌')
        
        if missing:
            all_pass = False
        
        print(f"{r_id:<8} {concept_id:<8} {role:<12} {tokens_str:<55} {headers_str:<10} {bridge_str}")
    print("-" * 140)

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"All headers present: {'✅ YES' if all_pass else '❌ NO'}")

# Check for solution leakage
leakage = []
for concept_id, reinforcer_ids in BATCH_R1.items():
    for r_id in reinforcer_ids:
        content = lessons.get(str(r_id), {}).get('content', '')
        if 'Solution:' in content or 'Solution Code:' in content:
            leakage.append(r_id)

print(f"Solution leakage: {len(leakage)} lessons")
if leakage:
    print(f"  Affected: {leakage}")
