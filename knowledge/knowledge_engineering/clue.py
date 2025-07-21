from ..propositional_logic import Symbol, Not, And, Or
from ..inference.model_checking import ModelChecker


class ClueGame:
    """Knowledge engineering for the Clue game."""

    def __init__(self, people, rooms, weapons):
        """
        Initialize Clue game with cards.

        :param people: list of person names
        :type people: list[str]
        :param rooms: list of room names
        :type rooms: list[str]
        :param weapons: list of weapon names
        :type weapons: list[str]
        """
        # Create symbols for each card
        self.people = [Symbol(p) for p in people]  # Person symbols
        self.rooms = [Symbol(r) for r in rooms]  # Room symbols
        self.weapons = [Symbol(w) for w in weapons]  # Weapon symbols

        # Initialize knowledge base
        self.knowledge = []  # Empty KB

        # Game rules: exactly one person, room, and weapon
        self.knowledge.append(Or(*self.people))  # At least one person
        self.knowledge.append(Or(*self.rooms))  # At least one room
        self.knowledge.append(Or(*self.weapons))  # At least one weapon

    def add_card(self, card):
        """
        Add knowledge that a card is not in the envelope.

        :param card: name of card seen
        :type card: str
        """
        self.knowledge.append(Not(Symbol(card)))  # Card not in envelope

    def add_guess_result(self, person, room, weapon, was_wrong):
        """
        Add knowledge from a guess result.

        :param person: guessed person
        :type person: str
        :param room: guessed room
        :type room: str
        :param weapon: guessed weapon
        :type weapon: str
        :param was_wrong: whether guess was incorrect
        :type was_wrong: bool
        """
        if was_wrong:  # Guess was wrong
            # At least one of these is not in the envelope
            self.knowledge.append(
                Or(Not(Symbol(person)),  # Person wrong
                   Not(Symbol(room)),  # Room wrong
                   Not(Symbol(weapon)))  # Weapon wrong
            )

    def check_knowledge(self):
        """
        Check what we can deduce from current knowledge.

        :return: deduction results for each card
        :rtype: dict[str, str]
        """
        checker = ModelChecker(self.knowledge)  # Create model checker
        results = {}  # Store results

        # Check each symbol
        all_symbols = self.people + self.rooms + self.weapons  # All cards
        for symbol in all_symbols:
            if checker.entails(symbol):  # Symbol must be true
                results[symbol.name] = "YES (must be in envelope)"
            elif checker.entails(Not(symbol)):  # Symbol must be false
                results[symbol.name] = "NO (definitely not)"
            else:  # Can't determine
                results[symbol.name] = "MAYBE"

        return results  # Return all deductions