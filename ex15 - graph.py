"""
graph data structure
https://www.python.org/doc/essays/graphs/

1. build it out
2. find path from A -> B
3. find all path
4. find shortest path
5. find locations in map that connect to other location (except headquarter A)

Test Data
    A -> B  => 1 -> 2
    A -> C
    B -> C
    B -> D
    C -> D
    D -> C
    E -> F
    F -> C
"""
from collections import defaultdict

paths = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 3), (5, 6), (6, 3)]


def convert_path_to_graph(routes):
    graph = defaultdict(list)
    for a, b in routes:
        graph[a].append(b)
    return graph


def find_import_locations_in_graph(locations, graph, visited_locations):
    for location in locations:

        if location not in visited_locations:
            visited_locations.append(location)
            if location in graph.keys():
                yield location

            yield from find_import_locations_in_graph(
                graph[location], graph, visited_locations
            )


print(f"paths = {paths}")
graph = convert_path_to_graph(paths)
print(f"graph = {dict(graph)}")
route_for_root_location = graph[paths[0][0]]
# print(route_for_root_location)
print(
    f"import routes = {list(find_import_locations_in_graph(route_for_root_location, graph, []))}"
)
