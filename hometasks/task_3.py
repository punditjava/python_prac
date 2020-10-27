import numpy as np


class BatchGenerator:
    def __init__(self, list_of_sequences, batch_size, shuffle=False):
        self.batch_size = batch_size
        if shuffle:
            for s in list_of_sequences:
                if type(s) == list:
                    s = np.array(s)
                np.random.shuffle(s)
        self.list_of_sequences = list_of_sequences

    def __iter__(self):
        self.ind = 0
        return self

    def __next__(self):
        if self.ind >= np.size(self.list_of_sequences[0]):
            raise StopIteration
        batch = list()
        for s in self.list_of_sequences:
            batch.append(s[self.ind : self.ind + self.batch_size])
        self.ind += self.batch_size
        return batch
