"""
Identify the nodes that require for stay in order all points in graph to stay connected.
"""
from collections import defaultdict, deque
from itertools import product, chain


def convert_points_to_graph(points):
    graph = defaultdict(list)
    for point in points:
        graph[point[0]].append(point[1])
    return graph


def dfs_explore_paths(graph, start):
    queue = deque()
    queue.append([start])

    while queue:
        current_path = queue.popleft()
        node = current_path[-1]
        # print(f" -- starting node: {node}")

        for neighbour in graph[node]:
            if neighbour not in current_path:
                new_path = list(current_path)
                new_path.append(neighbour)

                # print(f"  --- new path {new_path}")
                if neighbour not in graph.keys():  # reached to the end of node in graph
                    # print(f" +++ not more sub path")
                    yield new_path
                else:
                    queue.append(
                        new_path
                    )  # add to queue when there are additional connections


def store_paths(current_path, paths):
    route = (current_path[0], current_path[-1])
    paths[route].append(current_path[1:-1])


def get_articulation_points_from_paths(paths):
    articulation_points = set()
    for current_route in paths.values():

        if len(current_route) > 1:
            ## Option 1
            #     [
            #         articulation_points.update(set(a) - set(b))
            #         for a, b in product(current_route, current_route)
            #     ]
            # Option 2
            articulation_points.update(chain.from_iterable(current_route))
        else:
            articulation_points.update({current_route[0][0]})
    return articulation_points


def is_point_has_multi_paths(point, graph):
    return point in graph and len(graph[point]) > 1


def locate_paths_and_articulation_points(start_point, points):
    graph = convert_points_to_graph(points)
    connected_paths = defaultdict(list)
    for current_path in dfs_explore_paths(graph, start_point):
        print(f"path: {current_path}")
        store_paths(current_path, connected_paths)

    articulation_points = get_articulation_points_from_paths(connected_paths)
    print(f"articulation_points = {articulation_points}\n")


"""
Test Case 1
                     1
                   /  \                              DFS with direct graph
                  2    3
                  \  /  \
                   4     6
                    \     \
                     5     7 - 8
"""
print(" =========  Test Case 1 ========= ")
points_set_one = [(1, 2), (1, 3), (2, 4), (3, 4), (3, 6), (6, 7), (4, 5), (7, 8)]
locate_paths_and_articulation_points(1, points_set_one)

"""
Test Case 2
                     1
                   /  \                              DFS with direct graph
                  2    3
                /  \  /  \
               4    5  -  6
                   /       \
                  7        8 - 9
"""
print(" =========  Test Case 2 ========= ")
points_set_two = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (3, 5),
    (3, 6),
    (5, 6),
    (5, 7),
    (6, 8),
    (8, 9),
]
locate_paths_and_articulation_points(1, points_set_two)
