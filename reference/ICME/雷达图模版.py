import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# 1. 基础设置
# -------------------------
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'  # 设置全局字体加粗
plt.rcParams['axes.labelweight'] = 'bold'  # 设置轴标签加粗
plt.rcParams['axes.titleweight'] = 'bold'  # 设置标题加粗

# 评估维度
categories = ['Abstract', 'Tactile', 'Practical', 'Craftsmanship',
              'Spatial', 'Visual', 'Material']
num_vars = len(categories)

# -------------------------
# 2. 示例Recall数据 (假设区间 0~70)
# -------------------------
evaluator_1_scores = np.array([48, 28, 23, 32, 52, 33, 43])
evaluator_2_scores = np.array([33, 34, 36, 32, 38, 37, 35])

# -------------------------
# 3. 计算角度并闭合数据
# -------------------------
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

# 闭合数据
evaluator_1_scores = np.concatenate((evaluator_1_scores, [evaluator_1_scores[0]]))
evaluator_2_scores = np.concatenate((evaluator_2_scores, [evaluator_2_scores[0]]))
angles = np.concatenate((angles, [angles[0]]))

# -------------------------
# 4. 绘制雷达图
# -------------------------
fig, ax = plt.subplots(figsize=(12, 12))  # 增加图形大小以适应更大的字体
ax = plt.subplot(111, projection='polar')

color_e1 = '#76C6C2'  
color_e2 = '#E6CF8B'  

# 绘制Evaluator 1
ax.plot(angles, evaluator_1_scores, 'o-', linewidth=2.5, label='Whitebox Evaluator',
        color=color_e1, alpha=0.8)
ax.fill(angles, evaluator_1_scores, alpha=0.25, color=color_e1)

# 绘制Evaluator 2
ax.plot(angles, evaluator_2_scores, 'o-', linewidth=2.5, label='Blackbox Evaluator',
        color=color_e2, alpha=0.8)
ax.fill(angles, evaluator_2_scores, alpha=0.25, color=color_e2)

# 只设置角度刻度，不显示默认标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels([])

# -------------------------
# 5. 让标签文字位于外圈之外，增加字体大小和间距
# -------------------------
r_out = 70  # 增加标签距离
for idx, (label, angle) in enumerate(zip(categories, angles[:-1])):    
    if label == 'Practical':
        # 单独微调 "Practical" 避免飘太远
        ax.text(angle, 65, label,
                ha='center', va='center',
                fontsize=28, fontweight='bold')  # 增加字体大小

    elif label == 'Craftsmanship':
        ax.text(angle, 78, label,
        ha='center', va='center',
        fontsize=28, fontweight='bold')
    else:
        ax.text(angle, r_out, label,
                ha='center', va='center',
                fontsize=28, fontweight='bold')  # 增加字体大小

# -------------------------
# 6. 设置纵轴刻度为 0~60，只显示 [40, 50, 60]
# -------------------------
ax.set_ylim(0, 60)
ax.set_yticks([40, 50, 60])                 
ax.set_yticklabels([f"{i}" for i in [40, 50, 60]], fontsize=28, fontweight='bold')  # 增加刻度字体大小

# -------------------------
# 7. 网格可见度 & 图例
# -------------------------
ax.grid(True, alpha=0.95, linewidth=1.2)  


# 设置图例:
# - loc='upper right': 图例位置在右上角
# - fontsize=16: 图例字体大小为16
# - bbox_to_anchor=(1.4, 1.2): 微调图例位置,向右上方偏移
# - prop={'weight': 'bold'}: 设置图例字体为粗体
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.2),
          prop={'weight': 'bold', 'size': 28})

# plt.title("Evaluators' Classification Recall (0–60)",
#           pad=65, fontsize=38, fontweight='bold')  # 增加标题字体大小和上边距

# 调整图形布局，增加边距
plt.subplots_adjust(top=0.85, right=0.85)  # 增加顶部和右侧边距
plt.show()