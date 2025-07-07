class PropositionalLogic:
   """
   This class implements propositional logic operations.
   """

   def __init__(self, p, q):
       """
       This function initializes the class

       :param p: first proposition
       :param q: second proposition
       """
       self.p = p  # Store first proposition
       self.q = q  # Store second proposition

   def logic_not(self):
       """
       This function returns the negation of a propositional formula.

       :return: the negation of a propositional formula
       """
       return not self.p  # Return negation of p

   def logic_and(self):
       """
       This function returns the conjunction of two propositional formulas.

       :return: the conjunction of two propositional formulas
       """
       return self.p and self.q  # Return p AND q

   def logic_or(self):
       """
       This function returns the disjunction of two propositional formulas.

       :return: the disjunction of two propositional formulas
       """
       return self.p or self.q  # Return p OR q

   def logic_implies(self):
       """
       This function returns the implication of two propositional formulas.

       :return: the implication of two propositional formulas
       """
       if self.p and not self.q:  # If p is true and q is false
           return False  # Implication fails

       return True  # Otherwise implication holds

   def logic_biconditional(self):
       """
       This function returns the biconditional of two propositional formulas.

       :return: the biconditional of two propositional formulas
       """
       if self.p == self.q:  # If both have same truth value
           return True  # Biconditional is true

       return False  # Otherwise biconditional is false

class Model:
   """
   This class implements a propositional model.
   """

   def __init__(self, p, q, knowledge_base):
       """
       This function initializes the class

       :param p: first proposition value
       :param q: second proposition value
       :param knowledge_base: list of known facts
       """
       self.p = p  # Store first proposition
       self.q = q  # Store second proposition
       self.knowledge_base = knowledge_base  # Store knowledge base

   def entailment(self, conclusion):
       """
       This function returns the entailment of two propositional formulas.

       :param conclusion: conclusion to check
       :type conclusion: bool

       :return: the entailment of two propositional formulas
       """
       if not all(self.knowledge_base):  # Check if KB is consistent
           return False  # Can't entail from inconsistent KB

       if conclusion in self.knowledge_base:  # Direct check
           return True  # Conclusion is already in KB

       logic = PropositionalLogic(self.p, self.q)  # Create logic instance

       if self.p in self.knowledge_base:  # If p is in KB
           temp_logic = PropositionalLogic(self.p, conclusion)  # Create p→conclusion
           if temp_logic.logic_implies():  # Check if p implies conclusion
               return True  # Modus ponens applies

       if logic.logic_and() in self.knowledge_base:  # If p∧q is in KB
           if conclusion == self.p or conclusion == self.q:  # Check if conclusion is p or q
               return True  # Conjunction elimination applies

       if logic.logic_biconditional() and conclusion == self.q:  # If p↔q and conclusion is q
           return True  # Biconditional reasoning applies

       logic_not = PropositionalLogic(conclusion, None)  # Create negation checker
       if logic_not.logic_not() in self.knowledge_base:  # If ¬conclusion is in KB
           return False  # Conclusion contradicts KB

       return False  # No entailment found

   def knowledge_base_add(self, formula):
       """
       This function makes a knowledge base that is true

       :param formula: list of formulas to add
       :type formula: list

       :return: knowledge base
       """
       for item in formula:  # Iterate through formulas
           if item is True:  # Only add true formulas
               self.knowledge_base.append(item)  # Add to KB

       return self.knowledge_base  # Return updated KB


def main():
   pass

if __name__ == "__main__":
   main()