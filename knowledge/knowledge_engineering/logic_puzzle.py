from

class Symbol:
    """
    Represents a propositional symbol (atomic proposition).
    """

    def __init__(self, name):
        """
        Initialize a propositional symbol.

        :param name: the name of the symbol
        :type name: str
        """
        self.name = name

    def evaluate(self, model):
        """
        Evaluate the symbol using the given model.

        :param model: dictionary mapping symbol names to truth values
        :type model: dict
        :return: truth value of this symbol in the model
        :rtype: bool
        """
        if model is None or self.name not in model:
            raise ValueError(f"Symbol '{self.name}' not found in model")
        return model[self.name]

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

class LogicPuzzle:
    def __init__(self, people, houses):


        self.people = people
        self.house = houses

    def knowledge_add(self):
