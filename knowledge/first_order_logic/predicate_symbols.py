from knowledge.propositional_logic.logic_operations import Symbol, Not, And, Implies


class PredicateSymbols:
    """Represents an entity that can have various predicates applied to it."""

    def __init__(self, name):
        """
        Initialize entity as a symbol.

        :param name: name of the entity
        :type name: str
        """
        self.name = name  # Store entity name
        self.symbol = Symbol(name)  # Create symbol for this entity

    def person(self, negated=False):
        """
        Create person predicate for this entity.

        :param negated: whether to negate the predicate
        :type negated: bool
        :return: person predicate symbol or its negation
        :rtype: Symbol or Not
        """

        symbol = Symbol(f"{self.name}_is_person")  # Create person predicate symbol
        return Not(symbol) if negated else symbol  # Return negated or regular symbol

    def not_person(self):
        """
        Create negated person predicate.

        :return: negated person predicate
        :rtype: Not
        """

        return self.person(negated=True)  # Return negated person predicate

    def house(self, negated=False):
        """
        Create house predicate for this entity.

        :param negated: whether to negate the predicate
        :type negated: bool
        :return: house predicate symbol or its negation
        :rtype: Symbol or Not
        """

        symbol = Symbol(f"{self.name}_is_house")  # Create house predicate symbol
        return Not(symbol) if negated else symbol  # Return negated or regular symbol

    def not_house(self):
        """
        Create negated house predicate.

        :return: negated house predicate
        :rtype: Not
        """

        return self.house(negated=True)  # Return negated house predicate

    def belongs_to(self, name2, negated=False):
        """
        Create belongs_to predicate for this entity.

        :param name2: entity this belongs to
        :type name2: str
        :param negated: whether to negate the predicate
        :type negated: bool
        :return: belongs_to predicate symbol or its negation
        :rtype: Symbol or Not
        """

        symbol = Symbol(f"{self.name}_belongs_to_{name2}")  # Create belongs_to predicate symbol
        return Not(symbol) if negated else symbol  # Return negated or regular symbol

    def not_belongs_to(self, name2):
        """
        Create negated belongs_to predicate.

        :param name2: entity this does not belong to
        :type name2: str
        :return: negated belongs_to predicate
        :rtype: Not
        """

        return self.belongs_to(name2, negated=True)  # Return negated belongs_to predicate

    def get_symbol(self):
        """
        Get the base symbol for this entity.

        :return: base symbol representing this entity
        :rtype: Symbol
        """

        return self.symbol  # Return the entity's base symbol

    def __str__(self):
        """
        String representation of the entity.

        :return: entity name
        :rtype: str
        """
        return self.name  # Return entity name

    def __repr__(self):
        """
        Representation of the entity.

        :return: formatted representation
        :rtype: str
        """
        return f"PredicateSymbols({self.name})"  # Return formatted representation


def main():

    harry = PredicateSymbols("harry")
    gryffindor = PredicateSymbols("gryffindor")

    harry_is_person = harry.person()
    harry_not_person = harry.not_person()
    gryffindor_is_house = gryffindor.house()
    gryffindor_not_person = gryffindor.not_person()
    harry_belongs_gryffindor = harry.belongs_to("gryffindor")

    knowledge = And(
        harry_is_person,
        gryffindor_is_house,
        gryffindor_not_person,
        harry_belongs_gryffindor,
        Implies(harry_is_person, harry_belongs_gryffindor)
    )

    model = {
        "harry_is_person": True,
        "gryffindor_is_house": True,
        "gryffindor_is_person": False,
        "harry_belongs_to_gryffindor": True
    }

    print(f"Harry is person: {harry_is_person.evaluate(model)}")
    print(f"Harry is NOT person: {harry_not_person.evaluate(model)}")
    print(f"Gryffindor is house: {gryffindor_is_house.evaluate(model)}")
    print(f"Gryffindor is NOT person: {gryffindor_not_person.evaluate(model)}")
    print(f"Harry belongs to Gryffindor: {harry_belongs_gryffindor.evaluate(model)}")
    print(f"Knowledge base satisfied: {knowledge.evaluate(model)}")

    print(f"\nHarry base symbol: {harry.get_symbol()}")
    print(f"Gryffindor base symbol: {gryffindor.get_symbol()}")


if __name__ == "__main__":
    main()