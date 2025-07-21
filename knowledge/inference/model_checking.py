from itertools import product
from ..propositional_logic import Symbol, Not, And, Or, Implies, Biconditional


class ModelChecker:
    """Performs model checking for propositional logic."""

    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base  # List of logical formulas

    def entails(self, query):
        """Check if KB ⊨ query using model checking algorithm."""
        symbols = self._extract_symbols()

        # Check all possible models
        for model in self._generate_models(symbols):
            # If KB is true in this model
            if self._kb_true_in_model(model):
                # Query must also be true
                if not query.evaluate(model):
                    return False  # Found counterexample

        return True  # Query is true in all models where KB is true

    def _extract_symbols(self):
        """Extract all unique symbols from KB."""
        symbols = set()

        def extract(formula):
            if isinstance(formula, Symbol):
                symbols.add(formula)
            elif hasattr(formula, 'operands'):  # And, Or
                for op in formula.operands:
                    extract(op)
            elif hasattr(formula, 'operand'):  # Not
                extract(formula.operand)
            elif hasattr(formula, 'antecedent'):  # Implies
                extract(formula.antecedent)
                extract(formula.consequent)
            elif hasattr(formula, 'left'):  # Biconditional
                extract(formula.left)
                extract(formula.right)

        for statement in self.knowledge_base:
            extract(statement)

        return list(symbols)

    def _generate_models(self, symbols):
        """Generate all possible truth assignments."""
        n = len(symbols)
        for values in product([True, False], repeat=n):
            model = {}
            for i, symbol in enumerate(symbols):
                model[symbol.name] = values[i]
            yield model

    def _kb_true_in_model(self, model):
        """Check if all KB statements are true in model."""
        for statement in self.knowledge_base:
            if not statement.evaluate(model):
                return False
        return True