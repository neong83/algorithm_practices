"""
Map:
    _   _   _   _   _   _              _ is blank spot
    _   _   _   _   _   _              o is post office location
    _   _   _   _   o   _               suggestion is to use BFS to solve this problem
    _   o   _   _   _   _
    _   _   _   _   _   o
    _   _   _   o   _   _
    _   _   _   _   _   _
"""
from typing import Dict
from collections import defaultdict


def build_map_data(post_offices) -> Dict:
    matrix = defaultdict(dict)
    for x in range(6):
        for y in range(6):
            has_post_office = 0 if (x, y) in post_offices else -1
            # print(f"x={x} y={y} has_office={has_post_office}")
            matrix[x][y] = has_post_office
    return matrix


def possible_directions(x, y):
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1


def move_to(point, map):
    for x, y in possible_directions(*point):
        if x in map.keys() and y in map[x].keys():
            yield (x, y)


def explore_map(office, city_map):
    print(f"--- start at {office}")
    visited_locations = set()
    stops = [office]
    travel_path = []
    found_path = False

    while stops and not found_path:
        place = stops.pop(0)
        travel_path.append(place)
        print(f"visited place: {place}")
        visited_locations.add(place)

        for new_place in move_to(place, city_map):
            if new_place not in visited_locations:
                stops.append(new_place)
            if (
                city_map[new_place[0]][new_place[1]] == 0
                and not new_place == office
            ):
                travel_path.append(new_place)
                found_path = True
                print(f"path {travel_path}")
                break


post_office_locations = [(1, 3), (3, 5), (4, 2), (5, 4)]
city_map = build_map_data(post_office_locations)
print(city_map)
for office in post_office_locations:
    explore_map(office, city_map)
