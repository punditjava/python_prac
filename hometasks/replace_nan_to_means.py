import numpy as np
import random


def replace_nan_to_means(array):
    mask = np.isnan(array)
    return np.where(mask, np.ma.array(array, mask=mask).mean(axis=0), array)


print(random.sample(range(0, 10000), 1000))