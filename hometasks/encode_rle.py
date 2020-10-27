import numpy as np


def encode_rle(array):
    mask = np.where(np.diff(array) != 0)
    if len(mask[0]) == 0:
        return [array[0]], [len(array)]
    numbers = np.append(array[mask[0]], array[-1])
    quantity = np.concatenate([[mask[0][0] + 1], np.diff(mask[0]), [len(array) - mask[0][-1] - 1]])
    return numbers, quantity
