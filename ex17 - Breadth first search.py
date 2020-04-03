from typing import Type
from dataclasses import dataclass
from abc import ABC, abstractmethod
from collections import defaultdict

# version 1 with linked list


class BaseBFSGraph(ABC):
    @abstractmethod
    def add(self, source, destination):
        pass

    @abstractmethod
    def explore(self, start):
        pass


@dataclass
class Node:
    value: int
    next: Type["Node"]


@dataclass
class AdjacencyList:
    head: Node


class BFSGraphWithLinkList(BaseBFSGraph):
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
            print(place, end=" ")
            visited_set.add(place)
            travel_path: Node = self.array[place].head

            while travel_path:
                if travel_path.value not in visited_set:
                    stops.append(travel_path.value)
                    visited_set.add(travel_path.value)
                else:
                    travel_path = travel_path.next


class BFSGraphWithList(BaseBFSGraph):
    def __init__(self, size):
        del size
        self.array = defaultdict(list)

    def add(self, source, destination):
        self.array[source].append(destination)

    def explore(self, start):
        queue = [start]
        visited = set(queue)

        while queue:
            last_place = queue.pop(0)
            print(last_place, end=" ")

            for i in self.array[last_place]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)


def test(graph_class: BaseBFSGraph):
    graph = graph_class(size=6)
    graph.add(0, 2)
    graph.add(0, 1)
    graph.add(1, 4)
    graph.add(1, 3)
    graph.add(1, 2)
    graph.add(3, 1)
    graph.add(4, 1)
    graph.add(2, 5)
    graph.add(2, 1)
    graph.add(5, 2)

    graph.explore(start=0)


print(f"Test BFSGraph with Linked List")
test(BFSGraphWithLinkList)
print("")
print(f"Test BFSGraph with List")
test(BFSGraphWithList)
