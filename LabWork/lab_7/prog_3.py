'''
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
print(a)


import numpy as np
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(b)


import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[0])
print(b[0, 0])


import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[0:2])
print(b[0:2, 0])
print(b[0:2, 0:2])
print(b[:, 2:])


import numpy as np
data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data + ones)
print(data - ones)
print(data * ones)
print(data / ones)


import numpy as np
print(data * 2)
print(data.sum())


import numpy as np
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(b.sum(axis=0))
print(b.sum(axis=1))


import numpy as np
data = np.array([1.0, 2.0])
print(data * 1.6)


import numpy as np
data = np.array([1.0, 2.0])
print(data.max())
print(data.min())
print(data.sum())


import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
print(a.std())
print(a.prod())


import numpy as np
print(np.zeros(2))
print(np.ones(2))
print(np.random.random(2))


import numpy as np
print(np.zeros((2, 2)))
print(np.ones((2, 2)))
print(np.random.random((2, 2)))


import numpy as np
print(np.arange(7))
print(np.arange(7).reshape(7, 1))


import numpy as np
print(np.eye(3))


import numpy as np
array = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(array)
print(unique_values)
unique_values, counts = np.unique(array, return_counts=True)
print(counts)


import numpy as np
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(b.T)


import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
print(a.reshape(2, 3))
print(a.reshape(2, -1))


import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.flip(arr))


import numpy as np
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(np.flip(array_2d))
print(np.flip(array_2d, axis=0))
print(np.flip(array_2d, axis=1))


import numpy as np
square_matrix = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(square_matrix))


import numpy as np
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(array_2d.flatten())
print(array_2d.ravel())


import numpy as np
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
np.save('myarray.npy', array_2d)
loaded_array = np.load('myarray.npy')
print(loaded_array)

'''