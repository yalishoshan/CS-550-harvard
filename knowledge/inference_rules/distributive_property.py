from ..propositional_logic import Symbol, And, Or  # Import Symbol and And and Or classes


class DistributiveProperty:
    """Implements the Distributive Property inference rule."""

    def __init__(self, symbol_a, symbol_b):
        """
        Initialize DistributiveProperty with two symbols 'a' and 'b'.
        """

        self.symbol_a = Symbol(symbol_a)  # Create Symbol object for premise A
        self.symbol_b = Symbol(symbol_b)  # Create Symbol object for premise B


    def apply(self, kb):
        """
        Apply the Distributive Property rule on the given kb.

        :param kb: knowledge base
        :type kb: lst
        :return: a and b or a and c
        :rtype: lst
        """

        for statement in kb: # Check if the statement is an And
            if isinstance(statement, And) and len(statement.operands) == 2:  # Check if the statement is an And
                first = statement.operands[0]  # First symbol
                second = statement.operands[1]  # Second symbol

                # Check: A ∧ (B ∨ C) pattern
                if (first == self.symbol_a and isinstance(second, Or) and
                        len(second.operands) == 2 and second.operands[0] == self.symbol_b):  # Check if the statement is a Or (b and c)
                    c = second.operands[1]  # Third symbol can be anything
                    return [Or(And(self.symbol_a, self.symbol_b),
                               And(self.symbol_a, c))]  # Return a and b or a and c
        return []  # else return an empty list


    def reverse_apply(self, kb):
        """
        Apply the reverse of Distributive Property rule on the given kb.

        :param kb: knowledge base
        :type kb: lst
        :return: a or c and a or b
        :rtype: lst
        """


        for statement in kb: # Check if the statement is an And
            if isinstance(statement, And) and len(statement.operands) == 2:  # Check if the statement is an And
                first = statement.operands[0]  # First symbol
                second = statement.operands[1]  # Second symbol

                # Check: A ∧ (B ∨ C) pattern
                if (first == self.symbol_a and isinstance(second, Or) and
                        len(second.operands) == 2 and second.operands[0] == self.symbol_b):  # Check if the statement is a Or (b and c)
                    c = second.operands[1]  # Third symbol can be anything
                    return [And(Or(self.symbol_a, self.symbol_b),
                               Or(self.symbol_a, c))]  # Return a and b or a and c
        return []  # else return an empty list







def main():
    dp = DistributiveProperty("A", "B")
    print(dp.apply([And(Symbol("A"), Or(Symbol("B"), Symbol("C")))]))
    print(dp.reverse_apply([Or(Symbol("A"), And(Symbol("B"), Symbol("C")))]))



if __name__ == "__main__":
    main()
