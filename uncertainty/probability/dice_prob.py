class Probability:
    def __init__(self, red_dice, blue_dice):
        """
        Initialize the Probability object with red and blue dice values.
        :param red_dice: list of integers representing the red die faces.
        :param blue_dice: list of integers representing the blue die faces.
        """
        self.red_dice = red_dice  # Store the list of values for the red die
        self.blue_dice = blue_dice  # Store the list of values for the blue die

    def all_possible_outcomes(self):
        """
        Generate all possible outcomes from rolling the red and blue dice.
        :return: set of tuples (red_value, blue_value) representing each unique outcome.
        """
        possibility_outcomes = set()  # Initialize a set to store unique outcomes
        for i in range(0, 6):  # Loop through all possible indices for the red die
            for j in range(0, 6):  # Loop through all possible indices for the blue die
                # Add a tuple of (value from red die, value from blue die) to the set
                possibility_outcomes.add((self.red_dice[i], self.blue_dice[j]))
        return possibility_outcomes  # Return all unique possible outcomes

    def outcome_sum(self):
        """
        Calculate the sum for each possible dice outcome and return them sorted.
        :return: sorted list of sums of each (red, blue) tuple.
        """
        # Create a list of sums from each possible outcome
        outcome_sum = [sum(possibility) for possibility in self.all_possible_outcomes()]
        return sorted(outcome_sum)  # Return the sums in ascending order

    def sum_to(self, x):
        """
        Calculate the probability and ratio of outcomes that sum to a specific value.
        :param x: integer target sum to check for.
        :return: tuple containing:
                 - a string representation of ratio (count/total)
                 - a float probability value (count divided by total outcomes)
        """
        # Count how many sums equal x, store it for repeated use
        count_x = self.outcome_sum().count(x)
        total_outcomes = len(self.all_possible_outcomes())  # Total number of possible outcomes
        # Return both the fraction as a string and the probability as a float
        return f"{count_x}/{total_outcomes}", count_x / total_outcomes

def main():
    red_dice = [1, 2, 3, 4, 5, 6]
    blue_dice = [1, 2, 3, 4, 5, 6]
    p = Probability(red_dice, blue_dice)
    print(p.sum_to(3))


if __name__ == "__main__":
    main()






