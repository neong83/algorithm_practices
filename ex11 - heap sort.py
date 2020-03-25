"""
heap sort
"""

from random import randint

a = [4, 10, 3, 5, 1]


def heapify_first_attempt(array, parent_node, index):
    left_child_node = index * 2
    right_child_node = index * 2 + 1
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
        heapify_first_attempt(array, parent_node, largest_node)


def heapify_second_attempt(array, parent_node, index):
    left_child_node = index * 2
    right_child_node = index * 2 + 1
    had_swapped = False

    # print(
    #     f"left node={left_child_node}, right node={right_child_node}, "
    #     f"parent node={parent_node}, array={array}"
    # )

    # if left index exist and larger than parent
    if left_child_node < parent_node and array[left_child_node] > array[index]:
        array[left_child_node], array[index] = (
            array[index],
            array[left_child_node],
        )
        had_swapped = True

    # if right index exist and larger than parent
    if right_child_node < parent_node and array[right_child_node] > array[index]:
        array[right_child_node], array[index] = (
            array[index],
            array[right_child_node],
        )
        had_swapped = True

    if had_swapped:
        heapify_second_attempt(array, parent_node, left_child_node)
        heapify_second_attempt(array, parent_node, right_child_node)


def heap_soft(array, heapify_method):
    length = len(array) - 1
    result = array.copy()

    # prepared the heapify tree
    for i in range((length // 2), -1, -1):
        # print(f"- iterated {i} times, array form heapify {array}")
        heapify_method(result, length, i)
        # print(f"- result = {array}")

    # swap with re-heapify the tree again
    for i in range(length, 0, -1):
        # print(f"+ iterated {i} times, array form heapify {array}")
        # print(f"     swapping {0} with {i}")
        result[0], result[i] = result[i], result[0]
        # print(f"     new array = {array}")
        heapify_method(result, i, 0)
        # print(f"+ result = {array}")
    return result


print(f"original value = {a}")
print(f"sorted value with first attempt = {heap_soft(a, heapify_first_attempt)}")
print(f"sorted value with second attempt = {heap_soft(a, heapify_second_attempt)}")

for tests in range(1000):
    array = []

    for i in range(randint(10, 100)):
        array.append(randint(1, 100))

    first_attempt_result = heap_soft(array, heapify_first_attempt)
    second_attempt_result = heap_soft(array, heapify_second_attempt)

    assert (
        first_attempt_result == second_attempt_result
    ), f"array={array}, first attempt={first_attempt_result}, second attempt={second_attempt_result}"
