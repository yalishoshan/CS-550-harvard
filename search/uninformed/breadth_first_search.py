def bfs(tree, start, goal):
    """
    This function implements the breadth first search

    :param tree: the graph
    :type tree: dict
    :param start:
    :type start: str
    :param goal:
    :type goal: str
    :return: true if the goal is found, false otherwise
    :rtype: bool
    """
    explored_set = set()  # Track visited nodes, prevents infinite loops
    shallow = [start]  # FIFO structure for breadth-first exploration

    while shallow:  # Continue until no more nodes to explore
        current = shallow.pop(0)  # Get oldest node (FIFO behavior)

        if current in explored_set:  # Skip already visited nodes
            continue  # Go to next iteration

        if current == goal:  # Check if we found the target
            return True  # Success - path exists

        explored_set.add(current)  # Mark current node as visited

        for neighbor in tree[current]:  # Check all adjacent nodes
            if neighbor not in explored_set:  # Skip already visited neighbors
                shallow.append(neighbor)  # Add to queue for future exploration

    return False  # No path found - goal unreachable


def main():
    tree = {'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []}
    print(bfs(tree, 'A', 'F'))


if __name__ == '__main__':
    main()
