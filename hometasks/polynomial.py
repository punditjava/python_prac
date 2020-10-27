class Polynomial:
    def __init__(self, *factors):
        self.factors = factors

    def __call__(self, param):
        return sum([param ** i * self.factors[i]
                    for i in range(len(self.factors))])
