import itertools

class Inference:
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r

    def model_check(self, kb, query, model, propositions):
        for combination in itertools.product([True, False], repeat=len(propositions)):
            model = {}
            for i in range(len(propositions)):
                model[propositions[i]] = combination[i]

                j







