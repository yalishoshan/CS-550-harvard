from ..propositional_logic import Symbol, Implies, Or, Not  # Import Symbol and Implies classes

class ImplicationElimination:
    """A class to apply the Implication Elimination inference rule."""

    def __init__(self, a, implication):
        """
        Initialize ImplicationElimination with symbol a and implication .
        """

        self.a = Symbol(a)  # Create Symbol object for premise A
        self.implication = implication  # get the implication

    def apply(self, kb):
        """
        Apply the Implication Elimination rule on the given kb.

        :param kb: knowledge base
        :type kb: lst
        :return: b or not a
        :rtype: lst

        """

        if self.a in kb:  # Check if A is true
            if isinstance(self.implication,
                          Implies) and self.implication.antecedent == self.a:  # Check if implication is true and A is antecedent
                return [Or(self.implication.consequent, Not(self.a))]  # Return not A or B

        return []  # Otherwise, return an empty list


def main():
    a = Symbol("A")
    b = Symbol("B")
    implication = Implies(a, b)
    kb = [a]
    ie = ImplicationElimination("A", implication)


if __name__ == "__main__":
    main()
