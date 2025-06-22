def dfs(tree, start, goal):
    """
    This function implements the depth first search

    :param tree: the graph
    :type tree: dict
    :param start:
    :type start: str
    :param goal:
    :type goal: str
    :return: true if the goal is found, false otherwise
    :rtype: bool
    """
    explored_set = set()    # Track visited nodes, prevents infinite loops
    stack = [start]         # LIFO structure for depth-first exploration
    if start == goal:       # Check if the start and goal are the same
        return True         # Success

    while stack:                           # Continue until no more nodes to explore
        current = stack.pop()              # Get most recent node (LIFO behavior)

        if current in explored_set:        # Skip already visited nodes
           continue                        # (prevents infinite loops)

        if current == goal:                # Check if we found the target
            return True                    # Success - path exists

        if current not in explored_set:    # Only process unvisited nodes
            explored_set.add(current)      # Mark current node as visited
            for neighbor in tree[current]: # Check all adjacent nodes
                stack.append(neighbor)     # Add to stack for future exploration

    return False                          # No path found - goal unreachable

def main():
    tree = {'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []}
    print(dfs(tree, 'A', 'F'))

if __name__ == '__main__':
    main()