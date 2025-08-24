
'''
import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)


import numpy as np
a = np.arange(15).reshape(3, 5)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))


import numpy as np
b = np.array([6, 7, 8])
print(b)
print(type(b))


import numpy as np
a = np.array([2, 3, 4])
print(a)
print(a.dtype)


import numpy as np
b = np.array([[1.5, 2, 3], [4, 5, 6]])
print(b)
print(b.dtype)


import numpy as np
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)


import numpy as np
print(np.zeros((3, 4)))
print(np.ones((2, 3, 4), dtype=np.int16))
print(np.empty((2, 3)))


import numpy as np
print(np.arange(10, 30, 5))
print(np.arange(0, 2, 0.3))


import numpy as np
from numpy import pi
print(np.linspace(0, 2, 9))
x = np.linspace(0, 2 * pi, 100)
print(np.sin(x))


import numpy as np
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b)
c = a - b
print(c)
print(b**2)
print(10 * np.sin(a))
print(a < 35)


import numpy as np
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(A * B)
print(A @ B)
print(A.dot(B))


import numpy as np
a = np.ones((2, 3), dtype=int)
b = np.random.random((2, 3))
a *= 3
print(a)
b += a
print(b)


import numpy as np
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print(b.dtype.name)
c = a + b
print(c)
print(c.dtype.name)
d = np.exp(c * 1j)
print(d)
print(d.dtype.name)


import numpy as np
a = np.random.random((2, 3))
print(a.sum())
print(a.min())
print(a.max())


import numpy as np
b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum(axis=0))
print(b.min(axis=1))
print(b.cumsum(axis=1))


import numpy as np
B = np.arange(3)
print(np.exp(B))
print(np.sqrt(B))
C = np.array([2., -1., 4.])
print(np.add(B, C))


import numpy as np
a = np.arange(10)**3
print(a)
print(a[2])
print(a[2:5])


import numpy as np
a[:6:2] = 1000
print(a)


import numpy as np
a[:6:2] = 1000
print(a[::-1])


import numpy as np
a[:6:2] = 1000
for i in a:
    print(i**(1/3.))


import numpy as np
def f(x, y):
    return 10 * x + y
b = np.fromfunction(f, (5, 4), dtype=int)
print(b)
print(b[2, 3])
print(b[0:5, 1])
print(b[1:3, :])


import numpy as np
def f(x, y):
    return 10 * x + y
b = np.fromfunction(f, (5, 4), dtype=int)
print(b[-1])

import numpy as np
def f(x, y):
    return 10 * x + y
b = np.fromfunction(f, (5, 4), dtype=int)
for row in b:
    print(row)

    
import numpy as np
def f(x, y):
    return 10 * x + y
b = np.fromfunction(f, (5, 4), dtype=int)
for element in b.flat:
    print(element)


import numpy as np
a = np.floor(10 * np.random.random((3, 4)))
print(a)
print(a.shape)
print(a.ravel())
print(a.reshape(6, 2))
print(a.T)
print(a.T.shape)
print(a.shape)


import numpy as np
a = np.floor(10 * np.random.random((3, 4)))
a.resize((2, 6))
print(a)


import numpy as np
a = np.floor(10 * np.random.random((2, 2)))
b = np.floor(10 * np.random.random((2, 2)))
print(a)
print(b)
print(np.vstack((a, b)))
print(np.hstack((a, b)))


import numpy as np
from numpy import newaxis
a = np.array([4., 2.])
b = np.array([3., 8.])
print(np.column_stack((a, b)))
print(a[:, newaxis])
print(np.column_stack((a[:, newaxis], b[:, newaxis])))
print(np.hstack((a[:, newaxis], b[:, newaxis])))


import numpy as np
a = np.floor(10 * np.random.random((2, 12)))
print(a)
print(np.hsplit(a, 3))
print(np.hsplit(a, (3, 4)))


import numpy as np
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
b = a
print(b is a)


import numpy as np
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
c = a.view()
print(c is a)
print(c.base is a)
print(c.flags.owndata)
c = c.reshape((2, 6))
print(c.shape)
print(a.shape)


import numpy as np
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
d = a.copy()
print(d is a)
print(d.base is a)
d[0, 0] = 9999
print(d)
print(a)




'''


