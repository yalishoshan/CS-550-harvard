import itertools

class Inference:
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r

    def model_check(self, kb, query, model):

        for combination in itertools.product([True, False], repeat=len(kb)):
            model = {}

        for i in range(len(kb)):
            model[kb[i]] = combination[i]

        if







