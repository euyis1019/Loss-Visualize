import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# 设置字体和样式 - 增大基础字体大小
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14  # 从12增加到14
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['axes.labelsize'] = 16  # 增加轴标签字体大小
plt.rcParams['axes.titlesize'] = 18  # 增加标题字体大小
plt.rcParams['xtick.labelsize'] = 14  # 增加刻度标签字体大小
plt.rcParams['ytick.labelsize'] = 14  # 增加刻度标签字体大小
plt.rcParams['legend.fontsize'] = 14  # 增加图例字体大小

# 数据定义
# 15-1 setting
steps_15_1 = np.arange(0, 6, 1)
MiB_15_1 = np.array([78, 75, 60, 59, 42, 38])
PLOP_15_1 = np.array([80, 74, 70, 65, 59, 56])
MiB_NeST_15_1 = np.array([79, 76, 65, 61, 47, 40])
PLOP_NeST_15_1 = np.array([81, 77, 72, 67, 51, 39])

# SAM增强版本
MiB_SAM_15_1 = np.array([79, 76, 62, 60, 43, 39])
PLOP_SAM_15_1 = np.array([82, 77, 72, 68, 60, 59])
MiB_NeST_SAM_15_1 = np.array([80, 77, 66, 62, 48, 41])
PLOP_NeST_SAM_15_1 = np.array([83, 79, 74, 69, 52, 40])

# 10-1 setting
steps_10_1 = np.arange(0, 11, 1)
MiB_10_1 = np.array([80, 75, 65, 55, 45, 40, 35, 30, 25, 20, 15])
PLOP_10_1 = np.array([80, 74, 70, 60, 55, 50, 45, 40, 35, 30, 25])
MiB_NeST_10_1 = np.array([80, 77, 68, 65, 60, 58, 55, 50, 45, 40, 38])
PLOP_NeST_10_1 = np.array([80, 76, 74, 70, 68, 65, 60, 55, 50, 45, 42])

# SAM增强版本
MiB_SAM_10_1 = np.array([82, 78, 68, 58, 47, 42, 37, 32, 27, 22, 17])
PLOP_SAM_10_1 = np.array([82, 77, 73, 62, 57, 52, 47, 42, 37, 32, 27])
MiB_NeST_SAM_10_1 = np.array([83, 80, 71, 68, 63, 60, 57, 52, 47, 42, 39])
PLOP_NeST_SAM_10_1 = np.array([84, 80, 77, 73, 70, 67, 62, 57, 52, 47, 44])

def create_modern_dual_panel_with_diff():
    # 定义优雅的配色方案
    colors = {
        'MiB': '#1f77b4',       # 深蓝色
        'PLOP': '#ff7f0e',      # 橙色
        'MiB_NeST': '#2ca02c',  # 绿色
        'PLOP_NeST': '#d62728', # 红色
    }
    
    # 创建图形
    fig = plt.figure(figsize=(16, 7))
    gs = GridSpec(1, 2, width_ratios=[1, 2], wspace=0.25)
    
    # 15-1 setting (左面板)
    ax1 = fig.add_subplot(gs[0])
    
    # 基本方法 (虚线)
    ax1.plot(steps_15_1, MiB_15_1, '--', color=colors['MiB'], lw=2, marker='o', ms=7, label='MiB')
    ax1.plot(steps_15_1, PLOP_15_1, '--', color=colors['PLOP'], lw=2, marker='s', ms=7, label='PLOP')
    ax1.plot(steps_15_1, MiB_NeST_15_1, '--', color=colors['MiB_NeST'], lw=2, marker='^', ms=7, label='MiB+NeST')
    ax1.plot(steps_15_1, PLOP_NeST_15_1, '--', color=colors['PLOP_NeST'], lw=2, marker='d', ms=7, label='PLOP+NeST')
    
    # 添加半透明填充区域展示SAM增益
    ax1.fill_between(steps_15_1, MiB_15_1, MiB_SAM_15_1, color=colors['MiB'], alpha=0.25)
    ax1.fill_between(steps_15_1, PLOP_15_1, PLOP_SAM_15_1, color=colors['PLOP'], alpha=0.25)
    ax1.fill_between(steps_15_1, MiB_NeST_15_1, MiB_NeST_SAM_15_1, color=colors['MiB_NeST'], alpha=0.25)
    ax1.fill_between(steps_15_1, PLOP_NeST_15_1, PLOP_NeST_SAM_15_1, color=colors['PLOP_NeST'], alpha=0.25)
    
    # SAM增强版本 (实线)
    ax1.plot(steps_15_1, MiB_SAM_15_1, '-', color=colors['MiB'], lw=2.5, marker='o', ms=8, label='MiB+SAM')
    ax1.plot(steps_15_1, PLOP_SAM_15_1, '-', color=colors['PLOP'], lw=2.5, marker='s', ms=8, label='PLOP+SAM')
    ax1.plot(steps_15_1, MiB_NeST_SAM_15_1, '-', color=colors['MiB_NeST'], lw=2.5, marker='^', ms=8, label='MiB+NeST+SAM')
    ax1.plot(steps_15_1, PLOP_NeST_SAM_15_1, '-', color=colors['PLOP_NeST'], lw=2.5, marker='d', ms=8, label='PLOP+NeST+SAM')
    
    # 样式设置 - 增大字体
    ax1.set_xlabel('Task', fontsize=18, fontweight='bold')
    ax1.set_ylabel('mIoU (%)', fontsize=18, fontweight='bold')
    ax1.set_title('15-1 Setting with SAM Enhancement', fontsize=20, fontweight='bold', pad=15)
    ax1.grid(True, linestyle='--', alpha=0.3)
    ax1.set_ylim(35, 85)
    ax1.set_xticks(steps_15_1)
    ax1.tick_params(axis='both', which='major', labelsize=16)
    
    # 10-1 setting (右面板)
    ax2 = fig.add_subplot(gs[1])
    
    # 基本方法 (虚线)
    ax2.plot(steps_10_1, MiB_10_1, '--', color=colors['MiB'], lw=2, marker='o', ms=7)
    ax2.plot(steps_10_1, PLOP_10_1, '--', color=colors['PLOP'], lw=2, marker='s', ms=7)
    ax2.plot(steps_10_1, MiB_NeST_10_1, '--', color=colors['MiB_NeST'], lw=2, marker='^', ms=7)
    ax2.plot(steps_10_1, PLOP_NeST_10_1, '--', color=colors['PLOP_NeST'], lw=2, marker='d', ms=7)
    
    # 添加半透明填充区域展示SAM增益
    ax2.fill_between(steps_10_1, MiB_10_1, MiB_SAM_10_1, color=colors['MiB'], alpha=0.25)
    ax2.fill_between(steps_10_1, PLOP_10_1, PLOP_SAM_10_1, color=colors['PLOP'], alpha=0.25)
    ax2.fill_between(steps_10_1, MiB_NeST_10_1, MiB_NeST_SAM_10_1, color=colors['MiB_NeST'], alpha=0.25)
    ax2.fill_between(steps_10_1, PLOP_NeST_10_1, PLOP_NeST_SAM_10_1, color=colors['PLOP_NeST'], alpha=0.25)
    
    # SAM增强版本 (实线)
    ax2.plot(steps_10_1, MiB_SAM_10_1, '-', color=colors['MiB'], lw=2.5, marker='o', ms=8)
    ax2.plot(steps_10_1, PLOP_SAM_10_1, '-', color=colors['PLOP'], lw=2.5, marker='s', ms=8)
    ax2.plot(steps_10_1, MiB_NeST_SAM_10_1, '-', color=colors['MiB_NeST'], lw=2.5, marker='^', ms=8)
    ax2.plot(steps_10_1, PLOP_NeST_SAM_10_1, '-', color=colors['PLOP_NeST'], lw=2.5, marker='d', ms=8)
    
    # 样式设置 - 增大字体
    ax2.set_xlabel('Task', fontsize=18, fontweight='bold')
    ax2.set_ylabel('mIoU (%)', fontsize=18, fontweight='bold')
    ax2.set_title('10-1 Setting with SAM Enhancement', fontsize=20, fontweight='bold', pad=15)
    ax2.grid(True, linestyle='--', alpha=0.3)
    ax2.set_ylim(10, 85)
    ax2.set_xticks(range(0, 11, 2))
    
    # 设置刻度标签为粗体
    ax2.tick_params(axis='both', which='major', labelsize=16)
    for label in ax2.get_xticklabels() + ax2.get_yticklabels():
        label.set_fontweight('bold')
    
    # 在右侧子图左下角添加图例 - 调整为4行2列，文字加粗
    lines, labels = ax1.get_legend_handles_labels()
    legend = ax2.legend(lines, labels, loc='lower left', bbox_to_anchor=(0.02, 0.02),
                       fancybox=True, shadow=True, ncol=2, fontsize=12)
    plt.setp(legend.get_texts(), fontweight='bold')
    
    # 同样设置左侧子图的刻度标签为粗体
    for label in ax1.get_xticklabels() + ax1.get_yticklabels():
        label.set_fontweight('bold')
    
    # 调整布局
    plt.tight_layout()
    
    # 保存图表
    plt.savefig('exp_with_sam_enhance.svg', format='svg', dpi=300, bbox_inches='tight', transparent=True)
    plt.savefig('exp_with_sam_enhance.png', format='png', dpi=600, bbox_inches='tight', transparent=True)
    
    # 显示图表
    plt.show()
    
    return fig

if __name__ == "__main__":
    create_modern_dual_panel_with_diff()
    print("可视化图表已生成，文字大小已增加。") 