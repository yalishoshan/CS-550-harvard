import csv
import sys

from source_code import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.

    :param directory: path to directory containing CSV files
    :type directory: str
    :return: None (modifies global dictionaries)
    :rtype: None
    """

    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:  # Open people CSV file with UTF-8 encoding
        reader = csv.DictReader(f)  # Create CSV reader that returns dictionaries
        for row in reader:  # Process each person row
            people[row["id"]] = {  # Store person data using their ID as key
                "name": row["name"],  # Person's full name
                "birth": row["birth"],  # Birth year
                "movies": set()  # Initialize empty set for movies they starred in
            }
            if row["name"].lower() not in names:  # Check if name is new (case-insensitive)
                names[row["name"].lower()] = {row["id"]}  # Create new set with this person's ID
            else:
                names[row["name"].lower()].add(row["id"])  # Add ID to existing name set (handles duplicate names)

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:  # Open movies CSV file
        reader = csv.DictReader(f)  # Create CSV reader for movies
        for row in reader:  # Process each movie row
            movies[row["id"]] = {  # Store movie data using movie ID as key
                "title": row["title"],  # Movie title
                "year": row["year"],  # Release year
                "stars": set()  # Initialize empty set for actors who starred in this movie
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:  # Open stars CSV file (person-movie relationships)
        reader = csv.DictReader(f)  # Create CSV reader for star relationships
        for row in reader:  # Process each person-movie relationship
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])  # Add movie to person's filmography
                movies[row["movie_id"]]["stars"].add(row["person_id"])  # Add person to movie's cast
            except KeyError:  # Handle case where person or movie doesn't exist in our data
                pass  # Skip invalid relationships


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    :param source: person_id of starting actor
    :type source: str
    :param target: person_id of target actor
    :type target: str
    :return: list of (movie_id, person_id) pairs forming the shortest path, None if no path exists
    :rtype: list or None
    """

    explored_set = set()  # Track visited nodes, prevents infinite loops
    queue = [source]  # FIFO structure for breadth-first exploration
    parent = dict()  # Maps person_id to (parent_person_id, connecting_movie_id) for path reconstruction

    if source == target:  # Check if source and target are the same person
        return []  # Return empty path for same person

    while queue:  # Continue until no more nodes to explore
        current = queue.pop(0)  # Get oldest node (FIFO behavior for BFS)

        if current in explored_set:  # Skip already visited nodes
            continue  # Go to next iteration

        explored_set.add(current)  # Mark current node as visited

        for movie_id, person_id in neighbors_for_person(current):  # Check all adjacent nodes (co-stars)
            if person_id not in explored_set and person_id not in parent:  # Skip already visited people and those already in parent chain
                parent[person_id] = (current, movie_id)  # Record how we reached this person (from current via movie_id)
                queue.append(person_id)  # Add person to queue for future exploration

                if person_id == target:  # Check if we found the target person
                    path = []  # Initialize path list for reconstruction
                    current_person = target  # Start path reconstruction from target

                    while current_person in parent:  # Follow parent chain backwards to source
                        parent_person, movie = parent[current_person]  # Get parent and connecting movie
                        path.append((movie, current_person))  # Add connection to path
                        current_person = parent_person  # Move to parent for next iteration

                    path.reverse()  # We built it backwards, so reverse to get source-to-target order
                    return path  # Return the shortest path

    return None  # No path found - goal unreachable


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.

    :param person_id: ID of person to find co-stars for
    :type person_id: str
    :return: set of (movie_id, person_id) pairs representing connections
    :rtype: set
    """

    movie_ids = people[person_id]["movies"]  # Get all movies this person appeared in
    neighbors = set()  # Initialize set to store neighbor connections
    for movie_id in movie_ids:  # Loop through each movie this person was in
        for person_id in movies[movie_id]["stars"]:  # Loop through all actors in this movie
            neighbors.add((movie_id, person_id))  # Add movie-person pair as potential connection
    return neighbors  # Return all possible connections through shared movies


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.

    :param name: actor's name to search for
    :type name: str
    :return: person_id if found, None if not found or selection failed
    :rtype: str or None
    """

    person_ids = list(names.get(name.lower(), set()))  # Get all person IDs matching this name (case-insensitive)
    if len(person_ids) == 0:  # Check if no matches found
        return None  # Return None if person not found
    elif len(person_ids) > 1:  # Check if multiple people have same name
        print(f"Which '{name}'?")  # Ask user to clarify which person they mean
        for person_id in person_ids:  # Show all people with this name
            person = people[person_id]  # Get person details
            name = person["name"]  # Get full name
            birth = person["birth"]  # Get birth year
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")  # Display person info for selection
        try:
            person_id = input("Intended Person ID: ")  # Get user's choice
            if person_id in person_ids:  # Validate user selected valid ID
                return person_id  # Return selected person ID
        except ValueError:  # Handle invalid input
            pass  # Fall through to return None
        return None  # Return None if selection failed
    else:
        return person_ids[0]  # Return the single matching person ID


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    print(names, people, movies)

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


if __name__ == "__main__":
    main()