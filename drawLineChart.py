# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Arial']#如果要显示中文字体，则在此处设为：SimHei
plt.rcParams['axes.unicode_minus']=False#显示负号

# x = np.array([3,5,7,9,11,13,15,17])
# A = np.array([0.5342, 0.5313, 0.5326, 0.5315, 0.5331, 0.5374, 0.5336, 0.5317])


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
results = np.array([0.5342, 0.5313, 0.5326, 0.5315, 0.5331, 0.5374, 0.5336, 0.5317, 0.5321])

# label在图示(legend)中显示。若为数学公式,则最好在字符串前后添加"$"符号
# color：b:blue、g:green、r:red、c:cyan、m:magenta、y:yellow、k:black、w:white、、、
# 线型：-  --   -.  :    ,
# marker：.  ,   o   v    <    *    +    1
plt.figure(figsize=(10, 5))
plt.grid(linestyle="--")  # 设置背景网格线为虚线
ax = plt.gca()
ax.spines['top'].set_visible(False)  # 去掉上边框
ax.spines['right'].set_visible(False)  # 去掉右边框


plt.plot(x, results, marker='o', color="blue", linewidth=1.5)

group_labels = ['20', '25', '30', '35', '40', ' 45', '50', '55', '60']  # x轴刻度的标识
plt.xticks(x, group_labels, fontsize=12, fontweight='bold')  # 默认字体大小为10
plt.yticks(fontsize=12, fontweight='bold')
# plt.title("example", fontsize=12, fontweight='bold')  # 默认字体大小为12
plt.xlabel("L", fontsize=13, fontweight='bold')
plt.ylabel("AVGmAP@IoU(0.1-0.7)", fontsize=13, fontweight='bold')
plt.xlim(0.9, 9.1)  # 设置x轴的范围
plt.ylim(0.53, 0.54)

# plt.legend()          #显示各曲线的图例
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=12, fontweight='bold')  # 设置图例字体的大小和粗细

#设置数字标签
for a, b in zip(x, results):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=12)

plt.savefig('./L.jpg', format='jpeg', dpi=300)  # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中
plt.show()
