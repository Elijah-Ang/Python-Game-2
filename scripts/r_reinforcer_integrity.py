"""
Step 0: R Reinforcer Integrity Check
Verify every R concept has exactly 4 reinforcers
"""

import json
from collections import defaultdict

with open('frontend/public/data/lessons.json', 'r') as f:
    lessons = json.load(f)

# R concepts are 4-digit IDs (2000-2999)
# R reinforcers are 5-digit IDs (20000-29999) where first 4 digits match concept

r_concepts = {}
r_reinforcers = defaultdict(list)

for lid, lesson in lessons.items():
    try:
        lesson_id = int(lid)
    except:
        continue
    
    # R concept: 2000-2999
    if 2000 <= lesson_id <= 2999:
        r_concepts[lesson_id] = lesson
    
    # R reinforcer: 5-digit starting with 2
    elif 20000 <= lesson_id <= 29999:
        # Extract parent concept (first 4 digits)
        parent_concept = lesson_id // 10
        r_reinforcers[parent_concept].append((lesson_id, lesson))

# Report
print("=" * 80)
print("R REINFORCER INTEGRITY CHECK")
print("=" * 80)

concepts_missing = []
concepts_extra = []
concepts_ok = []

for concept_id in sorted(r_concepts.keys()):
    concept = r_concepts[concept_id]
    reinforcers = r_reinforcers.get(concept_id, [])
    count = len(reinforcers)
    
    status = "✅" if count == 4 else ("⚠️ MISSING" if count < 4 else "🔶 EXTRA")
    
    if count < 4:
        concepts_missing.append((concept_id, concept.get('title', ''), count, 4 - count))
    elif count > 4:
        concepts_extra.append((concept_id, concept.get('title', ''), count))
    else:
        concepts_ok.append(concept_id)

print(f"\nR Concepts with 4 reinforcers: {len(concepts_ok)}")
print(f"R Concepts missing reinforcers: {len(concepts_missing)}")
print(f"R Concepts with extra reinforcers: {len(concepts_extra)}")

if concepts_missing:
    print("\n--- MISSING REINFORCERS ---")
    for cid, title, count, needed in concepts_missing:
        print(f"  {cid}: {title} - has {count}, needs {needed} more")

if concepts_extra:
    print("\n--- EXTRA REINFORCERS (do not delete) ---")
    for cid, title, count in concepts_extra:
        print(f"  {cid}: {title} - has {count}")

# Check for reinforcers without concepts
orphan_reinforcers = []
for parent_id, reinfs in r_reinforcers.items():
    if parent_id not in r_concepts:
        for rid, r in reinfs:
            orphan_reinforcers.append((rid, r.get('title', '')))

if orphan_reinforcers:
    print(f"\n--- ORPHAN REINFORCERS ---")
    for rid, title in orphan_reinforcers[:10]:
        print(f"  {rid}: {title}")

print(f"\n--- SUMMARY ---")
print(f"Total R concepts: {len(r_concepts)}")
print(f"Total R reinforcers: {sum(len(v) for v in r_reinforcers.values())}")
print(f"Concepts needing new reinforcers: {len(concepts_missing)}")
print(f"Total reinforcers to create: {sum(c[3] for c in concepts_missing)}")
