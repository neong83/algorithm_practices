"""
first thing on quick sort is to find pivot
"""

a = [6, 8, 2, 4, 3, 8, 1]


# quick sort with array data structure
def quick_sort(array, low, high):
    # print(f"array={array}, low={low}, high={high}")

    if low > high:
        return array

    mid = low + (high - low) // 2
    # print(f"mid = {mid}")
    pivot = array[mid]

    # handle pivot is larger than number on its right
    if low == high:
        if mid - 1 >= 0 and array[mid - 1] > pivot:
            array[mid], array[mid - 1] = array[mid - 1], array[mid]
        return array

    for i in range(low, mid + 1, 1):
        for j in range(high, mid, -1):
            # print(f"process i={i}, j={j}")
            if array[i] >= pivot > array[j]:
                # print(f"i = {i}, j = {j}, swap {array[i]} with {array[j]}")
                array[i], array[j] = array[j], array[i]
                # print(f"result = {array}")

    # print(f"array = {array}")

    if low < mid:
        array = quick_sort(array, low, mid)
    if mid < high:
        array = quick_sort(array, mid + 1, high)

    return array


print(f"original list = {a}")
print(f"sorted list = {quick_sort(a, 0, len(a) - 1)}")
