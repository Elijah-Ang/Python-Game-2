import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as mpath
from matplotlib.collections import PatchCollection
import os

# Ensure assets directory exists
OUTPUT_DIR = "frontend/public/assets/sql-diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_plot(filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(filepath, bbox_inches='tight', dpi=100)
    plt.close()
    print(f"Generated {filepath}")

def draw_table_anatomy(filename):
    """Draws a table structure illustrating Rows and Columns."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Draw Header (Columns)
    header = patches.Rectangle((1, 4), 6, 1, linewidth=2, edgecolor='#1e40af', facecolor='#dbeafe')
    ax.add_patch(header)
    ax.text(4, 4.5, "Columns (Attributes)", ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')

    # Draw Rows (Records)
    for i in range(4):
        y = 3 - i
        row = patches.Rectangle((1, y), 6, 1, linewidth=1, edgecolor='#94a3b8', facecolor='white')
        ax.add_patch(row)
        ax.text(4, y + 0.5, f"Row {i+1} (Record)", ha='center', va='center', fontsize=10, color='#64748b')

    # Labels/Arrows
    ax.annotate("Primary Key", xy=(1.5, 4.2), xytext=(0, 5), 
                arrowprops=dict(arrowstyle="->", color="#ef4444", lw=2), color="#ef4444")

    save_plot(filename)

def draw_venn_join(join_type, filename):
    """Draws Venn diagrams for different JOIN types."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Circles
    circle_a = patches.Circle((3, 3), 1.5, edgecolor='#3b82f6', facecolor='none', linewidth=2)
    circle_b = patches.Circle((5, 3), 1.5, edgecolor='#10b981', facecolor='none', linewidth=2)
    
    # Fill based on join type
    if join_type == "inner":
        # Intersection only
        # Creating a clip path is complex in simple matplotlib, using a simpler overlap approach
        # Draw overlap circle
        overlap = patches.Circle((3, 3), 1.5, facecolor="#93c5fd", alpha=0.5)
        # Use simple visual overlap hack or just logical coloring
        # Simpler: Just colored circles
        c1 = patches.Circle((3, 3), 1.5, facecolor='none', edgecolor='#3b82f6')
        c2 = patches.Circle((5, 3), 1.5, facecolor='none', edgecolor='#10b981')
        ax.add_patch(c1)
        ax.add_patch(c2)
        
        # Shade intersection
        # This is hard to do perfectly with just circles, so representing conceptually
        ax.text(4, 3, "MATCH", ha='center', va='center', fontweight='bold')
        ax.text(4, 5, "INNER JOIN", ha='center', va='center', fontsize=14, fontweight='bold')
        
        # Add visual intersection patch (approximate with an ellipse or just text)
        intersection = patches.Ellipse((4, 3), 1, 1.8, color='#bfdbfe', alpha=0.9, zorder=0)
        ax.add_patch(intersection)

    elif join_type == "left":
        c1 = patches.Circle((3, 3), 1.5, facecolor='#dbeafe', edgecolor='#3b82f6', alpha=0.8)
        c2 = patches.Circle((5, 3), 1.5, facecolor='white', edgecolor='#10b981')
        ax.add_patch(c2)
        ax.add_patch(c1) # Schema A on top
        ax.text(4, 5, "LEFT JOIN", ha='center', va='center', fontsize=14, fontweight='bold')
        ax.text(2.5, 3, "Table A\n(All Rows)", ha='center', va='center')
        ax.text(5.5, 3, "Table B\n(Matches)", ha='center', va='center', color='#94a3b8')

    elif join_type == "right":
        c1 = patches.Circle((3, 3), 1.5, facecolor='white', edgecolor='#3b82f6')
        c2 = patches.Circle((5, 3), 1.5, facecolor='#d1fae5', edgecolor='#10b981', alpha=0.8)
        ax.add_patch(c1)
        ax.add_patch(c2)
        ax.text(4, 5, "RIGHT JOIN", ha='center', va='center', fontsize=14, fontweight='bold')
        ax.text(2.5, 3, "Table A\n(Matches)", ha='center', va='center', color='#94a3b8')
        ax.text(5.5, 3, "Table B\n(All Rows)", ha='center', va='center')

    save_plot(filename)

def draw_execution_order(filename):
    """Draws a flowchart of SQL execution order."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    steps = ["FROM/JOIN", "WHERE", "GROUP BY", "HAVING", "SELECT", "ORDER BY", "LIMIT"]
    x_positions = [1 + i * 1.2 for i in range(len(steps))]
    
    for i, step in enumerate(steps):
        # Arrow
        if i > 0:
            ax.annotate("", xy=(x_positions[i] - 0.4, 3), xytext=(x_positions[i-1] + 0.4, 3),
                        arrowprops=dict(arrowstyle="->", lw=2, color="#64748b"))
        
        # Box
        color = '#3b82f6' if step == "SELECT" else '#94a3b8'
        face = '#eff6ff' if step == "SELECT" else 'white'
        box = patches.FancyBboxPatch((x_positions[i] - 0.5, 2.5), 1, 1, boxstyle="round,pad=0.1",
                                     edgecolor=color, facecolor=face, linewidth=2)
        ax.add_patch(box)
        
        # Text
        ax.text(x_positions[i], 3, str(i+1), ha='center', va='bottom', fontsize=10, fontweight='bold', color=color)
        ax.text(x_positions[i], 2.8, step, ha='center', va='top', fontsize=8, rotation=45 if len(step)>8 else 0)

    ax.text(5, 5, "SQL Order of Execution", ha='center', va='center', fontsize=14, fontweight='bold')
    
    save_plot(filename)

def draw_filter_funnel(filename):
    """Draws a funnel visualizing WHERE clause filtering."""
    fig, ax = plt.subplots(figsize=(5, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Funnel shape
    polygon = patches.Polygon([(1, 9), (9, 9), (6, 5), (6, 2), (4, 2), (4, 5)], 
                              closed=True, edgecolor='#3b82f6', facecolor='#eff6ff', alpha=0.5)
    ax.add_patch(polygon)

    # Input rows
    for i in range(5):
        ax.plot([2, 8], [8.5 - i*0.5, 8.5 - i*0.5], color='#94a3b8', lw=2)
    ax.text(1.5, 7.5, "All Rows", rotation=90, va='center')

    # Filter
    ax.text(5, 5.5, "WHERE condition", ha='center', va='center', fontweight='bold', color='#ef4444')
    
    # Output rows
    ax.plot([4.2, 5.8], [3, 3], color='#10b981', lw=2)
    ax.plot([4.2, 5.8], [2.5, 2.5], color='#10b981', lw=2)
    ax.text(7, 3, "Filtered Result", ha='left', va='center', color='#10b981', fontweight='bold')

    save_plot(filename)

def draw_relationships(filename):
    """Draws a relationship between two tables (PK-FK)."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Table A (Customers)
    rect_a = patches.Rectangle((1, 1), 3, 4, linewidth=2, edgecolor='#1e40af', facecolor='#eff6ff')
    ax.add_patch(rect_a)
    ax.text(2.5, 4.5, "customers", ha='center', va='center', fontweight='bold', color='#1e3a8a')
    ax.text(1.5, 4, "id (PK)", ha='left', va='center', fontweight='bold', color='#ef4444')
    ax.text(1.5, 3.5, "name", ha='left', va='center', color='#64748b')

    # Table B (Orders)
    rect_b = patches.Rectangle((6, 1), 3, 4, linewidth=2, edgecolor='#10b981', facecolor='#ecfdf5')
    ax.add_patch(rect_b)
    ax.text(7.5, 4.5, "orders", ha='center', va='center', fontweight='bold', color='#065f46')
    ax.text(6.5, 4, "id (PK)", ha='left', va='center', color='#64748b')
    ax.text(6.5, 3.5, "cust_id (FK)", ha='left', va='center', fontweight='bold', color='#ef4444')

    # The Link (PK to FK)
    arrow = patches.FancyArrowPatch((4, 4), (6, 3.5), arrowstyle='<->', 
                                    mutation_scale=20, color='#ef4444', lw=2,
                                    connectionstyle="arc3,rad=0.2")
    ax.add_patch(arrow)
    ax.text(5, 4.2, "Relates", ha='center', color='#ef4444', fontweight='bold')

    save_plot(filename)

def draw_group_by(filename):
    """Draws buckets visualizing GROUP BY aggregation."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Input rows (dots)
    colors = ['#3b82f6', '#10b981', '#3b82f6', '#3b82f6', '#10b981']
    for i, c in enumerate(colors):
        ax.scatter(1, 4.5 - i*0.5, color=c, s=100)
    ax.text(1, 5, "Source Rows", ha='center', va='bottom', fontsize=10)

    # Buckets
    bucket_a = patches.FancyBboxPatch((4, 2), 2, 2, boxstyle="round,pad=0.2", linewidth=2, edgecolor='#3b82f6', facecolor='#eff6ff')
    bucket_b = patches.FancyBboxPatch((7, 2), 2, 2, boxstyle="round,pad=0.2", linewidth=2, edgecolor='#10b981', facecolor='#ecfdf5')
    ax.add_patch(bucket_a)
    ax.add_patch(bucket_b)
    
    ax.text(5, 4.5, "Group A", ha='center', va='bottom', color='#1e3a8a', fontweight='bold')
    ax.text(8, 4.5, "Group B", ha='center', va='bottom', color='#065f46', fontweight='bold')

    # Arrows to buckets
    ax.annotate("", xy=(4, 3), xytext=(1.5, 4), arrowprops=dict(arrowstyle="->", color='#3b82f6', lw=1.5))
    ax.annotate("", xy=(7, 3), xytext=(1.5, 3.5), arrowprops=dict(arrowstyle="->", color='#10b981', lw=1.5))

    # Aggregated Result
    ax.text(5, 2.5, "COUNT: 3", ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(8, 2.5, "COUNT: 2", ha='center', va='center', fontsize=12, fontweight='bold')

    ax.text(5, 5.5, "GROUP BY & AGGREGATE", ha='center', va='center', fontsize=14, fontweight='bold')

    save_plot(filename)

def draw_subquery(filename):
    """Draws a 'Russian Doll' style visual for subqueries."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Outer Query
    outer = patches.Rectangle((1, 1), 8, 8, linewidth=2, edgecolor='#3b82f6', facecolor='#eff6ff')
    ax.add_patch(outer)
    ax.text(5, 8.5, "OUTER QUERY", ha='center', va='center', fontweight='bold', color='#1e3a8a')

    # Inner Query
    inner = patches.Rectangle((2.5, 2.5), 5, 5, linewidth=2, edgecolor='#10b981', facecolor='#ecfdf5')
    ax.add_patch(inner)
    ax.text(5, 7, "INNER (SUB) QUERY", ha='center', va='center', fontweight='bold', color='#065f46')
    
    ax.text(5, 5, "Returns values\nto use in WHERE", ha='center', va='center', fontsize=10, style='italic')

    save_plot(filename)

def draw_union(filename):
    """Draws a visual for UNION (stacking)."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Result Set A
    set_a = patches.Rectangle((2, 6), 6, 3, linewidth=2, edgecolor='#3b82f6', facecolor='#eff6ff')
    ax.add_patch(set_a)
    ax.text(5, 7.5, "Result Set A", ha='center', va='center', fontweight='bold')

    # UNION Label
    ax.text(5, 5.5, "UNION", ha='center', va='center', fontweight='bold', color='#ef4444', fontsize=16)

    # Result Set B
    set_b = patches.Rectangle((2, 2), 6, 3, linewidth=2, edgecolor='#10b981', facecolor='#ecfdf5')
    ax.add_patch(set_b)
    ax.text(5, 3.5, "Result Set B", ha='center', va='center', fontweight='bold')

    # Flow
    ax.annotate("", xy=(5, 5.8), xytext=(5, 6.2), arrowprops=dict(arrowstyle="<-", lw=2))
    ax.annotate("", xy=(5, 5.2), xytext=(5, 4.8), arrowprops=dict(arrowstyle="->", lw=2))

    save_plot(filename)

def draw_champion(filename):
    """Draws a celebratory 'SQL Master' badge/visual."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Shield/Badge
    badge = patches.RegularPolygon((5, 5), numVertices=6, radius=4, orientation=0,
                                   linewidth=5, edgecolor='#fbbf24', facecolor='#fef3c7')
    ax.add_patch(badge)

    # Text
    ax.text(5, 6, "SQL", ha='center', va='center', fontsize=30, fontweight='bold', color='#1e3a8a')
    ax.text(5, 4, "MASTER", ha='center', va='center', fontsize=24, fontweight='bold', color='#1e3a8a')
    
    # Stars
    for (x, y) in [(3, 7.5), (7, 7.5), (5, 8.5), (3, 2.5), (7, 2.5)]:
        ax.scatter(x, y, color='#fbbf24', s=400, marker='*')

    save_plot(filename)

def draw_all():
    print("Generating SQL diagrams...")
    draw_table_anatomy("table_anatomy.png")
    draw_venn_join("inner", "venn_inner.png")
    draw_venn_join("left", "venn_left.png")
    draw_venn_join("right", "venn_right.png")
    draw_execution_order("sql_execution_order.png")
    draw_filter_funnel("filter_funnel.png")
    draw_relationships("relational_link.png")
    draw_group_by("group_by_buckets.png")
    draw_subquery("subquery_concept.png")
    draw_union("union_stack.png")
    draw_champion("champion_sql.png")
    print("All SQL diagrams generated.")

if __name__ == "__main__":
    draw_all()
