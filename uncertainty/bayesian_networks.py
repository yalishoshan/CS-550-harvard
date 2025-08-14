class Probability:
    def __init__(self):
        self.probabilities = {}

    def root(self, root_name, prob_dict):
        self.probabilities[root_name]  = prob_dict

    def first_depend(self, child_name, cond_probs):
        self.probabilities[child_name] = cond_probs


    def print_probs(self, node_name):
        """Print probabilities for a node"""
        print(f"{node_name}: {self.probabilities[node_name]}")

    def inference(self):

def main():
    # Example usage:
    network = Probability()

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
        "none, yes" : {"on_time" : 0.8, "delayed" : 0.2},
        "none, no": {"on_time": 0.9, "delayed": 0.1},
        "light, yes": {"on_time": 0.6, "delayed": 0.4},
        "light, no": {"on_time": 0.7, "delayed": 0.3},
        "heavy, yes": {"on_time": 0.4, "delayed": 0.6},
        "heavy, no": {"on_time": 0.5, "delayed": 0.5}
    }

    appointment = {
        "on_time" : {"attend" : 0.9, "miss" : 0.1} ,
        "delayed" : {"attend" : 0.6, "miss" : 0.4}
    }

    network.first_depend("maintenance", track_maintenance_probs)
    network.first_depend("Train", train)
    network.first_depend("appointment", appointment)

    # Print them
    network.print_probs("rain")
    network.print_probs("maintenance")
    network.print_probs("Train")
    network.print_probs("appointment")

if __name__ == "__main__":
    main()
