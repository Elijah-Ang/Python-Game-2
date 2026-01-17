"""
R Curriculum Reinforcer Scoring Script - Phase 1A

Evaluates each reinforcer on 4 dimensions:
1. Relevance (0-3): Does it clearly reinforce the concept above?
2. Difficulty Jump (0-3): 0 = big jump/hidden prereq, 3 = smooth
3. Explanation Quality (0-3): Why/how clarity
4. Robustness (0-3): Clear task, clear outcome

Also flags hidden prerequisites or implicit assumptions.
"""

import json
import re
from pathlib import Path

def load_data():
    """Load course structure and lesson content."""
    with open('frontend/public/data/course-r-fundamentals.json', 'r') as f:
        course = json.load(f)
    with open('frontend/public/data/lessons.json', 'r') as f:
        lessons = json.load(f)
    with open('scripts/r_reinforcer_audit_mapping.json', 'r') as f:
        mappings = json.load(f)
    return course, lessons, mappings

def get_concept_keywords(concept_content):
    """Extract key concepts/functions taught in the concept lesson."""
    keywords = []
    
    # Look for code blocks and extract function names
    code_blocks = re.findall(r'```r\n(.*?)```', concept_content, re.DOTALL)
    for block in code_blocks:
        # Extract function calls like filter(, ggplot(, etc.
        funcs = re.findall(r'\b(\w+)\s*\(', block)
        keywords.extend(funcs)
    
    # Look for inline code references
    inline_code = re.findall(r'`(\w+)`', concept_content)
    keywords.extend(inline_code)
    
    return list(set(keywords))

def score_reinforcer(reinforcer_lesson, concept_lesson, reinforcer_type, all_previous_concepts):
    """
    Score a single reinforcer.
    
    Returns: {
        'relevance': 0-3,
        'difficulty_jump': 0-3,
        'explanation_quality': 0-3,
        'robustness': 0-3,
        'notes': [],
        'hidden_prereqs': []
    }
    """
    score = {
        'relevance': 0,
        'difficulty_jump': 3,  # Assume smooth unless issues found
        'explanation_quality': 0,
        'robustness': 0,
        'notes': [],
        'hidden_prereqs': []
    }
    
    if not reinforcer_lesson:
        score['notes'].append("❌ Lesson content not found")
        return score
    
    content = reinforcer_lesson.get('content', '')
    starter_code = reinforcer_lesson.get('starter_code', '')
    solution_code = reinforcer_lesson.get('solution_code', '')
    expected_output = reinforcer_lesson.get('expected_output', '')
    
    concept_content = concept_lesson.get('content', '') if concept_lesson else ''
    concept_keywords = get_concept_keywords(concept_content)
    
    # === RELEVANCE (0-3) ===
    # Does the reinforcer directly use/reference the concept above?
    relevance_score = 0
    
    # Check if reinforcer mentions concept keywords
    reinforcer_text = content + starter_code + solution_code
    keyword_matches = sum(1 for kw in concept_keywords if kw.lower() in reinforcer_text.lower())
    
    if keyword_matches >= 3:
        relevance_score = 3
    elif keyword_matches >= 2:
        relevance_score = 2
    elif keyword_matches >= 1:
        relevance_score = 1
    else:
        score['notes'].append("⚠️ Low keyword overlap with concept")
    
    # Boost if explicit reference to concept
    if 'above' in content.lower() or 'previous' in content.lower() or 'we learned' in content.lower():
        relevance_score = min(3, relevance_score + 1)
    
    score['relevance'] = relevance_score
    
    # === DIFFICULTY JUMP (0-3) ===
    # Check for hidden prerequisites - functions/concepts not yet taught
    difficulty_score = 3
    
    # Known functions by chapter (simplified - could be expanded)
    r_known_funcs = {
        'basic': ['print', 'c', 'length', 'class', 'typeof', 'sum', 'mean', 'max', 'min'],
        'ggplot': ['ggplot', 'geom_point', 'geom_line', 'geom_bar', 'geom_smooth', 'aes', 'labs', 'theme'],
        'dplyr': ['filter', 'select', 'mutate', 'arrange', 'group_by', 'summarize', 'count'],
        'tidyr': ['pivot_longer', 'pivot_wider', 'separate', 'unite'],
        'stringr': ['str_c', 'str_length', 'str_sub', 'str_detect', 'str_replace'],
    }
    
    # Extract functions used in solution
    solution_funcs = re.findall(r'\b(\w+)\s*\(', solution_code) if solution_code else []
    
    # Check for very advanced functions that might indicate a jump
    advanced_patterns = ['map(', 'reduce(', 'nest(', 'unnest_wider', 'across(', '{{', '!!']
    for pattern in advanced_patterns:
        if pattern in solution_code:
            difficulty_score -= 1
            score['notes'].append(f"⚠️ Uses advanced function: {pattern}")
    
    # Check if content has clear step-by-step guidance
    if '1.' in content or '- ' in content or 'step' in content.lower():
        pass  # Good - has structured guidance
    else:
        difficulty_score -= 1
        score['notes'].append("No step-by-step guidance")
    
    score['difficulty_jump'] = max(0, difficulty_score)
    
    # === EXPLANATION QUALITY (0-3) ===
    # Does it explain WHY the concept is used and HOW it works?
    explanation_score = 0
    
    content_length = len(content)
    
    # Basic length check
    if content_length >= 400:
        explanation_score = 3
    elif content_length >= 250:
        explanation_score = 2
    elif content_length >= 150:
        explanation_score = 1
    else:
        score['notes'].append("Content too short")
    
    # Check for explanatory keywords
    why_how_keywords = ['because', 'why', 'how', 'when you', 'this works', 'notice', 'remember']
    if any(kw in content.lower() for kw in why_how_keywords):
        explanation_score = min(3, explanation_score + 1)
    else:
        score['notes'].append("Missing why/how explanation")
        explanation_score = max(0, explanation_score - 1)
    
    # Check for examples in content
    if '```' in content:
        pass  # Good - has code examples
    else:
        explanation_score = max(0, explanation_score - 1)
        score['notes'].append("No code examples in explanation")
    
    score['explanation_quality'] = explanation_score
    
    # === ROBUSTNESS (0-3) ===
    # Clear task, clear expected outcome
    robustness_score = 0
    
    # Has starter code?
    if starter_code.strip():
        robustness_score += 1
    else:
        score['notes'].append("Missing starter code")
    
    # Has solution code?
    if solution_code.strip():
        robustness_score += 1
    else:
        score['notes'].append("Missing solution code")
    
    # Has expected output?
    if expected_output.strip():
        robustness_score += 1
    else:
        score['notes'].append("Missing expected output")
    
    # Clear task description?
    if '🎯' in content or 'task' in content.lower() or 'your task' in content.lower():
        pass
    else:
        score['notes'].append("No clear task marker")
        robustness_score = max(0, robustness_score - 1)
    
    score['robustness'] = robustness_score
    
    return score

def main():
    print("Loading data...")
    course, lessons, mappings_data = load_data()
    
    mappings = mappings_data['mappings']
    
    # Track all scored reinforcers
    all_scores = []
    set_averages = []
    
    print("Scoring reinforcers...\n")
    
    for m in mappings:
        concept_id = m['concept']['id']
        concept_lesson = lessons.get(str(concept_id))
        
        set_scores = {
            'concept_id': concept_id,
            'concept_title': m['concept']['title'],
            'chapter': m['chapter'],
            'concept_name': m['concept_name'],
            'reinforcers': [],
            'total_score': 0,
            'avg_score': 0
        }
        
        # Build list of previous concept IDs for prereq checking
        previous_concepts = []
        
        for r_idx, r in enumerate(m['reinforcers']):
            r_id = r['id']
            r_lesson = lessons.get(str(r_id))
            
            # Determine reinforcer type from title
            title = r['title'].lower()
            if 'analogy' in title:
                r_type = 'analogy'
            elif 'variation' in title:
                r_type = 'variation'
            elif 'fix' in title:
                r_type = 'fix_the_code'
            elif 'challenge' in title:
                r_type = 'challenge'
            else:
                r_type = 'unknown'
            
            # Score the reinforcer
            score = score_reinforcer(r_lesson, concept_lesson, r_type, previous_concepts)
            
            total = score['relevance'] + score['difficulty_jump'] + score['explanation_quality'] + score['robustness']
            
            reinforcer_result = {
                'id': r_id,
                'title': r['title'],
                'type': r_type,
                'relevance': score['relevance'],
                'difficulty_jump': score['difficulty_jump'],
                'explanation_quality': score['explanation_quality'],
                'robustness': score['robustness'],
                'total': total,
                'notes': score['notes'],
                'hidden_prereqs': score['hidden_prereqs']
            }
            
            set_scores['reinforcers'].append(reinforcer_result)
            set_scores['total_score'] += total
            all_scores.append(reinforcer_result)
        
        set_scores['avg_score'] = set_scores['total_score'] / 4
        set_averages.append(set_scores)
    
    # Sort by average score (lowest first) for worst sets
    set_averages.sort(key=lambda x: x['avg_score'])
    
    # OUTPUT 1: Full mapping table
    print("=" * 140)
    print("FULL R REINFORCER SCORING TABLE")
    print("=" * 140)
    print(f"{'Concept ID':<12} {'Concept Title':<35} {'R ID':<8} {'R Title':<35} {'Rel':<4} {'Diff':<5} {'Expl':<5} {'Rob':<4} {'Notes'}")
    print("-" * 140)
    
    for s in set_averages:
        for i, r in enumerate(s['reinforcers']):
            concept_display = f"{s['concept_id']}" if i == 0 else ""
            title_display = s['concept_title'][:33] if i == 0 else ""
            notes_str = "; ".join(r['notes'][:2]) if r['notes'] else ""
            print(f"{concept_display:<12} {title_display:<35} {r['id']:<8} {r['title'][:33]:<35} {r['relevance']:<4} {r['difficulty_jump']:<5} {r['explanation_quality']:<5} {r['robustness']:<4} {notes_str[:40]}")
        print("-" * 140)
    
    # OUTPUT 2: Top 20 worst reinforcer sets
    print("\n\n" + "=" * 100)
    print("TOP 20 WORST REINFORCER SETS (ranked by lowest average score)")
    print("=" * 100)
    
    worst_20 = set_averages[:20]
    
    for rank, s in enumerate(worst_20, 1):
        print(f"\n#{rank}: Concept {s['concept_id']} - {s['concept_title']}")
        print(f"    Chapter: {s['chapter']} / {s['concept_name']}")
        print(f"    Average Score: {s['avg_score']:.2f}/12 ({s['total_score']}/48)")
        print(f"    Issues:")
        
        # Aggregate issues across all 4 reinforcers
        all_notes = []
        for r in s['reinforcers']:
            if r['notes']:
                all_notes.extend([f"R{s['reinforcers'].index(r)+1} ({r['type']}): {n}" for n in r['notes']])
        
        # Show top 3 issues
        for note in all_notes[:3]:
            print(f"      • {note}")
    
    # Save full results to JSON
    output = {
        'summary': {
            'total_sets': len(set_averages),
            'total_reinforcers': len(all_scores),
            'avg_score_overall': sum(s['avg_score'] for s in set_averages) / len(set_averages),
            'worst_20_ids': [s['concept_id'] for s in worst_20]
        },
        'all_sets': set_averages,
        'worst_20': worst_20
    }
    
    with open('scripts/r_reinforcer_scores.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\n\nDetailed scores saved to scripts/r_reinforcer_scores.json")
    print(f"\nOverall Average Score: {output['summary']['avg_score_overall']:.2f}/12")

if __name__ == '__main__':
    main()
