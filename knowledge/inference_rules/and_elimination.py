from ..propositional_logic import Symbol, And  # Import Symbol and And classes

class AndElimination:
    """Implements the And Elimination inference rule."""

    def __init__(self, and_formula):
        """
        Initialize AndElimination with and rule."""

        self.and_formula = and_formula  # get the And

    def apply(self, kb):
        """
        Apply the And Elimination rule on the given model.

        :param kb: knowledge base
        :type kb: lst
        :return: a or b
        :rtype: lst

        """

        if self.and_formula in kb:  # Check if the And is true
            if isinstance(self.and_formula, And):  # Check if and rulet
                return [self.and_formula.operands[0], self.and_formula.operands[1]]  # Return A and B

        return []  # Otherwise, return an empty list


def main():
    a = Symbol("A")
    b = Symbol("B")
    and_formula = And(a, b)

    kb = [and_formula, a, b]

    ae = AndElimination(and_formula)
    print(ae.apply(kb))
if __name__ == "__main__":
    main()