import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec

# 生成合成损失函数地形数据的函数
def generate_loss_landscape(width, height, complexity=2, seed=42):
    """生成包含多个山峰和山谷的合成损失函数地形数据"""
    np.random.seed(seed)  # 设置随机种子以确保可重复性
    
    # 创建x和y坐标网格
    x = np.linspace(-5, 5, width)
    y = np.linspace(-5, 5, height)
    X, Y = np.meshgrid(x, y)
    
    # 初始化地形数据
    Z = np.zeros((height, width))
    
    # 添加多个随机高斯组件以创建复杂地形
    for _ in range(complexity):
        # 随机生成高斯分布的中心点
        x0 = np.random.uniform(-4, 4)
        y0 = np.random.uniform(-4, 4)
        # 随机生成高斯分布的标准差
        sigma_x = np.random.uniform(0.5, 2.0)
        sigma_y = np.random.uniform(0.5, 2.0)
        # 随机生成振幅
        amplitude = np.random.uniform(-15, 15)
        
        # 添加高斯组件到地形
        Z += amplitude * np.exp(-((X - x0)**2 / (2 * sigma_x**2) + (Y - y0)**2 / (2 * sigma_y**2)))
    
    # 添加噪声以增加纹理
    Z += np.random.normal(0, 0.5, Z.shape)
    
    # 确保数值在合理的可视化范围内
    Z = Z - np.max(Z)  # 使最大值变为0
    
    return Z

# 对数据应用sigmoid函数的函数
def apply_sigmoid(data):
    """对数据应用sigmoid函数进行转换"""
    return 1 / (1 + np.exp(-data))

# 可视化单个损失函数地形的函数
def plot_3d_landscape(data, ax, colormap='Spectral', alpha=0.8, elev=30, azim=-60, 
                     hide_axis=True, zlim=None, title=None):
    """创建损失函数地形的3D表面图"""
    height, width = data.shape
    x = np.arange(width)
    y = np.arange(height)
    X, Y = np.meshgrid(x, y)
    
    # 定义颜色映射范围
    vmin = np.min(data)
    vmax = np.max(data)
    
    # 创建3D表面
    surf = ax.plot_surface(X, Y, data, cmap=colormap, alpha=alpha, 
                          vmin=vmin, vmax=vmax, edgecolor='none')
    
    # 设置视角
    ax.view_init(elev=elev, azim=azim)
    
    # 如果指定了z轴限制，则应用
    if zlim:
        ax.set_zlim(zlim)
    
    # 如果需要隐藏坐标轴
    if hide_axis:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        ax.grid(False)
        plt.axis('off')
    
    if title:
        ax.set_title(title, fontsize=10)
    
    return surf

# 创建完整可视化图的函数
def create_full_visualization(categories=['Train', 'Sheep', 'Potted Plant', 'Sofa']):
    """创建包含多个类别和处理步骤的完整可视化图"""
    # 计算行数（类别数+1用于标题行）和列数
    n_rows = len(categories) + 1
    n_cols = 7  # 图像、t-1步预测、t-1步背景logits、t步背景适应、t步背景logits(Sigmoid)、t步预测、类别
    
    # 使用gridspec创建图形
    fig = plt.figure(figsize=(20, 16))
    gs = gridspec.GridSpec(n_rows, n_cols, width_ratios=[1, 1, 1, 1, 1, 1, 1])
    
    # 数据生成参数
    width, height = 50, 50
    np.random.seed(42)  # 设置随机种子以确保可重复性
    seeds = np.random.randint(0, 1000, n_rows)
    
    # 定义z轴限制以确保一致的缩放
    zlim = (-20, 5)
    
    # 标题标签
    headers = ['图像', 't-1步预测', 't-1步背景logits', 
               't步背景适应', 't步背景logits(Sigmoid)',
               't步预测', 't步类别']
    
    # 添加标题标签
    for col, header in enumerate(headers):
        header_ax = fig.add_subplot(gs[0, col])
        header_ax.text(0.5, -0.1, header, ha='center', va='center', fontsize=10, transform=header_ax.transAxes)
        header_ax.axis('off')
    
    # 处理每个类别
    for row, category in enumerate(categories):
        # 使用不同的随机种子生成基础数据
        base_data = generate_loss_landscape(width, height, complexity=3, seed=seeds[row])
        
        # 为不同的处理步骤创建数据变体
        data_t_minus_1 = base_data + np.random.normal(0, 2, base_data.shape)
        data_adaptation = base_data - data_t_minus_1  # 残差
        data_t = data_t_minus_1 + data_adaptation  # 组合结果
        data_sigmoid = apply_sigmoid(data_t)  # 应用sigmoid
        
        # 为t-1和t步创建颜色编码的预测掩码
        mask_t_minus_1 = np.zeros((height, width, 3))
        mask_t = np.zeros((height, width, 3))
        
        # 随机化可视化颜色
        colors = [(0.7, 0.3, 0.7), (0.3, 0.7, 0.7), (0.8, 0.2, 0.3), (0.2, 0.8, 0.3)]
        color = colors[row % len(colors)]
        
        # 创建随机形状的掩码
        center_x = width // 2 + np.random.randint(-10, 10)
        center_y = height // 2 + np.random.randint(-10, 10)
        radius = np.random.randint(15, 25)
        
        for y in range(height):
            for x in range(width):
                dist = np.sqrt((x - center_x)**2 + (y - center_y)**2)
                if dist < radius:
                    mask_t_minus_1[y, x] = color
                    
                # t步使用稍微不同的形状
                dist_mod = dist + np.sin(x/5) * 3 + np.cos(y/5) * 3
                if dist_mod < radius:
                    mask_t[y, x] = color
        
        # 为每行创建子图
        
        # 列0：图像（在实际实现中会是真实图像）
        ax_img = fig.add_subplot(gs[row+1, 0])
        ax_img.text(0.5, 0.5, f"{category} 图像", ha='center', va='center')
        ax_img.axis('off')
        
        # 列1：t-1步预测
        ax_pred_t_minus_1 = fig.add_subplot(gs[row+1, 1])
        ax_pred_t_minus_1.imshow(mask_t_minus_1)
        ax_pred_t_minus_1.axis('off')
        
        # 列2：t-1步背景logits
        ax_bg_t_minus_1 = fig.add_subplot(gs[row+1, 2], projection='3d')
        plot_3d_landscape(data_t_minus_1, ax_bg_t_minus_1, zlim=zlim)
        
        # 列3：t步背景适应
        ax_adapt = fig.add_subplot(gs[row+1, 3], projection='3d')
        plot_3d_landscape(data_adaptation, ax_adapt, zlim=zlim)
        
        # 列4：t步背景logits(Sigmoid)
        ax_sigmoid = fig.add_subplot(gs[row+1, 4], projection='3d')
        plot_3d_landscape(data_sigmoid, ax_sigmoid, zlim=(0, 1))
        
        # 列5：t步预测
        ax_pred_t = fig.add_subplot(gs[row+1, 5])
        ax_pred_t.imshow(mask_t)
        ax_pred_t.axis('off')
        
        # 列6：类别名称
        ax_cat = fig.add_subplot(gs[row+1, 6])
        ax_cat.text(0.5, 0.5, category, ha='center', va='center', fontsize=14)
        ax_cat.set_facecolor(f'C{row}')
        ax_cat.axis('off')
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.95)
    plt.suptitle("背景适应结果的3D可视化", fontsize=16)
    
    return fig

# 生成与示例相同类别的可视化
fig = create_full_visualization(categories=['火车', '绵羊', '盆栽植物', '沙发'])

# 保存图形
plt.savefig("loss_landscape_visualization.png", dpi=300, bbox_inches='tight')
plt.show()

# 生成单个3D地形可视化的函数
def create_single_3d_visualization(width=100, height=100, complexity=3, seed=42, 
                                  colormap='Spectral', elev=60, azim=-90):
    """创建单个高质量的损失函数地形3D可视化"""
    # 生成数据
    data = generate_loss_landscape(width, height, complexity, seed)
    
    # 创建图形
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 绘制表面
    plot_3d_landscape(data, ax, colormap=colormap, alpha=0.8, 
                     elev=elev, azim=azim, zlim=(-20, 0))
    
    plt.savefig(f"single_loss_landscape_seed{seed}.png", dpi=300, 
               transparent=True, bbox_inches='tight')
    
    return fig

# 创建单个高质量可视化的示例
create_single_3d_visualization(seed=123)