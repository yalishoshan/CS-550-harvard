from ..propositional_logic import Symbol, And, Or, Not  # Import Symbol and And and Or and Not classes


class DeMorgansLaw:
    """Implements the De Morgan's Law inference rule."""

    def __init__(self, symbol_name):
        """
        Initialize DeMorgansLaw with a symbol.

        """

        self.symbol_name = Symbol(symbol_name)  # Create Symbol

    def apply(self, kb):
        """
        Apply the De Morgan's Law rule on the given kb.

        :param kb: knowledge base
        :type kb: lst
        :return: not A and  B
        :rtype: lst
        """

        for statement in kb: # Check if the statement is both not and and
            if isinstance(statement, Not) and isinstance(statement.operand, And) and statement.operand.operand == self.symbol_name: # Check if the statement is both not and and
                return [Or(Not(statement.operand.operands[0]), Not(statement.operand.operands[1]))] # Return not A and not B

        return [] # else return an empty list




    def reverse_apply(self, kb):
        """
        Apply the reverse of De Morgan's Law rule on the given kb.

        :param kb: knowledge base
        :type kb: lst
        :return: not A or not B
        :rtype: lst
        """

        for statement in kb:  # Check if the statement is both not and and
            if isinstance(statement, Not) and isinstance(statement.operand,
                                                       Or) and statement.operand.operand == self.symbol_name:  # Check if the statement is both not and and
                return [Or(Not(statement.operand.operands[0]),
                           Not(statement.operand.operands[1]))]  # Return not A and not B

        return []  # else return an empty list


def main():
    dml = DeMorgansLaw("A")
    kb = [Not(And(Symbol("A"), Symbol("B")))]
    print(dml.apply(kb))

if __name__ == "__main__":
    main()
