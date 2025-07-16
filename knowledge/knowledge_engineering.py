from propositional_logic import Or, Not, And
from functools import reduce
from inference import ModelCheck

class Symbol:
    """
    This class represents a symbol in propositional logic

    """

    def __init__(self, name):
        """
        Initialize the symbol

        :param name: name of the symbol
        :type name: str
        """

        self.name = name # Name of the symbol

    def __str__(self):
        """
        Returns the name of the symbol

        :return: name of the symbol
        :rtype: str
        """

        return self.name  # Return the name of the symbol

    def __modelcheck__(self, model):
        """
        Returns the value of the symbol in the model

        :param model: model to check
        :type model: dict
        :return: value of the symbol in the model
        :rtype: bool
        """

        return model[self.name]

class KnowledgeEngineering:
    """"
    This class implements the knowledge engineering process
    """

    def __init__(self, people, rooms, weapons, knowledge=None):
        """
        Initialize the knowledge engineering process
        
        :param people: lst of people
        :type people: list
        :param rooms: lst of rooms
        :type rooms: list
        :param weapons: lst of weapons
        :type weapons: list
        """

        self.people = [Symbol(person) for person in people] # List of people as symbols
        self.rooms = [Symbol(room) for room in rooms] # List of rooms as symbols
        self.weapons = [Symbol(weapon) for weapon in weapons] # List of weapons as symbols
        self.symbols = self.people + self.rooms + self.weapons # List of all symbols
        self.knowledge = set()

        # # There must be a person, room, and weapon.
        self.knowledge.add(And(
            Or(self.people[0], self.people[1], self.people[2]),
            Or(self.rooms[0], self.rooms[1], self.rooms[2]),
            Or(self.weapons[0], self.weapons[1], self.weapons[2])
        ))


    def my_card(self, card, i):
        """
        This function returns the card in my hand as not the solution cause it is known

        :param card: card in my hand
        :type card: tuple
        :param i: index of the card in the tuple
        :type i: int
        """

        # Initial cards
        self.knowledge.add(Not(card[i]))

    def known_card(self, card):
        """
        This function returns the known card

        :param card: known card
        :type card: str
        """

        # Known card
        self.knowledge.add(Not(Symbol(card)))

    def guess(self, card):
        """
        This function returns the guess of the unknown card

        :param card: unknown card
        :type card: tuple
        """

        # Unknown card
        self.knowledge.add(Or(Not(Symbol(card[0])), Not(Symbol(card[1])), Not(Symbol(card[2]))))



    def check_guess(knowledge, symbols):
        """"
        This function checks the guess of the unknown card

        :param knowledge: knowledge base
        :type knowledge: set
        :param symbols: list of symbols
        :type symbols: list
        """

        for symbol in symbols:
            if ModelCheck(knowledge, symbol):
                return symbol

            elif not ModelCheck(knowledge, Not(symbol)):
                return "maybe"





def main():
    people = ["mustard", "plum", "scarlet"]
    rooms = ["ballroom", "kitchen", "library"]
    weapons = ["knife", "revolver", "wrench"]
    game1 = KnowledgeEngineering(people, rooms, weapons)


if __name__ == "__main__":
    main()
