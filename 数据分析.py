import numpy as np


def npSum():
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([5, 6, 7, 8, 9])

    c = a ** 2 + b ** 3
    return c

C = np.array([0, 1, 2, 3, 4])
print(npSum())

A = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
print(A.ndim)
print(A.shape)# (2, 5)
print(A.size) # 10
print(A.dtype) #int32
print(
    A.itemsize
) # 4


np.zeros((3, 6), dtype= np.int32)#array([[0, 0, 0, 0, 0, 0],
       #[0, 0, 0, 0, 0, 0],
       #[0, 0, 0, 0, 0, 0]])

np.arange(10) #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.ones((3, 6)) # = array([[1., 1., 1., 1., 1., 1.],
       #[1., 1., 1., 1., 1., 1.],
       #[1., 1., 1., 1., 1., 1.]])
np.linspace(1, 10, 4) # = array([ 1.,  4.,  7., 10.])
np.concatenate((C, A))
a = np.arange(24).reshape((2, 3, 4))
a
#array([[[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]],
#       [[12, 13, 14, 15],
#        [16, 17, 18, 19],
#        [20, 21, 22, 23]]])