import numpy as np
import random


def get_max_before_zero(array):
    values = array[np.where(array[:-1] == 0)[0] + 1]
    return None if len(values) == 0 else values.max()
