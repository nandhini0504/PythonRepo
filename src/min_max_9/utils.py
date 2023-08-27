import numpy as np
def minimum(new_array):
    print(np.max(np.min(new_array, axis=1)))
    return np.max(np.min(new_array, axis=1))