import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
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

# ===== 方案1: 现代化双面板设计 =====
def create_modern_dual_panel():
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
    ax1.fill_between(steps_15_1, MiB_15_1, MiB_SAM_15_1, color=colors['MiB'], alpha=0.25, label='_nolegend_')
    ax1.fill_between(steps_15_1, PLOP_15_1, PLOP_SAM_15_1, color=colors['PLOP'], alpha=0.25, label='_nolegend_')
    ax1.fill_between(steps_15_1, MiB_NeST_15_1, MiB_NeST_SAM_15_1, color=colors['MiB_NeST'], alpha=0.25, label='_nolegend_')
    ax1.fill_between(steps_15_1, PLOP_NeST_15_1, PLOP_NeST_SAM_15_1, color=colors['PLOP_NeST'], alpha=0.25, label='_nolegend_')
    
    # SAM增强版本 (实线)
    ax1.plot(steps_15_1, MiB_SAM_15_1, '-', color=colors['MiB'], lw=2.5, marker='o', ms=8, label='MiB+SAM')
    ax1.plot(steps_15_1, PLOP_SAM_15_1, '-', color=colors['PLOP'], lw=2.5, marker='s', ms=8, label='PLOP+SAM')
    ax1.plot(steps_15_1, MiB_NeST_SAM_15_1, '-', color=colors['MiB_NeST'], lw=2.5, marker='^', ms=8, label='MiB+NeST+SAM')
    ax1.plot(steps_15_1, PLOP_NeST_SAM_15_1, '-', color=colors['PLOP_NeST'], lw=2.5, marker='d', ms=8, label='PLOP+NeST+SAM')
    
    # 样式设置 - 增大字体
    ax1.set_xlabel('Step', fontsize=18, fontweight='bold')
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
    ax2.fill_between(steps_10_1, MiB_10_1, MiB_SAM_10_1, color=colors['MiB'], alpha=0.25, label='_nolegend_')
    ax2.fill_between(steps_10_1, PLOP_10_1, PLOP_SAM_10_1, color=colors['PLOP'], alpha=0.25, label='_nolegend_')
    ax2.fill_between(steps_10_1, MiB_NeST_10_1, MiB_NeST_SAM_10_1, color=colors['MiB_NeST'], alpha=0.25, label='_nolegend_')
    ax2.fill_between(steps_10_1, PLOP_NeST_10_1, PLOP_NeST_SAM_10_1, color=colors['PLOP_NeST'], alpha=0.25, label='_nolegend_')
    
    # SAM增强版本 (实线)
    ax2.plot(steps_10_1, MiB_SAM_10_1, '-', color=colors['MiB'], lw=2.5, marker='o', ms=8)
    ax2.plot(steps_10_1, PLOP_SAM_10_1, '-', color=colors['PLOP'], lw=2.5, marker='s', ms=8)
    ax2.plot(steps_10_1, MiB_NeST_SAM_10_1, '-', color=colors['MiB_NeST'], lw=2.5, marker='^', ms=8)
    ax2.plot(steps_10_1, PLOP_NeST_SAM_10_1, '-', color=colors['PLOP_NeST'], lw=2.5, marker='d', ms=8)
    
    # 样式设置 - 增大字体
    ax2.set_xlabel('Step', fontsize=18, fontweight='bold')
    ax2.set_ylabel('mIoU (%)', fontsize=18, fontweight='bold')
    ax2.set_title('10-1 Setting with SAM Enhancement', fontsize=20, fontweight='bold', pad=15)
    ax2.grid(True, linestyle='--', alpha=0.3)
    ax2.set_ylim(10, 85)
    ax2.set_xticks(range(0, 11, 2))
    ax2.tick_params(axis='both', which='major', labelsize=16)

    # 在右侧添加统一图例 - 增大字体
    lines, labels = ax1.get_legend_handles_labels()
    fig.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, 0.02),
              fancybox=True, shadow=True, ncol=4, fontsize=14)
    
    # 调整布局
    plt.tight_layout(rect=[0, 0.07, 1, 0.95])
    
    # 保存为SVG格式
    plt.savefig('modern_dual_panel.svg', format='svg', dpi=300, bbox_inches='tight', transparent=True)
    
    # 保存为PNG格式（高分辨率）
    plt.savefig('modern_dual_panel.png', format='png', dpi=600, bbox_inches='tight', transparent=True)
    
    return fig

# ===== 方案2: 增强对比可视化 =====
def create_enhanced_comparison():
    fig, axes = plt.subplots(2, 1, figsize=(12, 12), sharex=False)

    # 共享颜色定义
    color_map = {
        'MiB': '#1a76b4',
        'PLOP': '#ff7f0e', 
        'MiB_NeST': '#2ca02c',
        'PLOP_NeST': '#d62728'
    }
    
    # 15-1 setting (上图)
    ax1 = axes[0]
    
    # 计算SAM带来的增益
    MiB_gain_15_1 = MiB_SAM_15_1 - MiB_15_1
    PLOP_gain_15_1 = PLOP_SAM_15_1 - PLOP_15_1
    MiB_NeST_gain_15_1 = MiB_NeST_SAM_15_1 - MiB_NeST_15_1
    PLOP_NeST_gain_15_1 = PLOP_NeST_SAM_15_1 - PLOP_NeST_15_1
    
    # 基础性能展示
    ax1.plot(steps_15_1, MiB_15_1, '-', color=color_map['MiB'], lw=3, label='MiB')
    ax1.plot(steps_15_1, PLOP_15_1, '-', color=color_map['PLOP'], lw=3, label='PLOP')
    ax1.plot(steps_15_1, MiB_NeST_15_1, '-', color=color_map['MiB_NeST'], lw=3, label='MiB+NeST')
    ax1.plot(steps_15_1, PLOP_NeST_15_1, '-', color=color_map['PLOP_NeST'], lw=3, label='PLOP+NeST')
    
    # 使用填充区域展示SAM增益
    ax1.fill_between(steps_15_1, MiB_15_1, MiB_SAM_15_1, color=color_map['MiB'], alpha=0.3)
    ax1.fill_between(steps_15_1, PLOP_15_1, PLOP_SAM_15_1, color=color_map['PLOP'], alpha=0.3)
    ax1.fill_between(steps_15_1, MiB_NeST_15_1, MiB_NeST_SAM_15_1, color=color_map['MiB_NeST'], alpha=0.3)
    ax1.fill_between(steps_15_1, PLOP_NeST_15_1, PLOP_NeST_SAM_15_1, color=color_map['PLOP_NeST'], alpha=0.3)
    
    # SAM增强版本
    ax1.plot(steps_15_1, MiB_SAM_15_1, '--', color=color_map['MiB'], lw=2, label='MiB+SAM')
    ax1.plot(steps_15_1, PLOP_SAM_15_1, '--', color=color_map['PLOP'], lw=2, label='PLOP+SAM')
    ax1.plot(steps_15_1, MiB_NeST_SAM_15_1, '--', color=color_map['MiB_NeST'], lw=2, label='MiB+NeST+SAM')
    ax1.plot(steps_15_1, PLOP_NeST_SAM_15_1, '--', color=color_map['PLOP_NeST'], lw=2, label='PLOP+NeST+SAM')
    
    # 样式设置 - 增大字体
    ax1.set_xlabel('Step', fontsize=18, fontweight='bold')
    ax1.set_ylabel('mIoU (%)', fontsize=18, fontweight='bold')
    ax1.set_title('15-1 Setting with SAM Enhancement', fontsize=20, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.3)
    ax1.set_ylim(35, 85)
    ax1.set_xticks(steps_15_1)
    ax1.tick_params(axis='both', which='major', labelsize=16)
    
    # 10-1 setting (下图)
    ax2 = axes[1]
    
    # 计算SAM带来的增益
    MiB_gain_10_1 = MiB_SAM_10_1 - MiB_10_1
    PLOP_gain_10_1 = PLOP_SAM_10_1 - PLOP_10_1
    MiB_NeST_gain_10_1 = MiB_NeST_SAM_10_1 - MiB_NeST_10_1
    PLOP_NeST_gain_10_1 = PLOP_NeST_SAM_10_1 - PLOP_NeST_10_1
    
    # 基础性能展示
    ax2.plot(steps_10_1, MiB_10_1, '-', color=color_map['MiB'], lw=3)
    ax2.plot(steps_10_1, PLOP_10_1, '-', color=color_map['PLOP'], lw=3)
    ax2.plot(steps_10_1, MiB_NeST_10_1, '-', color=color_map['MiB_NeST'], lw=3)
    ax2.plot(steps_10_1, PLOP_NeST_10_1, '-', color=color_map['PLOP_NeST'], lw=3)
    
    # 使用填充区域展示SAM增益
    ax2.fill_between(steps_10_1, MiB_10_1, MiB_SAM_10_1, color=color_map['MiB'], alpha=0.3)
    ax2.fill_between(steps_10_1, PLOP_10_1, PLOP_SAM_10_1, color=color_map['PLOP'], alpha=0.3)
    ax2.fill_between(steps_10_1, MiB_NeST_10_1, MiB_NeST_SAM_10_1, color=color_map['MiB_NeST'], alpha=0.3)
    ax2.fill_between(steps_10_1, PLOP_NeST_10_1, PLOP_NeST_SAM_10_1, color=color_map['PLOP_NeST'], alpha=0.3)
    
    # SAM增强版本
    ax2.plot(steps_10_1, MiB_SAM_10_1, '--', color=color_map['MiB'], lw=2)
    ax2.plot(steps_10_1, PLOP_SAM_10_1, '--', color=color_map['PLOP'], lw=2)
    ax2.plot(steps_10_1, MiB_NeST_SAM_10_1, '--', color=color_map['MiB_NeST'], lw=2)
    ax2.plot(steps_10_1, PLOP_NeST_SAM_10_1, '--', color=color_map['PLOP_NeST'], lw=2)
    
    # 样式设置 - 增大字体
    ax2.set_xlabel('Step', fontsize=18, fontweight='bold')
    ax2.set_ylabel('mIoU (%)', fontsize=18, fontweight='bold')
    ax2.set_title('10-1 Setting with SAM Enhancement', fontsize=20, fontweight='bold')
    ax2.grid(True, linestyle='--', alpha=0.3)
    ax2.set_ylim(10, 85)
    ax2.set_xticks(range(0, 11, 2))
    ax2.tick_params(axis='both', which='major', labelsize=16)
    
    # 图例 - 增大字体
    lines, labels = ax1.get_legend_handles_labels()
    fig.legend(lines, labels, loc='lower center', bbox_to_anchor=(0.5, 0.02),
              fancybox=True, shadow=True, ncol=4, fontsize=14)
    
    plt.tight_layout(rect=[0, 0.07, 1, 0.95])
    plt.savefig('enhanced_comparison.pdf', dpi=300, bbox_inches='tight')
    return fig

# ===== 方案3: 增益热图可视化 =====
def create_heatmap_visualization():
    # 创建图形
    fig = plt.figure(figsize=(18, 8))
    gs = GridSpec(2, 6, width_ratios=[5, 5, 0.4, 0.8, 5, 0.4], height_ratios=[1, 1], wspace=0.3)
    
    # 15-1 setting 折线图
    ax1 = fig.add_subplot(gs[0, 0:2])
    
    # 定义配色方案
    colors = {
        'MiB': '#1f77b4',       # 深蓝色
        'PLOP': '#ff7f0e',      # 橙色
        'MiB_NeST': '#2ca02c',  # 绿色
        'PLOP_NeST': '#d62728', # 红色
    }
    
    # 基本方法 (虚线)
    ax1.plot(steps_15_1, MiB_15_1, '--', color=colors['MiB'], lw=2, marker='o', ms=7, label='MiB')
    ax1.plot(steps_15_1, PLOP_15_1, '--', color=colors['PLOP'], lw=2, marker='s', ms=7, label='PLOP')
    ax1.plot(steps_15_1, MiB_NeST_15_1, '--', color=colors['MiB_NeST'], lw=2, marker='^', ms=7, label='MiB+NeST')
    ax1.plot(steps_15_1, PLOP_NeST_15_1, '--', color=colors['PLOP_NeST'], lw=2, marker='d', ms=7, label='PLOP+NeST')
    
    # SAM增强版本 (实线)
    ax1.plot(steps_15_1, MiB_SAM_15_1, '-', color=colors['MiB'], lw=2.5, marker='o', ms=8, label='MiB+SAM')
    ax1.plot(steps_15_1, PLOP_SAM_15_1, '-', color=colors['PLOP'], lw=2.5, marker='s', ms=8, label='PLOP+SAM')
    ax1.plot(steps_15_1, MiB_NeST_SAM_15_1, '-', color=colors['MiB_NeST'], lw=2.5, marker='^', ms=8, label='MiB+NeST+SAM')
    ax1.plot(steps_15_1, PLOP_NeST_SAM_15_1, '-', color=colors['PLOP_NeST'], lw=2.5, marker='d', ms=8, label='PLOP+NeST+SAM')
    
    # 样式设置 - 增大字体
    ax1.set_xlabel('Step', fontsize=16, fontweight='bold')
    ax1.set_ylabel('mIoU (%)', fontsize=16, fontweight='bold')
    ax1.set_title('15-1 Setting Performance', fontsize=18, fontweight='bold', pad=10)
    ax1.grid(True, linestyle='--', alpha=0.3)
    ax1.set_ylim(35, 85)
    ax1.set_xticks(steps_15_1)
    ax1.tick_params(axis='both', which='major', labelsize=14)
    
    # 图例 - 增大字体
    ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4, fontsize=12)
    
    # 10-1 setting 折线图
    ax2 = fig.add_subplot(gs[1, 0:2])
    
    # 基本方法
    ax2.plot(steps_10_1, MiB_10_1, '--', color=colors['MiB'], lw=2, marker='o', ms=7, label='MiB')
    ax2.plot(steps_10_1, PLOP_10_1, '--', color=colors['PLOP'], lw=2, marker='s', ms=7, label='PLOP')
    ax2.plot(steps_10_1, MiB_NeST_10_1, '--', color=colors['MiB_NeST'], lw=2, marker='^', ms=7, label='MiB+NeST')
    ax2.plot(steps_10_1, PLOP_NeST_10_1, '--', color=colors['PLOP_NeST'], lw=2, marker='d', ms=7, label='PLOP+NeST')
    
    # SAM增强版本
    ax2.plot(steps_10_1, MiB_SAM_10_1, '-', color=colors['MiB'], lw=2.5, marker='o', ms=8, label='MiB+SAM')
    ax2.plot(steps_10_1, PLOP_SAM_10_1, '-', color=colors['PLOP'], lw=2.5, marker='s', ms=8, label='PLOP+SAM')
    ax2.plot(steps_10_1, MiB_NeST_SAM_10_1, '-', color=colors['MiB_NeST'], lw=2.5, marker='^', ms=8, label='MiB+NeST+SAM')
    ax2.plot(steps_10_1, PLOP_NeST_SAM_10_1, '-', color=colors['PLOP_NeST'], lw=2.5, marker='d', ms=8, label='PLOP+NeST+SAM')
    
    # 样式设置 - 增大字体
    ax2.set_xlabel('Step', fontsize=16, fontweight='bold')
    ax2.set_ylabel('mIoU (%)', fontsize=16, fontweight='bold')
    ax2.set_title('10-1 Setting Performance', fontsize=18, fontweight='bold', pad=10)
    ax2.grid(True, linestyle='--', alpha=0.3)
    ax2.set_ylim(10, 85)
    ax2.set_xticks(range(0, 11, 2))
    ax2.tick_params(axis='both', which='major', labelsize=14)
    
    # 图例 - 增大字体
    ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4, fontsize=12)
    
    # 计算15-1 setting的SAM增益
    MiB_gain_15_1 = MiB_SAM_15_1 - MiB_15_1
    PLOP_gain_15_1 = PLOP_SAM_15_1 - PLOP_15_1
    MiB_NeST_gain_15_1 = MiB_NeST_SAM_15_1 - MiB_NeST_15_1
    PLOP_NeST_gain_15_1 = PLOP_NeST_SAM_15_1 - PLOP_NeST_15_1
    
    # 创建15-1 setting的增益热图数据
    gain_data_15_1 = np.array([
        MiB_gain_15_1,
        PLOP_gain_15_1,
        MiB_NeST_gain_15_1,
        PLOP_NeST_gain_15_1
    ])
    
    # 15-1 setting的增益热图
    ax3 = fig.add_subplot(gs[0, 4])
    im1 = ax3.imshow(gain_data_15_1, cmap='YlGnBu', aspect='auto')
    
    # 添加增益值文本标注 - 增大字体
    for i in range(4):
        for j in range(len(steps_15_1)):
            text = ax3.text(j, i, f"{gain_data_15_1[i, j]:.1f}",
                          ha="center", va="center", color="black", fontsize=12, fontweight='bold')
    
    # 设置y轴标签 - 增大字体
    methods = ['MiB', 'PLOP', 'MiB+NeST', 'PLOP+NeST']
    ax3.set_yticks(range(len(methods)))
    ax3.set_yticklabels(methods, fontsize=14)
    
    # 设置x轴标签 - 增大字体
    ax3.set_xticks(range(len(steps_15_1)))
    ax3.set_xticklabels(steps_15_1, fontsize=14)
    
    # 设置标题 - 增大字体
    ax3.set_title('SAM Enhancement Gains (15-1)', fontsize=18, fontweight='bold', pad=10)
    ax3.set_xlabel('Step', fontsize=16, fontweight='bold')
    
    # 添加15-1热图颜色条 - 增大字体
    cbar1 = plt.colorbar(im1, cax=fig.add_subplot(gs[0, 5]))
    cbar1.set_label('Gain (mIoU %)', fontsize=14, fontweight='bold')
    cbar1.ax.tick_params(labelsize=12)
    
    # 计算10-1 setting的SAM增益
    MiB_gain_10_1 = MiB_SAM_10_1 - MiB_10_1
    PLOP_gain_10_1 = PLOP_SAM_10_1 - PLOP_10_1
    MiB_NeST_gain_10_1 = MiB_NeST_SAM_10_1 - MiB_NeST_10_1
    PLOP_NeST_gain_10_1 = PLOP_NeST_SAM_10_1 - PLOP_NeST_10_1
    
    # 创建10-1 setting的增益热图数据
    gain_data_10_1 = np.array([
        MiB_gain_10_1,
        PLOP_gain_10_1,
        MiB_NeST_gain_10_1,
        PLOP_NeST_gain_10_1
    ])
    
    # 10-1 setting的增益热图
    ax4 = fig.add_subplot(gs[1, 4])
    im2 = ax4.imshow(gain_data_10_1, cmap='YlGnBu', aspect='auto')
    
    # 添加增益值文本标注 - 增大字体
    for i in range(4):
        for j in range(len(steps_10_1)):
            # 仅在足够空间时显示文本
            if len(steps_10_1) <= 6 or j % 2 == 0:
                text = ax4.text(j, i, f"{gain_data_10_1[i, j]:.1f}",
                              ha="center", va="center", color="black", fontsize=11, fontweight='bold')
    
    # 设置y轴标签 - 增大字体
    ax4.set_yticks(range(len(methods)))
    ax4.set_yticklabels(methods, fontsize=14)
    
    # 设置x轴标签 - 增大字体
    ax4.set_xticks(range(0, len(steps_10_1), 2))
    ax4.set_xticklabels(steps_10_1[::2], fontsize=14)
    
    # 设置标题 - 增大字体
    ax4.set_title('SAM Enhancement Gains (10-1)', fontsize=18, fontweight='bold', pad=10)
    ax4.set_xlabel('Step', fontsize=16, fontweight='bold')
    
    # 添加10-1热图颜色条 - 增大字体
    cbar2 = plt.colorbar(im2, cax=fig.add_subplot(gs[1, 5]))
    cbar2.set_label('Gain (mIoU %)', fontsize=14, fontweight='bold')
    cbar2.ax.tick_params(labelsize=12)
    
    # 整体标题 - 增大字体
    fig.suptitle('Segmentation Performance & SAM Enhancement Gains', fontsize=22, fontweight='bold', y=0.98)
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('heatmap_visualization.pdf', dpi=300, bbox_inches='tight')
    return fig

# 创建所有可视化
create_modern_dual_panel()
create_enhanced_comparison()
create_heatmap_visualization()

print("可视化图表已生成，文字大小已增加。")