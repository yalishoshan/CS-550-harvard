from ..propositional_logic import Symbol, Not, And, Or
from ..inference.model_checking import ModelChecker


class ClueGame:
    """Knowledge engineering for the Clue game."""

    def __init__(self, people, rooms, weapons):
        # Create symbols
        self.people = [Symbol(p) for p in people]
        self.rooms = [Symbol(r) for r in rooms]
        self.weapons = [Symbol(w) for w in weapons]

        # Initialize knowledge base
        self.knowledge = []

        # Game rules: exactly one person, room, and weapon
        self.knowledge.append(Or(*self.people))
        self.knowledge.append(Or(*self.rooms))
        self.knowledge.append(Or(*self.weapons))

    def add_card(self, card):
        """Add knowledge that a card is not in the envelope."""
        self.knowledge.append(Not(Symbol(card)))

    def add_guess_result(self, person, room, weapon, was_wrong):
        """Add knowledge from a guess result."""
        if was_wrong:
            # At least one of these is not in the envelope
            self.knowledge.append(
                Or(Not(Symbol(person)),
                   Not(Symbol(room)),
                   Not(Symbol(weapon)))
            )

    def check_knowledge(self):
        """Check what we can deduce from current knowledge."""
        checker = ModelChecker(self.knowledge)
        results = {}

        # Check each symbol
        all_symbols = self.people + self.rooms + self.weapons
        for symbol in all_symbols:
            if checker.entails(symbol):
                results[symbol.name] = "YES (must be in envelope)"
            elif checker.entails(Not(symbol)):
                results[symbol.name] = "NO (definitely not)"
            else:
                results[symbol.name] = "MAYBE"

        return results


# Demo usage
def main():
    game = ClueGame(
        people=["Colonel Mustard", "Miss Scarlet", "Professor Plum"],
        rooms=["Ballroom", "Kitchen", "Library"],
        weapons=["Knife", "Revolver", "Wrench"]
    )

    # Add initial cards (what I have)
    game.add_card("Colonel Mustard")
    game.add_card("Kitchen")
    game.add_card("Revolver")

    # Someone shows me a card
    game.add_card("Professor Plum")

    # Check what we know
    results = game.check_knowledge()
    print("\nCurrent knowledge:")
    for item, status in results.items():
        if status != "MAYBE":
            print(f"{item}: {status}")


if __name__ == "__main__":
    main()