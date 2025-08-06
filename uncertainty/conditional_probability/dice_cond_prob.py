class Probability:
    """
    A class to calculate conditional probabilities using dice roll outcomes.

    This class models probability calculations involving two dice (red and blue)
    and provides methods to compute various probability scenarios including
    conditional probabilities based on fixed die values.
    """

    def __init__(self, red_dice, blue_dice):
        """
        Initialize the Probability object with red and blue dice.

        :param red_dice: list of integers representing the red die faces.
        :param blue_dice: list of integers representing the blue die faces.
        """
        # Store the red die faces list as an instance variable
        self.red_dice = red_dice
        # Store the blue die faces list as an instance variable
        self.blue_dice = blue_dice

    def all_possible_outcomes(self, red_dice):
        """
        Generate all possible outcomes for a fixed red die value against all blue die values.

        This method creates all possible combinations where the red die shows a specific
        value and the blue die can show any of its possible values.

        :param red_dice: int value representing the fixed red die result.
        :return: set of tuples containing (red_value, blue_value).
        """
        # Create a set to store unique outcome tuples (sets automatically handle duplicates)
        possibility_outcomes = set()

        # Loop over each index of the blue die list to get all possible blue outcomes
        for i in range(0, len(self.blue_dice)):
            # Add a tuple with the fixed red value and current blue value to the set
            possibility_outcomes.add((red_dice, self.blue_dice[i]))

            # Return all possible (red, blue) outcome pairs as a set
        return possibility_outcomes

    def outcome_odds(self, red_dice):
        """
        Calculate the probability of the given red die value with any blue die value.

        This method computes the likelihood of getting a specific red die value
        when considering all possible outcomes of both dice.

        :param red_dice: int value representing the fixed red die result.
        :return: probability as a float.
        """
        # Get the number of outcomes with the fixed red value (numerator)
        favorable_outcomes = len(self.all_possible_outcomes(red_dice))

        # Calculate total possible outcomes (red die possibilities × blue die possibilities)
        total_outcomes = len(self.blue_dice) * len(self.red_dice)

        # Divide favorable outcomes by total outcomes to get probability
        return favorable_outcomes / total_outcomes

    def outcome_sum(self, red_dice):
        """
        Get a sorted list of sums for all possible outcomes with a fixed red die value.

        This method calculates the sum of each (red, blue) pair where the red die
        shows a specific value, then returns these sums in ascending order.

        :param red_dice: int value representing the fixed red die result.
        :return: sorted list of outcome sums.
        """
        # Create a list comprehension that sums each tuple from all possible outcomes
        outcome_sum = [sum(possibility) for possibility in self.all_possible_outcomes(red_dice)]

        # Return the sums sorted in ascending order for easier analysis
        return sorted(outcome_sum)

    def sum_to(self, red_dice, x):
        """
        Calculate the probability that the sum equals x for a fixed red die value.

        This method determines how likely it is to get a specific sum when
        the red die shows a particular value and the blue die can be any value.

        :param red_dice: int value representing the fixed red die result.
        :param x: target sum to check for.
        :return: probability as a float.
        """
        # Count how many times the target sum x appears in all possible sums
        count_of_target_sum = self.outcome_sum(red_dice).count(x)

        # Get the total number of possible outcomes with this red die value
        total_possible_outcomes = len(self.all_possible_outcomes(red_dice))

        # Calculate probability by dividing count by total outcomes
        return count_of_target_sum / total_possible_outcomes

    def calculate_conditional_prob(self, red_dice, x):
        """
        Calculate a conditional probability based on a fixed red die value and a target sum.

        Note: The current implementation multiplies probabilities instead of dividing them.
        This does not correctly implement conditional probability P(A|B) = P(A∩B)/P(B).

        :param red_dice: int value representing the fixed red die result.
        :param x: target sum to check for.
        :return: conditional probability as a float (incorrectly calculated).
        """
        # Get the probability that sum equals x given the fixed red die value
        prob_sum_equals_x = self.sum_to(red_dice, x)

        # Get the probability of getting this red die value
        prob_red_die = self.outcome_odds(red_dice)

        # Multiply the probabilities (this is incorrect for conditional probability)
        # The correct formula should be: p(sum=x|red=red_dice) = p(sum=x AND red=red_dice) / p(red=red_dice)
        return prob_sum_equals_x * prob_red_die