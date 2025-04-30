import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 指定字体路径（替换为你的系统路径）
font_path = "/System/Library/Fonts/Supplemental/Songti.ttc"  # 宋体
font_prop = FontProperties(fname=font_path)

# 数据
labels = ['始终理性消费', '大部分理性消费', '经常非理性消费']
sizes = [30.5, 50.2, 19.3]  # 数据
# 基于你提供的色系重新定义颜色
colors = ['#8B5CF6', '#A78BFA', '#C4B5FD']

explode = (0.1, 0, 0)  # 突出第一个部分

# 绘制饼状图
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        colors=colors, startangle=90, wedgeprops={'edgecolor': 'black'},
        textprops={'fontproperties': font_prop})
plt.title('大学生对理性消费的自我评价', fontproperties=font_prop)

# 显示图表
plt.show()