"""
heap sort
"""

a = [4, 10, 3, 5, 1]


def heapify(array, parent_node, index):
    left_child_node = index * 2 + 1
    right_child_node = index * 2 + 2
    largest_node = index

    # print(
    #     f"left node={left_child_node}, right node={right_child_node}, "
    #     f"parent node={largest_node}, array={array}"
    # )

    # if left index exist and larger than parent
    if left_child_node < parent_node and array[left_child_node] > array[largest_node]:
        largest_node = left_child_node

    # if right index exist and larger than parent
    if right_child_node < parent_node and array[right_child_node] > array[largest_node]:
        largest_node = right_child_node

    if largest_node != index:
        # print(f"     swapping {index} with {largest_node}")
        array[index], array[largest_node] = array[largest_node], array[index]  # swap
        # print(f"     new array = {array}")
        heapify(array, parent_node, largest_node)


def heap_soft(array):
    length = len(array) - 1

    # prepared the heapify tree
    for i in range((length // 2), -1, -1):
        # print(f"- iterated {i} times, array form heapify {array}")
        heapify(array, length, i)
        # print(f"- result = {array}")

    # swap with re-heapify the tree again
    for i in range(length, 0, -1):
        # print(f"+ iterated {i} times, array form heapify {array}")
        # print(f"     swapping {0} with {i}")
        array[0], array[i] = array[i], array[0]
        # print(f"     new array = {array}")
        heapify(array, i, 0)
        # print(f"+ result = {array}")


print(f"original value = {a}")
heap_soft(a)
print(f"sorted value = {a}")
