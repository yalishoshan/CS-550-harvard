from biconditional_elimination import BiconditionalElimination
from implication_elimination import ImplicationElimination
from de_morgans_law import DeMorgansLaw
from distributive_property import DistributiveProperty
from ..propositional_logic import Symbol, Not, Or, Implies, Biconditional, And


class ConvToCNF:
    """Converts propositional logic statements to CNF using a target symbol."""

    def __init__(self, symbol_name):
        """
        Initialize CNF converter with a target symbol.

        :param symbol_name: name of symbol to use for conversions
        :type symbol_name: str
        """
        self.symbol_name = symbol_name  # Store symbol name for elimination classes

    def apply(self, kb):
        """
        Convert knowledge base to CNF by applying transformation rules.

        :param kb: knowledge base containing logical statements
        :type kb: list
        :return: knowledge base in CNF form
        :rtype: list
        """

        converted_statements = []  # Store all converted statements

        for statement in kb:  # Process each statement in knowledge base
            if isinstance(statement, Biconditional):  # Handle A ↔ B
                be = BiconditionalElimination(self.symbol_name)  # Use stored symbol
                converted_statements.extend(be.apply([statement]))  # Apply and collect results

            elif isinstance(statement, Implies):  # Handle A → B
                ie = ImplicationElimination(self.symbol_name, statement)  # Use stored symbol
                converted_statements.extend(ie.apply([statement]))  # Apply and collect results

            elif isinstance(statement, Not):  # Handle ¬(A ∧ B) or ¬(A ∨ B)
                dml = DeMorgansLaw(self.symbol_name)  # Use stored symbol
                converted_statements.extend(dml.apply([statement]))  # Apply and collect results

            elif isinstance(statement, Or):  # Handle A ∨ B
                dp = DistributiveProperty(self.symbol_name, statement)  # Use stored symbol
                converted_statements.extend(dp.apply([statement]))  # Apply and collect results

            else:  # Statement already in CNF form
                converted_statements.append(statement)  # Keep as-is

        return converted_statements  # Return all converted statements


def main():
    # Create CNF converter for symbol "A"
    cnf = ConvToCNF("A")

    # Test symbols
    a = Symbol("A")
    b = Symbol("B")

    print("=== Test Case 1: Biconditional A ↔ B ===")
    kb1 = [Biconditional(a, b)]
    result1 = cnf.apply(kb1)
    print(f"Input: {kb1}")
    print(f"Output: {result1}")
    print()

    print("=== Test Case 2: Implication A → B ===")
    kb2 = [Implies(a, b)]
    result2 = cnf.apply(kb2)
    print(f"Input: {kb2}")
    print(f"Output: {result2}")
    print()

    print("=== Test Case 3: De Morgan's ¬(A ∧ B) ===")
    kb3 = [Not(And(a, b))]
    result3 = cnf.apply(kb3)
    print(f"Input: {kb3}")
    print(f"Output: {result3}")
    print()

    print("=== Test Case 4: Mixed statements ===")
    kb4 = [
        Biconditional(a, b),  # A ↔ B
        Implies(a, b),  # A → B
        Not(And(a, b)),  # ¬(A ∧ B)
        Or(a, b)  # A ∨ B (already CNF)
    ]
    result4 = cnf.apply(kb4)
    print(f"Input: {kb4}")
    print(f"Output: {result4}")


if __name__ == "__main__":
    main()