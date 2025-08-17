class ProbabilityRules:
    """
    A class to demonstrate fundamental probability rules and operations.

    This class implements key probability rules including negation, inclusion-exclusion,
    marginalization, and conditioning for two events A and B.
    """

    def __init__(self, a, b, not_a, not_b):
        """
        Initialize the Probability object with probabilities for events A and B.

        :param a: probability of event A occurring
        :param b: probability of event B occurring
        :param not_a: probability of event A not occurring (complement of A)
        :param not_b: probability of event B not occurring (complement of B)
        """
        # Store probability P(A)
        self.a = a
        # Store probability P(B)
        self.b = b
        # Store probability P(not A) - complement of event A
        self.not_a = not_a
        # Store probability P(not B) - complement of event B
        self.not_b = not_b

    def negation(self):
        """
        Apply the negation rule: P(not A) = 1 - P(A).

        This demonstrates that the probability of an event not occurring
        equals 1 minus the probability of it occurring.

        :return: probability of not A occurring
        """
        # Calculate P(not A) using negation rule: P(not A) = 1 - P(A)
        p_not_a = 1 - self.a
        # Return the probability of the complement event
        return p_not_a

    def inclusion_exclusion(self, p_a_and_b):
        """
        Apply the inclusion-exclusion principle: P(A or B) = P(A) + P(B) - P(A and B).

        This rule calculates the probability of at least one of two events occurring
        by adding individual probabilities and subtracting their intersection.

        :param p_a_and_b: probability of both A and B occurring together
        :return: probability of A or B occurring
        """
        # Apply inclusion-exclusion: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
        p_a_or_b = self.a + self.b - p_a_and_b
        # Return probability of union of events A and B
        return p_a_or_b

    def marginalization(self, p_a_and_b, p_a_and_not_b):
        """
        Apply the marginalization rule: P(A) = P(A and B) + P(A and not B).

        This rule shows how to recover marginal probabilities from joint probabilities
        by summing over all possible values of the other variable.

        :param p_a_and_b: probability of A and B both occurring
        :param p_a_and_not_b: probability of A occurring but not B
        :return: marginal probability of A
        """
        # Apply marginalization: P(A) = P(A ∩ B) + P(A ∩ B̄)
        p_a = p_a_and_b + p_a_and_not_b
        # Return marginal probability obtained by summing over all B values
        return p_a

    def conditioning(self, p_a_given_b, p_a_given_not_b):
        """
        Apply the law of total probability (conditioning rule):
        P(A) = P(A|B) * P(B) + P(A|not B) * P(not B).

        This rule calculates marginal probability by conditioning on another variable
        and weighing by the probability of each conditioning event.

        :param p_a_given_b: conditional probability P(A|B)
        :param p_a_given_not_b: conditional probability P(A|not B)
        :return: marginal probability of A calculated via conditioning
        """
        # Apply law of total probability: P(A) = P(A|B)P(B) + P(A|B̄)P(B̄)
        p_a = p_a_given_b * self.b + p_a_given_not_b * self.not_b
        # Return marginal probability calculated by conditioning on B
        return p_a


def main():
    p = ProbabilityRules(0.8, 0.1, 0.3, 0.4)
    print(p.negation(), p.inclusion_exclusion(0.8), p.marginalization(0.1, 0.4), p.conditioning(0.1, 0.4))


if __name__ == "__main__":
    main()