from ..propositional_logic import Symbol, Not, And, Or, Implies
from ..inference.model_checking import ModelChecker


class LogicPuzzle:
    def __init__(self, names, houses, knowledge_base, symbols):
        self.names = names
        self.houses = houses
        self.knowledge_base = And()
        self.symbols = []

    def symbol_add:
        for name in names:
            for house in houses:
                symbols.append(Symbol(f"{name}{house}"))

    def knowledge_add:
        for name in names:
            knowledge_base.add(Or(
                Symbol(f"{name}Gryffindor"),
                Symbol(f"{name}Hufflepuff"),
                Symbol(f"{name}Ravenclaw"),
                Symbol(f"{name}Slytherin")
            ))

    def only_one_person:
        for name in names:
            for h1 in houses:
                for h2 in houses:
                    if h1 != h2:
                        knowledge.base.add(Implies(Symbol(f"{name}{h1}"), Not(Symbol(f"{name}{h2}"))))

    def only_one_house:
        for house in houses:
            for name1 in names:
                for name2 in names:
                    if name1 != name2:
                        knowledge.base.add(Implies(Symbol(f"{name1}{house}"), Not(Symbol(f"{name2}{house}"))))

    def check_knowledge:
        for symbol in symbols:
            if ModelChecker().check(knowledge_base, symbol):
                print(f"{symbol} is True")