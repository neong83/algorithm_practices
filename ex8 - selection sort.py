a = [1, 8, 5, 3, 11, 6, 15]


def selection_sort(array):
    for i in range(len(array)):
        swap_from = i
        swap_to = -1

        for j in range(i + 1, len(array)):
            if array[swap_from] > array[j] and (
                    swap_to == -1 or array[swap_to] > array[j]
            ):
                swap_to = j
        if swap_to > 0:
            temp = array[swap_from]
            array[swap_from] = array[swap_to]
            array[swap_to] = temp

    return array


print(selection_sort(a))
