import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据，移除Gemini Flash
models = ['Claude Sonnet 3.5', 'Gemini Pro 1.5', 'GPT4o', 
          'Cambrian-34B', 'LLaVANeXT-34B', 'Chameleon-30B']

data = {
    'Model': models * 2,
    'Metric': ['Precision'] * len(models) + ['Recall'] * len(models),
    'Value': [
        # Precision scores
        42.3, 36.8, 35.4, 25.1, 24.5, 22.2,
        # Recall scores
        48.7, 42.1, 41.5, 31.9, 31.2, 29.8
    ]
}

# 转换为DataFrame
df = pd.DataFrame(data)

# 根据Recall值确定颜色主题
recall_data = df[df['Metric'] == 'Recall']
model_colors = {}
for model in models:
    recall_value = float(recall_data[recall_data['Model'] == model]['Value'])
    if recall_value > 40:
        if model == 'Claude Sonnet 3.5':
            model_colors[model] = ['#A7C7E7', '#6FA8DC']  # 图中的主题蓝色
        elif model == 'Gemini Pro 1.5':
            model_colors[model] = ['#F6B7B6', '#E06666']  # 图中的主题粉色
        elif model == 'GPT4o':
            model_colors[model] = ['#B6D7A8', '#93C47D']  # 图中的主题绿色
    else:
        model_colors[model] = ['#C0C0C0', '#808080']  # 灰色主题

# 设置绘图风格
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(12, 8))

# 设置全局字体粗细
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'

# 创建分组条形图
ax = plt.gca()
bar_positions = np.arange(len(models))
bar_width = 0.35

# 设置边框样式
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.spines['top'].set_color('black')
ax.spines['right'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

# 分别绘制Precision和Recall
precision_data = df[df['Metric'] == 'Precision']
recall_data = df[df['Metric'] == 'Recall']

# 绘制网格线 (设置较低的zorder)
plt.grid(True, axis='x', linestyle='--', alpha=0.7, zorder=0)

# 添加40%的参考线 (设置较低的zorder)
plt.axvline(x=40, color='black', linestyle='--', alpha=0.5, zorder=1)

# 绘制条形图并添加数值标签
for idx, (model, prec, rec) in enumerate(zip(models, 
                                           precision_data['Value'], 
                                           recall_data['Value'])):
    # 绘制Precision条形图 (中等zorder)
    prec_bar = plt.barh(idx - bar_width/2, prec, bar_width, 
                       color=model_colors[model][0], 
                       zorder=2)
    
    # 绘制Recall条形图 (中等zorder)
    rec_bar = plt.barh(idx + bar_width/2, rec, bar_width, 
                      color=model_colors[model][1], 
                      zorder=2)
    
    # 添加数值标签 (最高zorder)，增加字体粗细
    ax.text(prec + 0.5, idx - bar_width/2, f'P: {prec:.1f}%', 
            va='center', fontsize=14, weight='bold', zorder=4)
    ax.text(rec + 0.5, idx + bar_width/2, f'R: {rec:.1f}%', 
            va='center', fontsize=14, weight='bold', zorder=4)

# 添加40%标记文本 (最高zorder)
plt.text(40.5, len(models)-0.5, '40%', va='center', alpha=0.7, 
         fontsize=14, weight='bold', zorder=4)

# 自定义图表样式
plt.title('Model Performance Comparison', pad=20, fontsize=18, weight='bold')
plt.xlabel('Precision(P) and Recall(R) (%)', fontsize=16, weight='bold')
plt.ylabel('Models', fontsize=16, weight='bold')

# 设置y轴标签，增加字体粗细
plt.yticks(range(len(models)), models, fontsize=14, weight='bold')
plt.xticks(fontsize=14, weight='bold')

# 调整x轴范围以容纳标签
plt.xlim(0, max(df['Value'].max() * 1.15, 50))

# 调整布局以确保所有元素可见
plt.tight_layout()

# 显示图表
plt.show()