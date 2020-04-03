from typing import Type
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: Type["Node"]


@dataclass
class AdjacencyList:
    head: Node


class BFSGraph:
    def __init__(self, size):
        self.array: [AdjacencyList] = [None] * size

    def add(self, source: int, destination: int):
        new_node = Node(destination, None)
        if self.array[source]:
            new_node.next = self.array[source].head
            self.array[source].head = new_node
        else:
            self.array[source] = AdjacencyList(new_node)

    def explore(self, start: int):
        visited_set = set()  # using set because `x in/not in l` is O(1)
        stops = [start]

        while stops:
            place = stops.pop(0)
            print(f"Visited place: {place}")
            visited_set.add(place)
            travel_path: Node = self.array[place].head

            while travel_path:
                if travel_path.value not in visited_set:
                    stops.append(travel_path.value)
                    visited_set.add(travel_path.value)
                else:
                    travel_path = travel_path.next


graph = BFSGraph(size=6)
graph.add(0, 1)
graph.add(0, 2)
graph.add(1, 4)
graph.add(1, 3)
graph.add(1, 2)
graph.add(3, 1)
graph.add(4, 1)
graph.add(2, 5)
graph.add(2, 1)
graph.add(5, 2)

graph.explore(start=0)
