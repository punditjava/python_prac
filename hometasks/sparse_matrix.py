class CooSparseMatrix:

    def __init__(self, ijx_list, shape):
        self.ijx_dict = dict()
        for i, j, x in ijx_list:
            if i >= shape[0] or j >= shape[1] \
                    or type(i) != int or type(j) != int:
                raise TypeError
            if x == 0:
                continue
            if (i, j) in self.ijx_dict.keys():
                raise TypeError
            self.ijx_dict[(i, j)] = x
        self.shape = shape

    def __setattr__(self, key, value):
        if key == 'ijx_dict':
            self.__dict__[key] = value
        elif key == 'shape':
            try:
                old_value = self.shape
                if not isinstance(value[0], int) or not isinstance(value[1], int) or \
                        value[0] * value[1] != self.shape[0] * self.shape[1]:
                    raise TypeError
                elif old_value == value or len(self.ijx_dict) == 0:
                    self.__dict__[key] = old_value
                else:
                    values = []
                    dict1 = {}
                    for i in range(self.shape[0]):
                        for j in range(self.shape[1]):
                            values.append(self.ijx_dict.get((i, j), 0))
                    k = 0
                    for i in range(value[0]):
                        for j in range(value[1]):
                            if values[k] != 0:
                                dict1.update({(i, j): values[k]})
                            k += 1
                    self.ijx_dict = dict1
                    self.__dict__[key] = value
            except AttributeError:
                self.__dict__[key] = value
        elif key == 'T':
            raise AttributeError

    def __getattr__(self, item):
        if item != 'T':
            return self.__getattribute__(item)
        else:
            trans = CooSparseMatrix([], shape=self.shape)
            trans.ijx_dict = {k[::-1]: self.ijx_dict.get(k) for k in self.ijx_dict.keys()}
            return trans

    def __getitem__(self, key):
        if isinstance(key, int):
            if key >= self.shape[0]:
                raise TypeError
            new_list = list()
            for index in self.ijx_dict.keys():
                if index[0] == key:
                    new_list.append((index[0], index[1], self.ijx_dict[index]))
            return CooSparseMatrix(new_list, shape=(1, self.shape[1]))
        else:
            j = key[1]
            i = key[0]
            if j >= self.shape[1] or i >= self.shape[0] \
                    or type(i) != int or type(j) != int:
                raise TypeError
            if key in self.ijx_dict:
                return self.ijx_dict[key]
            return 0

    def __setitem__(self, key, val):
        if val == 0:
            if key in self.ijx_dict:
                del self.ijx_dict[key]
        else:
            self.ijx_dict.update({key: val})

    def sub_add(self, other, func):
        if self.shape != other.shape:
            raise TypeError
        matrix = CooSparseMatrix([], shape=self.shape)
        matrix.ijx_dict = self.ijx_dict.copy()
        for key, value in other.ijx_dict.items():
            if key in matrix.ijx_dict:
                summ = func(matrix.ijx_dict[key], value)
                if summ == 0:
                    del matrix.ijx_dict[key]
                else:
                    matrix.ijx_dict.update({key: summ})
            else:
                matrix.ijx_dict.update({key: func(0, value)})
        return matrix

    def __add__(self, other):
        return self.sub_add(other, lambda x, y: x + y)

    def __sub__(self, other):
        return self.sub_add(other, lambda x, y: x - y)

    def mul(self, other):
        matrix = CooSparseMatrix([], shape=self.shape)
        matrix.ijx_dict = self.ijx_dict.copy()
        for key in matrix.ijx_dict:
            matrix.ijx_dict[key] *= other
        return matrix

    def __mul__(self, other):
        return self.mul(other)

    def __rmul__(self, other):
        return self.mul(other)
