class BayesRule:
    """
    A class to calculate Bayes' rule for posterior probability estimation.

    This class implements Bayes' theorem: P(H|E) = P(E|H) * P(H) / P(E)
    where H is hypothesis (unknown cause) and E is evidence (effect).
    """

    def __init__(self, effect, unknown_cause, a):
        """
        Initialize the Probability object with prior probabilities.

        :param effect: P(E|H) - probability of effect given the unknown cause
        :param unknown_cause: P(H) - prior probability of the unknown cause
        :param a: P(E) - total probability of the effect (normalizing constant)
        """
        # Store the conditional probability P(effect | unknown_cause)
        self.effect = effect
        # Store the prior probability P(unknown_cause)
        self.unknown_cause = unknown_cause
        # Store the total probability P(effect) used for normalization
        self.a = a

        # Validate that effect probability is within valid range [0,1]
        if self.effect > 1 or self.effect < 0:
            # Raise error if probability is outside valid range
            raise ValueError("Effect is out of range")
        # Validate that unknown cause probability is within valid range [0,1]
        if self.unknown_cause > 1 or self.unknown_cause < 0:
            # Raise error if probability is outside valid range
            raise ValueError("Unknown cause is out of range")
        # Validate that normalizing constant is within valid range [0,1]
        if self.a > 1 or self.a < 0:
            # Raise error if probability is outside valid range
            raise ValueError("A is out of range")

    def bayes_rule(self):
        """
        Apply Bayes' rule to calculate posterior probability.

        Computes P(unknown_cause | effect) = P(effect | unknown_cause) * P(unknown_cause) / P(effect)

        :return: float representing the posterior probability
        """
        # Calculate numerator: P(effect | unknown_cause) * P(unknown_cause)
        numerator = self.unknown_cause * self.effect
        # Divide by total probability P(effect) to get posterior probability
        return numerator / self.a


def main():
    bays = BayesRule(0.1, 0.8, 0.4)
    print(bays.bayes_rule())


if __name__ == "__main__":
    main()