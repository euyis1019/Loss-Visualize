import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

# 设置风格
plt.style.use('seaborn-v0_8-paper')  # 使用更专业的论文风格
plt.rcParams.update({
    'font.family': 'Times New Roman',  # 设置字体
    'font.size': 16,                   # 增大基础字体大小
    'font.weight': 'bold',             # 设置全局字体加粗
    'axes.labelsize': 20,              # 增大坐标轴标签大小
    'xtick.labelsize': 16,             # 增大x轴刻度标签大小
    'ytick.labelsize': 16,             # 增大y轴刻度标签大小
    'axes.linewidth': 1.5,             
    'axes.grid': True,                 # 显示网格
    'grid.linestyle': '--',            # 网格线型为虚线
    'grid.alpha': 0.5,                 # 网格透明度
    'axes.titleweight': 'bold',        # 坐标轴标题加粗
    'axes.labelweight': 'bold',        # 坐标轴标签加粗
})

# 数据 - 我们的方法
L_values = [8, 16, 32, 64]
L_19_1 = [79.30, 83.30, 83.95, 83.36]
L_10_1 = [80.07, 82.56, 83.12, 81.30]
L_15_1 = [78.63, 81.73, 83.40, 82.69]

G_values = [0, 1, 2]
G_19_1 = [73.16, 83.95, 83.08]
G_10_1 = [77.84, 83.12, 83.82]
G_15_1 = [78.34, 83.40, 83.88]

D_values = [1, 31, 51]
D_19_1 = [80.94, 83.95, 83.04]
D_10_1 = [80.58, 83.12, 82.42]
D_15_1 = [80.02, 83.40, 82.80]

# PLOP数据 (固定值)
PLOP_19_1 = 72.04
PLOP_10_1 = 30.45
PLOP_15_1 = 53.11

# 创建图形和子图
fig, axs = plt.subplots(1, 3, figsize=(18, 6), dpi=150, facecolor='white')

# 添加总标题
fig.suptitle('Sensitive Experiments', fontsize=20, fontweight='bold', y=0.91)

# 设置颜色方案为提供的颜色
task_colors = {
    '19-1 (2 tasks)': '#1f77b4',    # 蓝色
    '10-1 (11 tasks)': '#2ca02c',   # 绿色
    '15-1 (6 tasks)': '#ff7f0e'     # 橙色
}

# 标签和标记 - 为不同方法使用清晰的区分
task_labels = ['19-1 (2 tasks)', '10-1 (11 tasks)', '15-1 (6 tasks)']
method_markers = {'Ours': 'o', 'PLOP': '^'}  # 圆形表示我们的方法，三角形表示PLOP

# 更改线型以提高论文质量
method_linestyles = {'Ours': '-', 'PLOP': '--'}  # 使用虚线表示PLOP基线方法

# 子图标题
subplot_titles = ['LoRA Rank', 'Number of Hidden Layers', 'Number of Descriptions']

# 绘制三个子图
for idx, (subplot_title, x_values, datasets) in enumerate([
    (subplot_titles[0], L_values, [L_19_1, L_10_1, L_15_1]),
    (subplot_titles[1], G_values, [G_19_1, G_10_1, G_15_1]),
    (subplot_titles[2], D_values, [D_19_1, D_10_1, D_15_1])
]):
    ax = axs[idx]
    
    # 设置背景色为浅灰色以突出数据线
    ax.set_facecolor('white')  # 修改为白色背景
    
    # 为每个任务绘制我们的方法
    for i, (data, label) in enumerate(zip(datasets, task_labels)):
        ax.plot(x_values, data, marker=method_markers['Ours'], linewidth=2.5, markersize=7, 
                label=f'Ours - {label}', color=task_colors[label], linestyle=method_linestyles['Ours'])
        
        # 为PLOP添加不同任务的数据点
        plop_value = PLOP_19_1 if label == '19-1 (2 tasks)' else \
                    PLOP_10_1 if label == '10-1 (11 tasks)' else \
                    PLOP_15_1
        
        plop_y = [plop_value] * len(x_values)
        ax.plot(x_values, plop_y, marker=method_markers['PLOP'], linestyle=method_linestyles['PLOP'], 
                linewidth=2, markersize=7, label=f'PLOP - {label}', color=task_colors[label])
    
    # 不设置标题，只使用x轴标签
    # ax.set_title(subplot_title, fontsize=14, fontweight='bold', pad=10)
    
    # 设置x轴标签
    ax.set_xlabel(subplot_title, fontsize=18, fontweight='bold')
    
    # 只在第一个子图上显示y轴标签
    if idx == 0:
        ax.set_ylabel('mIoU (%)', fontsize=18, fontweight='bold')
    else:
        ax.set_yticklabels([])
    
    # 设置刻度和网格
    ax.set_xticks(x_values)
    ax.set_ylim(25, 90)
    ax.grid(True, linestyle='--', alpha=0.4, color='#cccccc')
    
    # 添加边框
    for spine in ax.spines.values():
        spine.set_edgecolor('#333333')
        spine.set_linewidth(1)

# 创建自定义图例
handles, labels = [], []
for task in task_labels:
    # 我们的方法
    task_line = plt.Line2D([0], [0], color=task_colors[task], marker=method_markers['Ours'], 
                          linestyle=method_linestyles['Ours'], markersize=10, linewidth=2)  # 增大marker大小
    handles.append(task_line)
    labels.append(f'Ours - {task}')
    
    # PLOP方法
    plop_line = plt.Line2D([0], [0], color=task_colors[task], marker=method_markers['PLOP'], 
                           linestyle=method_linestyles['PLOP'], markersize=10, linewidth=2)  # 增大marker大小
    handles.append(plop_line)
    labels.append(f'PLOP - {task}')

# 在最下方添加图例，确保不遮挡
legend = fig.legend(handles, labels, 
                   loc='upper center', 
                   bbox_to_anchor=(0.5, 0.15), 
                   ncol=3, 
                   frameon=True, 
                   framealpha=0.95, 
                   edgecolor='#333333',
                   prop={'weight': 'bold', 'size': 16})  # 增大图例字体大小

# 调整布局，为标题留出空间
plt.tight_layout(rect=[0.01, 0.12, 1, 0.96])  # 修改了top margin从0.97到0.95，为标题留出更多空间

# 保存图像
plt.savefig('parameter_sensitivity_improved.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()