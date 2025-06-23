cost_dict = {}  # Dictionary to store the cost of each position
goal = None     # Global variable to store the goal

def solve_maze(maze, start, end):
    """
    This function uses A* algorithm to find a path from start to end in a maze.

    :param maze: a 2D list representing the maze
    :type maze: list
    :param start: start position
    :type start: tuple
    :param end: end position
    :type end: tuple
    :return: the path from start to end if it exists, False otherwise
    :rtype: bool
    """
    global cost_dict  # This tells Python you want to modify the global variable
    global goal # This tells Python you want to modify the global variable
    goal = end # Set the goal
    print(f"Debug: goal set to {goal}")

    cost_dict.clear()  # reset dictionary


    visited = []  # List to keep track of positions we've already checked
    queue = [start]  # Queue of positions to check next (starts with just the start position)
    cost_dict[start] = 0 # Set the cost of the start position to 0


    while queue:  # Keep looping while there are positions to check
        best = 0  # Initialize best position index to 0
        for i in range(len(queue)):  # Loop through all positions in queue
            if h(queue[i]) + g(queue[i]) < h(queue[best]) + g(queue[best]):  # If current position is with the sum of cost and distance is the best
                best = i  # Update best position index

        current = queue.pop(best)  # Take the closest position to end from queue

        if current == end:  # If we reached the end position, we found a path!
            return True  # Success! Path exists


        if current in visited:  # If we already checked this position, skip it

            continue  # Go to next iteration of while loop

        visited.append(current)  # Mark this position as visited so we don't check it again
        row, col = current  # Get current row and column from the tuple

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Check all 4 directions: right, down, left, up
            new_row = row + dr  # Calculate new row by adding direction change
            new_col = col + dc  # Calculate new column by adding direction change

            if (0 <= new_row < len(maze) and  # New row is within maze bounds
                    0 <= new_col < len(maze[0]) and  # New column is within maze bounds
                    maze[new_row][new_col] != '*' and  # New position is not a wall
                    (new_row, new_col) not in visited):  # We haven't been here before


                if (new_row, new_col) not in cost_dict:  # If this position is not in our cost dictionary
                    cost_dict[(new_row, new_col)] = g(current) + 1  # Set the cost to the current position + 1
                    queue.append((new_row, new_col))  # Add this valid new position to our queue to check later

                else:
                        if g(current) + 1 < cost_dict[(new_row, new_col)]:
                            cost_dict[(new_row, new_col)] = g(current) + 1
                            queue.append((new_row, new_col))  # Add this valid new position to our queue to check later


    return False  # If we exit the while loop, queue is empty and we never found end


def h(n):
    """
    This function returns the manhattan distance between two positions

    :param n: our current position
    :type n: tuple
    :return: the manhattan distance between two positions
    :rtype: int
    """
    return abs(n[0] - goal[0]) + abs(n[1] - goal[1])  # Calculate Manhattan distance between two positions


def g(n):
    """
    This function calculates the cost to reach a given position in the maze.

    :param n: the current position as a tuple (row, col)
    :type n: tuple
    :return: the cost to reach for the given position
    :rtype: int
    """
    return cost_dict[n] # Return the cost of the current position


def main():
    maze = []
    for i in range(10):
        maze.append(list(input()))

    start = (0, 0)
    goal_pos = (9, 9)

    if solve_maze(maze, start, goal_pos):
        print("Path exists!")
    else:
        print("Path does not exist.")

    if solve_maze(maze, start, goal_pos):
        print("Path exists!")
    else:
        print("Path does not exist.")


if __name__ == "__main__":
    main()

