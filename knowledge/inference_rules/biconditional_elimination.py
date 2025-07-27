from ..propositional_logic import Symbol, Biconditional, And, Implies  # Import Symbol and biconditional, implies classes


class BiconditionalElimination:
    """Implements the Biconditional Elimination inference rule."""

    def __init__(self, biconditional):
        """
        Initialize BiconditionalElimination with the given biconditional.

        """
        self.biconditional = biconditional

    def apply(self, kb):
        """
        Apply the Biconditional Elimination rule on the given kb.

        :param kb: knowledge base
        :type kb: lst
        :return: an implies b and b implies a
        :rtype: lst

        """

        if self.biconditional in kb:  # Check if the biconditional is true
            if isinstance(self.biconditional, Biconditional):  # Check if biconditional is true
                return [And(Implies(self.biconditional.left, self.biconditional.right), Implies(self.biconditional.left, self.biconditional.right))]  # Return A implies B and B implies A

        return []  # Otherwise, return an empty list



def main():
    be = BiconditionalElimination(Biconditional(Symbol("A"), Symbol("B")))
    kb = [Biconditional(Symbol("A"), Symbol("B"))]
    print(be.apply(kb))

if __name__ == '__main__':
    main()