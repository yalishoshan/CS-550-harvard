class JointProbability:
    """
    A class to calculate joint and conditional probabilities for two events.

    This class models the relationship between two binary events (c and r)
    and computes various probability measures including joint probabilities,
    conditional probabilities, and normalization constants.
    """

    def __init__(self, c, not_c, r, not_r):
        """
        Initialize the Probability object with marginal probabilities.

        :param c: probability of event c occurring
        :param not_c: probability of event c not occurring
        :param r: probability of event r occurring
        :param not_r: probability of event r not occurring
        """
        # Store probability of event c
        self.c = c
        # Store probability of event r
        self.r = r
        # Store probability of complement of event c
        self.not_c = not_c
        # Store probability of complement of event r
        self.not_r = not_r

        # Validate that probabilities for event c form a complete probability space
        if self.c + self.not_c != 1:
            # Raise error if c and its complement don't sum to 1
            raise ValueError("c and not_c must sum to 1")
        # Validate that probabilities for event r form a complete probability space
        if self.r + self.not_r != 1:
            # Raise error if r and its complement don't sum to 1
            raise ValueError("r and not_r must sum to 1")

    def joint_probabilities(self):
        """
        Calculate all joint probabilities for the two events.

        Assumes independence: P(A,B) = P(A) * P(B)

        :return: dictionary containing all four joint probabilities
        """
        # Create dictionary to store all joint probability combinations
        joint_probabilities = {
            # Calculate P(c and r) = P(c) * P(r) assuming independence
            "p(c, r)": self.c * self.r,
            # Calculate P(c and not r) = P(c) * P(not r) assuming independence
            "p(c, not r)": self.c * self.not_r,
            # Calculate P(not c and r) = P(not c) * P(r) assuming independence
            "p(not c, r)": self.not_c * self.r,
            # Calculate P(not c and not r) = P(not c) * P(not r) assuming independence
            "p(not c, not r)": self.not_c * self.not_r
        }

        # Return the complete joint probability distribution
        return joint_probabilities

    def deduce(self):
        """
        Calculate all conditional probabilities from joint probabilities.

        Uses the formula P(A|B) = P(A,B) / P(B) for all combinations.

        :return: dictionary containing all conditional probabilities
        """
        # Get the joint probability distribution first
        joints = self.joint_probabilities()

        # Calculate P(c given r) = P(c,r) / P(r)
        p_c_given_r = joints["p(c, r)"] / self.r
        # Calculate P(c given not r) = P(c, not r) / P(not r)
        p_c_given_not_r = joints["p(c, not r)"] / self.not_r

        # Calculate P(not c given r) = P(not c, r) / P(r)
        p_not_c_given_r = joints["p(not c, r)"] / self.r
        # Calculate P(not c given not r) = P(not c, not r) / P(not r)
        p_not_c_given_not_r = joints["p(not c, not r)"] / self.not_r

        # Create dictionary with all conditional probabilities using consistent formula P(A|B) = P(A,B)/P(B)
        conditional_probs = {
            # P(c|r) = P(c,r) / P(r)
            "P(c|r)": joints["p(c, r)"] / self.r,
            # P(c|not_r) = P(c,not_r) / P(not_r)
            "P(c|not_r)": joints["p(c, not r)"] / self.not_r,
            # P(not_c|r) = P(not_c,r) / P(r)
            "P(not_c|r)": joints["p(not c, r)"] / self.r,
            # P(not_c|not_r) = P(not_c,not_r) / P(not_r)
            "P(not_c|not_r)": joints["p(not c, not r)"] / self.not_r,
            # P(r|c) = P(c,r) / P(c) - reverse conditional
            "P(r|c)": joints["p(c, r)"] / self.c,
            # P(r|not_c) = P(not_c,r) / P(not_c) - reverse conditional
            "P(r|not_c)": joints["p(not c, r)"] / self.not_c,
            # P(not_r|c) = P(c,not_r) / P(c) - reverse conditional
            "P(not_r|c)": joints["p(c, not r)"] / self.c,
            # P(not_r|not_c) = P(not_c,not_r) / P(not_c) - reverse conditional
            "P(not_r|not_c)": joints["p(not c, not r)"] / self.not_c
        }

        # Return all calculated conditional probabilities
        return conditional_probs

    def a_find(self):
        """
        Calculate the normalization constant for conditional probabilities given r.

        This finds the constant 'a' such that a*P(c,r) + a*P(not_c,r) = 1
        which ensures P(c|r) + P(not_c|r) = 1

        :return: the normalization constant a
        """
        # Get joint probabilities to use in normalization calculation
        joints = self.joint_probabilities()

        # Comment shows the relationship: a * P(c,r) + a * P(not_c,r) = 1
        # Solving for a: a * [P(c,r) + P(not_c,r)] = 1
        # Therefore: a = 1 / [P(c,r) + P(not_c,r)]
        # Note: P(c,r) + P(not_c,r) = P(r) by law of total probability
        a = 1 / (joints["p(c, r)"] + joints["p(not c, r)"])
        # Return the normalization constant
        return a


def main():
    p = JointProbability(0.4, 0.6, 0.1, 0.9)
    joint_probabilities = p.joint_probabilities()
    deduce = p.deduce()
    a_found = p.a_find()

    print(joint_probabilities)
    print(deduce)
    print(a_found)


if __name__ == "__main__":
    main()