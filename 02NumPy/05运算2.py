import numpy as np

A = np.arange(2,14).reshape((3,4))

print(A)
# [[ 2  3  4  5]
#  [ 6  7  8  9]
#  [10 11 12 13]]

print(np.argmin(A)) # 索引的最小值 -> 0
print(np.argmax(A)) # 索引的最大值 -> 11

print(np.mean(A)) # 平均值 -> 7.5
print(A.mean()) # 平均值 -> 7.5
print(np.average(A)) # 平均值 -> 7.5

print(np.median(A)) # 中位数 -> 7.5

print(np.cumsum(A)) # 累加,前缀和 -> [ 2  5  9 14 20 27 35 44 54 65 77 90]
print(np.diff(A)) # 差分，相邻元素做后减前，求差值。
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]

print(np.nonzero(A)) # 找出数组里不为 0 的元素的下标索引。
# (array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]))

print(np.sort(A))  # 逐行排序

print(np.transpose(A)) # 转置：矩阵行和列互换。行↔列互换
print(A.T) # # 转置：矩阵行和列互换。行↔列互换
# 三维、四维优先用 transpose(轴顺序)，不要用 .T
# [[ 2  6 10]
#  [ 3  7 11]
#  [ 4  8 12]
#  [ 5  9 13]]

print(np.clip(A,5,9)) # 把数组里的全部数值强制限制在 [min, max] 区间。
