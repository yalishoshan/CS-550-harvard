from propositional_logic import LogicNot, LogicAnd, LogicOr, LogicImplies, LogicBiconditional, LogicXor
from search.projects.degrees import people
from functools import reduce

logic_operations = {
    "¬": LogicNot,
    "∧": LogicAnd,
    "∨": LogicOr,
    "→": LogicImplies,
    "↔": LogicBiconditional,
    "⊕": LogicXor
}


class KnowledgeEngineering:
    """"
    This class implements the knowledge engineering process
    """

    def __init__(self, people, rooms, weapons):
        """
        Initialize the knowledge engineering process
        
        :param people: lst of people
        :type people: list
        :param rooms: lst of rooms
        :type rooms: list
        :param weapons: lst of weapons
        :type weapons: list
        """""
        self.people = people # List of people
        self.rooms = rooms # List of rooms
        self.weapons = weapons # List of weapons

    def first_clue(self):
        """
        This function
        """
        or1 = LogicOr(people[0], people[1], people[2])
        or2 = LogicOr(rooms[0], rooms[1], rooms[2])
        or3 =LogicOr(weapons[0], weapons[1], weapons[2])


    def card_in_my_hand(self, card):
        """
        This function
        """
        # logic_operations["¬"] card in my hand

    def guess(self):
        """
        This function returns the guess
        """
        # not guess(people, rooms, weapons)






def main():
    people = ["mustard", "plum", "scarlet"]
    rooms = ["ballroom", "kitchen", "library"]
    weapons = ["knife", "revolver", "wrench"]

    game1 = KnowledgeEngineering(people, rooms, weapons)


if __name__ == "__main__":
    main()