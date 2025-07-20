from itertools import product

class Not:
    """
    This class implements the logical NOT operation (negation).
    Represents the negation operator (¬) in propositional logic.
    """

    def __init__(self, operand):
        """
        Initialize the NOT operation with one proposition.

        :param operand: the proposition to negate
        :type operand: bool or Symbol or LogicOperation
        """
        self.operand = operand

    def evaluate(self, model=None):
        """
        Returns the negation of the propositional formula.

        :param model: dictionary mapping symbols to truth values
        :type model: dict or None
        :return: negation of the operand (¬operand)
        :rtype: bool
        """
        if hasattr(self.operand, 'evaluate'):  # Check if operand has evaluate method
            return not self.operand.evaluate(model)
        return not self.operand

    def __str__(self):
        return f"¬{self.operand}"


class And:
    """
    This class implements the logical AND operation (conjunction).
    Represents the conjunction operator (∧) in propositional logic.
    """

    def __init__(self, *operands):
        """
        Initialize the AND operation with multiple propositions.

        :param operands: propositions to conjoin
        :type operands: bool or Symbol or LogicOperation
        """
        if len(operands) < 2:  # Validate minimum operands
            raise ValueError("AND operation requires at least 2 operands")
        self.operands = operands

    def evaluate(self, model=None):
        """
        Returns the conjunction of all propositional formulas.

        :param model: dictionary mapping symbols to truth values
        :type model: dict or None
        :return: conjunction of all operands (op1 ∧ op2 ∧ ... ∧ opN)
        :rtype: bool
        """
        for operand in self.operands:  # Check all operands
            if hasattr(operand, 'evaluate'):
                if not operand.evaluate(model):
                    return False
            elif not operand:
                return False
        return True

    def __str__(self):
        return f"({' ∧ '.join(str(op) for op in self.operands)})"


class Or:
    """
    This class implements the logical OR operation (disjunction).
    Represents the disjunction operator (∨) in propositional logic.
    """

    def __init__(self, *operands):
        """
        Initialize the OR operation with multiple propositions.

        :param operands: propositions to dis join
        :type operands: bool or Symbol or LogicOperation
        """
        if len(operands) < 2:  # Validate minimum operands
            raise ValueError("OR operation requires at least 2 operands")
        self.operands = operands

    def evaluate(self, model=None):
        """
        Returns the disjunction of all propositional formulas.

        :param model: dictionary mapping symbols to truth values
        :type model: dict or None
        :return: disjunction of all operands (op1 ∨ op2 ∨ ... ∨ opN)
        :rtype: bool
        """
        for operand in self.operands:  # Check all operands
            if hasattr(operand, 'evaluate'):
                if operand.evaluate(model):
                    return True
            elif operand:
                return True
        return False

    def __str__(self):
        return f"({' ∨ '.join(str(op) for op in self.operands)})"


class Implies:
    """
    This class implements the logical IMPLIES operation (implication).
    Represents the implication operator (→) in propositional logic.
    """

    def __init__(self, antecedent, consequent):
        """
        Initialize the IMPLIES operation with two propositions.

        :param antecedent: the "if" part of the implication
        :type antecedent: bool or Symbol or LogicOperation
        :param consequent: the "then" part of the implication
        :type consequent: bool or Symbol or LogicOperation
        """
        self.antecedent = antecedent
        self.consequent = consequent

    def evaluate(self, model=None):
        """
        Returns the implication of two propositional formulas.
        Uses the logical equivalence: p → q ≡ ¬p ∨ q

        :param model: dictionary mapping symbols to truth values
        :type model: dict or None
        :return: implication antecedent → consequent
        :rtype: bool
        """
        # Get antecedent value
        if hasattr(self.antecedent, 'evaluate'):
            ant_val = self.antecedent.evaluate(model)
        else:
            ant_val = self.antecedent

        # Get consequent value
        if hasattr(self.consequent, 'evaluate'):
            cons_val = self.consequent.evaluate(model)
        else:
            cons_val = self.consequent

        return not ant_val or cons_val  # p → q ≡ ¬p ∨ q

    def __str__(self):
        return f"({self.antecedent} → {self.consequent})"


class Biconditional:
    """
    This class implements the logical BICONDITIONAL operation (if and only if).
    Represents the biconditional operator (↔) in propositional logic.
    """

    def __init__(self, left_operand, right_operand):
        """
        Initialize the BICONDITIONAL operation with two propositions.

        :param left_operand: first propositional formula
        :type left_operand: bool or Symbol or LogicOperation
        :param right_operand: second propositional formula
        :type right_operand: bool or Symbol or LogicOperation
        """
        self.left_operand = left_operand
        self.right_operand = right_operand

    def evaluate(self, model=None):
        """
        Returns the biconditional of two propositional formulas.
        True when both operands have the same truth value.

        :param model: dictionary mapping symbols to truth values
        :type model: dict or None
        :return: biconditional left_operand ↔ right_operand
        :rtype: bool
        """
        # Get left operand value
        if hasattr(self.left_operand, 'evaluate'):
            left_val = self.left_operand.evaluate(model)
        else:
            left_val = self.left_operand

        # Get right operand value
        if hasattr(self.right_operand, 'evaluate'):
            right_val = self.right_operand.evaluate(model)
        else:
            right_val = self.right_operand

        return left_val == right_val  # True when both have same truth value

    def __str__(self):
        return f"({self.left_operand} ↔ {self.right_operand})"


class Xor:
    """
    This class implements the logical XOR operation (exclusive or).
    Represents the exclusive or operator (⊕) in propositional logic.
    """

    def __init__(self, left_operand, right_operand):
        """
        Initialize the XOR operation with two propositions.

        :param left_operand: first propositional formula
        :type left_operand: bool or Symbol or LogicOperation
        :param right_operand: second propositional formula
        :type right_operand: bool or Symbol or LogicOperation
        """
        self.left_operand = left_operand
        self.right_operand = right_operand

    def evaluate(self, model=None):
        """
        Returns the exclusive or of two propositional formulas.
        True when exactly one operand is true, but not both.

        :param model: dictionary mapping symbols to truth values
        :type model: dict or None
        :return: exclusive or of left_operand ⊕ right_operand
        :rtype: bool
        """
        # Get left operand value
        if hasattr(self.left_operand, 'evaluate'):
            left_val = self.left_operand.evaluate(model)
        else:
            left_val = self.left_operand

        # Get right operand value
        if hasattr(self.right_operand, 'evaluate'):
            right_val = self.right_operand.evaluate(model)
        else:
            right_val = self.right_operand

        return left_val != right_val  # XOR: true when values differ


class Symbol:
    """
    Represents a propositional symbol (atomic proposition).
    """

    def __init__(self, name):
        """
        Initialize a propositional symbol.

        :param name: the name of the symbol
        :type name: str
        """
        self.name = name

    def evaluate(self, model):
        """
        Evaluate the symbol using the given model.

        :param model: dictionary mapping symbol names to truth values
        :type model: dict
        :return: truth value of this symbol in the model
        :rtype: bool
        """
        if model is None or self.name not in model:
            raise ValueError(f"Symbol '{self.name}' not found in model")
        return model[self.name]

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


# Dictionary for easy access to logic operations
logic_operations = {
    "¬": Not,
    "not": Not,
    "∧": And,
    "and": And,
    "∨": Or,
    "v": Or,
    "or": Or,
    "→": Implies,
    "implies": Implies,
    "↔": Biconditional,
    "iff": Biconditional,
    "⊕": Xor,
    "xor": Xor
}


def main():
    print("=== Propositional Logic Operations Demo ===")

    p = Symbol("P")
    q = Symbol("Q")
    model = {"P": True, "Q": False}

    not_op = Not(p)
    print(f"¬P = {not_op.evaluate(model)}")

    and_op = And(p, q)
    print(f"P ∧ Q = {and_op.evaluate(model)}")


    or_op = Or(p, q)
    print(f"P ∨ Q = {or_op.evaluate(model)}")

    implies_op = Implies(p, q)
    print(f"P → Q = {implies_op.evaluate(model)}")


    biconditional_op = Biconditional(p, q)
    print(f"P ↔ Q = {biconditional_op.evaluate(model)}")

    xor_op = Xor(p, q)
    print(f"P ⊕ Q = {xor_op.evaluate(model)}")

    complex_formula = Implies(And(p, q), Or(p, q))
    print(f"(P ∧ Q) → (P ∨ Q) = {complex_formula.evaluate(model)}")

    print(f"\nFormula representation: {complex_formula}")


if __name__ == "__main__":
    main()

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
        for combination in product([True, False], repeat=len(self.propositions)):
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
                "¬": Not,
                "∧": And,
                "∨": Or,
                "v": Or,
                "→": Implies,
                "↔": Biconditional,
                "⊕": Xor
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
            "¬": Not,
            "∧": And,
            "∨": Or,
            "v": Or,
            "→": Implies,
            "↔": Biconditional,
            "⊕": Xor
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