class Symbol:
    """Represents a propositional symbol (atomic proposition)."""

    def __init__(self, name):
        self.name = name

    def evaluate(self, model):
        if model is None or self.name not in model:
            raise ValueError(f"Symbol '{self.name}' not found in model")
        return model[self.name]

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Not:
    """Logical NOT operation (¬)."""

    def __init__(self, operand):
        self.operand = operand

    def evaluate(self, model=None):
        if isinstance(self.operand, Symbol):
            return not self.operand.evaluate(model)
        elif hasattr(self.operand, 'evaluate'):
            return not self.operand.evaluate(model)
        return not self.operand

    def __str__(self):
        return f"¬{self.operand}"


class And:
    """Logical AND operation (∧)."""

    def __init__(self, *operands):
        if len(operands) < 2:
            raise ValueError("AND requires at least 2 operands")
        self.operands = operands

    def evaluate(self, model=None):
        for operand in self.operands:
            if isinstance(operand, Symbol):
                if not operand.evaluate(model):
                    return False
            elif hasattr(operand, 'evaluate'):
                if not operand.evaluate(model):
                    return False
            elif not operand:
                return False
        return True

    def __str__(self):
        return f"({' ∧ '.join(str(op) for op in self.operands)})"


class Or:
    """Logical OR operation (∨)."""

    def __init__(self, *operands):
        if len(operands) < 2:
            raise ValueError("OR requires at least 2 operands")
        self.operands = operands

    def evaluate(self, model=None):
        for operand in self.operands:
            if isinstance(operand, Symbol):
                if operand.evaluate(model):
                    return True
            elif hasattr(operand, 'evaluate'):
                if operand.evaluate(model):
                    return True
            elif operand:
                return True
        return False

    def __str__(self):
        return f"({' ∨ '.join(str(op) for op in self.operands)})"


class Implies:
    """Logical IMPLIES operation (→)."""

    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

    def evaluate(self, model=None):
        # p → q ≡ ¬p ∨ q
        ant_val = self._get_value(self.antecedent, model)
        cons_val = self._get_value(self.consequent, model)
        return not ant_val or cons_val

    def _get_value(self, operand, model):
        if isinstance(operand, Symbol):
            return operand.evaluate(model)
        elif hasattr(operand, 'evaluate'):
            return operand.evaluate(model)
        return operand

    def __str__(self):
        return f"({self.antecedent} → {self.consequent})"


class Biconditional:
    """Logical BICONDITIONAL operation (↔)."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, model=None):
        left_val = self._get_value(self.left, model)
        right_val = self._get_value(self.right, model)
        return left_val == right_val

    def _get_value(self, operand, model):
        if isinstance(operand, Symbol):
            return operand.evaluate(model)
        elif hasattr(operand, 'evaluate'):
            return operand.evaluate(model)
        return operand

    def __str__(self):
        return f"({self.left} ↔ {self.right})"