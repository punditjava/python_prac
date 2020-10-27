import numpy as np
from numpy.lib.stride_tricks import as_strided


def calc_expectations(h, w, X, Q):
    advanced_q = np.pad(Q, pad_width=((h - 1, 0), (w - 1, 0)), mode='constant')
    leprikon_shape = (h, w)
    goal_shape = tuple(np.subtract(advanced_q.shape,
                                   leprikon_shape) + 1) + leprikon_shape
    q_window = as_strided(advanced_q, goal_shape, advanced_q.strides * 2)
    q_window = q_window.reshape((-1,) + leprikon_shape)
    return X * np.sum(q_window, axis=(1, 2)).reshape(X.shape)
