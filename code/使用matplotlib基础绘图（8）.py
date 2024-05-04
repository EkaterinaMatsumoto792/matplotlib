"""
pyplot基础图，散点图，折线图，饼图，柱形图，条形图，箱线图代码
"""
# 1、使用matplotlib基础绘图1
import numpy as np
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib','inline')
data = np.arange(0, 1.1, 0.01)
plt.title('lines')  # 添加标题
plt.xlabel('x')  # 添加x轴的名称
plt.ylabel('y')  # 添加y轴的名称
plt.xlim((0, 1))  # 确定x轴范围
plt.ylim((0, 1))  # 确定y轴范围
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])  # 规定x轴刻度
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])  # 确定y轴刻度
plt.plot(data, data)  # 添加y=x曲线
plt.plot(data, data**2)  # 添加y=x^2曲线
plt.legend(['y=x', 'y=x^2'])
plt.savefig('../tmp/不包含子图.png')
plt.show()



# 2、使用matplotlib基础绘图2
rad = np.arange(0, np.pi*2, 0.01)
# 第一幅子图
p1 = plt.figure(figsize=(8, 10), dpi=80)  # 确定画布大小
ax1 = p1.add_subplot(2, 1, 1)  # 创建一个两行1列的子图，并开始绘制第一幅
plt.title('lines')  # 添加标题
plt.xlabel('x1')  # 添加x轴的名称
plt.ylabel('y1')  # 添加y轴的名称
plt.xlim((0, 1))  # 确定x轴范围
plt.ylim((0, 1))  # 确定y轴范围
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])  # 规定x轴刻度
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])  # 确定y轴刻度
plt.plot(rad, rad)  # 添加y=x^2曲线
plt.plot(rad, rad**2)  # 添加y=x^4曲线
plt.legend(['y=x', 'y=x^2'])
# 第二幅子图
ax2 = p1.add_subplot(2, 1, 2)  # 创开始绘制第2幅
plt.title('sin/cos')  # 添加标题
plt.xlabel('x2')  # 添加x轴的名称
plt.ylabel('y2')  # 添加y轴的名称
plt.xlim((0, np.pi * 2))  # 确定x轴范围
plt.ylim((-1, 1))  # 确定y轴范围
plt.xticks([0, np.pi / 2, np.pi, np.pi * 1.5, np.pi * 2])  # 规定x轴刻度
plt.yticks([-1, -0.5, 0, 0.5, 1])  # 确定y轴刻度
plt.plot(rad, np.sin(rad))  # 添加sin曲线
plt.plot(rad, np.cos(rad))  # 添加cos曲线
plt.legend(['sin', 'cos'])
plt.savefig('../tmp/包含子图.png')
plt.show()



# 3、使用matplotlib基础绘图3
print('Matplotlib中预设风格为：\n', plt.style.available)

x = np.linspace(0, 1, 1000)
plt.title('y=x & y=x^2')  # 添加标题
plt.style.use('bmh')  # 使用bmh风格
plt.plot(x, x)
plt.plot(x, x ** 2)
plt.legend(['y=x', 'y=x^2'])  # 添加图例
plt.savefig('../tmp/bmh风格.png')  # 保存图片
plt.show()



# 4、使用matplotlib基础绘图4，调节线条的rc参数
# 原图
x = np.linspace(0, 4 * np.pi)  # 生成x轴数据
y = np.sin(x)  # 生成y轴数据
plt.plot(x, y, label='$sin(x)$')  # 绘制sin曲线图
plt.title('sin')
plt.savefig('../tmp/线条rc参数原图.png')
plt.show()

# 5、修改rc参数后的图
plt.rcParams['lines.linestyle'] = '--'
plt.rcParams['lines.linewidth'] = 4
plt.plot(x, y, label='$sin(x)$')
plt.title('sin')
plt.savefig('../tmp/线条rc参数修改后.png')
plt.show()



# 6、使用matplotlib基础绘图5，修改坐标轴常用的rc参数
# 原图
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 4 * np.pi)  # 生成x轴数据
y = np.sin(x)  # 生成y轴数据
plt.plot(x, y, label='$sin(x)$')  # 绘制三角函数
plt.title('sin')
plt.savefig('../tmp/坐标轴rc参数原图.png')
plt.show()

# 7、修改rc参数后的图
plt.rcParams['axes.edgecolor'] = 'r'  # 轴颜色设置为蓝色
plt.rcParams['axes.grid'] = True  # 添加网格
plt.rcParams['axes.spines.top'] = False  # 去除顶部轴
plt.rcParams['axes.spines.right'] = False  # 去除右侧轴
plt.rcParams['axes.xmargin'] = 0.1  # x轴余留为区间长度的0.1倍
plt.plot(x, y, label='$sin(x)$')  # 绘制三角函数
plt.title('sin')
plt.savefig('../tmp/坐标轴rc参数修改后.png')
plt.show()



# 8、使用matplotlib基础绘图6，修改字体的rc参数
# 原图
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 4 * np.pi)  # 生成x轴数据
y = np.sin(x) #生成y轴数据
plt.plot(x, y, label='$sin(x)$')  # 绘制三角函数
plt.title('sin曲线')
plt.savefig('../tmp/文字rc参数原图.png')
plt.show()

# 修改rc参数后的图
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号“-”显示异常
plt.plot(x, y, label='$sin(x)$')  # 绘制三角函数
plt.title('sin曲线')
plt.savefig('../tmp/文字rc参数修改后.png')
plt.show()



