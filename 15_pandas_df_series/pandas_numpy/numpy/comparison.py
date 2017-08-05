import numpy as np
from datetime import datetime as dt

c = []
def m(a, b): 
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c

def m_np(a_np, b_np):
    c = a_np * b_np
    return c

print('                  array      list')
print('No. of items   (microSec) (microSec)    ratio')
for num in [100, 1000, 10000, 100000]:
    a = range(num)
    b = range(num)
    a_np = np.arange(num)
    b_np = np.arange(num)

    start = dt.now()
    m(a, b)
    end = dt.now()
    delta = (end - start).microseconds

    start = dt.now()
    m_np(a_np, b_np)
    end = dt.now()
    array_delta = (end - start).microseconds
    ratio = round(delta/array_delta)
    print('{}{}{}{}'.format(str(num).ljust(11), str(array_delta).rjust(9),
                            str(delta).rjust(12), str(ratio).rjust(13)))