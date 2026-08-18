import numpy as np
import random

t1 = np.array([1,2,3,])

# 使用NumPy生成数组，得到ndarray的类型
print(t1)
print(type(t1)) # <class 'numpy.ndarray'>

t2 = np.array([range(10)])
print(t2)   # [[0 1 2 3 4 5 6 7 8 9]]

# np.arrange的用法：arange([start],[stop],[step],dtype=None)
t3 = np.arange(10)
print(t3)   # [0 1 2 3 4 5 6 7 8 9]

t4 = np.arange(4,10,2)
print(t4) # [4 6 8]
print(t4.dtype) #int32

# numPy中的数据类型
t5 = np.array(range(1,4),dtype=float)
print(t5)
print(t5.dtype) # float64\
t6 = np.array(range(1,4),dtype='float32')
print(t6.dtype) # float32

# numPy中的bool类型
t6 =np.array([1,1,0,1,0,0],dtype=bool)
print(t6) # [ True  True False  True False False]
print(t6.dtype) # bool

# 调整数据类型
t7 = t6.astype('int8')
print(t7)
print(t7.dtype) # int8

# numpy中的小数
t8 = np.array([random.random()for i in range(10)])
print(t8)
print(t8.dtype)
# 取2位小数
t9 = np.round(t8,2)
print(t9) # [0.01 0.39 0.89 0.01 0.5  1.   0.92 0.73 0.04 0.08]
