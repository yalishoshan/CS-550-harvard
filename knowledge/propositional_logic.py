class LogicNot:
    """
    This class implements the logical NOT operation (negation).
    Represents the negation operator (¬) in propositional logic.
    """

    def __init__(self, operand):
        """
        Initialize the NOT operation with one proposition.

        :param operand: the proposition to negate
        :type operand: bool
        """
        self.operand = operand  # Store the proposition value to negate

    def evaluate(self):
        """
        Returns the negation of the propositional formula.

        :return: negation of the operand (¬operand)
        :rtype: bool
        """
        return not self.operand  # Return logical NOT of the operand


class LogicAnd:
    """
    This class implements the logical AND operation (conjunction).
    Represents the conjunction operator (∧) in propositional logic.
    """

    def __init__(self, left_operand, right_operand):
        """
        Initialize the AND operation with two propositions.

        :param left_operand: first propositional formula value
        :type left_operand: bool
        :param right_operand: second propositional formula value
        :type right_operand: bool
        """
        self.left_operand = left_operand  # Store first proposition
        self.right_operand = right_operand  # Store second proposition

    def evaluate(self):
        """
        Returns the conjunction of two propositional formulas.

        :return: conjunction of left_operand and right_operand (left ∧ right)
        :rtype: bool
        """
        return self.left_operand and self.right_operand  # Return logical AND


class LogicOr:
    """
    This class implements the logical OR operation (disjunction).
    Represents the disjunction operator (∨) in propositional logic.
    """

    def __init__(self, left_operand, right_operand, third_operand=None):
        """
        Initialize the OR operation with two propositions.

        :param left_operand: first propositional formula value
        :type left_operand: bool
        :param right_operand: second propositional formula value
        :type right_operand: bool
        :param third_operand: optional third propositional formula value
        :type third_operand: bool or None
        """
        self.left_operand = left_operand  # Store first proposition
        self.right_operand = right_operand  # Store second proposition
        self.third_operand = third_operand  # Store optional third proposition

    def evaluate(self):
        """
        Returns the disjunction of propositional formulas.

        :return: disjunction of operands (left ∨ right ∨ third)
        :rtype: bool
        """
        if self.third_operand is not None:
            return self.left_operand or self.right_operand or self.third_operand  # Return logical OR with three operands
        return self.left_operand or self.right_operand  # Return logical OR with two operands


class LogicImplies:
    """
    This class implements the logical IMPLIES operation (implication).
    Represents the implication operator (→) in propositional logic.
    """

    def __init__(self, antecedent, consequent):
        """
        Initialize the IMPLIES operation with two propositions.

        :param antecedent: the "if" part of the implication
        :type antecedent: bool
        :param consequent: the "then" part of the implication
        :type consequent: bool
        """
        self.antecedent = antecedent  # Store the "if" part
        self.consequent = consequent  # Store the "then" part

    def evaluate(self):
        """
        Returns the implication of two propositional formulas.
        Uses the logical equivalence: p → q ≡ ¬p ∨ q

        :return: implication antecedent → consequent
        :rtype: bool
        """
        return not self.antecedent or self.consequent  # p → q is equivalent to ¬p ∨ q


class LogicBiconditional:
    """
    This class implements the logical BICONDITIONAL operation (if and only if).
    Represents the biconditional operator (↔) in propositional logic.
    """

    def __init__(self, left_operand, right_operand):
        """
        Initialize the BICONDITIONAL operation with two propositions.

        :param left_operand: first propositional formula value
        :type left_operand: bool
        :param right_operand: second propositional formula value
        :type right_operand: bool
        """
        self.left_operand = left_operand  # Store first proposition
        self.right_operand = right_operand  # Store second proposition

    def evaluate(self):
        """
        Returns the biconditional of two propositional formulas.
        True when both operands have the same truth value.

        :return: biconditional left_operand ↔ right_operand
        :rtype: bool
        """
        return self.left_operand == self.right_operand  # True when both have same truth value


class LogicXor:
    """
    This class implements the logical XOR operation (exclusive or).
    Represents the exclusive or operator (⊕) in propositional logic.
    """

    def __init__(self, left_operand, right_operand):
        """
        Initialize the XOR operation with two propositions.

        :param left_operand: first propositional formula value
        :type left_operand: bool
        :param right_operand: second propositional formula value
        :type right_operand: bool
        """
        self.left_operand = left_operand  # Store first proposition
        self.right_operand = right_operand  # Store second proposition

    def evaluate(self):
        """
        Returns the exclusive or of two propositional formulas.
        True when exactly one operand is true, but not both.

        :return: exclusive or of left_operand ⊕ right_operand
        :rtype: bool
        """
        return (self.left_operand or self.right_operand) and not (self.left_operand and self.right_operand)  # XOR logic


# Dictionary for easy access to logic operations
logic_operations = {
    "¬": LogicNot,
    "not": LogicNot,
    "∧": LogicAnd,
    "and": LogicAnd,
    "∨": LogicOr,
    "v": LogicOr,  # Your requested v symbol
    "or": LogicOr,
    "→": LogicImplies,
    "implies": LogicImplies,
    "↔": LogicBiconditional,
    "iff": LogicBiconditional,
    "⊕": LogicXor,
    "xor": LogicXor
}


def main():
    """
    Demonstrates usage of all logic operation classes.
    """
    print("=== Propositional Logic Operations Demo ===")

    # Test NOT operation
    not_op = LogicNot(True)
    print(f"NOT True = {not_op.evaluate()}")  # False

    # Test AND operation
    and_op = LogicAnd(True, False)
    print(f"True AND False = {and_op.evaluate()}")  # False

    # Test OR operation
    or_op = LogicOr(True, False)
    print(f"True OR False = {or_op.evaluate()}")  # True

    # Test IMPLIES operation
    implies_op = LogicImplies(True, False)
    print(f"True → False = {implies_op.evaluate()}")  # False

    # Test BICONDITIONAL operation
    biconditional_op = LogicBiconditional(True, True)
    print(f"True ↔ True = {biconditional_op.evaluate()}")  # True

    # Test XOR operation
    xor_op = LogicXor(True, False)
    print(f"True ⊕ False = {xor_op.evaluate()}")  # True

    # Demo using the dictionary
    print("\n=== Using Logic Operations Dictionary ===")
    v = logic_operations["v"]  # Get OR operation
    and_op = logic_operations["∧"]  # Get AND operation

    # Create some logical formulas
    formula1 = v(True, False)  # True v False
    formula2 = and_op(True, False)  # True ∧ False

    print(f"True v False = {formula1.evaluate()}")  # True
    print(f"True ∧ False = {formula2.evaluate()}")  # False


if __name__ == "__main__":
    main()