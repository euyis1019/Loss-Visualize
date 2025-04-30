import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'Times New Roman'

# Design evaluation dimensions
categories = ['Abstract', 'Tactile', 'Practical', 'Craftsmanship', 
              'Spatial', 'Visual', 'Material']
num_vars = len(categories)

# Sample evaluation scores (can be adjusted based on actual data)
design_a_scores = [0.92, 0.85, 0.88, 0.95, 0.89, 0.93, 0.90]
design_b_scores = [0.87, 0.90, 0.85, 0.88, 0.92, 0.86, 0.89]

# Calculate angles
angles = np.linspace(0, 2*np.pi, num_vars, endpoint=False)

# Close the plot
design_a_scores = np.concatenate((design_a_scores, [design_a_scores[0]]))
design_b_scores = np.concatenate((design_b_scores, [design_b_scores[0]]))
angles = np.concatenate((angles, [angles[0]]))

# Create figure
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

# Plot radar chart
ax.plot(angles, design_a_scores, 'o-', linewidth=2, label='Design A', 
        color='#6FA8DC', alpha=0.8)
ax.fill(angles, design_a_scores, alpha=0.25, color='#A7C7E7')

ax.plot(angles, design_b_scores, 'o-', linewidth=2, label='Design B',
        color='#E06666', alpha=0.8)
ax.fill(angles, design_b_scores, alpha=0.25, color='#F6B7B6')

# Set tick labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=14)

# Adjust label positions
ax.tick_params(axis='x', pad=15)  # Increase padding to avoid overlap

# Set y-axis range and adjust grid
ax.set_ylim(0, 1)
ax.tick_params(axis='y', labelsize=12)
ax.grid(True, alpha=0.3)

# Add legend
plt.legend(loc='upper right', fontsize=14, bbox_to_anchor=(1.2, 1.1))

# Set title
plt.title('Design Evaluation Comparison', pad=20, fontsize=16, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()