import itertools
from Propositional_Logic import LogicNot, LogicAnd, LogicOr, LogicImplies, LogicBiconditional, LogicXor


class Inference:
    """
    This class implements propositional logic inference using model checking.
    """

    def __init__(self, p, q, r):
        """
        Initialize the inference engine.

        :param p: first proposition name
        :param q: second proposition name
        :param r: third proposition name
        """
        self.p = p  # Store first proposition name
        self.q = q  # Store second proposition name
        self.r = r  # Store third proposition name

    def model_check(self, kb, query, model, propositions):
        """
        Perform model checking to determine if knowledge base entails query.

        :param kb: knowledge base statements
        :param query: query to check
        :param model: model dictionary (will be built during execution)
        :param propositions: list of proposition names
        """
        valid_models = []  # Store models that satisfy KB

        # Generate all possible truth value combinations
        for combination in itertools.product([True, False], repeat=len(propositions)):
            model = {}  # Create empty model for this combination

            # Build the model by assigning truth values to propositions
            for i in range(len(propositions)):
                model[propositions[i]] = combination[i]  # Assign truth value to proposition

            print(f"Checking model: {model}")

            # Check if all KB statements are satisfied in this model
            for statement in kb:
                operation = statement[0]  # Get the logical operation type

                # Dictionary mapping operation names to classes
                logic_operations = {
                    "not": LogicNot,
                    "and": LogicAnd,
                    "or": LogicOr,
                    "implies": LogicImplies,
                    "biconditional": LogicBiconditional,
                    "xor": LogicXor
                }

                if operation in logic_operations:
                    LogicClass = logic_operations[operation]  # Get the appropriate class

                    if operation == "not":
                        # NOT operation needs one parameter
                        p_value = model[statement[1]]  # Get proposition value from model
                        logic_op = LogicClass(p_value)  # Create logic operation object
                    else:
                        # Binary operations need two parameters
                        p_value = model[statement[1]]  # Get first proposition value
                        q_value = model[statement[2]]  # Get second proposition value
                        logic_op = LogicClass(p_value, q_value)  # Create logic operation object

                    # Check if this statement is false in the current model
                    if not logic_op.evaluate():
                        print(f"❌ KB fails - discarding model")
                        break  # Exit KB checking loop, move to next model
            else:
                # If we completed the KB loop without breaking, all statements were true
                print(f"✅ KB satisfied - keeping model")
                valid_models.append(model.copy())  # Store copy of valid model

        return valid_models  # Return all models that satisfy the knowledge base


def main():
    """
    Example usage of the model checking algorithm.
    """
    pass


if __name__ == "__main__":
    main()