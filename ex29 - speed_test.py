from random import randint
from time import time


def bubble_sort(arr):
    # n = len(arr)
    #
    # while n >= 0:
    #     for i in range(n):
    #         if i + 1 < n and arr[i] > arr[i + 1]:
    #             arr[i], arr[i + 1] = arr[i + 1], arr[i]
    #     n -= 1

    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):
    # bad
    # n = len(arr)
    #
    # while n >= 0:
    #     for i in range(n):
    #         value = arr[i]
    #         j = i - 1
    #
    #         for j in range(j, -2, -1):
    #             if arr[j] > value:
    #                 arr[j + 1] = arr[j]
    #             else:
    #                 break
    #
    #         arr[j + 1] = value
    #
    #     n -= 1
    # good
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def validation():
    test_array = [6, 5, 4, 3, 2, 1]
    a = test_array.copy()
    b = test_array.copy()

    bubble_sort(a)
    print(f"bubble sort: {a}")

    insertion_sort(b)
    print(f"insertion sort: {b}")


def speedTest():
    test_arrays = []
    for _ in range(1000):
        test = []
        for _ in range(200):
            test.append(randint(1, 101))
        test_arrays.append(test)

    a = test_arrays.copy()
    b = test_arrays.copy()

    start_time = time()
    for test in a:
        bubble_sort(test)
    print(f"bubble sort took {time() - start_time} seconds")

    start_time = time()
    for test in b:
        insertion_sort(test)
    print(f"insertion sort took {time() - start_time} seconds")


# validation()
speedTest()
