def minimax_for_min(s):
    """
     This function returns the best action for the minimizer

     :param s: state
     :type s: list
     :return: best action for the minimizer
     :rtype: str
     """

    best_action = None  # Initialize best action found
    best_value = 2  # Start with worst possible value for minimizer

    for a in actions(s):  # Try each possible action
        action_value = max_value(result(s, a))  # Get value after opponent responds optimally

        if action_value < best_value:  # Check if this action is better for minimizer
            best_value = action_value  # Update best value found
            best_action = a  # Remember this action

    return best_action  # Return the optimal action


def minimax_for_max(s):
    """
    This function returns the best action for the maximizer

    :param s: state
    :type s: list
    :return: best action for the maximizer
    :rtype: str
    """

    best_action = None  # Initialize best action found
    best_value = -2  # Start with worst possible value for maximizer

    for a in actions(s):  # Try each possible action
        action_value = min_value(result(s, a))  # Get value after opponent responds optimally

        if action_value > best_value:  # Check if this action is better for maximizer
            best_value = action_value  # Update best value found
            best_action = a  # Remember this action

    return best_action  # Return the optimal action


def players(s):
    """
    This function returns the player who should move next

    :param s: state
    :type s: list
    :return: the player who should move next
    :rtype: str
    """

    count = 0  # Counter for number of moves made
    for i in range(3):  # Loop through each row
        for j in range(3):  # Loop through each column
            if s[i][j].isalpha():  # Check if cell contains a letter (X or O)
                count += 1  # Increment move counter

    if count % 2 == 0:  # Even number of moves means X's turn
        return "X"  # Return X as next player
    else:  # Odd number of moves means O's turn
        return "O"  # Return O as next player


def actions(s):
    """
    This function returns a list of all possible actions

    :param s: state
    :type s: list
    :return: all possible actions
    :rtype: list
    """

    actions_lst = []  # Initialize list of available actions
    for i in range(3):  # Loop through each row
        for j in range(3):  # Loop through each column
            if not s[i][j].isalpha():  # Check if cell is empty (not X or O)
                actions_lst.append((i, j))  # Add coordinates to available actions

    return actions_lst  # Return list of available moves


def result(s, a):
    new_state = [row[:] for row in s]  # Create deep copy of current state
    new_state[a[0]][a[1]] = players(s)  # Place current player's symbol at action position

    return new_state  # Return new game state


def terminal(s):
    """
    This function returns True if the game is over

    :param s: state
    :type s: list
    :return: True if the game is over else False
    :rtype: bool
    """

    count = 0  # Counter for filled cells
    for i in range(3):  # Loop through each row
        for j in range(3):  # Loop through each column
            if s[i][j].isalpha():  # Check if cell is filled
                count += 1  # Increment filled cell counter

    if count == 9:  # All cells filled means game over
        return True  # Return game over

    for row in s:  # Check each row for three in a row
        if row[0] == row[1] == row[2] and row[0] != " ":  # Three identical non-empty symbols
            return True  # Return game over (someone won)

    for col in range(3):  # Check each column for three in a row
        if s[0][col] == s[1][col] == s[2][col] and s[0][col] != " ":  # Three identical non-empty symbols
            return True  # Return game over (someone won)

    if (s[0][0] == s[1][1] == s[2][2] and s[0][0] != " ") or (
            s[0][2] == s[1][1] == s[2][0] and s[0][2] != " "):  # Check both diagonals
        return True  # Return game over (someone won)

    return False  # Game continues


def utility(s):
    """
    This function returns the utility of the state

    :param s: state
    :type s: list
    :return: utility of the state
    :rtype: int
    """

    for row in s:  # Check each row for winner
        if row[0] == row[1] == row[2] and row[0] != " ":  # Three identical non-empty symbols
            if row[0] == "X":  # X wins
                return 1  # Return positive utility
            elif row[0] == "O":  # O wins
                return -1  # Return negative utility

    for col in range(3):  # Check each column for winner
        if s[0][col] == s[1][col] == s[2][col] and s[0][col] != " ":  # Three identical non-empty symbols
            if s[0][col] == "X":  # X wins
                return 1  # Return positive utility
            elif s[0][col] == "O":  # O wins
                return -1  # Return negative utility

    if (s[0][0] == s[1][1] == s[2][2] and s[0][0] != " ") or (
            s[0][2] == s[1][1] == s[2][0] and s[0][2] != " "):  # Check diagonals
        if s[0][0] == "X" or s[0][2] == "X":  # X wins on diagonal
            return 1  # Return positive utility
        elif s[0][0] == "O" or s[0][2] == "O":  # O wins on diagonal
            return -1  # Return negative utility

    return 0  # No winner, return neutral utility


def max_value(s):
    """
    This function returns the maximum value achievable

    :param s: state
    :type s: list
    :return: maximum value achievable
    :rtype: int
    """

    v = -2  # Initialize with worst possible value for maximizer
    if terminal(s):  # Check if game is over
        return utility(s)  # Return final game value

    for a in actions(s):  # Try each possible action
        v = max(v, min_value(result(s, a)))  # Get maximum value from minimizer's response

    return v  # Return best value achievable


def min_value(s):
    """
    This function returns the minimum value achievable

    :param s: state
    :type s: list
    :return: minimum value achievable
    :rtype: int
    """

    v = 2  # Initialize with worst possible value for minimizer
    if terminal(s):  # Check if game is over
        return utility(s)  # Return final game value

    for a in actions(s):  # Try each possible action
        v = min(v, max_value(result(s, a)))  # Get minimum value from maximizer's response

    return v  # Return best value achievable


def main():
    starting_state = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    print(minimax_for_max(starting_state))


if __name__ == "__main__":
    main()
