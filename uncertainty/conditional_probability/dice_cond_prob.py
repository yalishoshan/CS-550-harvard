class Probability:
    def __init__(self, red_dice, blue_dice):
        """
        Initialize the Probability object with red and blue dice.

        :param red_dice: list of integers representing the red die faces.
        :param blue_dice: list of integers representing the blue die faces.
        """

        self.red_dice = red_dice  # Store the red die faces list
        self.blue_dice = blue_dice  # Store the blue die faces list

    def all_possible_outcomes(self, red_dice):
        """
        Generate all possible outcomes for a fixed red die value against all blue die values.

        :param red_dice: int value representing the fixed red die result.
        :return: set of tuples containing (red_value, blue_value).
        """

        possibility_outcomes = set()  # Create a set to store unique outcome tuples
        for i in range(0, len(self.blue_dice)):  # Loop over each index of the blue die list
            possibility_outcomes.add((red_dice, self.blue_dice[i]))  # Add a tuple with red and blue values
        return possibility_outcomes  # Return all possible (red, blue) outcome pairs

    def outcome_odds(self, red_dice):
        """
        Calculate the probability of the given red die value with any blue die value.

        :param red_dice: int value representing the fixed red die result.
        :return: probability as a float.
        """

        # Divide the number of outcomes with the fixed red value by total possible outcomes
        return len(self.all_possible_outcomes(red_dice)) / (len(self.blue_dice) * len(self.red_dice))

    def outcome_sum(self, red_dice):
        """
        Get a sorted list of sums for all possible outcomes with a fixed red die value.

        :param red_dice: int value representing the fixed red die result.
        :return: sorted list of outcome sums.
        """

        # Create a list of sums from each (red, blue) outcome tuple
        outcome_sum = [sum(possibility) for possibility in self.all_possible_outcomes(red_dice)]
        return sorted(outcome_sum)  # Return the sums sorted in ascending order

    def sum_to(self, red_dice, x):
        """
        Calculate the probability that the sum equals x for a fixed red die value.

        :param red_dice: int value representing the fixed red die result.
        :param x: target sum to check for.
        :return: probability as a float.
        """

        # Count how many times x appears in the sums and divide by total possible outcomes
        return self.outcome_sum(red_dice).count(x) / len(self.all_possible_outcomes(red_dice))

    def calculate_conditional_prob(self, red_dice, x):
        """
        Calculate a conditional probability based on a fixed red die value and a target sum.

        Note: The current implementation multiplies probabilities instead of dividing them.
        :param red_dice: int value representing the fixed red die result.
        :param x: target sum to check for.
        :return: conditional probability as a float.
        """

        # Multiply the probability of sum = x by the probability of the red die outcome
        return self.sum_to(red_dice, x) * self.outcome_odds(red_dice)
        # Intended formula (not implemented): p(a|b) = p(a and b) / p(b)


def main():
    red_dice = [1, 2, 3, 4, 5, 6]
    blue_dice = [1, 2, 3, 4, 5, 6]
    p = Probability(red_dice, blue_dice)
    print(p.all_possible_outcomes(6))
    print(p.outcome_odds(6))
    print(p.outcome_sum(6))
    print(p.sum_to(6, 12))
    print(p.calculate_conditional_prob(6, 12))

if __name__ == "__main__":
    main()






