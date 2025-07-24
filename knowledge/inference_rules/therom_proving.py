# Import all the inference rule modules
from and_elimination import *              # Import AND elimination rule
from biconditional_elimination import *    # Import biconditional elimination rule
from de_morgans_law import *               # Import De Morgan's Law
from implication_elimination import *      # Import implication elimination rule
from double_negation_elimination import *  # Import double negation elimination rule
from modus_pones import *                  # Import Modus Ponens rule


class TheoremProving:  # Class that manages the proof process using inference rules
    def __init__(self, start_kb, actions, goal):  # Initialize the proof engine with knowledge base, rules, and goal
        """
        Initialize the theorem proving system

        Args:
            start_kb (list): Initial knowledge base (list of logical statements)       # The list of known facts
            actions (list): List of inference rule instances to apply                 # The inference rules to use
            goal (Symbol): The statement we want to prove                             # The target conclusion
        """
        self.start_kb = start_kb.copy()        # Copy the initial KB to avoid modifying the original
        self.actions = actions                 # Store the list of inference rules
        self.goal = goal                       # Store the goal we want to prove

    def prove(self):  # Attempt to prove the goal using the inference rules
        """
        Apply inference rules step by step to prove the goal

        Returns:
            tuple: (success: bool, steps: list, final_kb: list)  # Whether the goal was proven, steps taken, and final KB
        """
        current_kb = self.start_kb.copy()      # Create a working copy of the knowledge base
        steps = []                             # List to record each step of the proof
        steps_num = 0                          # Step counter

        for action in self.actions:            # Iterate over all inference rule instances
            steps_num += 1                     # Increment the step number

            try:
                new_statements = action.apply(current_kb)  # Apply the rule to the current KB

                if new_statements:             # If the rule produced any new statements
                    for statement in new_statements:               # Go through each derived statement
                        if statement not in current_kb:            # Only add if it's not already in the KB
                            current_kb.append(statement)           # Append the new statement to the KB

                    steps.append({                                # Record this successful step
                        'step': steps_num,                         # Step number
                        'rule': action.__class__.__name__,        # Name of the rule class
                        'new_statements': new_statements,         # List of newly derived statements
                        'kb_size': len(current_kb)                 # Size of the KB after this step
                    })

                    if self.goal in current_kb:                   # If the goal has been proven
                        return True, steps, current_kb            # Return success with the steps and final KB

            except Exception as e:                                 # If applying the rule caused an error
                steps.append({                                     # Record the failed step
                    'step': steps_num,                             # Step number
                    'rule': action.__class__.__name__,            # Name of the rule class
                    'error': str(e),                               # Description of the error
                    'kb_size': len(current_kb)                     # Current KB size
                })

        return self.goal in current_kb, steps, current_kb          # Return whether the goal was reached and all steps taken

def main():

    A = Symbol("A")
    B = Symbol("B")
    implication = Implies(A, B)

    start_kb = [A, implication]
    goal = B


    actions = [
        ModusPones(A, implication),  # Assuming ModusPones accepts premises as input
    ]

    prover = TheoremProving(start_kb, actions, goal)
    success, steps, final_kb = prover.prove()

    print("=== THEOREM PROVING ===")
    print(f"Initial KB: {start_kb}")
    print(f"Goal: {goal}\n")

    for step in steps:
        print(f"Step {step['step']}: {step['rule']}")
        if 'new_statements' in step:
            print(f"  New statements: {step['new_statements']}")
        if 'error' in step:
            print(f"  Error: {step['error']}")
        print(f"  KB size: {step['kb_size']}\n")

    print("=== RESULT ===")
    if success:
        print("✓ Goal PROVEN!")
    else:
        print("✗ Goal NOT proven")
    print(f"Final KB: {final_kb}")


if __name__ == "__main__":
    main()