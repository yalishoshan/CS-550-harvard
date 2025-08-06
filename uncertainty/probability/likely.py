class Likely:
    def __init__(self, red_dice, blue_dice):
         self.red_dice =  red_dice
         self.blue_dice = blue_dice

    def all_possible_outcomes(self):
        possibility_outcomes = set()
        for i in range(0, 6):
            for j in range(0, 6):
                possibility_outcomes.add((self.red_dice[i], self.blue_dice[j]))

        return possibility_outcomes

    def outcome_sum(self):
        return [sum(possibility) for possibility in self.all_possible_outcomes()]

    def sum_likely(self, x):
        return self.outcome_sum().count(x) // len(self.all_possible_outcomes())

def main():
    red_dice = [1, 2, 3, 4, 5, 6]
    blue_dice = [1, 2, 3, 4, 5, 6]
    likely = Likely(red_dice, blue_dice)
    print(likely.sum_likely(7))

if __name__ == "__main__":
    main()






