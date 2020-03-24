def bubble_sort(array):
    n = len(array)
    temp = 0

    while n >= 0:
        for i in range(n):
            print(f'i = {i}  n = {n}')
            if i + 1 < n and array[i] > array[i + 1]:
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
        n -= 1
    return array


array_of_unsorted_int = [1, 3, 5, 2, 8, 6, 7]

print(bubble_sort(array_of_unsorted_int))
