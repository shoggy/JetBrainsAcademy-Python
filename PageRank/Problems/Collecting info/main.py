import numpy as np


def collect_info(array: np.ndarray):
    return f"Shape: {array.shape}; " \
           f"dimensions: {array.ndim}; " \
           f"length: {len(array)}; " \
           f"size: {array.size}"
