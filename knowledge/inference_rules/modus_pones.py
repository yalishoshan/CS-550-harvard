from ..propositional_logic import Symbol, Implies  # Import Symbol class and Implies class
class ModusPones:
    """A class to apply the Modus Pones inference rule."""

    def __init__(self, a, implication):
        """
        Initialize ModusPones with symbol a and implication.
        """

        self.a = Symbol(a)  # Create Symbol object for premise A
        self.implication = implication  # get the implication
    def apply(self, kb):
        """
        Apply the Modus Pones rule on the given model.

        :param kb: A knowledge base
        :type kb: list
        :return: b
        :rtype: list

        """
        if self.a in kb:  # Check if A is true
            if isinstance(self.implication, Implies) and self.implication.antecedent == self.a:  # Check if implication is true and A is antecedent
                return [self.implication.consequent]  # Return B

        return []  # Otherwise, return an empty list

def main():
    a = Symbol("A")
    b = Symbol("B")
    implication = Implies(a, b)


    kb = [a, implication]

    mp = ModusPones("A", implication)
    print(mp.apply(kb))
if __name__ == "__main__":
    main()
