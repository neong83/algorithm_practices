"""
Map:
    _   _   _   _   _   _              _ is blank spot
    _   _   _   _   _   _              o is post office location
    _   _   _   _   o   _               suggestion is to use BFS to solve this problem
    _   o   _   _   _   _
    _   _   _   _   _   o
    _   _   _   o   _   _
"""
from typing import Dict
from collections import defaultdict, deque


def build_map_data(post_offices) -> Dict:
    matrix = defaultdict(dict)
    for x in range(6):
        for y in range(6):
            has_post_office = 0 if (x, y) in post_offices else -1
            # print(f"x={x} y={y} has_office={has_post_office}")
            matrix[x][y] = has_post_office
    return matrix


def is_post_office(point, city_map):
    return True if city_map[point[0]][point[1]] == 0 else False


def possible_directions(x, y):
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1


def get_neighbours_from_node(point, map):
    for x, y in possible_directions(*point):
        if x in map.keys() and y in map[x].keys():
            yield (x, y)


def bfs_nearest_office_in_map(office, city_map):
    print(f"--- start at {office}")
    visited_locations = set()
    queue = deque()
    queue.append([office])

    while queue:
        path = queue.popleft()  # get the first path from queue
        node = path[-1]  # get the last location from current path
        print(f"  - current location: {node}")
        if node not in visited_locations:
            for neighbour in get_neighbours_from_node(node, city_map):
                new_path = list(path)  # make a new copy of the current path
                new_path.append(neighbour)  # add the new location to the path
                queue.append(new_path)
                print(f"   - new path: {new_path}")

                if neighbour != office and is_post_office(neighbour, city_map):
                    return new_path

            visited_locations.add(node)

    return -1


post_office_locations = [(1, 3), (3, 5), (4, 2), (5, 4)]
city_map = build_map_data(post_office_locations)
print(city_map)
for office in post_office_locations:
    path = bfs_nearest_office_in_map(office, city_map)
    print(f"Path to closest post office from {office} to {path[-1]} is '{path}'")
