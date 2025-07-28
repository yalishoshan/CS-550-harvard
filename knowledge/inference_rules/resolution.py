from ..propositional_logic import Symbol, Not, Or  # Import Symbol class, Not class and Or class


class Resolution:
    """Implements the Unit Resolution inference rule for propositional logic."""

    def __init__(self, symbol_name):
        """
        Initialize Resolution with a symbol.

        """

        self.symbol_name = Symbol(symbol_name)  # Create Symbol object from string name

    def unit_resolution(self, kb):
        """
        This method implements the unit resolution inference rule: P ∨ Q^n, ¬P ⊢ Q^n

        :param kb: knowledge base containing logical statements
        :type kb: list
        :return: derived conclusion
        :rtype: list
        """

        # Step 1: Look for the disjunction (P ∨ Q)
        findings = []  # Initialize empty list to store found statements
        for statement in kb:  # Iterate through each statement in knowledge base
            if isinstance(statement,
                          Or) and self.symbol_name in statement.operands:  # Check if statement is Or and contains our symbol
                findings.append(statement)  # Add the disjunction to findings list
                break  # Exit loop once disjunction is found

        # Step 2: Look for the negation (¬P)
        for statement in kb:  # Iterate through knowledge base again
            if isinstance(statement,
                          Not) and statement.operand == self.symbol_name:  # Check if statement is negation of our symbol
                findings.append(True)  # Add True to indicate negation was found
                break  # Exit loop once negation is found

        # Step 3 Alternative: Return each remaining operand separately
        if len(findings) == 2:
            remaining_operands = []
            for operand in findings[0].operands:
                if operand != self.symbol_name:
                    remaining_operands.append(operand)

            # Smart return based on count
            if len(remaining_operands) == 1:
                return remaining_operands  # Single literal
            elif len(remaining_operands) > 1:
                return [Or(*remaining_operands)]  # Multiple literals as Or
            else:
                return []  # Return empty list if no disjunction or negation found

        else:
            return []  # Return empty list if no disjunction or negation found

    def unit_resolution_alternative(self, kb):
        """
        Alternative resolution method for two clauses: P ∨ Q and ¬P ∨ R ⊢ Q ∨ R

        :param kb: knowledge base containing logical statements
        :type kb: list
        :return: derived conclusion from resolving two clauses
        :rtype: list
        """

        # Step 1: Look for the disjunction (P ∨ Q)
        findings = []  # Initialize empty list to store found statements
        for statement in kb:  # Iterate through each statement in knowledge base
            if isinstance(statement,
                          Or) and self.symbol_name in statement.operands:  # Check if statement is Or and contains our symbol
                findings.append(statement)  # Add the disjunction to findings list
                break  # Exit loop once disjunction is found

        # Step 2: Look for clause containing ¬P
        for statement in kb:  # Iterate through knowledge base again
            if isinstance(statement, Or) and Not(
                    self.symbol_name) in statement.operands:  # Check if statement contains ¬P
                findings.append(statement)  # Add clause with ¬P to findings list
                break  # Exit loop once found

        # Step 3: If we have both, apply resolution to get Q ∨ R
        if len(findings) == 2:  # Check if we found both required clauses
            remaining_operands = []  # Initialize list to collect remaining operands after resolution

            # From P ∨ Q, get Q (skip P)
            for operand in findings[0].operands:  # Iterate through operands of first clause
                if operand != self.symbol_name:  # Check if operand is not P
                    remaining_operands.append(operand)  # Add non-P operand to remaining list

            # From ¬P ∨ R, get R (skip ¬P)
            for operand in findings[1].operands:  # Iterate through operands of second clause
                if operand != Not(self.symbol_name):  # Check if operand is not ¬P
                    remaining_operands.append(operand)  # Add non-¬P operand to remaining list

            # Return Q ∨ R based on remaining operands
            if len(remaining_operands) > 1:  # If multiple operands remain after resolution
                return [Or(*remaining_operands)]  # Return combined operands as Or clause
            elif len(remaining_operands) == 1:  # If only one operand remains
                return remaining_operands  # Return single operand as list
            else:  # If no operands remain
                return ["CONTRADICTION"]  # Return contradiction indicator

        return []  # Return empty list if resolution conditions not met


def main():
    resolution = Resolution("P")
    p = Symbol("P")
    q = Symbol("Q")

    print("=== Test Case 1: P ∨ Q, ¬P ⊢ Q ===")
    kb1 = [Or(p, q), Not(p)]
    result1 = resolution.unit_resolution(kb1)
    print(f"Knowledge Base: {kb1}")
    print(f"Result: {result1}")
    print(f"Expected: [Q], Got: {result1}")
    print()

    print("=== Test Case 2: Only P ∨ Q (missing ¬P) ===")
    kb2 = [Or(p, q)]
    result2 = resolution.unit_resolution(kb2)
    print(f"Knowledge Base: {kb2}")
    print(f"Result: {result2}")
    print(f"Expected: [], Got: {result2}")
    print()

    print("=== Test Case 3: Only ¬P (missing P ∨ Q) ===")
    kb3 = [Not(p)]
    result3 = resolution.unit_resolution(kb3)
    print(f"Knowledge Base: {kb3}")
    print(f"Result: {result3}")
    print(f"Expected: [], Got: {result3}")
    print()

    print("=== Test Case 4: P ∨ Q ∨ R, ¬P ⊢ Q ∨ R ===")
    r = Symbol("R")
    kb4 = [Or(p, q, r), Not(p)]
    result4 = resolution.unit_resolution(kb4)
    print(f"Knowledge Base: {kb4}")
    print(f"Result: {result4}")
    print(f"Note: Returns first non-P operand: {result4}")
    print()

    print("=== Test Case 5: Wrong symbol (looking for P, KB has X ∨ Y) ===")
    x = Symbol("X")
    y = Symbol("Y")
    kb5 = [Or(x, y), Not(x)]
    result5 = resolution.unit_resolution(kb5)
    print(f"Knowledge Base: {kb5}")
    print(f"Result: {result5}")
    print(f"Expected: [], Got: {result5} (P not found in X ∨ Y)")


if __name__ == "__main__":
    main()