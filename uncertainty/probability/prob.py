class Prob:
    def __init__(self, value, value_lst):
        self.value = value
        self.value_lst = [value_lst]


    def omega(self):
        if self.value < 0 or self.value > 1:
            raise ValueError ("Chances range is only between 0 and 1")

        elif self.value == 0:
            return "Impossible event"

        elif self.value == 1:
            return "Certain to happen"

        elif 1 > self.value > 0:
            return self.value


    def sigma(self):
        if sum(self.value_lst) != 1:
            raise ValueError ("Sum of probabilities must be 1")

        else:
            return "Probability distribution"




        