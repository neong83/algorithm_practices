"""
    interploation search

    # interploation and binary are both require a SORTED list

    let said you have the follow phone number prefix array, and you are looking for 1144
    0011, 0022, 0033, 1144, 1166, 1188, 3322, 3344, 3399

    instead of using binary search in the middle, or linear search from the left.
    we only want to search the subset with same prefix, like inside [1144, 1166, 1188]

    to calculate the mid

    mid = low + ((high - low) / (A[high] - A[low])) * (x - A[low])  # x is the value we are seeking
"""
data = list(range(1_000_001))
search_value = 999_999


def linear_search(search_value, data):
    for index, value in enumerate(data):
        if value == search_value:
            print(f"Element is found after {index} attempts")


def binary_search(search_value, data):
    left = 0
    right = len(data) - 1
    attempts = 1

    founded = False
    while not founded:
        mid = ((right - left) // 2) + left
        # print(f"left {left}")
        # print(f'right {right}')
        # print(f"mid {mid}")
        if data[mid] == search_value:
            print(f"Element is found after {attempts} attempts")
            founded = True

        if search_value < data[mid]:
            right = mid - 1
        else:
            left = mid + 1

        attempts += 1


def interploation_search(search_value, data):
    left = 0
    right = len(data) - 1
    attempts = 1

    founded = False
    while not founded:
        mid = int(
            left
            + ((right - left) / data[right] - data[left]) * (search_value - data[left])
        )
        # print(f"left {left}")
        # print(f"right {right}")
        # print(f"mid {mid}")
        if data[mid] == search_value:
            print(f"Element is found after {attempts} attempts")
            founded = True

        if search_value < data[mid]:
            right = mid - 1
        else:
            left = mid + 1

        attempts += 1


linear_search(search_value, data)
binary_search(search_value, data)
interploation_search(search_value, data)
