import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import shutil

# Ensure assets directory exists
OUTPUT_DIR = "frontend/public/assets/r-diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)
PYTHON_DIR = "frontend/public/assets/python-diagrams"

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

    # Draw the box (Container) - R Theme (Blue/Purple)
    box = patches.FancyBboxPatch((3, 2), 4, 4, boxstyle="round,pad=0.2", 
                                 linewidth=2, edgecolor='#8b5cf6', facecolor='#f3e8ff')
    ax.add_patch(box)

    # Label (Variable Name)
    ax.text(5, 6.5, name, ha='center', va='center', fontsize=16, 
            fontweight='bold', color='#5b21b6')
    
    # Arrow sticking to the box
    arrow = patches.FancyArrowPatch((5, 6.2), (5, 5.2), arrowstyle='-|>', 
                                    mutation_scale=20, color='#5b21b6')
    ax.add_patch(arrow)

    # Value inside
    ax.text(5, 4, str(value), ha='center', va='center', fontsize=20, 
            fontfamily='monospace', color='#4c1d95')
    
    # "Memory" label
    ax.text(5, 1.5, "Computer Memory", ha='center', va='center', 
            fontsize=10, color='#64748b', style='italic')

    save_plot(filename)

def draw_dataframe(data, columns, filename):
    """Draws a DataFrame/Tibble grid."""
    rows = len(data)
    cols = len(columns)
    
    fig, ax = plt.subplots(figsize=(cols * 2, rows + 1))
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows + 1)
    ax.axis('off')

    # Column Headers
    for j, col in enumerate(columns):
        # Header Box
        rect = patches.Rectangle((j, rows), 1, 1, linewidth=1, edgecolor='black', facecolor='#ede9fe')
        ax.add_patch(rect)
        ax.text(j + 0.5, rows + 0.5, col, ha='center', va='center', fontsize=10, fontweight='bold')

    # Data Rows
    for i, row in enumerate(data):
        y = rows - 1 - i  # Start from top
        # Index Label (left of row) - R starts at 1 usually, but tibbles often don't show index
        ax.text(-0.2, y + 0.5, str(i + 1), ha='right', va='center', fontsize=8, color='#64748b')
        
        for j, val in enumerate(row):
            # Cell
            rect = patches.Rectangle((j, y), 1, 1, linewidth=1, edgecolor='#cbd5e1', facecolor='white')
            ax.add_patch(rect)
            ax.text(j + 0.5, y + 0.5, str(val), ha='center', va='center', fontsize=10)

    # DataFrame Label
    ax.text(cols/2, rows + 1.2, "Tibble / Data Frame", ha='center', va='bottom', fontsize=12, fontweight='bold', color='#475569')

    save_plot(filename)

def draw_scatterplot(filename):
    """Draws a simple scatterplot mimicking ggplot2 default theme."""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # ggplot2 gray background with white grid
    ax.set_facecolor('#ebebeb')
    ax.grid(color='white', linewidth=1)
    
    # Random data points
    # Flipper length vs Body Mass correlation
    x = [181, 186, 195, 205, 210, 217, 220, 190, 200, 215]
    y = [3750, 3800, 4200, 4700, 5000, 5200, 5400, 3900, 4100, 4800]
    
    ax.scatter(x, y, color='black', alpha=0.7, s=50)
    
    ax.set_xlabel("flipper_length_mm")
    ax.set_ylabel("body_mass_g")
    ax.set_title("Penguin Trends")
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    save_plot(filename)

def copy_generic_diagrams():
    """Copies generic diagrams from Python folder used in R."""
    generics = ["flowchart_if.png", "function_machine.png"]
    for gen in generics:
        src = os.path.join(PYTHON_DIR, gen)
        dst = os.path.join(OUTPUT_DIR, gen)
        if os.path.exists(src):
            shutil.copy(src, dst)
            print(f"Copied {gen}")

def draw_all():
    print("Generating R diagrams...")
    
    # 1. Variables (Analogy: Kitchen box with plates)
    draw_variable_box("kitchen", '"plates"', "variable_box_kitchen.png")
    
    # 2. Variable Variation (pet = dog)
    draw_variable_box("pet", '"dog"', "variable_box_pet.png")
    
    # 3. Data Frame (Tibble)
    draw_dataframe(
        [["Adelie", 38.8, 18.1], ["Gentoo", 46.1, 13.2], ["Chinstrap", 47.9, 19.5]],
        ["species", "bill_len", "bill_dep"],
        "dataframe_penguins.png"
    )

    save_plot(filename)

def draw_scatterplot(filename, variant="simple"):
    """Draws a simple scatterplot mimicking ggplot2."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_facecolor('#ebebeb')
    ax.grid(color='white', linewidth=1)
    
    # Data
    x = [10, 20, 30, 40, 50, 60, 70, 80]
    y = [15, 25, 35, 40, 48, 55, 65, 75]
    colors = 'black'
    
    if "colored" in variant or "color" in variant:
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'brown']
        
    ax.scatter(x, y, color=colors, alpha=0.7, s=60)
    
    if "trend" in variant:
        ax.plot(x, y, color='blue', linewidth=2, alpha=0.5)

    ax.set_title("Scatter Plot")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    save_plot(filename)

def draw_histogram(filename):
    """Draws a histogram."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_facecolor('#ebebeb')
    ax.grid(color='white', linewidth=1)
    
    data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 4, 3, 2, 5, 4]
    ax.hist(data, bins=6, color='#374151', edgecolor='white')
    
    ax.set_title("Histogram")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    save_plot(filename)

def draw_boxplot(filename):
    """Draws a boxplot."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_facecolor('#ebebeb')
    ax.grid(color='white', linewidth=1)
    
    data = [[1, 2, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 8]]
    ax.boxplot(data, patch_artist=True, boxprops=dict(facecolor="white"))
    
    ax.set_title("Boxplot")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    save_plot(filename)

def draw_empty(filename, axes=False):
    """Draws empty canvas."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_facecolor('#ebebeb')
    if axes:
        ax.grid(color='white', linewidth=1)
    else:
        ax.axis('off') # Truly empty? Or just background
        ax.grid(color='white', linewidth=1)
        
    if "axes" in filename:
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        
    save_plot(filename)

def draw_facets(filename):
    """Draws facets (subplots)."""
    fig, axs = plt.subplots(2, 2, figsize=(6, 4))
    for ax in axs.flat:
        ax.set_facecolor('#ebebeb')
        ax.grid(color='white', linewidth=1)
        ax.scatter([1, 2, 3], [1, 3, 2], s=20)
    
    plt.tight_layout()
    save_plot(filename)

def draw_all():
    print("Generating R diagrams...")
    
    # 1. Variables
    draw_variable_box("kitchen", '"plates"', "variable_box_kitchen.png")
    draw_variable_box("pet", '"dog"', "variable_box_pet.png")
    
    # 2. Data Frame
    draw_dataframe(
        [["Adelie", 38.8, 18.1], ["Gentoo", 46.1, 13.2], ["Chinstrap", 47.9, 19.5]],
        ["species", "bill_len", "bill_dep"],
        "dataframe_penguins.png"
    )

    # 3. Scatterplots
    draw_scatterplot("penguin_scatter_trend.png", variant="trend")
    draw_scatterplot("penguin_scatter.png", variant="simple")
    draw_scatterplot("penguin_scatter_colored.png", variant="colored")
    draw_scatterplot("mpg_scatter_themed.png", variant="simple")
    draw_scatterplot("mpg_scatter_labeled.png", variant="simple")
    draw_scatterplot("mpg_mapping_color.png", variant="colored")

    # 4. Histograms/Boxplots
    draw_histogram("diamond_histogram.png")
    draw_boxplot("diamond_boxplot.png")
    draw_boxplot("mpg_boxplot_reordered.png")
    
    # 5. Basics/Structure
    draw_empty("ggplot_empty.png", axes=False)
    draw_empty("ggplot_axes.png", axes=True)
    draw_facets("mpg_facets.png")
    
    # 6. Layers
    draw_scatterplot("mpg_geoms_layers.png", variant="trend") # Scatter + Trend

    # Copy generic flowcharts
    copy_generic_diagrams()

    print("All R diagrams generated.")

if __name__ == "__main__":
    draw_all()
