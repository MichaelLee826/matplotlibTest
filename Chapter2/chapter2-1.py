import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 数值
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 1, 4, 5, 8, 9, 7, 2]

# 条形图
plt.bar(x, y, align="center", color="c", tick_label=["q", "a", "c", "e", "r", "j", "b", "p"], hatch="/")

# 横向条形图
# plt.barh(x, y, align="center", color="c", tick_label=["q", "a", "c", "e", "r", "j", "b", "p"], hatch="/")

# 坐标轴名称
plt.xlabel("箱子编号")
plt.ylabel("箱子重量（kg）")

# plt.xlabel("箱子重量（kg）")
# plt.ylabel("箱子编号")

plt.show()
