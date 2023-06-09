# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    y = x > 0
    return y.astype(np.int)

X = np.arange(-5.0, 5.0, 0.1)
Y = step_function(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.5)  # 指定图中绘制的y轴的范围
plt.show()
