import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
import seaborn as sns
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib as mpl
from matplotlib import gridspec

# Set font family
plt.rcParams['font.family'] = 'Times New Roman'

# Function to create a filled area between a line and the baseline in 3D
def fill_between_3d(ax, x, y, z, baseline, color='blue', alpha=0.5):
    verts = []
    # Create bottom vertices
    for i in range(len(y)):
        verts.append([x, y[i], baseline])
    # Create top vertices
    for i in range(len(y)-1, -1, -1):
        verts.append([x, y[i], z[i]])
    
    poly = [verts]
    # Make sure color is a valid RGB or RGBA tuple
    if isinstance(color, tuple) and len(color) in [3, 4]:
        # Ensure RGB values are between 0 and 1
        color = tuple(min(1.0, max(0.0, c)) for c in color)
    
    poly_collection = Poly3DCollection(poly, alpha=alpha, facecolor=color)
    ax.add_collection3d(poly_collection)

# Function to create our 3D plot
def create_method_comparison_plot(ax, steps_data, methods_data, method_names, title):
    # Get the number of methods
    n_methods = len(methods_data)
    
    # Create a beautiful palette
    base_colors = sns.color_palette("husl", n_colors=n_methods)
    # Override 'Ours' with a bright red
    method_colors = list(base_colors)
    ours_index = method_names.index('Ours')
    method_colors[ours_index] = '#ff3333'  # Bright red for 'Ours'
    
    # Create fill colors (ensure they are valid RGBA)
    fill_colors = []
    for color in method_colors:
        rgb = mpl.colors.to_rgb(color)
        # Make it lighter but ensure it stays in the valid range
        fill_colors.append((min(1.0, rgb[0] + 0.2), min(1.0, rgb[1] + 0.2), min(1.0, rgb[2] + 0.2)))
    
    # Find the minimum performance value for the baseline
    baseline = min([np.min(data) for data in methods_data]) - 5
    
    # Get the appropriate steps array
    if isinstance(steps_data, list):
        steps = steps_data[0]  # Use the first one if there are multiple
    else:
        steps = steps_data
    
    # Plot each method
    for i, (method_data, method_name, color, fill_color) in enumerate(zip(methods_data, method_names, method_colors, fill_colors)):
        x_offset = i
        x_coords = np.full_like(steps, x_offset)
        
        # Draw the performance line - make 'Ours' stand out
        is_ours = method_name == 'Ours'
        linewidth = 2.5 if is_ours else 1.5
        marker = '^' if is_ours else 'o'
        markersize = 8 if is_ours else 5
        zorder = 10 if is_ours else 5
        
        ax.plot(x_coords, steps, method_data, color=color, 
                label=method_name, linewidth=linewidth,
                marker=marker, markersize=markersize, zorder=zorder)
        
        # Fill between the line and baseline
        fill_alpha = 0.6 if is_ours else 0.3
        fill_between_3d(ax, x_offset, steps, method_data, baseline, color=fill_color, alpha=fill_alpha)
        
        # Draw the baseline
        ax.plot(x_coords, steps, np.full_like(steps, baseline), color="black", linestyle='-', alpha=0.1)
    
    # Customize the plot
    ax.set_xlabel('Methods', fontsize=18, fontweight='bold', labelpad=10)
    ax.set_ylabel('Steps', fontsize=18, fontweight='bold', labelpad=10)
    ax.set_zlabel('mIoU (%)', fontsize=18, fontweight='bold', labelpad=10)
    
    # Set title
    ax.set_title(title, fontsize=22, fontweight='bold', pad=10)
    
    # Set axis ticks
    ax.set_xticks(np.arange(0, n_methods, 1))
    ax.set_xticklabels(method_names, fontsize=14)
    ax.set_yticklabels(steps, fontsize=12)
    
    # Set axis limits
    ax.set_xlim(-0.5, n_methods-0.5)
    ax.set_zlim(baseline, 85)
    
    # Remove grid and spines for a cleaner look
    ax.grid(False)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    
    # Set an optimal viewing angle
    ax.view_init(elev=30, azim=45)

# Data for 4-2 setting
steps_4_2 = np.arange(0, 9, 1)
MiB_4_2 = np.array([66, 47, 45, 31, 22, 19, 15, 9, 6])
PLOP_4_2 = np.array([66, 52, 37, 27, 20, 14, 8, 8, 8])
MiB_NeST_4_2 = np.array([68, 49, 40, 36, 28, 23, 16, 11, 7])
PLOP_NeST_4_2 = np.array([67, 49, 46, 34, 29, 25, 17, 9, 10])
ours_4_2 = np.array([72, 69, 71, 70, 68, 66, 65, 62.4, 61])

# Data for 2-2 setting
steps_2_2 = np.arange(0, 10, 1)
MiB_2_2 = np.array([63, 34, 30, 35, 24, 11, 8, 9, 7, 5])
PLOP_2_2 = np.array([70, 36, 29, 29, 19, 15, 9, 8, 8, 8])
MiB_NeST_2_2 = np.array([68, 37, 32, 31, 26, 15, 11, 9, 7, 6])
PLOP_NeST_2_2 = np.array([74, 39, 32, 27, 24, 16, 14, 12, 9, 7])
ours_2_2 = np.array([77, 72, 69, 71, 70, 68, 66, 65, 62.4, 61])

# Reorder methods with 'Ours' as the first column
method_names = ['Ours', 'MiB', 'PLOP', 'MiB+NeST', 'PLOP+NeST']

# Create one figure with two subplots
plt.figure(figsize=(20, 10), dpi=300)
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])

# Reorder data arrays to match the requested order
methods_data_4_2 = [ours_4_2, MiB_4_2, PLOP_4_2, MiB_NeST_4_2, PLOP_NeST_4_2]
methods_data_2_2 = [ours_2_2, MiB_2_2, PLOP_2_2, MiB_NeST_2_2, PLOP_NeST_2_2]
# methods_data_4_2 = [MiB_4_2, PLOP_4_2, MiB_NeST_4_2, PLOP_NeST_4_2, ours_4_2]
# methods_data_2_2 = [MiB_2_2, PLOP_2_2, MiB_NeST_2_2, PLOP_NeST_2_2, ours_2_2]
# Create subplot for 4-2 setting
ax1 = plt.subplot(gs[0], projection='3d')
create_method_comparison_plot(ax1, steps_4_2, methods_data_4_2, method_names, "4-2 setting")

# Create subplot for 2-2 setting
ax2 = plt.subplot(gs[1], projection='3d')
create_method_comparison_plot(ax2, steps_2_2, methods_data_2_2, method_names, "2-2 setting")

# Create a single legend for the entire figure
handles, labels = ax1.get_legend_handles_labels()
fig = plt.gcf()
fig.legend(handles, labels, loc='lower center', ncol=5, frameon=True, 
           fancybox=True, shadow=True, fontsize=16, bbox_to_anchor=(0.5, 0.02))

plt.tight_layout(rect=[0, 0.08, 1, 1])  # Adjust for the legend at the bottom
plt.savefig("difficult_setting.png", transparent=True, bbox_inches='tight')
plt.savefig("difficult_setting.pdf", transparent=True, bbox_inches='tight')
plt.close()

print("图片已保存为 difficult_setting.png 和 difficult_setting.pdf！")