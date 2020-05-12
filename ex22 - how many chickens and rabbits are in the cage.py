"""
鸡兔同笼问题。有鸡和兔在一个笼子中，数头共 50 个头，数脚共 120 只脚，问：鸡和兔分别有多少只？

Chicken and rabbit in the same cage. There are chickens and rabbits in a cage with 50 heads and 120 feet. 
Q: How many chickens and rabbits are there?
"""


def count_animals_in_cage():
    animals = []
    # each chicken has 2 feets, 50 of them will only has 100 feet
    for chickens in range(50):
        rabbits = 50 - chickens

        if rabbits * 4 + chickens * 2 == 120:
            animals.append(f"rabbits: {rabbits}, chickens: {chickens}")

    return animals


ways_of_animal_combinations = count_animals_in_cage()
print(
    f"There are {len(ways_of_animal_combinations)} ways for total of 50 chickens and rabbits in a cage with 120 feet")
for way in ways_of_animal_combinations:
    print(way)
