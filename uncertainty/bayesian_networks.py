import itertools  # Import itertools for generating all combinations of hidden variables


class BayesianNetwork:
    """
    A class to represent and perform inference on Bayesian Networks.

    This class stores probability tables for nodes and their dependencies,
    and provides methods for exact inference using enumeration.
    """

    def __init__(self):
        """
        Initialize an empty Bayesian Network.
        """
        # Dictionary to store probability tables for each node in the network
        self.probabilities = {}

    def root(self, root_name, prob_dict):
        """
        Add a root node (no parents) to the network.

        :param root_name: string name of the root node
        :param prob_dict: dictionary mapping values to their probabilities
        """
        # Store the probability distribution for a root node (no conditional dependencies)
        self.probabilities[root_name] = prob_dict

    def first_depend(self, child_name, cond_probs):
        """
        Add a dependent node (has parents) to the network.

        :param child_name: string name of the dependent node
        :param cond_probs: conditional probability table as nested dictionary
        """
        # Store the conditional probability table for a node that depends on parent nodes
        self.probabilities[child_name] = cond_probs

    def print_probs(self, node_name):
        """
        Print probabilities for a node.

        :param node_name: string name of the node to print probabilities for
        """
        # Display the probability table for the specified node
        print(f"{node_name}: {self.probabilities[node_name]}")

    def inference(self, x, e, y, x_probs, y_probs):
        """
        Perform probabilistic inference for a specific scenario.

        This method calculates probabilities when hidden variable values are known.

        :param x: query variable name
        :param e: tuple of evidence values
        :param y: hidden variable name
        :param x_probs: tuple of possible query variable values
        :param y_probs: tuple of possible hidden variable values
        :return: dictionary with probabilities for each query outcome
        """
        # Extract probability of first hidden variable value given evidence
        likely_value = self.probabilities[y][e[0], e[1]][y_probs[0]]
        # Extract probability of second hidden variable value given evidence
        less_likely_value = self.probabilities[y][e[0], e[1]][y_probs[1]]

        # Calculate P(query=first_outcome | hidden=likely_scenario)
        do_it_when_likely_prob = self.probabilities[x][likely_value][x_probs[0]]
        # Calculate P(query=second_outcome | hidden=likely_scenario)
        do_it_when_unlikely_prob = self.probabilities[x][likely_value][x_probs[1]]

        # Calculate P(query=first_outcome | hidden=unlikely_scenario)
        miss_if_likely_prob = self.probabilities[x][less_likely_value][x_probs[0]]
        # Calculate P(query=second_outcome | hidden=unlikely_scenario)
        miss_if_unlikely_prob = self.probabilities[x][less_likely_value][x_probs[1]]

        # Sum probabilities across scenarios: P(attend) = P(attend|likely)*P(likely) + P(attend|unlikely)*P(unlikely)
        prob_do = (do_it_when_likely_prob * likely_value + do_it_when_unlikely_prob * less_likely_value)

        # Sum probabilities across scenarios: P(miss) = P(miss|likely)*P(likely) + P(miss|unlikely)*P(unlikely)
        prob_miss = (miss_if_likely_prob * likely_value + miss_if_unlikely_prob * less_likely_value)

        # Return dictionary with probability distribution over query variable outcomes
        results = {"attend": prob_do, "miss": prob_miss}

        return results

    def enumerate(self, x, e, y_vars, x_values, y_value_options):
        """
        Perform inference by enumeration over all possible hidden variable assignments.

        This method implements the mathematical formula: P(X|e) = Σ_y P(X,e,y)

        :param x: query variable name
        :param e: evidence dictionary
        :param y_vars: list of hidden variable names
        :param x_values: list of possible query variable values
        :param y_value_options: list of possible values for each hidden variable
        :return: dictionary with normalized probability distribution
        """
        # Generate all possible combinations of hidden variable assignments using Cartesian product
        all_combinations = list(itertools.product(*y_value_options))
        # Initialize dictionary to store final probability results
        results = {}

        # Initialize accumulator for total probability across all scenarios
        total_probability = 0.0

        # For each possible value the query variable can take
        for x_value in x_values:
            # Consider every possible assignment to hidden variables
            for combination in all_combinations:
                # Use existing inference method to calculate probabilities for this specific scenario
                scenario_result = self.inference(x_value, e, combination, x_values, combination)

                # Extract the probability contribution for current query value from scenario result
                probability_contribution = scenario_result[x_value]
                # Add this scenario's contribution to running total (implements Σ summation)
                total_probability += probability_contribution

            # Store the accumulated probability for this query value
            results[x_value] = total_probability

        # Return the probability distribution over query variable values
        return results


def main():
    # Example usage:
    network = BayesianNetwork()

    # Set root node (Rain)
    rain_probs = {"none": 0.7, "light": 0.2, "heavy": 0.1}
    network.root("rain", rain_probs)

    # Set dependent node (Traffic depends on Rain)
    track_maintenance_probs = {
        "none": {"light": 0.4, "heavy": 0.6},
        "light": {"light": 0.2, "heavy": 0.8},
        "heavy": {"light": 0.1, "heavy": 0.9}
    }

    train = {
        "none, yes": {"on_time": 0.8, "delayed": 0.2},
        "none, no": {"on_time": 0.9, "delayed": 0.1},
        "light, yes": {"on_time": 0.6, "delayed": 0.4},
        "light, no": {"on_time": 0.7, "delayed": 0.3},
        "heavy, yes": {"on_time": 0.4, "delayed": 0.6},
        "heavy, no": {"on_time": 0.5, "delayed": 0.5}
    }

    appointment = {
        "on_time": {"attend": 0.9, "miss": 0.1},
        "delayed": {"attend": 0.6, "miss": 0.4}
    }
    network.first_depend("maintenance", track_maintenance_probs)
    network.first_depend("Train", train)
    network.first_depend("appointment", appointment)

    # Print them
    network.print_probs("rain")
    network.print_probs("maintenance")
    network.print_probs("Train")
    network.print_probs("appointment")

    result = network.inference("appointment", ("light", "no"), "Train", ("on_time", "delayed"), ("on_time", "delayed"))


if __name__ == "__main__":
    main()