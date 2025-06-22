goal = ("x", "y") # Global variable to store the goal position

def solve_maze(maze, start, end):
    """
    This function uses a GFS algorithm to find a path from start to end in a maze.

    :param maze: a 2D list representing the maze
    :type maze: list
    :param start: start position
    :type start: tuple
    :param end: end position
    :type end: tuple
    :return: the path from start to end if it exists, False otherwise
    :rtype: bool
    """
    visited = []  # List to keep track of positions we've already checked
    queue = [start]  # Queue of positions to check next (starts with just the start position)

    while queue:  # Keep looping while there are positions to check
        best = 0  # Initialize best position index to 0
        for i in range(len(queue)):  # Loop through all positions in queue
            if h(queue[i]) + g(queue[i]) < h(queue[best]) + g(queue[best]):  # If current position is closer to end than best
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
    places = set()
    if n == (0, 0):
        return 0

    

def main():
    global goal

    maze = []
    for i in range(10):
        maze.append(list(input()))

    start = (0, 0)
    goal = (int(input()), int(input()))  # Get goal from input

    if solve_maze(maze, start, goal):
        print("Path exists!")
    else:
        print("Path does not exist.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()