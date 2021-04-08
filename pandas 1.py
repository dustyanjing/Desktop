import pandas as pd
import numpy as np
a = pd.Series([8, 7, 6], index=["a", "n", "b"])
print(a)
b = pd.Series({"a": 8, "c": 5, "d": 7}, index=["a", "n", "b"])
print(b)
n = pd.Series(np.arange(5), index=np.arange(9, 4, -1))
print(n)

d = {"one": pd.Series([8, 7, 6], index=["a", "n", "b"]),
     "twp": pd.Series({"a": 8, "c": 5, "d": 7}, index=["a", "n", "b", "d"])}
d1 = pd.DataFrame(d)
print(d1)
d2 = pd.DataFrame(d, index=["a", "n", "b", "d"], columns=["one", "two"])
print(d2)

c = {"one": [1, 2, 3, 4, 5], "two": [9, 8, 7, 6, 5]}
c1 = pd.DataFrame(c, index=["A", "B", "C", "V", "G"])
print(c1)
W = {"city": ["NY", "LA", "BS", "COU"],
     "temp": [7, 15, 12, 11],
     "date": [4.5, 4.5, 4.5, 4.5]}
w1 = pd.DataFrame(W, index=["A", "B", "C", "V"])
print(w1)