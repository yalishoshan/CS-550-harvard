from ..propositional_logic import Symbol, And, Or  # Import Symbol and And and Or classes


class DeMorgansLaw:
    """Implements the De Morgan's Law inference rule."""

    def __init__(self, a, b):
        """
        Initialize DeMorgansLaw with two symbols 'a' and 'b'.
        """
        self.a = Symbol(a)  # Create Symbol object for 'a'
        self.b = Symbol(b)  # Create Symbol object for 'b'

    def apply(self, model):
        """
        Apply the De Morgan's Law rule on the given model.

        :param model: A dictionary representing the truth values of symbols,
        :type model: dict
        :return: A string representing the result of applying the inference rule
        :rtype: str
        """

        if not (And(self.a, self.b)).evaluate(model):
            return f"{self.a} is False OR {self.b} is False (by De Morgan's Law)"  # If true, conclude one of a or b is false

        else:
            return f"cant conclude {self.a} is false or {self.b} is false as a fact (by De Morgan's Law)"  # Otherwise, cannot conclude one of a or b is false

    def reverse_apply(self, model):
        """
        Apply the De Morgan's Law rule on the given model.

        :param model: A dictionary representing the truth values of symbols,
        :type model: dict
        :return: A string representing the result of applying the inference rule
        :rtype: str
        """

        if not (Or(self.a, self.b)).evaluate(model):
            return f"{self.a}  And {self.b} is false (by De Morgan's Law)"  # If true, conclude a and b is false

        else:
            return f"cant conclude {self.a}  AND {self.b} is False (by De Morgan's Law)"  # Otherwise, cannot conclude a and b is false

def main():
    inference = DeMorgansLaw("A", "B")
    model = {"A": True, "B": True}
    print(inference.apply(model))

if __name__ == "__main__":
    main()
