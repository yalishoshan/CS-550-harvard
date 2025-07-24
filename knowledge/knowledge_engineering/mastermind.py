# Import the ModelChecker class for performing propositional model checking
from ..inference.model_checking import ModelChecker

# Import logical operators and Symbol class used to define logical formulas
from ..propositional_logic import Symbol, Not, Or, Implies


class MasterMind:
    """
    Represents a logical reasoning engine for a MasterMind-style deduction puzzle.
    Each color represents a person, and the goal is to determine their correct house
    assignments based on logical constraints.
    """

    def __init__(self, colors):
        """
        Initialize the MasterMind puzzle with a list of colors.

        Args:
            colors (list of str): List of person identifiers (e.g., "red", "blue", etc.)
        """
        self.colors = colors  # Store the input list of person identifiers
        self.knowledge_base = []  # Initialize the list that will hold logical statements (rules/constraints)
        self.symbols = []  # List of all propositional logic symbols used

    def symbol_add(self):
        """
        Create propositional symbols for each person (color) at each house index (0-3).
        Each symbol represents the proposition: "color is at position i".
        """
        for color in self.colors:  # Loop over all colors
            for i in range(4):  # Loop over 4 house indices (0–3)
                self.symbols.append(Symbol(f"{color}{i}"))  # Add symbol like "red0", "red1", ...

    def knowledge_add(self):
        """
        Add constraints to the knowledge base stating that each person (color) must
        belong to one of the four houses.
        """
        for color in self.colors:  # Loop over all people
            self.knowledge_base.append(Or(  # Add a disjunction (OR) of the possible house assignments
                Symbol(f"{color}Gryffindor"),  # Example: redGryffindor
                Symbol(f"{color}Hufflepuff"),
                Symbol(f"{color}Ravenclaw"),
                Symbol(f"{color}Slytherin")
            ))

    def only_one_person(self):
        """
        Add constraints to ensure each person (color) can only belong to one house index.
        If they are in one index, they cannot be in any of the others.
        """
        for color in self.colors:  # Loop over all people
            for i in range(4):  # For each possible index
                for j in range(4):  # Compare it with every other index
                    if i != j:  # Only consider different indices
                        self.knowledge_base.append(  # Add implication: if in i => not in j
                            Implies(Symbol(f"{color}{i}"), Not(Symbol(f"{color}{j}")))
                        )

    def only_one_house(self):
        """
        Add constraints to ensure each house index can be occupied by only one person (color).
        No two different people can occupy the same house index.
        """
        for i in range(4):  # For each index (position)
            for c1 in self.colors:  # First color
                for c2 in self.colors:  # Second color
                    if c1 != c2:  # Only compare different people
                        self.knowledge_base.append(  # If c1 is at i => c2 is not at i
                            Implies(Symbol(f"{c1}{i}"), Not(Symbol(f"{c2}{i}")))
                        )

    def check_knowledge(self):
        """
        Use model checking to evaluate which symbols are entailed (i.e., guaranteed true)
        based on the current knowledge base.
        """
        for symbol in self.symbols:  # Loop over all symbols created earlier
            checker = ModelChecker(self.knowledge_base)  # Create a model checker with current knowledge
            if checker.entails(symbol):  # Check if the symbol is logically entailed
                return print(f"{symbol} is True")  # Print any entailed (definitely true) symbol
