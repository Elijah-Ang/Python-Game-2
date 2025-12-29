import json

def update_lessons():
    path = 'frontend/public/data/lessons.json'
    with open(path, 'r') as f:
        data = json.load(f)
    
    # FIX 2: Lesson 113 (Final Boss)
    boss_id = '113' # Targeting directly
    
    if boss_id in data:
        print(f"Fixing Final Boss (ID: {boss_id})")
        # Add seed to starter code
        starter = data[boss_id].get('starter_code', '')
        if 'np.random.seed' not in starter:
            # Check if numpy is imported
            header = "import numpy as np\n" if "import numpy" not in starter else ""
            data[boss_id]['starter_code'] = header + "np.random.seed(42)  # 🔒 Fixed seed for verification\n" + starter
            
        # Add note to content
        content = data[boss_id].get('content', '')
        if "Professor's Note" not in content and "Verification Tip" not in content:
            data[boss_id]['content'] = content + "\n\n> [!TIP]\n> **Verification Tip**: We've set `np.random.seed(42)` so your random dataset matches the answer key perfectly."
            
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print("Updates saved!")

if __name__ == "__main__":
    update_lessons()
