import json

def update_lessons():
    path = 'frontend/public/data/lessons.json'
    with open(path, 'r') as f:
        data = json.load(f)
    
    # FIX 1: Lesson 40 (Sand Sphinx)
    # The ID might be 40 or 100 based on previous checks. Let's check both or search by title.
    sphinx_id = None
    for lid, l in data.items():
        if 'Sphinx' in l.get('title', ''):
            sphinx_id = lid
            break
            
    if sphinx_id:
        print(f"Fixing Sphinx (ID: {sphinx_id})")
        # Add seed to starter code
        starter = data[sphinx_id].get('starter_code', '')
        if 'random.seed' not in starter:
            data[sphinx_id]['starter_code'] = "import random\n\n# 🔒 PROFESSOR'S NOTE: We set a seed so the Sphinx plays the same numbers every time.\n# This helps us verify your solution!\nrandom.seed(42)\n\n" + starter
        
        # Add note to content
        content = data[sphinx_id].get('content', '')
        if "Professor's Note" not in content:
            data[sphinx_id]['content'] = content + "\n\n> [!NOTE]\n> **Professor's Tip**: We've added `random.seed(42)` to your code. This ensures the random numbers are the same every time you run it, which is necessary for the auto-grader to work!"

    # FIX 2: Lesson 113 (Final Boss)
    # ID might be 113 or 101. Search by title.
    boss_id = None
    for lid, l in data.items():
        if 'Final Boss' in l.get('title', ''):
            boss_id = lid
            break
            
    if boss_id:
        print(f"Fixing Final Boss (ID: {boss_id})")
        # Add seed to starter code
        starter = data[boss_id].get('starter_code', '')
        if 'np.random.seed' not in starter:
            # Check if numpy is imported
            header = "import numpy as np\n" if "import numpy" not in starter else ""
            data[boss_id]['starter_code'] = header + "np.random.seed(42)  # 🔒 Fixed seed for verification\n\n" + starter
            
        # Add note to content
        content = data[boss_id].get('content', '')
        if "Professor's Note" not in content:
            data[boss_id]['content'] = content + "\n\n> [!TIP]\n> **Verification Tip**: We've set `np.random.seed(42)` so your random dataset matches the answer key perfectly."

    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print("Updates saved!")

if __name__ == "__main__":
    update_lessons()
