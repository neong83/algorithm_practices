from collections import defaultdict

a = [0, 0, 0, 1, 2, 5, 0, 0, 2]

# build a hash map to store this data structure, but avoid storing 0
# and you will need to able to access the value inside the data structure
# like a[0] = 0, a[3] = 1

DICT_SIZE = 4


def convert_list_into_dict(array):
    hash = defaultdict(dict)
    for index, value in enumerate(array):
        if value:  # ignore zero
            global_index = index % DICT_SIZE
            hash[global_index][index] = value
    return hash


def get_value_from_hash(hash, position):
    global_index = position % DICT_SIZE
    if global_index in hash.keys() and position in hash[global_index].keys():
        return hash[global_index][position]
    return 0


hash = convert_list_into_dict(a)
print(hash)
for i in range(len(a)):
    assert a[i] == get_value_from_hash(
        hash, i
    ), f"position={i}, a[{i}]={a[i]}, hash[{i}]={get_value_from_hash(a, i)}"
