class Probability:
    def __init__(self, a, b, not_a, not_b):
        self.a = a
        self.b = b
        self.not_a = not_a
        self.not_b = not_b

    def negation(self):
        p_not_a = 1 - self.a
        return p_not_a

    def inclusion_exclusion(self, p_a_and_b):
        p_a_or_b = self.a + self.b - p_a_and_b
        return p_a_or_b

    def marginalization(self, p_a_and_b, p_a_and_not_b):
        p_a = p_a_and_b + p_a_and_not_b
        return p_a

    def conditioning(self, p_a_given_b, p_a_given_not_b):
        p_a = p_a_given_b * self.b + p_a_given_not_b * self.not_b
        return p_a

def main():
    p = Probability(0.8, 0.1, 0.3, 0.4)
    print(p.negation(), p.inclusion_exclusion(0.8), p.marginalization(0.1, 0.4), p.conditioning(0.1, 0.4))

if __name__ == "__main__":
    main()

