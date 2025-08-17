class Sample:
    def __init__(self, value_num, sample_num):
        self.value_num = value_num
        self.sample_num = sample_num

    def distribution(self):
        return self.value_num / self.sample_num

