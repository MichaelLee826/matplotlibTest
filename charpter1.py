import matplotlib.pyplot as plt
import numpy as np

# 数据
x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)
y1 = np.random.randn(100)

# 散点图
plt.scatter(x, y1, c="0.25", label="scatter figure")

# 曲线图
plt.plot(x, y, ls="--", lw="2", c="c", label="plot figure")

# 设置x，y轴范围
plt.xlim(0.0, 4.0)
plt.ylim(-3.0, 3.0)

# 设置x，y轴标签
plt.xlabel("x_axis")
plt.ylabel("y_axis")

# 设置网格线
plt.grid(True, ls=":", color="r")

# 平行于x轴的线
plt.axhline(y=0.0, c="r", ls="--", lw=2)

# 垂直于x轴的线条
plt.axvspan(xmin=1.0, xmax=2.0, facecolor="y", alpha=0.3)

# 注释（带箭头）
plt.annotate("maximum", xy=(np.pi/2, 1.0), xytext=((np.pi/2)+0.15, 1.5), weight="bold", color="r",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="r"))
plt.annotate("spines", xy=(0.75, -3), xytext=(0.35, -2.25), weight="bold", color="b",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="b"))

# 文本
plt.text(3.6, -2.70, "'|' is tickline", weight="bold", color="b")
plt.text(3.6, -2.95, "3.5 is ticklabel", weight="bold", color="b")

# 标题
plt.title("Structure of matplotlib")

# 图例
plt.legend(loc="upper right")

plt.show()
