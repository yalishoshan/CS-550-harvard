class Probability:
    def __init__(self, a, b, not_a, not_b):
        self.a = a
        self.b = b
        self.not_a = not_a
        self.not_b = not_b

    def negation(self):
        p_not_a = 1 - self.a
        return p_not_a

    def inclusion_exclusion(self):
        p_a_or_b = self.a + self.b - self.a * self.b
        return p_a_or_b

    def marginalization(self):
        p_a = self.a * self.b + self.a * self.not_b

        if self.a != p_a:
            raise ValueError("all doesnt sum up")

        else:
            return p_a

    def conditioning(self):
        p_a  = (self.a * self.b / self.b) * self.b + (self.a * self.not_b) * self.not_b

        if self.a != p_a:
            raise ValueError("all doesnt sum up")

        else:
            return p_a

def main():

if __name__ = "__main__":
    main()

