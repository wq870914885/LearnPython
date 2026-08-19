import pandas as pd
import numpy as np


s= pd.Series([1,3,4,np.nan,44,1])
print(s)
# 0     1.0
# 1     3.0
# 2     4.0
# 3     NaN
# 4    44.0
# 5     1.0
# dtype: float64
dates = pd.date_range('20160101',periods=6)
print(dates)
# DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
#                '2016-01-05', '2016-01-06'],
#               dtype='datetime64[ns]', freq='D')

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])
print(df)
#                    A         B         C         D
# 2016-01-01 -0.678266 -1.307157 -1.111507  0.928197
# 2016-01-02 -2.558324  1.220363  2.512119 -0.779040
# 2016-01-03 -0.841989  2.143242  0.544658  0.194079
# 2016-01-04  1.082961 -1.588725  0.985536  0.436380
# 2016-01-05 -0.653275 -0.703158 -0.585745 -0.033589
# 2016-01-06 -1.495958 -0.561281  0.775035  0.601736

df = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
print('===============')
print(df.columns)
# RangeIndex(start=0, stop=4, step=1)
print(df.values)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(df.describe())
#          0    1     2     3
# count  3.0  3.0   3.0   3.0
# mean   4.0  5.0   6.0   7.0
# std    4.0  4.0   4.0   4.0
# min    0.0  1.0   2.0   3.0
# 25%    2.0  3.0   4.0   5.0
# 50%    4.0  5.0   6.0   7.0
# 75%    6.0  7.0   8.0   9.0
# max    8.0  9.0  10.0  11.0
print(df.T)
#    0  1   2
# 0  0  4   8
# 1  1  5   9
# 2  2  6  10
# 3  3  7  11
print(df.sort_index(axis=1,ascending=False))    # 行排序，倒序
#     3   2  1  0
# 0   3   2  1  0
# 1   7   6  5  4
# 2  11  10  9  8
print(df.sort_values(by=1,ascending=False))
#    0  1   2   3
# 2  8  9  10  11
# 1  4  5   6   7
# 0  0  1   2   3