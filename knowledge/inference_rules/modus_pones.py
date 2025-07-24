from ..propositional_logic import Symbol, Implies  # Import Symbol and Implies classes

class ModusPonens:
    """A class to apply the Modus Ponens inference rule."""

    def __init__(self, a, b):
        """
        Initialize ModusPonens with two symbols A and B.
        """

        self.a = Symbol(a)  # Create Symbol object for premise A
        self.b = Symbol(b)  # Create Symbol object for conclusion B

    def apply(self, model):
        """
        Apply the Modus Ponens rule on the given model.

        :param model: A dictionary representing the truth values of symbols,
        :type model: dict
        :return: A string indicating whether B is necessarily true
        :rtype: str

        """
        implication = Implies(self.a, self.b)  # Create implication A → B
        if self.a.evaluate(model) and implication.evaluate(model):  # Check if A is true AND A → B is true
            return f"{self.b} is True (by Modus Ponens)"  # If yes, conclude B is true

        else:
            return f"Cannot conclude {self.b} is True"  # Otherwise, cannot conclude B is true

def main():
    mp = ModusPonens("A", "B")
    model = {"A": True, "B": True}
    print(mp.apply(model))
if __name__ == "__main__":
    main()
