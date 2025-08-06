class Probability:
    def __init__(self, c, not_c, r, not_r):
        self.c = c
        self.r = r
        self.not_c = not_c
        self.not_r = not_r

        if self.c + self.not_c != 1:
            raise ValueError("c and not_c must sum to 1")
        if self.r + self.not_r != 1:
            raise ValueError("r and not_r must sum to 1")


    def joint_probabilities(self):
        joint_probabilities = {
        "p(c, r)" : self.c * self.r,
        "p(c, not r)" : self.c * self.not_r,
        "p(not c, r)" : self.not_c * self.r,
        "p(not c, not r)" : self.not_c * self.not_r
        }

        return joint_probabilities

    def deduce(self):
        joints = self.joint_probabilities()

        p_c_given_r = joints["p(c, r)"] / self.r
        p_c_given_not_r = joints["p(c, not r)"] / self.not_r

        p_not_c_given_r = joints["p(not c, r)"] / self.r
        p_not_c_given_not_r = joints["p(not c, not r)"] / self.not_r

        conditional_probs = {
            "P(c|r)": p_c_given_r,
            "P(not_c|r)": p_not_c_given_r,
            "P(r|c)": p_c_given_not_r,
            "P(not_r|c)": p_not_c_given_not_r
        }

        return conditional_probs

    def a_find(self):
        joints = self.joint_probabilities()

        # cond_probs["p_c_given_r"] = "a" * joints["p(c,r)"]
        # a * joints["p(c, r)"] + a * joints["p(not c, r)"] == 1
        a = 1 / (joints["p(c, r)"] + joints["p(not c, r)"])
        return a

def main():
    p = Probability(0.4, 0.6, 0.1, 0.9)
    joint_probabilities = p.joint_probabilities()
    deduce = p.deduce()
    a_found = p.a_find()

    print(joint_probabilities)
    print(deduce)
    print(a_found)

if __name__ == "__main__":
    main()