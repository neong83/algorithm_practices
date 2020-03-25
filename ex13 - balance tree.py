"""
return unique number form list using balance tree (aka Red-Black tree)

Red-Black tree
1. every node either red or black
2. every None node is Black
3. every red node has two black child nodes
4. every path from node x (root) down to leaf as same number of black nodes
5. the root node is always black
6. new node should be in red

# reference and some of the code copy from here
https://medium.com/@donovan.adams/lets-paint-the-town-red-or-black-a-simple-introduction-to-red-black-trees-in-python-1e9faa34b31e
"""

from dataclasses import dataclass
from typing import Type
from enum import Enum


class NodeColor(Enum):
    RED = "red"
    BLACK = "black"


@dataclass
class Node:
    value: int
    color: NodeColor
    parent: Type["Node"]
    left: Type["Node"]
    right: Type["Node"]


class BalanceTree:
    def __init__(self):
        self.root = None

    def search(self):
        pass

    def left_rotate(self, node: Node):
        sibling = node.right
        node.right = sibling.left

        if sibling.left:
            sibling.left.parent = node
        sibling.parent = node.parent
        if not node.parent:
            self.root = sibling
        else:
            if node == node.parent.left:
                node.parent.left = sibling
            else:
                node.parent.right = sibling
        sibling.left = node
        node.parent = sibling

    def right_rotate(self, node: Node):
        sibling = node.left
        node.right = sibling.right

        if sibling.right:
            sibling.right.parent = node
        sibling.parent = node.parent

        if not node.parent:
            self.root = sibling
        else:
            if node == node.parent.right:
                node.parent.right = sibling
            else:
                node.parent.left = sibling
        sibling.right = node
        node.parent = sibling

    def fix_tree_after_added(self, new_node):
        while (
            new_node.parent
            and new_node.parent.color == NodeColor.RED
            and new_node != self.root
        ):
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle.color == NodeColor.RED:
                    new_node.parent.color = NodeColor.BLACK
                    uncle.color = NodeColor.BLACK
                    new_node.parent.parent.color = NodeColor.RED
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    new_node.parent.color = NodeColor.BLACK
                    new_node.parent.parent.color = NodeColor.RED
                    self.right_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle.color == NodeColor.RED:
                    new_node.parent.color = NodeColor.BLACK
                    uncle.color = NodeColor.BLACK
                    new_node.parent.parent.color = NodeColor.RED
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                    new_node.parent.color = NodeColor.BLACK
                    new_node.parent.parent.color = NodeColor.RED
                    self.left_rotate(new_node.parent.parent)
        self.root.color = NodeColor.BLACK

    def __obtain_node_for_new_node(self, new_node, root, child):
        if not child:
            return root
        return self.find_start_node(new_node, child)

    def find_start_node(self, new_node: Node, root: Node):
        if not root:
            return

        if root.value > new_node.value:
            return self.__obtain_node_for_new_node(new_node, root, root.left)
        return self.__obtain_node_for_new_node(new_node, root, root.right)

    def add(self, new_node: Node, root: Node):
        if not root:
            new_node.color = NodeColor.BLACK
            self.root = new_node
            return

        if root.value > new_node.value:
            root.left = new_node
        else:
            root.right = new_node
        new_node.parent = root

        self.fix_tree_after_added(new_node)

    def to_list(self, root: Node):
        if root.left:
            yield from self.to_list(root.left)
        yield root.value

        if root.right:
            yield from self.to_list(root.right)


a = [10, 8, 12, 7, 9, 11, 13]
print(f"original list = {a}")
binary_tree = BalanceTree()
for i in a:
    node = Node(i, NodeColor.RED, None, None, None)
    start_node = binary_tree.find_start_node(node, binary_tree.root)
    binary_tree.add(node, start_node)
print(f"nodes = {binary_tree.root}")
print(f"sorted list = {list(binary_tree.to_list(binary_tree.root))}")
