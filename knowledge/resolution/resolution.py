from knowledge.propositional_logic import Symbol, Not, Or  # Import Symbol class, Not class and Or class


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
        if len(findings) == 2:  # Check if we found both disjunction and negation
            remaining_operands = []  # Initialize list to collect remaining operands
            for operand in findings[0].operands:  # Iterate through operands of the disjunction
                if operand != self.symbol_name:  # Check if operand is not our target symbol
                    remaining_operands.append(operand)  # Add non-target operand to remaining list

            # Smart return based on count
            if len(remaining_operands) == 1:  # If only one operand remains
                return remaining_operands  # Return single literal as list
            elif len(remaining_operands) > 1:  # If multiple operands remain
                return [Or(*remaining_operands)]  # Return multiple literals as Or clause
            else:  # If no operands remain after removing target symbol
                return []  # Return empty list indicating no conclusion

        else:  # If we didn't find both required components
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

    def full_resolution(self, kb):
        """
        Find ANY two clauses that can be resolved (not limited to target symbol).

        :param kb: knowledge base containing logical statements
        :type kb: list
        :return: derived conclusion from resolving any resolvable pair
        :rtype: list
        """

        for i, statement1 in enumerate(kb):  # Iterate through each statement with index
            for j, statement2 in enumerate(kb[i + 1:],
                                           i + 1):  # Iterate through remaining statements to avoid duplicates

                # Case 1: Unit clauses P and ¬P → CONTRADICTION
                if (isinstance(statement1, Symbol) and isinstance(statement2, Not) and
                        statement2.operand == statement1):  # Check if statement1 is P and statement2 is ¬P
                    return ["CONTRADICTION"]  # Return contradiction when P and ¬P found
                if (isinstance(statement2, Symbol) and isinstance(statement1, Not) and
                        statement1.operand == statement2):  # Check reverse: statement1 is ¬P and statement2 is P
                    return ["CONTRADICTION"]  # Return contradiction when ¬P and P found

                # Case 2: Unit clause P and disjunction (¬P ∨ Q) → Q
                if isinstance(statement1, Symbol) and isinstance(statement2,
                                                                 Or):  # Check if first is unit, second is disjunction
                    for operand in statement2.operands:  # Iterate through operands of the disjunction
                        if isinstance(operand,
                                      Not) and operand.operand == statement1:  # Check if operand is negation of unit clause
                            remaining = [op for op in statement2.operands if
                                         op != operand]  # Collect operands except the negation
                            if len(remaining) == 0:  # If no operands remain after removing negation
                                return ["CONTRADICTION"]  # Return contradiction for empty clause
                            return remaining if len(remaining) == 1 else [
                                Or(*remaining)]  # Return single operand or Or of multiple

                # Case 3: Disjunction (¬P ∨ Q) and unit clause P → Q (reverse of case 2)
                if isinstance(statement2, Symbol) and isinstance(statement1,
                                                                 Or):  # Check if second is unit, first is disjunction
                    for operand in statement1.operands:  # Iterate through operands of the disjunction
                        if isinstance(operand,
                                      Not) and operand.operand == statement2:  # Check if operand is negation of unit clause
                            remaining = [op for op in statement1.operands if
                                         op != operand]  # Collect operands except the negation
                            if len(remaining) == 0:  # If no operands remain after removing negation
                                return ["CONTRADICTION"]  # Return contradiction for empty clause
                            return remaining if len(remaining) == 1 else [
                                Or(*remaining)]  # Return single operand or Or of multiple

                # Case 4: Two disjunctions (P ∨ Q) and (¬P ∨ R) → (Q ∨ R)
                if isinstance(statement1, Or) and isinstance(statement2,
                                                             Or):  # Check if both statements are disjunctions
                    for op1 in statement1.operands:  # Iterate through operands of first disjunction
                        for op2 in statement2.operands:  # Iterate through operands of second disjunction
                            # Check if operands are complementary (P and ¬P)
                            if ((isinstance(op1, Symbol) and isinstance(op2, Not) and op2.operand == op1) or
                                    (isinstance(op2, Symbol) and isinstance(op1,
                                                                            Not) and op1.operand == op2)):  # Found complementary pair

                                remaining = []  # Initialize list to collect remaining operands
                                # Add remaining operands from first clause (exclude the complementary one)
                                remaining.extend([op for op in statement1.operands if
                                                  op != op1])  # Add non-complementary operands from first clause
                                # Add remaining operands from second clause (exclude the complementary one)
                                remaining.extend([op for op in statement2.operands if
                                                  op != op2])  # Add non-complementary operands from second clause

                                if len(remaining) == 0:  # If no operands remain after resolution
                                    return ["CONTRADICTION"]  # Return contradiction for empty clause
                                elif len(remaining) == 1:  # If only one operand remains
                                    return remaining  # Return single operand as list
                                else:  # If multiple operands remain
                                    return [Or(*remaining)]  # Return multiple operands as Or clause

        return []  # Return empty list if no resolvable pairs found

    def engine(self, kb):
        """
        Runs iterative resolution using full_resolution until
        no more new clauses are derived or contradiction is found.

        :param kb: knowledge base
        :type kb: lst
        :return: derived conclusion from resolving two clauses
        :rtype: lst
        """
        derived_clauses = []  # Initialize list to track clauses derived during resolution
        previous_kb_size = 0  # Track KB size to detect when no progress is made

        while len(kb) != previous_kb_size:  # Continue while knowledge base is growing
            previous_kb_size = len(kb)  # Update previous size tracker

            result = self.full_resolution(kb)  # Apply full resolution to find any resolvable pair
            if result == ["CONTRADICTION"]:  # Check if contradiction was found
                return "Contradiction found — entailment proven ✅"  # Return success message for entailment
            if result and result not in kb and result not in derived_clauses:  # Check if new clause was derived and not duplicate
                kb.extend(result)  # Add new clause to knowledge base
                derived_clauses.extend(result)  # Add new clause to derived clauses tracker

        return f"No contradiction found. Final KB: {kb}"  # Return failure message with final knowledge base