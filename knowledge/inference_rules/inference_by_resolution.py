from ..propositional_logic import Symbol, Not  # Import Symbol and Not classes
from conversion_to_cnf import ConvToCNF
from knowledge.inference_rules.resolution.resolution import Resolution
class InferenceByResolution:
    def __init__(self, a):
        self.a = Symbol(a)  # Create Symbol object for premise a

    def apply(self, kb):
        """
        Apply the inference by resolution rule on the given knowledge base.

        :param kb: knowledge base
        :type kb: lst
        :return: whether the inference by resolution rule can be applied
        :rtype: str
        """

        negative_a = Not(self.a) # Create negative form of a
        extended_kb = kb + [negative_a] # Extend knowledge base
        cnf = ConvToCNF(str(negative_a)) # Create CNF converter
        cnf_converted_kb = cnf.apply(extended_kb) # Apply CNF on extended knowledge base
        resolution = Resolution(self.a)  # Create Resolution object`
        result = resolution.engine(cnf_converted_kb)  # Run the resolution engine
        if"Contradiction" in result:  # Check if contradiction was found
            return f"{True} kb entails {self.a}" # Return True

        else:
            return f"{False} kb does not entail {self.a}"


def main():
    kb = ["A", "B", "C"]
    print(InferenceByResolution("A").apply(kb))

if __name__ == "__main__":
    main()