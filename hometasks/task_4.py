class WordContextGenerator:
    def __init__(self, words, window_size):
        self.words = words
        self.window_size = window_size

    def __iter__(self):
        self.begin = 0
        self.end = 0
        return self

    def __next__(self):
        if self.begin == self.end == len(self.words) - 1:
            raise StopIteration
        else:
            if self.begin == self.end:
                self.end += 1
            if self.end >= len(self.words) or \
                    abs(self.end - self.begin) > self.window_size:
                self.begin += 1
                self.end = max(self.begin - self.window_size + 1, 1)
            else:
                self.end += 1
            return self.words[self.begin], self.words[self.end - 1]


for w1, w2 in WordContextGenerator(['negwar', 'bufs', 'ngbt', 'h', 'mawf'], 5):
    print(w1, w2)