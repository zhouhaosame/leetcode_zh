from numba import vectorize, float64,jit

import numpy as np
@vectorize(nopython=True)
def add_with_vec(yy, c):
    return yy + c

a=np.array([1,2,3])
print(add_with_vec(a,a))