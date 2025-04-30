import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
models = ['Claude Sonnet 3.5', 'Gemini Pro 1.5', 'GPT4o', 
          'Cambrian-34B', 'LLaVANeXT-34B', 'Chameleon-30B']

data = {
    'Model': models * 4,
    'Evaluator': ['Evaluator1'] * len(models) * 2 + ['Evaluator2'] * len(models) * 2,
    'Metric': ['Precision'] * len(models) + ['Recall'] * len(models) + 
              ['Precision'] * len(models) + ['Recall'] * len(models),
    'Value': [
        # Evaluator 1 - Precision scores
        42.3, 36.8, 35.4, 25.1, 24.5, 22.2,
        # Evaluator 1 - Recall scores
        48.7, 42.1, 41.5, 31.9, 31.2, 29.8,
        # Evaluator 2 - Precision scores
        36.3, 30.1, 28.9, 23.4, 21.9, 20.2,
        # Evaluator 2 - Recall scores
        37.9, 32.8, 29.1, 23.7, 22.5, 21.1
    ]
}

# 转换为DataFrame
df = pd.DataFrame(data)

# 设置颜色主题
def get_model_colors(model, evaluator):
    if evaluator == 'Evaluator1':
        if model == 'Claude Sonnet 3.5':
            return ['#A7C7E7', '#6FA8DC']
        elif model == 'Gemini Pro 1.5':
            return ['#F6B7B6', '#E06666']
        elif model == 'GPT4o':
            return ['#B6D7A8', '#93C47D']
        else:
            return ['#C0C0C0', '#808080']
    else:
        if model == 'Claude Sonnet 3.5':
            return ['#8BB1D1', '#5892C6']
        elif model == 'Gemini Pro 1.5':
            return ['#E0A1A0', '#CA5050']
        elif model == 'GPT4o':
            return ['#A0C192', '#7DAE67']
        else:
            return ['#AAAAAA', '#6A6A6A']

# 设置绘图风格
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(15, 10))

# 设置全局字体粗细
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'

# 创建子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(30, 14))

# 处理每个评价器的数据
for idx, (evaluator, ax) in enumerate([('Evaluator1', ax1), ('Evaluator2', ax2)]):
    evaluator_data = df[df['Evaluator'] == evaluator]
    
    bar_positions = np.arange(len(models))
    bar_width = 0.35

    # 设置边框样式
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('black')
        spine.set_linewidth(1.5)

    # 分别绘制Precision和Recall
    precision_data = evaluator_data[evaluator_data['Metric'] == 'Precision']
    recall_data = evaluator_data[evaluator_data['Metric'] == 'Recall']

    # 绘制网格线
    ax.grid(True, axis='x', linestyle='--', alpha=0.7, zorder=0)

    # 绘制条形图并添加数值标签
    for i, (model, prec, rec) in enumerate(zip(models, 
                                             precision_data['Value'], 
                                             recall_data['Value'])):
        colors = get_model_colors(model, evaluator)
        
        # 绘制Precision条形图
        ax.barh(i - bar_width/2, prec, bar_width, 
               color=colors[0], zorder=2)
        
        # 绘制Recall条形图
        ax.barh(i + bar_width/2, rec, bar_width, 
               color=colors[1], zorder=2)
        
        # 添加数值标签
        ax.text(prec + 0.5, i - bar_width/2, f'P: {prec:.1f}%', 
               va='center', fontsize=20, weight='bold', zorder=4)
        ax.text(rec + 0.5, i + bar_width/2, f'R: {rec:.1f}%', 
               va='center', fontsize=20, weight='bold', zorder=4)

    # 添加40%标记文本


    # 自定义图表样式
    ax.set_title(f'{evaluator} Performance', pad=20, fontsize=40, weight='bold')
    ax.set_xlabel('Precision(P) and Recall(R) (%)', fontsize=30, weight='bold')
    if idx == 0:
        ax.set_ylabel('Models', fontsize=40, weight='bold')
    
    # 设置y轴标签
    ax.set_yticks(range(len(models)))
    ax.set_yticklabels(models, fontsize=30, weight='bold')
    ax.tick_params(axis='x', labelsize=30)
    
    # 调整x轴范围
    ax.set_xlim(0, max(df['Value'].max() * 1.15, 50))
ax1.axvline(x=40, color='black', linestyle='--', alpha=0.5, zorder=1)
ax1.text(40.5, len(models)-0.5, '40%', va='center', alpha=0.7, fontsize=16, weight='bold', zorder=4)
ax2.axvline(x=25, color='black', linestyle='--', alpha=0.5, zorder=1)
ax.text(25.5, len(models)-0.5, '25%', va='center', alpha=0.7, fontsize=16, weight='bold', zorder=4)
# 调整子图之间的间距
plt.tight_layout()
plt.show()
# plt.savefig("precision_recall.png")