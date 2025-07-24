from ..propositional_logic import Symbol, Not  # Import Symbol and Not classes

class DoubleNegationElimination:
    """A class to apply the double negation elimination inference rule."""

    def __init__(self, a, b):
        """
        Initialize DoubleNegationElimination with two symbols A and B.
        """
        self.a = Symbol(a)  # Create Symbol object for premise A
        self.b = Symbol(b)  # Create Symbol object for conclusion B

    def apply(self, model):
        """
        Apply the Double Negation Elimination rule on the given model.

        :param model: A dictionary representing the truth values of symbols,
        :type model: dict
        :return: A dictionary representing the truth values of symbols after applying the rule,
        :rtype: dict

        """

        if not Not(self.a).evaluate(model):  # Check if ¬A is false (i.e., A is true)
            return f"{self.b} is True (by Double Negation Elimination)"  # Then B is true

def main():
    dne = DoubleNegationElimination("A", "B")
    model = {"A": True, "B": True}
    print(dne.apply(model))

if __name__ == "__main__":
    main()
