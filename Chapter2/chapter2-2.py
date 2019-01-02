import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.random.randint(0, 10, 100)

bins = range(0, 11, 1)

# 直方图
plt.hist(x, bins=bins, color="g", histtype="bar", rwidth=0.8, alpha=0.6)

plt.xlabel("箱子重量（kg）")
plt.ylabel("销售数量（个）")

plt.show()
