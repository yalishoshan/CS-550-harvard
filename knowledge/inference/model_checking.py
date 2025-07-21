from itertools import product
from ..propositional_logic import Symbol, Not, And, Or, Implies, Biconditional


class ModelChecker:
    """Performs model checking for propositional logic."""

    def __init__(self, knowledge_base):
        """
        Initialize model checker with knowledge base.

        :param knowledge_base: list of logical formulas
        :type knowledge_base: list
        """
        self.knowledge_base = knowledge_base  # Store KB formulas

    def entails(self, query):
        """
        Check if KB ⊨ query using model checking algorithm.

        :param query: formula to check
        :type query: logical operation
        :return: True if KB entails query
        :rtype: bool
        """
        symbols = self._extract_symbols()  # Get all symbols from KB

        # Check all possible models
        for model in self._generate_models(symbols):  # Generate each model
            # If KB is true in this model
            if self._kb_true_in_model(model):  # KB satisfied
                # Query must also be true
                if not query.evaluate(model):  # Query false
                    return False  # Found counterexample

        return True  # Query true in all KB-satisfying models

    def _extract_symbols(self):
        """
        Extract all unique symbols from KB.

        :return: list of unique symbols
        :rtype: list[Symbol]
        """
        symbols = set()  # Use set for uniqueness

        def extract(formula):
            """Recursively extract symbols from formula."""
            if isinstance(formula, Symbol):  # Base case: Symbol
                symbols.add(formula)
            elif hasattr(formula, 'operands'):  # And, Or have operands
                for op in formula.operands:
                    extract(op)
            elif hasattr(formula, 'operand'):  # Not has operand
                extract(formula.operand)
            elif hasattr(formula, 'antecedent'):  # Implies has two parts
                extract(formula.antecedent)
                extract(formula.consequent)
            elif hasattr(formula, 'left'):  # Biconditional has two parts
                extract(formula.left)
                extract(formula.right)

        for statement in self.knowledge_base:  # Extract from each KB statement
            extract(statement)

        return list(symbols)  # Convert set to list

    def _generate_models(self, symbols):
        """
        Generate all possible truth assignments.

        :param symbols: list of symbols
        :type symbols: list[Symbol]
        :yield: model dictionary
        :rtype: dict
        """
        n = len(symbols)  # Number of symbols
        for values in product([True, False], repeat=n):  # All combinations
            model = {}  # Create new model
            for i, symbol in enumerate(symbols):  # Assign values
                model[symbol.name] = values[i]
            yield model  # Yield this model

    def _kb_true_in_model(self, model):
        """
        Check if all KB statements are true in model.

        :param model: truth assignment
        :type model: dict
        :return: True if KB satisfied
        :rtype: bool
        """
        for statement in self.knowledge_base:  # Check each statement
            if not statement.evaluate(model):  # Statement false
                return False
        return True  # All statements true