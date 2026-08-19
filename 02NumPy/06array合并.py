import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])
print(np.vstack((A,B))) # 垂直，上下合并 vertical stack
# [[1 1 1]
#  [2 2 2]]
print(np.hstack((A,B))) # 水平，左右合并
# [1 1 1 2 2 2]
print(np.concatenate((A,B,B,A)))

# 分割
A = np.arange(12).reshape((3,4))
print(A)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(np.split(A,3,axis=0))
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

print(np.array_split(A,3,axis=1))
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2],
#        [ 6],
#        [10]]), array([[ 3],
#        [ 7],
#        [11]])]

print(np.hsplit(A,3))
print(c)