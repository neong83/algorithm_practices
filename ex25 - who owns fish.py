"""
It is said that there are five rooms with different colors arranged in a row,
each room contains a person of different nationality, each person drinks a
specific brand of beverage, smokes a specific brand of cigarettes, and raises pets.
There is no two individuals smoke the same brand of cigarettes, or drink the same brand
of beverages, or raise the same pet.

The question is who is raising fish as a pet?

Clues:
1) The British live in a red house
2) Swedes keep dogs as pets
3) Danes drink tea
4) The green house is next to the white house, and it's on its left side
5) The owner of the green house drinks coffee
6) People who smoke Pall Mall cigarettes raise birds
7) People in the yellow house smoke Dunhill cigarettes
8) The person who lives in the middle house drinks milk
9) The Norwegian lives in the first house
10) The person who smokes Blends cigarettes live next to the person who keeps cats
11) The person who raises the horse live next to the person who smokes Dunhill cigarettes
12) People who smoke BlueMaster cigarettes drink beer
13) Germans smoke Prince cigarettes
14) The Norwegian live next to the person living in the Blue House
15) People who smoke Blends cigarettes are next to people who drink mineral water

Solution:
house         nationality   drink         pet           cigarette
YELLOW        NORWAY        WATER         CAT           DUNHILL
BLUE          DANMARK       TEA           HORSE         BLENDS
RED           ENGLAND       MILK          BIRD          PALLMALL
GREEN         GERMAN        COFFEE        FISH          PRINCE
WHITE         SWEDEND       BEER          DOG           BLUEMASTER

Process Time:
Linear process: 45 minutes
Multi-processes process (6 Processes): 4 minutes
"""

from enum import Enum
from dataclasses import dataclass
from multiprocessing import Pool
from copy import deepcopy


class COLOR(Enum):
    BLUE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    WHITE = 4


class NATIONALITY(Enum):
    NORWAY = 0
    DANMARK = 1
    SWEDEND = 2
    ENGLAND = 3
    GERMAN = 4


class DRINK(Enum):
    TEA = 0
    WATER = 1
    COFFEE = 2
    BEER = 3
    MILK = 4


class PET(Enum):
    HORSE = 0
    CAT = 1
    BIRD = 2
    FISH = 3
    DOG = 4


class CIGARETTE(Enum):
    BLENDS = 0
    DUNHILL = 1
    PRINCE = 2
    PALLMALL = 3
    BLUEMASTER = 4


class ItemType(Enum):
    HOUSE = "house"
    NATIONALITY = "nationality"
    DRINK = "drink"
    PET = "pet"
    CIGARETTE = "cigarette"


@dataclass
class Item:
    type: ItemType
    value: Enum


@dataclass
class Clue:
    first_type: ItemType
    first_type_value: Enum
    second_type: ItemType
    second_type_value: Enum


class Group:
    def __init__(self):
        self.item_values = {}


def get_item_value_in_group(group: Group, item_type: ItemType):
    if group and item_type in group.item_values:
        return group.item_values[item_type]


def get_group_index_by_item(groups: [Group], item_type: ItemType, value: Enum):
    for index, group in enumerate(groups):
        if get_item_value_in_group(group, item_type) == value:
            return index

    return -1


def is_group_item_matches_bind_clue(
    groups: [Group], index: int, item_type: ItemType, value: Enum
):
    if not get_item_value_in_group(groups[index], item_type) == value:
        return False
    return True


def are_groups_match_bind_clues(groups: [Group], bind_clues: [Clue]):
    for clue in bind_clues:
        if (
            index := get_group_index_by_item(
                groups, clue.first_type, clue.first_type_value
            )
        ) > -1 and not is_group_item_matches_bind_clue(
            groups, index, clue.second_type, clue.second_type_value
        ):
            return False

    return True


def is_group_item_matches_relation_clue(
    groups: [Group], index: int, item_type: ItemType, value: Enum
):
    if index == 0:
        if not get_item_value_in_group(groups[index + 1], item_type) == value:
            return False
    elif index == len(groups) - 1:
        if not get_item_value_in_group(groups[index - 1], item_type) == value:
            return False
    else:
        if (
            not get_item_value_in_group(groups[index - 1], item_type) == value
            and not get_item_value_in_group(groups[index + 1], item_type) == value
        ):
            return False

    return True


def are_groups_match_relation_clues(groups: [Group], relation_clues: [Clue]):
    for clue in relation_clues:
        if (
            index := get_group_index_by_item(
                groups, clue.first_type, clue.first_type_value
            )
        ) > -1 and not is_group_item_matches_relation_clue(
            groups, index, clue.second_type, clue.second_type_value
        ):
            return False

    return True


def output_group_names():
    output = ""
    for item_type in ItemType:
        output += "{:<14}".format(item_type.value)
    print(output)


def output_group_values(group: Group):
    output = ""
    for item_type in ItemType:
        value = get_item_value_in_group(group, item_type)
        output += "{:<14}".format(value.name if value else "None")
    print(output)


def output_all_groups_value(groups: [Group]):
    output_group_names()
    for group in groups:
        output_group_values(group)
    print("\n")


def validate_if_groups_match_all_clues(groups: [Group]):
    if are_groups_match_bind_clues(
        groups, bind_clues_from_question
    ) and are_groups_match_relation_clues(groups, relation_clues_from_question):
        output_all_groups_value(groups)


def arrange_people_with_cigarettes_in_house(groups: [Group]):
    for option_a in CIGARETTE:
        for option_b in CIGARETTE:
            if option_a == option_b:
                continue
            for option_c in CIGARETTE:
                if option_c == option_b or option_c == option_a:
                    continue
                for option_d in CIGARETTE:
                    if (
                        option_d == option_a
                        or option_b == option_d
                        or option_d == option_c
                    ):
                        continue
                    for option_e in CIGARETTE:
                        if (
                            option_e == option_a
                            or option_e == option_b
                            or option_e == option_c
                            or option_e == option_d
                        ):
                            continue

                        groups[0].item_values[ItemType.CIGARETTE] = option_a
                        groups[1].item_values[ItemType.CIGARETTE] = option_b
                        groups[2].item_values[ItemType.CIGARETTE] = option_c
                        groups[3].item_values[ItemType.CIGARETTE] = option_d
                        groups[4].item_values[ItemType.CIGARETTE] = option_e

                        validate_if_groups_match_all_clues(groups)


def arrange_people_with_pets_in_house(groups: [Group]):
    for option_a in PET:
        for option_b in PET:
            if option_a == option_b:
                continue
            for option_c in PET:
                if option_c == option_b or option_c == option_a:
                    continue
                for option_d in PET:
                    if (
                        option_d == option_a
                        or option_b == option_d
                        or option_d == option_c
                    ):
                        continue
                    for option_e in PET:
                        if (
                            option_e == option_a
                            or option_e == option_b
                            or option_e == option_c
                            or option_e == option_d
                        ):
                            continue

                        groups[0].item_values[ItemType.PET] = option_a
                        groups[1].item_values[ItemType.PET] = option_b
                        groups[2].item_values[ItemType.PET] = option_c
                        groups[3].item_values[ItemType.PET] = option_d
                        groups[4].item_values[ItemType.PET] = option_e

                        arrange_people_with_cigarettes_in_house(groups)


def arrange_people_with_drinks_in_house(groups: [Group]):

    groups[2].item_values[ItemType.DRINK] = DRINK.MILK

    for option_a in DRINK:
        if option_a == DRINK.MILK:
            continue
        for option_b in DRINK:
            if option_b == option_a or option_b == DRINK.MILK:
                continue
            for option_c in DRINK:
                if (
                    option_c == option_a
                    or option_c == option_b
                    or option_c == DRINK.MILK
                ):
                    continue
                for option_d in DRINK:
                    if (
                        option_d == option_a
                        or option_d == option_b
                        or option_d == option_c
                        or option_d == DRINK.MILK
                    ):
                        continue

                    groups[0].item_values[ItemType.DRINK] = option_a
                    groups[1].item_values[ItemType.DRINK] = option_b
                    groups[3].item_values[ItemType.DRINK] = option_c
                    groups[4].item_values[ItemType.DRINK] = option_d

                    arrange_people_with_pets_in_house(groups)


def arrange_nationality_in_house(groups: [Group]):
    groups[0].item_values[ItemType.NATIONALITY] = NATIONALITY.NORWAY

    for option_a in NATIONALITY:
        if option_a == NATIONALITY.NORWAY:
            continue
        for option_b in NATIONALITY:
            if option_b == option_a or option_b == NATIONALITY.NORWAY:
                continue
            for option_c in NATIONALITY:
                if (
                    option_c == option_a
                    or option_c == option_b
                    or option_c == NATIONALITY.NORWAY
                ):
                    continue
                for option_d in NATIONALITY:
                    if (
                        option_d == option_a
                        or option_d == option_b
                        or option_d == option_c
                        or option_d == NATIONALITY.NORWAY
                    ):
                        continue

                    groups[1].item_values[ItemType.NATIONALITY] = option_a
                    groups[2].item_values[ItemType.NATIONALITY] = option_b
                    groups[3].item_values[ItemType.NATIONALITY] = option_c
                    groups[4].item_values[ItemType.NATIONALITY] = option_d

                    arrange_people_with_drinks_in_house(groups)


def arrange_color_for_house(groups: [Group], pools):
    possible_groups = []

    for option_a in COLOR:
        for option_b in COLOR:
            if option_a == option_b:
                continue
            for option_c in COLOR:
                if option_c == option_b or option_c == option_a:
                    continue
                for option_d in COLOR:
                    if (
                        option_d == option_a
                        or option_b == option_d
                        or option_d == option_c
                    ):
                        continue
                    for option_e in COLOR:
                        if (
                            option_e == option_a
                            or option_e == option_b
                            or option_e == option_c
                            or option_e == option_d
                        ):
                            continue

                        groups[0].item_values[ItemType.HOUSE] = option_a
                        groups[1].item_values[ItemType.HOUSE] = option_b
                        groups[2].item_values[ItemType.HOUSE] = option_c
                        groups[3].item_values[ItemType.HOUSE] = option_d
                        groups[4].item_values[ItemType.HOUSE] = option_e

                        for index in range(len(groups) - 1):
                            if (
                                groups[index].item_values[ItemType.HOUSE] == COLOR.GREEN
                                and groups[index + 1].item_values[ItemType.HOUSE]
                                == COLOR.WHITE
                            ):
                                # validate all possible cases in sequential format
                                # arrange_nationality_in_house(groups)

                                possible_groups.append(deepcopy(groups))

    # mapped out all possible groups for 1st level
    # spread and process them on 6 processes
    pools.map(arrange_nationality_in_house, possible_groups)


bind_clues_from_question = [
    Clue(ItemType.HOUSE, COLOR.RED, ItemType.NATIONALITY, NATIONALITY.ENGLAND),
    Clue(ItemType.NATIONALITY, NATIONALITY.SWEDEND, ItemType.PET, PET.DOG),
    Clue(ItemType.NATIONALITY, NATIONALITY.DANMARK, ItemType.DRINK, DRINK.TEA),
    Clue(ItemType.HOUSE, COLOR.GREEN, ItemType.DRINK, DRINK.COFFEE),
    Clue(ItemType.CIGARETTE, CIGARETTE.PALLMALL, ItemType.PET, PET.BIRD),
    Clue(ItemType.HOUSE, COLOR.YELLOW, ItemType.CIGARETTE, CIGARETTE.DUNHILL),
    Clue(ItemType.CIGARETTE, CIGARETTE.BLUEMASTER, ItemType.DRINK, DRINK.BEER),
    Clue(
        ItemType.NATIONALITY, NATIONALITY.GERMAN, ItemType.CIGARETTE, CIGARETTE.PRINCE
    ),
]

relation_clues_from_question = [
    Clue(ItemType.CIGARETTE, CIGARETTE.BLENDS, ItemType.PET, PET.CAT),
    Clue(ItemType.PET, PET.HORSE, ItemType.CIGARETTE, CIGARETTE.DUNHILL),
    Clue(ItemType.NATIONALITY, NATIONALITY.NORWAY, ItemType.HOUSE, COLOR.BLUE),
    Clue(ItemType.CIGARETTE, CIGARETTE.BLENDS, ItemType.DRINK, DRINK.WATER),
]


def test_Checkfunctions(group_size: int):
    def insert_value_into_group(group, color, nationality, drink, pet, cigarette):
        group.item_values[ItemType.HOUSE] = color
        group.item_values[ItemType.NATIONALITY] = nationality
        group.item_values[ItemType.DRINK] = drink
        group.item_values[ItemType.PET] = pet
        group.item_values[ItemType.CIGARETTE] = cigarette

    test_groups = []
    for _ in range(group_size):
        test_groups.append(Group())

    insert_value_into_group(
        test_groups[0],
        COLOR.YELLOW,
        NATIONALITY.NORWAY,
        DRINK.WATER,
        PET.CAT,
        CIGARETTE.DUNHILL,
    )
    insert_value_into_group(
        test_groups[1],
        COLOR.BLUE,
        NATIONALITY.DANMARK,
        DRINK.TEA,
        PET.HORSE,
        CIGARETTE.BLENDS,
    )
    insert_value_into_group(
        test_groups[2],
        COLOR.RED,
        NATIONALITY.ENGLAND,
        DRINK.MILK,
        PET.BIRD,
        CIGARETTE.PALLMALL,
    )
    insert_value_into_group(
        test_groups[3],
        COLOR.GREEN,
        NATIONALITY.GERMAN,
        DRINK.COFFEE,
        PET.FISH,
        CIGARETTE.PRINCE,
    )
    insert_value_into_group(
        test_groups[4],
        COLOR.WHITE,
        NATIONALITY.SWEDEND,
        DRINK.BEER,
        PET.DOG,
        CIGARETTE.BLUEMASTER,
    )

    assert are_groups_match_bind_clues(test_groups, bind_clues_from_question)
    assert are_groups_match_relation_clues(test_groups, relation_clues_from_question)


if __name__ == "__main__":
    GROUP_SIZE = 5
    test_groups = []

    for _ in range(GROUP_SIZE):
        test_groups.append(Group())

    pools = Pool(6)

    test_Checkfunctions(GROUP_SIZE)
    arrange_color_for_house(test_groups, pools)
