import matplotlib.pyplot as plt
import numpy as np

plt.subplot2grid((3, 3), (0, 0), colspan=3)
a = np.arange(0, 5, 0.02)
plt.plot(a, np.cos(2 * np.pi * a), "r--")

plt.xlabel("时间", fontproperties="simhei", fontsize=16, color="green")
plt.title("实例  $y=cos(2\\pi x)$", fontproperties="simhei", fontsize=16)
#plt.text(2, 1, "$\\mu= 100$", fontproperties="simhei")
plt.annotate("$\\mu= 100$", xy=(2, 1), xytext=(3, 1.5),
             arrowprops = dict(facecolor = "black", shrink=0.1, width=2))
plt.axis([-1, 6, -2, 2])
plt.grid(True) # 网格曲线


plt.subplot2grid((3, 3), (1, 0), colspan=3)
plt.show()