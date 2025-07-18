import itertools
from propositional_logic import LogicNot, LogicAnd, LogicOr, LogicImplies, LogicBiconditional, LogicXor


class ModelCheck:
    """
    Class that performs model checking to determine if knowledge base entails query.
    This class handles the core model checking algorithm.
    """

    def __init__(self, kb, query, model, propositions):
        """
        Initialize the model checking process.

        :param kb: knowledge base statements
        :param query: query statement
        :param model: model dictionary (will be built during execution)
        :param propositions: list of proposition names
        """
        self.kb = kb  # Store knowledge base statements
        self.query = query  # Store query statement
        self.model = model  # Store model dictionary
        self.propositions = propositions  # Store list of propositions

    def model_mapping(self):
        """
        Generate all possible models and check which ones satisfy the knowledge base.

        :return: list of valid models that satisfy KB
        """
        valid_models = []  # Store models that satisfy KB

        # Generate all possible truth value combinations
        for combination in itertools.product([True, False], repeat=len(self.propositions)):
            model = {}  # Create empty model for this combination

            # Build the model by assigning truth values to propositions
            for i in range(len(self.propositions)):
                model[self.propositions[i]] = combination[i]  # Assign truth value to proposition

            print(f"Checking model: {model}")

            # Check if this model satisfies the knowledge base
            if self.check_model_validity(model):
                print(f"✅ KB satisfied - keeping model")
                valid_models.append(model.copy())  # Store copy of valid model
            else:
                print(f"❌ KB fails - discarding model")

        return valid_models  # Return all models that satisfy the knowledge base

    def check_model_validity(self, model):
        """
        Check if a model satisfies all statements in the knowledge base.

        :param model: model to check
        :return: True if model satisfies KB, False otherwise
        """
        # Check if all KB statements are satisfied in this model
        for statement in self.kb:
            operation = statement[0]  # Get the logical operation type

            # Dictionary mapping operation symbols to classes
            logic_operations = {
                "¬": LogicNot,
                "∧": LogicAnd,
                "∨": LogicOr,
                "v": LogicOr,
                "→": LogicImplies,
                "↔": LogicBiconditional,
                "⊕": LogicXor
            }

            if operation in logic_operations:
                logic_class = logic_operations[operation]  # Get the appropriate class

                if operation == "¬":
                    # NOT operation needs one parameter
                    p_value = model[statement[1]]  # Get proposition value from model
                    logic_op = logic_class(p_value)  # Create logic operation object
                else:
                    # Binary operations need two parameters
                    p_value = model[statement[1]]  # Get first proposition value
                    q_value = model[statement[2]]  # Get second proposition value
                    logic_op = logic_class(p_value, q_value)  # Create logic operation object

                # Check if this statement is false in the current model
                if not logic_op.evaluate():
                    return False  # If any statement fails, model doesn't satisfy KB

        return True  # All statements passed, model satisfies KB

    def check_query_validity(self, model):
        """
        Check if a query statement is satisfied in a model.

        :param model: model to check
        :return: True if query is satisfied, False otherwise
        """
        # Check if query statement is satisfied in this model
        operation = self.query[0]  # Get the logical operation type

        # Dictionary mapping operation symbols to classes
        logic_operations = {
            "¬": LogicNot,
            "∧": LogicAnd,
            "∨": LogicOr,
            "v": LogicOr,
            "→": LogicImplies,
            "↔": LogicBiconditional,
            "⊕": LogicXor
        }

        if operation in logic_operations:
            logic_class = logic_operations[operation]  # Get the appropriate class

            if operation == "¬":
                # NOT operation needs one parameter
                p_value = model[self.query[1]]  # Get proposition value from model
                logic_op = logic_class(p_value)  # Create logic operation object
            else:
                # Binary operations need two parameters
                p_value = model[self.query[1]]  # Get first proposition value
                q_value = model[self.query[2]]  # Get second proposition value
                logic_op = logic_class(p_value, q_value)  # Create logic operation object

            return logic_op.evaluate()  # Directly return the result

        else:
            return False  # Treat unknown operations as false


def main():
    kb = [("→", "p", "q"), ("¬", "p")]
    query = ("∨", "p", "q")
    propositions = ["p", "q"]

    model_checker = ModelCheck(kb, query, {}, propositions)
    valid_models = model_checker.model_mapping()

    print(f"Found {len(valid_models)} valid models")

    query_result = model_checker.check_query_validity(valid_models[0])
    print(f"Query result: {query_result}")


if __name__ == "__main__":
    main()