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

        :param operands: propositions to disjoin
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