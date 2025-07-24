from ..propositional_logic import Symbol, And  # Import Symbol and And classes

class AndElimination:
    """Implements the And Elimination inference rule."""

    def __init__(self, a, b):
        """
        Initialize AndElimination with two symbols 'a' and 'b'."""

        self.a = Symbol(a)  # Create Symbol object for 'a'
        self.b = Symbol(b)  # Create Symbol object for 'b'

    def apply(self, model):
        """
        Apply the And Elimination rule on the given model.

        :param model: A dictionary representing the truth values of symbols,
        :type model: dict
        :return: A string representing the result of applying the inference rule,
        :rtype: str

        """

        if And(self.a, self.b).evaluate(model):  # Evaluate if (a ∧ b) is true in the given model
            return f"{self.a} is True (by And Elimination)"  # If true, conclude a is true

        else:
            return f"Cannot conclude {self.a} is True"  # Otherwise, cannot conclude a is true

def main():
    inference = AndElimination("A", "B")
    model = {"A": True, "B": True}
    print(inference.apply(model))

if __name__ == "__main__":
    main()