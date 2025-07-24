from ..inference.model_checking import ModelChecker
from ..propositional_logic import Symbol, Not, Or, Implies


class LogicPuzzle:
    def __init__(self, names, houses):
        self.names = names
        self.houses = houses
        self.knowledge_base = []
        self.symbols = []

    def symbol_add(self):
        for name in self.names:
            for house in self.houses:
                self.symbols.append(Symbol(f"{name}{house}"))

    def knowledge_add(self):
        for name in self.names:
            self.knowledge_base.append(Or(
                Symbol(f"{name}Gryffindor"),
                Symbol(f"{name}Hufflepuff"),
                Symbol(f"{name}Ravenclaw"),
                Symbol(f"{name}Slytherin")
            ))

    def only_one_person(self):
        for name in self.names:
            for h1 in self.houses:
                for h2 in self.houses:
                    if h1 != h2:
                        self.knowledge_base.append(Implies(Symbol(f"{name}{h1}"), Not(Symbol(f"{name}{h2}"))))

    def only_one_house(self):
        for house in self.houses:
            for name1 in self.names:
                for name2 in self.names:
                    if name1 != name2:
                        self.knowledge_base.append(Implies(Symbol(f"{name1}{house}"), Not(Symbol(f"{name2}{house}"))))

    def check_knowledge(self):
        for symbol in self.symbols:
            checker = ModelChecker(self.knowledge_base)
            if checker.entails(symbol):
                return print(f"{symbol} is True")

def main():
    names = ["Harry", "Draco", "Hermione"]
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    puzzle = LogicPuzzle(names, houses)
    puzzle.symbol_add()
    puzzle.knowledge_add()
    puzzle.only_one_person()
    puzzle.only_one_house()

    # רמז נוסף לדוגמה:
    from ..propositional_logic import Not, Symbol
    puzzle.knowledge_base.append(Not(Symbol("HermioneSlytherin")))

    # בדיקת הידע
    puzzle.check_knowledge()

if __name__ == "__main__":
    main()