"""
merge sort
"""

a = [1, 8, 7, 10, 4, 3, 2, 5, 9]


def merge_arrays_into_array_with_sorted(first_array, second_array):
    if not second_array:
        return first_array

    i = 0
    j = 0
    merged_array = []

    print(
        f"first array = {first_array}, second array = {second_array}, merged array = {merged_array}"
    )

    while i < len(first_array) or j < len(second_array):
        print(f"i = {i}, j = {j}, merged array = {merged_array}")
        if j >= len(second_array) or (
                i < len(first_array) and first_array[i] < second_array[j]
        ):
            merged_array.append(first_array[i])
            i += 1

        elif i >= len(first_array) or (
                j < len(second_array) and first_array[i] > second_array[j]
        ):
            merged_array.append(second_array[j])
            j += 1

    print(
        f"first array = {first_array}, second array = {second_array}, merged array = {merged_array}"
    )

    return merged_array


def merge_sort(array):
    sorted_array = [[x] for x in array]
    print(f"splited array = {sorted_array}")

    while len(sorted_array) > 1:
        merged_array = []
        for i in range(0, len(sorted_array), 2):
            if i + 1 < len(sorted_array):
                second_array = sorted_array[i + 1]
            else:
                second_array = None

            merged_array.append(
                merge_arrays_into_array_with_sorted(sorted_array[i], second_array)
            )
            print(f"merged array = {merged_array}")
        sorted_array = merged_array
        print(f"sub array = {sorted_array}")
    return sorted_array[0]


print(f"original array = {a}, sorted array = {merge_sort(a)}")
