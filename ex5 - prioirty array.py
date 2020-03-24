a = [0, 0, 0, 1, 2, 5, 0, 0, 2]


def resort_priority_array(array, current_index):
    if current_index == 0:
        return array

    if array[current_index] < array[current_index - 1]:
        temp = array[current_index - 1]
        array[current_index - 1] = array[current_index]
        array[current_index] = temp

        array = resort_priority_array(array, current_index - 1)
    return array


def convert_array_to_priority_array(array):
    priority_array = []
    for i in array:
        priority_array.append(i)
        priority_array = resort_priority_array(priority_array, len(priority_array) - 1)

    return priority_array


print(convert_array_to_priority_array(a))
