# <demo> silent
# Title: numpy demonstration
# Date: 20160206
# Filename: numpy_demo.py 
# Usage: demobatch.py numpy_demo.py 
# Description: A demonstration of some of the key functions
#              behaviors and characteristics of numpy  
# Author: Chalmer Lowe 
# Version: 0.5
# Python Revision: 3  
# IPython Revision: 4+
# TO DO:
# 
#---------------------------------------------------------

# <demo> stop
#
# Numpy is the fundamental package for scientific computing in Python.
# It provides:
#   a multidimensional array object
#   a collection of functions that perform operations including mathematical,
#                   logical, shape manipulation, sorting, selection, 
#                   Fourier transforms, linear algebra, statistical 
#                   operations, etc.


# <demo> stop
#
# Several important items to note:
#   NumPy arrays are a fixed size (note: Python's lists are not).
#   Elements in a NumPy array are required to be the same type
#   NumPy arrays execute vector mathematics/transforms without the need 
#        for 'for loops' resulting in a performance and efficiency improvement
#   Most scientific/math libraries use NumPy under the hood.
# 

# <demo> stop
#
import numpy as np
a = np.arange(42)
a

# <demo> stop
#
a1 = a.reshape(6, 7)
a1

# <demo> stop
#
print('number of dimenstions:', a1.ndim)
print('shape of the array:', a1.shape)
print('size of the array:', a1.size)
print('datatype:', a1.dtype)
print('size in bytes of each element:', a1.itemsize)
print('type of object:', type(a1))

# <demo> stop
#
f = np.array([1.0, 2.1, 3.2])
print(f.dtype)
f

# <demo> stop
#
dim2 = np.array([[1.0, 2.1, 3.2], [4.3, 5.4, 6.5]])
dim2


# <demo> stop
#
i8 = np.array([[1, 2, 3], [7, 8, 9]], dtype='int8')
i8.dtype

# <demo> stop
#
np.zeros((4,5))

# <demo> stop
#
np.ones((2, 3, 12))

# <demo> stop
#
np.empty((2,3,2))

# <demo> stop
#
np.arange(2, 20, 3)

# <demo> stop
#
np.arange(2, 20, 0.3)

# <demo> stop
#
np.linspace(2, 20, 61)

# <demo> stop
#
i = np.array([7, 13, 42, 99])
print('i:\n', i)

j = np.ones(4)
print('j:\n', j)

k = i - j
print('i - j:\n', k)

k2 = i + j
print('i + j:\n', k2)


# <demo> stop
#
x = np.array([[3, 4],
              [5, 6]])
y = np.array([[7, 8],
              [9, 0]])

print(x * y)

# <demo> stop
#
prices = np.array([3.49, 4.49, 3.99])
sales = np.array([[5, 6, 7, 6, 5],
                  [10, 11, 11, 11, 12],
                  [7, 6, 7, 6, 7]])

prices.dot(sales)

# output 1:  3.49 * 5 + 4.49 * 10 + 3.99 * 7 (total sales on day 1)

# output 2:  3.49 * 6 + 4.49 * 11 + 3.99 * 6 (total sales on day 2)




# <demo> stop
#

u = np.ones((4, 3), dtype=int)
u *= 5
u

# <demo> stop
#

r = np.random.random((3,4))
print(r)
print('Max:', r.max(), '\n')
print('Min:', r.min(), '\n')
print('Sum:', r.sum(), '\n')

# <demo> stop
#
i = np.arange(15).reshape(5, 3)
print('Sum (by col):', i.sum(axis=0), '\n')
print('Sum (by col):', i.sum(axis=0), '\n')


# <demo> stop
#
# Universal functions:
# sqrt, exp
print(np.sin(i))
print(np.sqrt(i))
print(np.mean(i, axis=1)



# <demo> stop
#
c = np.arange(8) ** 0.5


# <demo> stop
#
print(c[2])
print(c[2:6])
print(c[3:7:2])


# <demo> stop
#

c[3:7:2] = 42
print(c)

# <demo> stop
#

m = np.array([[11, 12, 13],
              [21, 22, 23],
              [31, 32, 33]])



# <demo> stop
#
m[0]

# m[1]
# m[0, 0]
# m[1, 0]
# m[1, 0:2]
# m[1, 0:3]





# <demo> stop
#
print(m)
print(m[0:3, 1])
print(m[:, 2])

# <demo> stop
#
m.ravel()


# <demo> stop
#
u.shape = (2, 6)
print(u)
print(u.T)

# u.resize((x, y))
# u.reshape(x, y)

# <demo> stop
#

v1 = np.arange(6).reshape((2,3))
v2 = np.arange(10, 16).reshape((2,3))

# <demo> stop
#
np.vstack((v1, v2))


# <demo> stop
#
np.hstack((v1, v2))


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


