import numpy as np
a = np.arange(4)
b = a
c = a
d = b
a[0] = 11
print(a)
print(b)
print(c)
print(d)
b = a.copy()
a[3] = 44
print(a)
print(b)