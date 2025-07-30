from knowledge.propositional_logic.logic_operations import And, Or
from predicate_symbols import PredicateSymbols

class Quantification:
    def __init__(self, quantifier, formula_list):
        """
        Initialize a Quantification object.

        """
        self.quantifier = quantifier.lower()  # Store quantifier in lowercase for consistency
        self.formula_list = formula_list      # Store the list of predicate formulas

    def universal(self):
        """
        Apply universal quantification (∀) to the formula list.

        :return: Logical conjunction of all formulas
        :rtype: And
        :raises ValueError: if quantifier is not 'forall'
        """
        if self.quantifier == 'forall':             # Check if quantifier type is universal
            return And(*self.formula_list)          # Combine all formulas using logical AND
        raise ValueError("Quantifier is not universal (∀).")  # Raise error if mismatched

    def existential(self):
        """
        Apply existential quantification (∃) to the formula list.

        :return: Logical disjunction of all formulas
        :rtype: Or
        :raises ValueError: if quantifier is not 'exists'
        """
        if self.quantifier == 'exists':             # Check if quantifier type is existential
            return Or(*self.formula_list)           # Combine all formulas using logical OR
        raise ValueError("Quantifier is not existential (∃).")  # Raise error if mismatched

def main():
    harry = PredicateSymbols("harry")
    hermione = PredicateSymbols("hermione")
    ron = PredicateSymbols("ron")

    entities = [harry, hermione, ron]
    all_person_predicates = [e.person() for e in entities]

    universal_statement = Quantification("forall", all_person_predicates).universal()
    existential_statement = Quantification("exists", all_person_predicates).existential()

    model = {
        "harry_is_person": True,
        "hermione_is_person": False,
        "ron_is_person": True
    }

    print(f"Universal statement holds: {universal_statement.evaluate(model)}")
    print(f"Existential statement holds: {existential_statement.evaluate(model)}")

if __name__ == "__main__":
    main()