import numpy as np
from PIL import Image
a = np.array(Image.open("qq.jpg").convert("L")).astype('float')
dept = 10.
grad = np.gradient(a)
print(grad)
grad_x, grad_y = grad
grad_x = grad_x*dept/100.
grad_y = grad_y * dept / 100
A = np.sqrt(grad_x**2 + grad_y**2 + 1.0)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

vec_a1 = np.pi/2.2
vec_a2 = np.pi/4
dx = np.cos(vec_a1) * np.cos(vec_a2)
dy = np.cos(vec_a1) * np.cos(vec_a2)
dz = np.sin(vec_a1)

b = 255 * (dx * uni_x + dx * uni_y + uni_z)
b = b.clip(0, 255)
im = Image.fromarray(b.astype("uint8"))
im.save("qq1.jpg")