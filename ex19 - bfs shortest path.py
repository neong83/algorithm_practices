"""
Using BFS to locate the shortest path between 2 points
                    A                  in terms of search from A -> D, we weill get
                /   |    \                                           [A]
               B  - E     C                                       /   |      \
               |  /     /  \                                 [A, B]  [A,C]  [A,E]
               D       F    G                                 /
                                                        [A,B,D] -> last node == stop, found and return
"""
from collections import deque

# sample graph implemented as a dictionary
graph = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["A", "B", "D"],
    "F": ["C"],
    "G": ["C"],
}


def bfs_shortest_path(graph, start, stop):
    visited = set()
    queue = deque()
    queue.append([start])

    if start == stop:
        print(f"Start = Stop")

    while queue:
        path = queue.popleft()
        node = path[-1]
        print(f"Node - {node}")

        if node not in visited:
            neighbours = graph[node]
            print(f" -- neighbours: {neighbours}")

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                print(f" -- new path: {new_path}")

                queue.append(new_path)

                if neighbour == stop:
                    return new_path

            visited.add(node)

    return None


start = "G"
stop = "D"
path = bfs_shortest_path(graph, start, stop)
print(f"shortest path from {start} to {stop} is '{path}'")
