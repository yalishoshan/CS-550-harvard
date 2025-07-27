from ..propositional_logic import Symbol, Not  # Import Symbol and Not classes

class DoubleNegationElimination:
    """A class to apply the double negation elimination inference rule."""

    def __init__(self, symbol_name):
        """
        Initialize DoubleNegationElimination with symbol.
        """
        self.symbol_name = Symbol(symbol_name)  # Create Symbol object

    def apply(self, kb):
        """
        Apply the Double Negation Elimination rule on the given kb.

        :param kb: knowledge base
        :type kb: lst
        :return: a\
        :rtype: lst

        """

        for statement in kb: # Check if the statement is a double negation
            if isinstance(statement, Not) and isinstance(statement.operand, Not) and statement.operand.operand == self.symbol_name: # Check if the statement is a double negation
                return [self.symbol_name] # Return the symbol

        return [] # else return an empty list

def main():
    dne = DoubleNegationElimination("A")
    a = Symbol("A")
    kb = [Not(Not(a))]
    print(f"Derived statements: { dne.apply(kb)}")

if __name__ == "__main__":
    main()
