class Prob:
    """
    A class to validate and categorize probability values and distributions.

    This class provides methods to check if probability values are valid,
    classify probability events, and validate probability distributions.
    """

    def __init__(self, value, value_lst):
        """
        Initialize the Prob object with a single probability value and a list of values.

        :param value: float representing a single probability value.
        :param value_lst: list of probability values to form a distribution.
        """
        # Store the single probability value as an instance variable
        self.value = value

        # Store the probability list wrapped in another list (note: this creates [[value_lst]])
        # This might be unintentional - should probably be: self.value_lst = value_lst
        self.value_lst = [value_lst]

    def omega(self):
        """
        Validate and categorize a probability value based on mathematical constraints.

        This method checks if a probability value falls within the valid range [0,1]
        and categorizes it as impossible, certain, or probabilistic event.

        :return: string description of the probability category or the value itself.
        :raises ValueError: if the probability value is outside the range [0,1].
        """
        # Check if the probability value is less than 0 or greater than 1 (invalid range)
        if self.value < 0 or self.value > 1:
            # Raise an exception for invalid probability values
            raise ValueError("Chances range is only between 0 and 1")

        # Check if the probability is exactly 0 (impossible event)
        elif self.value == 0:
            # Return string indicating this is an impossible event
            return "Impossible event"

        # Check if the probability is exactly 1 (certain event)
        elif self.value == 1:
            # Return string indicating this event is certain to happen
            return "Certain to happen"

        # Check if the probability is between 0 and 1 (exclusive)
        elif 1 > self.value > 0:
            # Return the actual probability value for valid probabilistic events
            return self.value

    def sigma(self):
        """
        Validate if the stored list of values forms a proper probability distribution.

        A valid probability distribution requires that all probability values
        sum to exactly 1.0.

        :return: string confirmation message if valid distribution.
        :raises ValueError: if the sum of probabilities does not equal 1.
        """
        # Calculate the sum of all values in the probability list
        # Note: self.value_lst is [[value_lst]], so we need to access the inner list
        probability_sum = sum(self.value_lst[0]) if self.value_lst else 0

        # Check if the sum of all probabilities is not equal to 1
        if probability_sum != 1:
            # Raise an exception for invalid probability distributions
            raise ValueError("Sum of probabilities must be 1")

        # If sum equals 1, return confirmation that this is a valid distribution
        else:
            return "Probability distribution"