import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
tmp = w*x
tmp = np.sum(w*x)
print(tmp + b)