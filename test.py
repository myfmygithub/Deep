import sys, os
import numpy as np
sys.path.append(os.pardir)
from common.util import im2col
x1 = np.random.rand(1, 2, 5, 5)
print(x1)
col1 = im2col(x1, 3, 3, stride=1, pad=0)
print(col1)
print(col1.shape) # (9, 75)
x2 = np.random.rand(2, 2, 5, 5) # 10个数据
print(x2)
col2 = im2col(x2, 3, 3, stride=1, pad=0)
print(col2)
print(col2.shape) # (90, 75)