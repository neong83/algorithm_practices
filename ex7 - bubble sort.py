def bubble_sort(array):
    n = len(array)

    while n >= 0:
        for i in range(n):
            print(f"i = {i}  n = {n}")
            if i + 1 < n and array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
        n -= 1


array_of_unsorted_int = [1, 3, 5, 2, 8, 6, 7]

bubble_sort(array_of_unsorted_int)
print(a)
