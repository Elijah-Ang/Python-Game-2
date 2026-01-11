import json

path = '/Users/elijahang/Python-Game-2/frontend/public/data/course-python-basics.json'

with open(path, 'r') as f:
    data = json.load(f)

# Data['chapters'] is the list
chapters = data['chapters']

# Find index of Loops and Logic
# Assuming current order: Variables (0), Loops (1), Logic (2)
# We want: Variables (0), Logic (1), Loops (2)

idx_loops = -1
idx_logic = -1

for i, ch in enumerate(chapters):
    if ch['title'] == "Loops (Iteration)":
        idx_loops = i
    elif ch['title'] == "Logic & Control Flow":
        idx_logic = i

if idx_loops != -1 and idx_logic != -1:
    print(f"Found Loops at {idx_loops}, Logic at {idx_logic}. Swapping...")
    # Swap elements
    chapters[idx_loops], chapters[idx_logic] = chapters[idx_logic], chapters[idx_loops]
    
    # Update data
    data['chapters'] = chapters
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print("Swap complete.")
else:
    print("Could not find both chapters.")
