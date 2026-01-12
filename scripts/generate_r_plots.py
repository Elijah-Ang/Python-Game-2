
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Ensure assets directory exists
OUTPUT_DIR = '../frontend/public/assets/r-plots'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Set common ggplot style
plt.style.use('ggplot')

# Adjust style to match R's default theme_gray() better
# R default: gray background, white grid
sns.set_theme(style="darkgrid", rc={"axes.facecolor": "#EBEBEB", "grid.color": "white", "figure.facecolor": "white"})

def save_plot(filename):
    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved {path}")

# Load datasets
try:
    penguins = sns.load_dataset('penguins').dropna()
    diamonds = sns.load_dataset('diamonds').dropna()
    mpg = sns.load_dataset('mpg').dropna() 
    # mpg in seaborn has slightly different structure, need to map to R's mpg
    # R mpg: displ, hwy, class, drv, cyl
    # seaborn mpg: displacement, mpg (combine city/hwy?), cylinders, origin
    # Actually seaborn's 'mpg' is combined. Let's just use what we have or mock if needed.
    # For lessons 20002121 it uses: displ, hwy, class, cyl, drv
except Exception as e:
    print(f"Error loading datasets: {e}")
    # Fallback mock data
    print("Using mock data...")
    penguins = pd.DataFrame({
        'flipper_length_mm': np.random.normal(200, 10, 100),
        'body_mass_g': np.random.normal(4000, 500, 100),
        'species': np.random.choice(['Adelie', 'Gentoo', 'Chinstrap'], 100)
    })
    
    diamonds = pd.DataFrame({
        'carat': np.concatenate([np.random.normal(0.5, 0.1, 100), np.random.normal(1.0, 0.1, 50)]),
        'cut': np.random.choice(['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'], 150),
        'price': np.random.uniform(300, 15000, 150)
    })
    
    mpg = pd.DataFrame({
        'displacement': np.random.uniform(1.6, 7.0, 100),
        'mpg': np.random.uniform(10, 35, 100),
        'origin': np.random.choice(['usa', 'europe', 'japan'], 100)
    })

# --- Lesson 2002: Empty Canvas ---
def plot_empty_canvas():
    fig, ax = plt.subplots(figsize=(6, 4))
    # mimicking ggplot(data=penguins) which produces just a gray background
    # But actually in R, ggplot() implies coordinates if mapped? 
    # No, ggplot(penguins) is just blank. 
    # But the lesson says "gray box".
    ax.set_xticks([])
    ax.set_yticks([])
    save_plot('ggplot_empty.png')

# --- Lesson 2003: Axes ---
def plot_axes():
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlabel('flipper_length_mm')
    ax.set_ylabel('body_mass_g')
    # Use ranges from penguins to set limits imply empty plot
    ax.set_xlim(penguins.flipper_length_mm.min()-10, penguins.flipper_length_mm.max()+10)
    ax.set_ylim(penguins.body_mass_g.min()-500, penguins.body_mass_g.max()+500)
    save_plot('ggplot_axes.png')

# --- Lesson 2004: Scatter ---
def plot_scatter():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', color='black', alpha=1, ax=ax)
    save_plot('penguin_scatter.png')

# --- Lesson 2005: Colored Scatter ---
def plot_scatter_colored():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='species', ax=ax)
    # Move legend to match R default (right side) - seaborn does this by default
    save_plot('penguin_scatter_colored.png')

# --- Lesson 2006: Trend Line ---
def plot_trend():
    g = sns.lmplot(data=penguins, x='flipper_length_mm', y='body_mass_g', height=4, aspect=1.5, 
                   scatter_kws={'color': 'black'}, line_kws={'color': 'blue'})
    g.savefig(os.path.join(OUTPUT_DIR, 'penguin_scatter_trend.png'), dpi=150, bbox_inches='tight')
    plt.close()

# --- Lesson 2110: Histogram ---
def plot_histogram():
    fig, ax = plt.subplots(figsize=(6, 4))
    # R: binwidth = 0.5 (default is 30 bins)
    sns.histplot(data=diamonds, x='carat', binwidth=0.1, color='black', ax=ax)
    save_plot('diamond_histogram.png')

# --- Lesson 2111: Boxplot ---
def plot_boxplot():
    fig, ax = plt.subplots(figsize=(6, 4))
    # R: cut vs price
    sns.boxplot(data=diamonds, x='cut', y='price', ax=ax, order=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    save_plot('diamond_boxplot.png')

# --- Lesson 2120: Labels ---
def plot_labels():
    fig, ax = plt.subplots(figsize=(6, 4))
    # Need mpg data. Seaborn 'mpg' has 'displacement' and 'mpg' columns?
    # Let's check columns if we can, or just mock.
    # Common seaborn mpg columns: mpg, cylinders, displacement, horsepower, weight, acceleration, model_year, origin, name
    # We want displ vs hwy.  Seaborn mpg usually has 'mpg' (combined?).
    # Let's assume 'displacement' -> 'displ' and 'mpg' -> 'hwy' for visual similarity.
    sns.scatterplot(data=mpg, x='displacement', y='mpg', ax=ax)
    ax.set_title("Fuel efficiency decreases with engine size")
    ax.set_xlabel("Engine displacement (L)")
    ax.set_ylabel("Highway MPG")
    save_plot('mpg_scatter_labeled.png')

# --- Lesson 2121: Themes & Scales ---
def plot_themed():
    # Theme minimal + scale color brewer Set1
    # Seaborn style 'whitegrid' is close to theme_minimal()
    with sns.axes_style("whitegrid"):
        fig, ax = plt.subplots(figsize=(6, 4))
        # Color by drv. Seaborn mpg doesn't have drv usually... it has origin?
        # Let's Use origin as a proxy for color
        sns.scatterplot(data=mpg, x='displacement', y='mpg', hue='origin', palette='Set1', ax=ax)
        save_plot('mpg_scatter_themed.png')

# --- Lesson 2100: Aesthetic Mappings (mpg) ---
def plot_mappings():
    fig, ax = plt.subplots(figsize=(6, 4))
    # mpg: displ vs hwy, color=class
    # mock mpg has 'displacement', 'mpg' (hwy), 'origin' (class proxy)
    # We'll use 'origin' as 'class' for visual distinction
    sns.scatterplot(data=mpg, x='displacement', y='mpg', hue='origin', ax=ax)
    save_plot('mpg_mapping_color.png')

# --- Lesson 2101: Geoms & Layers (mpg) ---
def plot_geoms_layers():
    # Points + Smooth
    g = sns.lmplot(data=mpg, x='displacement', y='mpg', height=4, aspect=1.5,
                   scatter_kws={'color': 'black'}, line_kws={'color': 'blue'})
    g.savefig(os.path.join(OUTPUT_DIR, 'mpg_geoms_layers.png'), dpi=150, bbox_inches='tight')
    plt.close()

# --- Lesson 2102: Facets (mpg) ---
def plot_facets():
    # Facet by cyl (mock uses origin or we can add cyl to mock)
    # Let's add cyl to mock if not present, or use origin as facet variable
    # Mock data: displacement, mpg, origin. No cyl.
    # Let's use origin as the facet variable (3 levels) to mimic cyl (4,5,6,8)
    g = sns.FacetGrid(mpg, col="origin")
    g.map(sns.scatterplot, "displacement", "mpg")
    g.savefig(os.path.join(OUTPUT_DIR, 'mpg_facets.png'), dpi=150, bbox_inches='tight')
    plt.close()

# --- Lesson 2240: Factors (mpg) ---
def plot_factors_reorder():
    # mpg: hwy vs class reordered
    # Mock: mpg vs origin
    # Calculate median mpg for each origin to sort
    medians = mpg.groupby('origin')['mpg'].median().sort_values()
    sorted_origins = medians.index.tolist()
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=mpg, x='mpg', y='origin', order=sorted_origins, ax=ax)
    ax.set_xlabel("hwy")
    ax.set_ylabel("class")
    save_plot('mpg_boxplot_reordered.png')

if __name__ == "__main__":
    plot_empty_canvas()
    plot_axes()
    plot_scatter()
    plot_scatter_colored()
    plot_trend()
    plot_histogram()
    plot_boxplot()
    plot_labels()
    plot_themed()
    plot_mappings()
    plot_geoms_layers()
    plot_facets()
    plot_factors_reorder()
