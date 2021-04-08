import matplotlib.pyplot as plt
import numpy as np
plt.subplot2grid((3, 3), (0, 0), colspan=3)
labels = ["frogs", "dogs", "cats", "tigers"]
size = [15, 40, 35, 10]
explode = (0, 0.1, 0, 0)
plt.pie(size, explode=explode, labels=labels, autopct="%1.1f%%",
        shadow=False, startangle=30)
plt.axis("equal")

plt.subplot2grid((3, 3), (1, 0), colspan=3)
np.random.seed(0)
m, s = 100, 20
a = np.random.normal(m, s, size=50)
print(a)
plt.hist(a, bins=60)# bins 数字组出现的取值范围，数字越大取值范围越大 数字越小取值范围越近
plt.title("histogram")

plt.show()
