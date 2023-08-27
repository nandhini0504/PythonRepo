import numpy as np
def floors(arr):
    array = np.array(arr)
    np.set_printoptions(legacy='1.13')
    print(np.floor(array))
    return np.floor(array)
def ceils(arr):
    array = np.array(arr)
    print(np.ceil(array))
    return np.ceil(array)
def rints(arr):
    array = np.array(arr)
    print(np.ceil(array))
    return np.rint(array)