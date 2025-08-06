class Probability:
    """
    A class to calculate basic probabilities for dice roll outcomes.

    This class models probability calculations involving two dice (red and blue)
    and provides methods to compute outcome probabilities and analyze sum distributions.
    """

    def __init__(self, red_dice, blue_dice):
        """
        Initialize the Probability object with red and blue dice values.

        :param red_dice: list of integers representing the red die faces.
        :param blue_dice: list of integers representing the blue die faces.
        """
        # Store the list of values for the red die as an instance variable
        self.red_dice = red_dice
        # Store the list of values for the blue die as an instance variable
        self.blue_dice = blue_dice

    def all_possible_outcomes(self):
        """
        Generate all possible outcomes from rolling the red and blue dice.

        This method creates a cartesian product of all red die values with all
        blue die values to represent every possible combination when rolling both dice.

        :return: set of tuples (red_value, blue_value) representing each unique outcome.
        """
        # Initialize a set to store unique outcomes (sets prevent duplicate entries)
        possibility_outcomes = set()

        # Loop through all possible indices for the red die (hardcoded to 6 faces)
        for i in range(0, 6):
            # Loop through all possible indices for the blue die (hardcoded to 6 faces)
            for j in range(0, 6):
                # Get the value from red die at index i and blue die at index j
                red_value = self.red_dice[i]
                blue_value = self.blue_dice[j]
                # Add a tuple of (red die value, blue die value) to the set
                possibility_outcomes.add((red_value, blue_value))

        # Return all unique possible outcomes as a set of tuples
        return possibility_outcomes

    def outcome_sum(self):
        """
        Calculate the sum for each possible dice outcome and return them sorted.

        This method takes each possible (red, blue) combination, adds the values
        together, and returns all possible sums in ascending order.

        :return: sorted list of sums of each (red, blue) tuple.
        """
        # Get all possible outcomes first
        all_outcomes = self.all_possible_outcomes()

        # Create a list comprehension that sums each tuple (red_value + blue_value)
        outcome_sum = [sum(possibility) for possibility in all_outcomes]

        # Return the sums in ascending order for easier analysis and readability
        return sorted(outcome_sum)

    def sum_to(self, x):
        """
        Calculate the probability and ratio of outcomes that sum to a specific value.

        This method determines both the fractional representation and decimal
        probability of achieving a target sum when rolling both dice.

        :param x: integer target sum to check for.
        :return: tuple containing:
                 - a string representation of ratio (count/total)
                 - a float probability value (count divided by total outcomes)
        """
        # Get all possible sums from rolling both dice
        all_sums = self.outcome_sum()

        # Count how many sums equal the target value x
        count_x = all_sums.count(x)

        # Calculate total number of possible outcomes (should be 36 for standard dice)
        total_outcomes = len(self.all_possible_outcomes())

        # Create a string representation of the fraction (e.g., "2/36")
        fraction_string = f"{count_x}/{total_outcomes}"

        # Calculate the decimal probability by dividing count by total
        decimal_probability = count_x / total_outcomes

        # Return both the fraction as a string and the probability as a float
        return fraction_string, decimal_probability