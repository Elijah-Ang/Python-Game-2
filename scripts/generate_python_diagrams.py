import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Ensure assets directory exists
OUTPUT_DIR = "frontend/public/assets/python-diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_plot(filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(filepath, bbox_inches='tight', dpi=100)
    plt.close()
    print(f"Generated {filepath}")

def draw_variable_box(name, value, filename):
    """Draws a simple variable as a labeled box."""
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Draw the box (Container)
    # Using a soft blue style
    box = patches.FancyBboxPatch((3, 2), 4, 4, boxstyle="round,pad=0.2", 
                                 linewidth=2, edgecolor='#3b82f6', facecolor='#eff6ff')
    ax.add_patch(box)

    # Label (Variable Name)
    ax.text(5, 6.5, name, ha='center', va='center', fontsize=16, 
            fontweight='bold', color='#1e3a8a')
    
    # Arrow sticking to the box
    arrow = patches.FancyArrowPatch((5, 6.2), (5, 5.2), arrowstyle='-|>', 
                                    mutation_scale=20, color='#1e3a8a')
    ax.add_patch(arrow)

    # Value inside
    ax.text(5, 4, str(value), ha='center', va='center', fontsize=20, 
            fontfamily='monospace', color='#1e40af')
    
    # "Memory" label
    ax.text(5, 1.5, "Computer Memory", ha='center', va='center', 
            fontsize=10, color='#64748b', style='italic')

    save_plot(filename)

def draw_flowchart_if(filename):
    """Draws a simple IF statement flowchart."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Styles
    box_props = dict(boxstyle="round,pad=0.3", fc="#eff6ff", ec="#3b82f6", lw=2)
    diamond_props = dict(boxstyle="darrow,pad=0.3", fc="#fff7ed", ec="#f97316", lw=2)
    
    # Nodes
    ax.text(5, 9, "Start", ha="center", va="center", size=12, bbox=box_props)
    ax.text(5, 7, "Condition\nTrue?", ha="center", va="center", size=12, bbox=diamond_props, rotation=0)
    
    # Yes Branch
    ax.text(8, 5, "Do This", ha="center", va="center", size=12, bbox=box_props)
    
    # End
    ax.text(5, 2, "Continue", ha="center", va="center", size=12, bbox=box_props)

    # Arrows
    # Start -> Condition
    ax.annotate("", xy=(5, 8.2), xytext=(5, 8.7), arrowprops=dict(arrowstyle="->", lw=2))
    
    # Condition -> Yes (Right)
    ax.annotate("Yes", xy=(6.5, 7), xytext=(6.2, 7.2), fontsize=10, color="green")
    ax.annotate("", xy=(8, 5.5), xytext=(6.2, 7), arrowprops=dict(arrowstyle="->", lw=2, connectionstyle="angle,angleA=0,angleB=90,rad=5"))
    
    # Condition -> No (Down)
    ax.annotate("No", xy=(5.2, 5.5), xytext=(5.2, 5.8), fontsize=10, color="red")
    ax.annotate("", xy=(5, 2.5), xytext=(5, 5.8), arrowprops=dict(arrowstyle="->", lw=2))
    
    # Yes -> End
    ax.annotate("", xy=(5.5, 2.2), xytext=(8, 4.5), arrowprops=dict(arrowstyle="->", lw=2, connectionstyle="angle,angleA=-90,angleB=0,rad=5"))

    save_plot(filename)

def draw_list_indices(data, filename):
    """Draws a list with indices."""
    n = len(data)
    fig, ax = plt.subplots(figsize=(n * 1.5 + 1, 3))
    ax.set_xlim(0, n + 1)
    ax.set_ylim(0, 3)
    ax.axis('off')

    for i, item in enumerate(data):
        # Index box
        rect = patches.Rectangle((i + 0.5, 1), 1, 1, linewidth=2, edgecolor='#3b82f6', facecolor='#eff6ff')
        ax.add_patch(rect)
        
        # Value
        ax.text(i + 1, 1.5, str(item), ha='center', va='center', fontsize=14, fontfamily='monospace')
        
        # Index label (positive)
        ax.text(i + 1, 0.7, str(i), ha='center', va='center', fontsize=12, color='#64748b', fontweight='bold')
        
        # Index label (negative)
        ax.text(i + 1, 0.3, str(i - n), ha='center', va='center', fontsize=10, color='#94a3b8')

    ax.text(0.2, 0.7, "Index:", ha='right', va='center', fontsize=12, color='#64748b')
    ax.text(0.2, 1.5, "Value:", ha='right', va='center', fontsize=12, color='black')

    save_plot(filename)

def draw_function_machine(input_val, func_name, output_val, filename):
    """Draws a function as a machine taking input and producing output."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # Input Arrow
    ax.text(1, 2.5, f"Input\n({input_val})", ha='center', va='center', fontsize=12)
    ax.annotate("", xy=(3, 2.5), xytext=(1.5, 2.5), arrowprops=dict(arrowstyle="->", lw=2, color="#64748b"))

    # Function Box (Machine)
    box = patches.FancyBboxPatch((3, 1), 4, 3, boxstyle="round,pad=0.2", 
                                 linewidth=2, edgecolor='#3b82f6', facecolor='#eff6ff')
    ax.add_patch(box)
    ax.text(5, 2.5, f"{func_name}()\n(Function)", ha='center', va='center', 
            fontsize=16, fontweight='bold', color='#1e3a8a')

    # Gears/Machine decoration
    circle = patches.Circle((6.5, 3.5), 0.3, color='#bfdbfe', alpha=0.5)
    ax.add_patch(circle)
    circle2 = patches.Circle((3.5, 1.5), 0.3, color='#bfdbfe', alpha=0.5)
    ax.add_patch(circle2)

    # Output Arrow
    ax.annotate("", xy=(8.5, 2.5), xytext=(7, 2.5), arrowprops=dict(arrowstyle="->", lw=2, color="#64748b"))
    ax.text(9, 2.5, f"Output\n({output_val})", ha='center', va='center', fontsize=12, fontweight='bold')

    save_plot(filename)

def draw_dict_mapping(data, filename):
    """Draws a dictionary as a key-value mapping."""
    n = len(data)
    fig, ax = plt.subplots(figsize=(6, n * 1.5 + 1))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, n * 1.5 + 1)
    ax.axis('off')
    
    # Title
    ax.text(5, n * 1.5 + 0.5, "Dictionary (Key → Value)", ha='center', va='center', 
            fontsize=14, fontweight='bold', color='#475569')

    for i, (key, value) in enumerate(data.items()):
        y = n * 1.5 - (i * 1.5) - 1
        
        # Key Box
        key_box = patches.Rectangle((1, y), 2.5, 1, linewidth=2, edgecolor='#f59e0b', facecolor='#fef3c7')
        ax.add_patch(key_box)
        ax.text(2.25, y + 0.5, repr(key), ha='center', va='center', fontsize=12, fontfamily='monospace')
        
        # Arrow
        ax.annotate("", xy=(6, y + 0.5), xytext=(3.5, y + 0.5), 
                    arrowprops=dict(arrowstyle="->", lw=2, color="#94a3b8"))
        
        # Value Box
        val_box = patches.Rectangle((6, y), 2.5, 1, linewidth=2, edgecolor='#10b981', facecolor='#d1fae5')
        ax.add_patch(val_box)
        ax.text(7.25, y + 0.5, repr(value), ha='center', va='center', fontsize=12, fontfamily='monospace')

    save_plot(filename)

    save_plot(filename)

def draw_dataframe(data, columns, filename):
    """Draws a simple DataFrame grid."""
    rows = len(data)
    cols = len(columns)
    
    fig, ax = plt.subplots(figsize=(cols * 2, rows + 1))
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows + 1)
    ax.axis('off')

    # Column Headers
    for j, col in enumerate(columns):
        # Header Box
        rect = patches.Rectangle((j, rows), 1, 1, linewidth=1, edgecolor='black', facecolor='#e2e8f0')
        ax.add_patch(rect)
        ax.text(j + 0.5, rows + 0.5, col, ha='center', va='center', fontsize=10, fontweight='bold')

    # Data Rows
    for i, row in enumerate(data):
        y = rows - 1 - i  # Start from top
        # Index Label (left of row)
        ax.text(-0.2, y + 0.5, str(i), ha='right', va='center', fontsize=8, color='#64748b')
        
        for j, val in enumerate(row):
            # Cell
            rect = patches.Rectangle((j, y), 1, 1, linewidth=1, edgecolor='#cbd5e1', facecolor='white')
            ax.add_patch(rect)
            ax.text(j + 0.5, y + 0.5, str(val), ha='center', va='center', fontsize=10)

    # DataFrame Label
    ax.text(cols/2, rows + 1.2, "DataFrame", ha='center', va='bottom', fontsize=12, fontweight='bold', color='#475569')

    save_plot(filename)

def draw_all():
    print("Generating Python diagrams...")
    
    # 1. Variables
    draw_variable_box("age", 25, "variable_box_age.png")
    draw_variable_box("name", "'Alice'", "variable_box_string.png")
    
    # 2. Control Flow
    draw_flowchart_if("flowchart_if.png")
    
    # 3. Data Structures
    draw_list_indices(["P", "y", "t", "h", "o", "n"], "string_indices.png")
    draw_list_indices([10, 20, 30, 40], "list_indices.png")
    
    # 4. Functions
    draw_function_machine(5, "double", 10, "function_machine.png")
    
    # 5. Dictionaries
    draw_dict_mapping({"name": "Alice", "age": 25, "city": "NYC"}, "dict_mapping.png")
    
    # 6. Pandas
    draw_dataframe(
        [["Alice", 25, "NYC"], ["Bob", 30, "LA"], ["Charlie", 35, "Chicago"]],
        ["name", "age", "city"],
        "dataframe_basic.png"
    )

    print("All diagrams generated.")

if __name__ == "__main__":
    draw_all()
