class linearize:
    def __init__(self, array):
        self.iter = iter(array)
        self.rec = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.rec is not None:
            try:
                elem = self.rec.__next__()
            except StopIteration:
                self.rec = None
            else:
                return elem
        if self.rec is None:
            try:
                elem = next(self.iter)
                if type(elem) == str and len(elem) == 1:
                    return elem
                iter(elem)
            except TypeError:
                return elem
            else:
                self.rec = linearize(elem)
                try:
                    elem = self.rec.__next__()
                except StopIteration:
                    self.rec = None
                    self.__next__()
                else:
                    return elem
