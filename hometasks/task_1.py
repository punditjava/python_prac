from bisect import bisect_right

import numpy as np


def encode_rle(array):
    mask = np.where(np.diff(array) != 0)
    if len(mask[0]) == 0:
        return [array[0]], [len(array)]
    numbers = np.append(array[mask[0]], array[-1])
    quantity = np.concatenate([[mask[0][0] + 1], np.diff(mask[0]), [len(array) - mask[0][-1] - 1]])
    return numbers, quantity


class RleSequence:
    def __init__(self, input_sequence):
        self.numbers, self.quantity = encode_rle(input_sequence)
        self.cumsum = np.cumsum(self.quantity)
        self.quant = np.sum(self.quantity)

    def __contains__(self, elem):
        return elem in self.numbers

    def __iter__(self):
        self.index = 0
        self.already_written = 0
        return self

    def __next__(self):
        if self.already_written >= self.quantity[self.index]:
            self.index += 1
            self.already_written = 0
        if self.index >= np.size(self.numbers):
            raise StopIteration
        else:
            self.already_written += 1
            return self.numbers[self.index]

    def __getitem__(self, item):
        if isinstance(item, slice):
            start, stop, step = item.start, item.stop, item.step
            if step is None:
                step = 1
            if stop is None:
                stop = self.quant
            if start is None:
                start = 0
            if start < 0:
                start += self.quant
            if stop < 0:
                stop += self.quant
            start = min(start, self.quant)
            stop = min(stop, self.quant)
            answer = []
            while start < stop:
                answer.append(self[start])
                start += step
            return np.array(answer)
        else:
            if item < 0:
                item = self.quant + item
            if item < 0 or item >= self.quant:
                raise IndexError
            return self.numbers[bisect_right(self.cumsum, item)]
