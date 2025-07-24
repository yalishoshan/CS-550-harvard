from ..propositional_logic import Symbol, And, Or  # Import Symbol and And and Or classes


class DistributiveProperty:
    """Implements the Distributive Property inference rule."""

    def __init__(self, a, b, c):
        """
        Initialize DistributiveProperty with two symbols 'a' and 'b'.
        """
        self.a = Symbol(a)  # Create Symbol object for 'a'
        self.b = Symbol(b)  # Create Symbol object for 'b'
        self.c = Symbol(c)  # Create Symbol object for 'c'

    def apply(self, model):
        """
        Apply the Distributive Property rule on the given model.

        :param model: A dictionary representing the truth values of symbols,
        :type model: dict
        :return: A string representing the result of applying the inference rule
        :rtype: str
        """

        if And(self.a, Or(self.b, self.c)).evaluate(model):
            return f"{self.a} and {self.b} or {self.a} and {self.c} (by Distributive Property)"  # If true, conclude that one of the and combinations is true

        else:
            return f"cant conclude that {self.a} and {self.b} or {self.a} and {self.c} (by Distributive Property)"  # If false, we can't conclude that one of the and combinations is true

    def reverse_apply(self, model):
        """
        Apply the Distributive Property rule on the given model.

        :param model: A dictionary representing the truth values of symbols,
        :type model: dict
        :return: A string representing the result of applying the inference rule
        :rtype: str
        """

        if Or(self.a, And(self.b, self.c)).evaluate(model):
            return f"{self.a} or {self.b} and {self.a} or {self.c} (by Distributive Property)"  # If true, conclude that both or combinations are true

        else:
            return f"cant conclude that {self.a} or {self.b} and {self.a} or {self.c} (by Distributive Property)"  # If false, we can't conclude that both ot combinations are true




def main():
    inference = DistributiveProperty("A", "B", "C")
    model = {"A": True, "B": True}
    print(inference.apply(model))


if __name__ == "__main__":
    main()
