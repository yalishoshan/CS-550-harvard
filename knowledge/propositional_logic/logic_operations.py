class Symbol:
    """Represents a propositional symbol (atomic proposition)."""

    def __init__(self, name):
        """
        Initialize a propositional symbol.

        :param name: the name of the symbol
        :type name: str
        """
        self.name = name  # Store symbol name

    def evaluate(self, model):
        """
        Evaluate the symbol using the given model.

        :param model: dictionary mapping symbol names to truth values
        :type model: dict
        :return: truth value of this symbol in the model
        :rtype: bool
        :raises ValueError: if symbol not found in model
        """
        if model is None or self.name not in model:  # Validate model contains symbol
            raise ValueError(f"Symbol '{self.name}' not found in model")
        return model[self.name]  # Return symbol's truth value

    def __str__(self):
        """
        String representation of the symbol.

        :return: symbol name
        :rtype: str
        """
        return self.name  # Return symbol name

    def __eq__(self, other):
        """
        Check equality between symbols.

        :param other: object to compare
        :type other: any
        :return: True if symbols have same name
        :rtype: bool
        """
        return isinstance(other, Symbol) and self.name == other.name  # Compare names

    def __hash__(self):
        """
        Generate hash for symbol (for use in sets/dicts).

        :return: hash of symbol name
        :rtype: int
        """
        return hash(self.name)  # Hash based on name

    def __repr__(self):
        return self.name  # Print the symbol's name


class Not:
    """Logical NOT operation (¬)."""

    def __init__(self, operand):
        """
        Initialize NOT operation.

        :param operand: proposition to negate
        :type operand: Symbol or logical operation
        """
        self.operand = operand  # Store operand

    def evaluate(self, model=None):
        """
        Evaluate the negation.

        :param model: truth value assignment
        :type model: dict or None
        :return: negated truth value
        :rtype: bool
        """
        if isinstance(self.operand, Symbol):  # Handle Symbol operand
            return not self.operand.evaluate(model)
        elif hasattr(self.operand, 'evaluate'):  # Handle logical operation
            return not self.operand.evaluate(model)
        return not self.operand  # Handle boolean operand

    def __str__(self):
        """
        String representation of NOT operation.

        :return: formatted string
        :rtype: str
        """
        return f"¬{self.operand}"  # Format with negation symbol


class And:
    """Logical AND operation (∧)."""

    def __init__(self, *operands):
        """
        Initialize AND operation.

        :param operands: propositions to conjoin
        :type operands: Symbol or logical operation
        :raises ValueError: if less than 2 operands
        """
        if len(operands) < 2:  # Validate minimum operands
            raise ValueError("AND requires at least 2 operands")
        self.operands = operands  # Store all operands

    def evaluate(self, model=None):
        """
        Evaluate the conjunction.

        :param model: truth value assignment
        :type model: dict or None
        :return: True if all operands are True
        :rtype: bool
        """
        for operand in self.operands:  # Check each operand
            if isinstance(operand, Symbol):  # Handle Symbol
                if not operand.evaluate(model):
                    return False
            elif hasattr(operand, 'evaluate'):  # Handle logical operation
                if not operand.evaluate(model):
                    return False
            elif not operand:  # Handle boolean
                return False
        return True  # All operands are True

    def __str__(self):
        """
        String representation of AND operation.

        :return: formatted string with ∧
        :rtype: str
        """
        return f"({' ∧ '.join(str(op) for op in self.operands)})"  # Join with ∧


class Or:
    """Logical OR operation (∨)."""

    def __init__(self, *operands):
        """
        Initialize OR operation.

        :param operands: propositions to disjoin
        :type operands: Symbol or logical operation
        :raises ValueError: if less than 2 operands
        """
        if len(operands) < 2:  # Validate minimum operands
            raise ValueError("OR requires at least 2 operands")
        self.operands = operands  # Store all operands

    def evaluate(self, model=None):
        """
        Evaluate the disjunction.

        :param model: truth value assignment
        :type model: dict or None
        :return: True if any operand is True
        :rtype: bool
        """
        for operand in self.operands:  # Check each operand
            if isinstance(operand, Symbol):  # Handle Symbol
                if operand.evaluate(model):
                    return True
            elif hasattr(operand, 'evaluate'):  # Handle logical operation
                if operand.evaluate(model):
                    return True
            elif operand:  # Handle boolean
                return True
        return False  # All operands are False

    def __str__(self):
        """
        String representation of OR operation.

        :return: formatted string with ∨
        :rtype: str
        """
        return f"({' ∨ '.join(str(op) for op in self.operands)})"  # Join with ∨


class Implies:
    """Logical IMPLIES operation (→)."""

    def __init__(self, antecedent, consequent):
        """
        Initialize implication.

        :param antecedent: the "if" part
        :type antecedent: Symbol or logical operation
        :param consequent: the "then" part
        :type consequent: Symbol or logical operation
        """
        self.antecedent = antecedent  # Store antecedent
        self.consequent = consequent  # Store consequent

    def evaluate(self, model=None):
        """
        Evaluate the implication using p → q ≡ ¬p ∨ q.

        :param model: truth value assignment
        :type model: dict or None
        :return: implication result
        :rtype: bool
        """
        ant_val = self._get_value(self.antecedent, model)  # Get antecedent value
        cons_val = self._get_value(self.consequent, model)  # Get consequent value
        return not ant_val or cons_val  # Apply implication formula

    def _get_value(self, operand, model):
        """
        Helper to get truth value of operand.

        :param operand: operand to evaluate
        :param model: truth value assignment
        :return: truth value
        :rtype: bool
        """
        if isinstance(operand, Symbol):  # Handle Symbol
            return operand.evaluate(model)
        elif hasattr(operand, 'evaluate'):  # Handle logical operation
            return operand.evaluate(model)
        return operand  # Handle boolean

    def __str__(self):
        """
        String representation of implication.

        :return: formatted string with →
        :rtype: str
        """
        return f"({self.antecedent} → {self.consequent})"  # Format with arrow


class Biconditional:
    """Logical BICONDITIONAL operation (↔)."""

    def __init__(self, left, right):
        """
        Initialize biconditional.

        :param left: first proposition
        :type left: Symbol or logical operation
        :param right: second proposition
        :type right: Symbol or logical operation
        """
        self.left = left  # Store left operand
        self.right = right  # Store right operand

    def evaluate(self, model=None):
        """
        Evaluate biconditional (true when both have same value).

        :param model: truth value assignment
        :type model: dict or None
        :return: True if both operands have same truth value
        :rtype: bool
        """
        left_val = self._get_value(self.left, model)  # Get left value
        right_val = self._get_value(self.right, model)  # Get right value
        return left_val == right_val  # True when equal

    def _get_value(self, operand, model):
        """
        Helper to get truth value of operand.

        :param operand: operand to evaluate
        :param model: truth value assignment
        :return: truth value
        :rtype: bool
        """
        if isinstance(operand, Symbol):  # Handle Symbol
            return operand.evaluate(model)
        elif hasattr(operand, 'evaluate'):  # Handle logical operation
            return operand.evaluate(model)
        return operand  # Handle boolean

    def __str__(self):
        """
        String representation of biconditional.

        :return: formatted string with ↔
        :rtype: str
        """
        return f"({self.left} ↔ {self.right})"  # Format with double arrow