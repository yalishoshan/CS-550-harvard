class Probability:
    """
    A class to model flight probability scenarios and independence calculations.

    This class represents probability distributions for flight outcomes including
    on-time arrivals, delays, and cancellations, along with independence calculations.
    """

    def __init__(self, flight):
        """
        Initialize the Probability object with a flight identifier.

        :param flight: string or identifier representing the flight being analyzed.
        """
        # Store the flight identifier as an instance variable for reference
        self.flight = flight

    def on_time(self):
        """
        Return the probability statement for on-time flight arrival.

        This method provides a formatted string showing the flight identifier
        and its associated on-time probability of 0.6 (60%).

        :return: string containing flight ID and on-time probability.
        """
        # Create a formatted string with flight identifier and on-time probability
        return f"{self.flight} = on time = 0.6"

    def delay(self):
        """
        Return the probability statement for flight delay.

        This method provides a formatted string showing the flight identifier
        and its associated delay probability of 0.3 (30%).

        :return: string containing flight ID and delay probability.
        """
        # Create a formatted string with flight identifier and delay probability
        return f"{self.flight} = delay = 0.3"

    def cancel(self):
        """
        Return the probability statement for flight cancellation.

        This method provides a formatted string showing the flight identifier
        and its associated cancellation probability of 0.1 (10%).

        :return: string containing flight ID and cancellation probability.
        """
        # Create a formatted string with flight identifier and cancellation probability
        return f"{self.flight} = cancel = 0.1"

    def probability_distribution(self):
        """
        Return the complete probability distribution for all flight outcomes.

        This method combines all possible flight outcomes (on-time, delay, cancel)
        into a single string representing the complete probability distribution.
        Note: The probabilities sum to 1.0 (0.6 + 0.3 + 0.1 = 1.0).

        :return: string containing the complete probability distribution.
        """
        # Get the on-time probability string
        on_time_prob = self.on_time()

        # Get the delay probability string
        delay_prob = self.delay()

        # Get the cancellation probability string
        cancel_prob = self.cancel()

        # Combine all probability statements into one formatted string
        return f"{on_time_prob}, {delay_prob}, {cancel_prob}"

    def independence(self):
        """
        Calculate and return the probability of independent events occurring together.

        This method demonstrates the independence principle where the probability
        of two independent events both occurring is the product of their individual
        probabilities: P(A and B) = P(A) × P(B).

        :return: string showing the independence calculation and result.
        """
        # Calculate the product of on-time probability (0.6) and delay probability (0.3)
        # This represents P(on-time AND delay) assuming independence
        independent_probability = 0.6 * 0.3

        # Create a formatted string showing the calculation and result (0.18 or 18%)
        return f"{self.flight} = independence = 0.6 * 0.3 = {independent_probability}"
