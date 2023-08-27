import numpy as np


def arr_mean(arr):
    print(np.mean(arr, axis=1))
    return np.mean(arr, axis=1)


def arr_var(arr):
    print(np.var(arr, axis=0))
    return np.var(arr, axis=0)


def arr_std(arr):
    k = np.std(arr, axis=None)
    print(k)
    return k.round(11)