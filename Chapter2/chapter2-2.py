import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 指定每个bin(箱子)分布的数据，对应x轴
x = np.random.randint(0, 10, 100)
print(x)
# y轴的值表示对应的x的值出现的频数（频率），例如100个数中有10个5，则5对应的y为10（0.1）

# 这个参数指定bin(箱子)的个数，也就是总共有几条条状图
bins = range(0, 11, 1)

# 直方图
plt.hist(x, bins=bins, density=False, color="g", histtype="bar", rwidth=0.8, alpha=0.6)
# density=True      y轴表示的是频率
# density=False     y轴表示的是频数

plt.xlabel("箱子重量（kg）")
plt.ylabel("销售数量（个）")

plt.show()
