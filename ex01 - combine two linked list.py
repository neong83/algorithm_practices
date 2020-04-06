a = [1, 5, 10, 15, 20]
b = [5, 11, 12, 13, 14]

# result:
# 1, 14, 5, 13, 10, 12, 15, 11, 20, 5

# first attempt in array
combined_list = []
reversed_b = b[::-1]
for i in range(len(a)):
    combined_list += [a[i], reversed_b[i]]
print(combined_list)

# ==================================
from dataclasses import dataclass
from typing import Type, List


@dataclass
class Node:
    num: int
    next: Type["Node"]


def build_linked_list_with_reversed_order(original_list) -> Node:
    reversed_list = original_list[::-1]
    leading_node = None

    for i in reversed_list:
        leading_node = Node(i, leading_node)

    return leading_node


def extract_linked_list_to_list(extracted_list: List[int], node: Node):
    if node:
        extracted_list.append(node.num)
        extracted_list = extract_linked_list_to_list(extracted_list, node.next)
    return extracted_list


leading_node_a = build_linked_list_with_reversed_order(a)
leading_node_b = build_linked_list_with_reversed_order(b)

extracted_list_b = []
extract_linked_list_to_list(extracted_list_b, leading_node_b)

assert extracted_list_b == b, f'extracted list={extracted_list_b}, original list={b}'

current_node = leading_node_a
combined_list_2 = []
while current_node:
    combined_list_2 += [current_node.num, extracted_list_b.pop()]
    if current_node.next:
        current_node = current_node.next
    else:
        current_node = None
print(combined_list_2)
