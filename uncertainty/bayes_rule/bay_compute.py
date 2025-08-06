class Probability:
    def __init__(self, effect, unknown_cause, a):
        self.effect = effect
        self.unknown_cause = unknown_cause
        self.a = a

        if self.effect > 1 or self.effect < 0:
            raise ValueError("Effect is out of range")
        if self.unknown_cause > 1 or self.unknown_cause < 0:
            raise ValueError("Unknown cause is out of range")
        if self.a > 1 or self.a < 0:
            raise ValueError("A is out of range")

    def bayes_rule(self):
        return (self.unknown_cause * self.effect) / self.a

def main():
    bays = Probability(0.1, 0.8, 0.4)
    print(bays.bayes_rule())

if __name__ ==  "__main__":
    main()