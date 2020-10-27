import numpy as np


def get_nonzero_diag_product(array):
    diag = np.diag(array)
    result = diag[diag > 0]
    return None if len(result) == 0 else np.prod(result)
