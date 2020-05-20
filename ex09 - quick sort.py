"""
first thing on quick sort is to find pivot
"""

# a = [6, 8, 2, 4, 3, 8, 1]
a = [-0.6402359108781127, -0.6151439299123905, 0.20108794197642793, 0.4543383723338165, 0.46107907742998355, 0.10908624229979466, 0.3174806170569898, 0.4520746887966805, 0.44980253585533153, 0.4588405199092222, -9.075129533678757, -1.1906779661016949, 0.4565936337329475, -0.8811410459587956, 0.4633093525179856, 0.560157145195613, 0.8314285714285714, 0.8710968775020016, 0.936734693877551, 1.8108705258506408]
# a = [-881,-640,-615,201,454,109,317,449,452,456,-9075,-1190,458,461,463,560,831,871,936,1810]
# a = [881,640,615,201,454,109,317,449,452,456,9075,1190,458,461,463,560,831,871,936,1810]


# def partition(array, low, high):
#     i = low
#     pivot = array[high]
#
#     for j in range(low, high):
#         if array[j] < pivot:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#
#     array[i], array[high] = array[high], array[i]
#     return i
#
#
# def quick_sort(array, low, high):
#     if low < high:
#         mid = partition(array, low, high)
#
#         quick_sort(array, low, mid - 1)
#         quick_sort(array, mid + 1, high)


# quick sort with array data structure
def quick_sort(array, low, high):
    # print(f"array={array}, low={low}, high={high}")

    if low > high:
        return

    mid = low + (high - low) // 2
    # print(f"mid = {mid}")
    pivot = array[mid]

    # handle pivot is larger than number on its right
    if low == high:
        if mid - 1 >= 0 and array[mid - 1] > pivot:
            array[mid], array[mid - 1] = array[mid - 1], array[mid]
        return

    for i in range(low, mid + 1, 1):
        for j in range(high, mid, -1):
            # print(f"process i={i} ({array[i]}), j={j} ({array[j]})")
            if array[j] < pivot:
                # print(f"i = {i}, j = {j}, swap {array[i]} with {array[j]}")
                array[i], array[j] = array[j], array[i]
                # print(f"result = {array}")

    # print(f"array = {array}")

    if low < mid:
        quick_sort(array, low, mid)
    if mid < high:
        quick_sort(array, mid + 1, high)

    return


print(f"original list = {a}")
quick_sort(a, 0, len(a) - 1)
print(f"sorted list = {a}")
