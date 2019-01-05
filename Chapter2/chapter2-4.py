import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

kinds = "A", "B", "C", "D"

colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3"]

nums = [0.0501, 0.45, 0.1499, 0.35]

plt.pie(nums, labels=kinds, autopct="%3.1f%%", shadow=False, startangle=90, colors=colors)
# labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
# autopct，圆里面的文本格式，%3.1f%%表示整数有3位，小数有1位的浮点数
# shadow，饼是否有阴影
# startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
# pctdistance，百分比的text离圆心的距离
# patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

plt.title("饼图")

plt.show()
