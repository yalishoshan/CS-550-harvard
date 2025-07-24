from ..propositional_logic import Symbol, Biconditional, And  # Import Symbol and biconditional classes


class BiconditionalElimination:
    """Implements the Biconditional Elimination inference rule."""

    def __init__(self, a, b):
        """
        Initialize BiconditionalElimination with two symbols 'a' and 'b'."""

        self.a = Symbol(a)  # Create Symbol object for 'a'
        self.b = Symbol(b)  # Create Symbol object for 'b'

    def apply(self, model):
        """
        Apply the Biconditional Elimination rule on the given model.

        :param model: A dictionary representing the truth values of symbols,
        :type model: dict
        :return: A string representing the result of applying the inference rule
        :rtype: str

        """

        if Biconditional(self.a, self.b).evaluate(model):  # Evaluate if (a ⇔ b) is true in the given model
            return f"{self.a} implies {self.b} AND {self.b} implies {self.a} is True (by Biconditional Elimination)"  # If true, conclude a implies b AND b implies a is true

        else:
            return f"Cannot conclude {self.a} implies {self.b} AND {self.b} implies {self.a} is True"  # Otherwise, cannot conclude a is true


def main():
    inference = BiconditionalElimination("A", "B")
    model = {"A": True, "B": True}
    print(inference.apply(model))

if __name__ == '__main__':
    main()