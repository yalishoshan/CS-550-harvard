def tree_minimax_for_max(tree, tree_values):
    """
    This function returns the best action for the maximizer using alpha-beta pruning

    :param tree: tree structure showing parent-child relationships
    :type tree: dict
    :param tree_values: leaf node values
    :type tree_values: dict
    :return: best action for the maximizer
    :rtype: str
    """
    best_action = None  # Initialize best action found
    best_value = -10  # Start with worst possible value for maximizer

    for action in tree["A"]:  # Try each possible action from root
        value = tree_min_value(action, tree, tree_values, -10, 10)  # Get value after opponent responds optimally
        if value > best_value:  # Check if this action is better for maximizer
            best_value = value  # Update best value found
            best_action = action  # Remember this action

    return best_action  # Return the optimal action


def tree_minimax_for_min(tree, tree_values):
    """
    This function returns the best action for the minimizer using alpha-beta pruning

    :param tree: tree structure showing parent-child relationships
    :type tree: dict
    :param tree_values: leaf node values
    :type tree_values: dict
    :return: best action for the minimizer
    :rtype: str
    """
    best_action = None  # Initialize best action found
    best_value = 10  # Start with worst possible value for minimizer

    for action in tree:  # Try each possible action
        value = tree_max_value(action, tree, tree_values, -10, 10)  # Get value after opponent responds optimally
        if value > best_value:  # Check if this action is better for minimizer
            best_value = value  # Update best value found
            best_action = action  # Remember this action

    return best_action  # Return the optimal action


def tree_max_value(node, tree, tree_values, alpha=-10, beta=10):
    """
    This function returns the maximum value achievable using alpha-beta pruning

    :param node: current node in the tree
    :type node: str
    :param tree: tree structure showing parent-child relationships
    :type tree: dict
    :param tree_values: leaf node values
    :type tree_values: dict
    :param alpha: best value maximizer can guarantee
    :type alpha: int
    :param beta: best value minimizer can guarantee
    :type beta: int
    :return: maximum value achievable from this node
    :rtype: int
    """

    if node in tree_values:  # Check if it's a leaf node
        return tree_values[node]  # Return the leaf value

    best = -10  # Initialize with worst possible value for maximizer
    children = tree[node]  # Get children of current node
    for child in children:  # Try each child
        result = tree_min_value(child, tree, tree_values, alpha, beta)  # Get value from minimizer's response
        alpha = max(alpha, result)  # Update maximizer's guarantee
        best = max(best, result)  # Update best value found
        if alpha >= beta:  # Check if pruning is possible
            break  # Prune remaining branches

    return best  # Return best value achievable


def tree_min_value(node, tree, tree_values, alpha=-10, beta=10):
    """
    This function returns the minimum value achievable using alpha-beta pruning

    :param node: current node in the tree
    :type node: str
    :param tree: tree structure showing parent-child relationships
    :type tree: dict
    :param tree_values: leaf node values
    :type tree_values: dict
    :param alpha: best value maximizer can guarantee
    :type alpha: int
    :param beta: best value minimizer can guarantee
    :type beta: int
    :return: minimum value achievable from this node
    :rtype: int
    """

    if node in tree_values:  # Check if it's a leaf node
        return tree_values[node]  # Return the leaf value

    best = 10  # Initialize with worst possible value for minimizer
    children = tree[node]  # Get children of current node
    for child in children:  # Try each child
        result = tree_max_value(child, tree, tree_values, alpha, beta)  # Get value from maximizer's response
        beta = min(beta, result)  # Update minimizer's guarantee
        best = min(best, result)  # Update best value found
        if alpha >= beta:  # Check if pruning is possible
            break  # Prune remaining branches

    return best  # Return best value achievable


def main():
    tree = {'A': ['B', 'C', 'D'],
            'B': ['E', 'F', 'G'],
            'C': ['H', 'I', 'J'],
            'D': ['K', 'L', 'M']}

    tree_values = {
               "E": 4, "F":8,"G": 6,
               "H": 7, "I": 3,"J": 9,
               "K": 2, "L": 7, "M": 8}


if __name__ == "__main__":
    main()