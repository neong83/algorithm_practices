array = [1, 3, 5, 5, 6, 6, 7, 8, 10, 10]


# using set
def get_unique_number_from_array_using_set(array):
    # convert into set to remove all duplicates
    array_set = set(array)

    # start to remove item from list to only contain duplicates numbers
    for i in array_set:
        array.remove(i)

    # find the difference between 2 set, which is the unique number
    unique_array = array_set - set(array)

    return list(unique_array)


result_from_set = get_unique_number_from_array_using_set(array)

array = [1, 3, 5, 5, 6, 6, 7, 8, 10, 10]


# use hashmap / dict
def get_unique_number_from_array_using_dict(array):
    number_hash = {}

    for i in array:
        if i in number_hash.keys():
            number_hash[i] += 1
        else:
            number_hash[i] = 1

    results = []
    for num, counts in number_hash.items():
        if counts == 1:
            results.append(num)

    return results


result_from_dict = get_unique_number_from_array_using_dict(array)

assert set(result_from_set) == set(
    result_from_dict
), f"result from set={result_from_set}, result from dict={result_from_dict}"
