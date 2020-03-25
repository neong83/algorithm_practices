from dataclasses import dataclass
from typing import Type
from random import randint


@dataclass
class Node:
    value: int
    left: Type["Node"]
    right: Type["Node"]


class BinaryTree:
    def __init__(self):
        self.root: Node = None

    def __obtain_proper_node_for_new_node(self, new_node, root_node, child_node):
        if not child_node:
            return root_node
        return self.get_start_node_for_node(new_node, child_node)

    def get_start_node_for_node(self, new_node, root):
        if not root:
            return

        # print(f" - start node ={root}, new node ={new_node}")
        if root.value > new_node.value:
            return self.__obtain_proper_node_for_new_node(new_node, root, root.left)

        # root.value <= new_node.value:
        return self.__obtain_proper_node_for_new_node(new_node, root, root.right)

    def add(self, new_node: Node, start_node):
        # print(f"start node = {start_node}, new node = {new_node}")
        if not start_node:
            self.root = new_node
            return

        if start_node.value > new_node.value:
            start_node.left = new_node
        else:
            start_node.right = new_node

    def to_list(self, parent_node):
        # print(f"start node: {parent_node}")
        if parent_node.left:
            # print("  call left")
            yield from self.to_list(parent_node.left)
        yield parent_node.value

        if parent_node.right:
            # print("  call right")
            yield from self.to_list(parent_node.right)


a = [10, 8, 12, 7, 9, 11, 13]
print(f"original list = {a}")
binary_tree = BinaryTree()
for i in a:
    node = Node(i, None, None)
    start_node = binary_tree.get_start_node_for_node(node, binary_tree.root)
    binary_tree.add(node, start_node)
print(f"nodes = {binary_tree.root}")
print(f"sorted list = {list(binary_tree.to_list(binary_tree.root))}")


for tests in range(10000):
    array = []
    for i in range(randint(10, 100)):
        array.append(randint(1, 100))

    binary_tree = BinaryTree()
    for i in array:
        node = Node(i, None, None)
        start_node = binary_tree.get_start_node_for_node(node, binary_tree.root)
        binary_tree.add(node, start_node)

    previous_value = -1
    for i in binary_tree.to_list(binary_tree.root):
        assert (
            previous_value <= i
        ), f"previous value = {previous_value}, current value = {i}"
        previous_value = i
