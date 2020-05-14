"""
Wolf, sheep, vegetables and farmers crossing the river

Farmers need to transport wolves, sheep, vegetables and themselves to the other side of the river. Only the farmer can
row a boat, and the boat is relatively small, except for the farmer.

If there is no farmer watching, sheep will steal food, wolves will eat sheep
"""

from enum import Enum
from collections import deque
from copy import deepcopy


class LOCATION(Enum):
    LEFT = "left"
    RIGHT = "right"


class ACTION(Enum):
    TRAVEL_BY_SELF = "farmer travel to other side alone"
    TRAVEL_WITH_WOLF = "farmer travel to other side with wolf"
    TRAVEL_WITH_SHEEP = "farmer travel to other side with sheep"
    TRAVEL_WITH_VEGE = "farmer travel to other side with vegetable"
    COME_BACK_BY_SELF = "farmer come back from other side alone"
    COME_BACK_WITH_WOLF = "farmer come back from other side with wolf"
    COME_BACK_WITH_SHEEP = "farmer come back from other side with sheep"
    COME_BACK_WITH_VEGE = "farmer come back from other side with vegetable"


class ItemState:
    def __init__(self):
        self.farmer = LOCATION.LEFT
        self.wolf = LOCATION.LEFT
        self.sheep = LOCATION.LEFT
        self.vegetable = LOCATION.LEFT
        self.action = "Init"

    def __eq__(self, other):
        return (
            self.farmer == other.farmer
            and self.wolf == other.wolf
            and self.sheep == other.sheep
            and self.vegetable == other.vegetable
        )

    def __str__(self):
        return str(self.current_state)

    @property
    def current_state(self):
        return (
            f"farmer: {self.farmer}",
            f"wolf: {self.wolf}",
            f"sheep: {self.sheep}",
            f"vege: {self.vegetable}",
        )

    def is_final_state(self):
        return (
            self.farmer == LOCATION.RIGHT
            and self.wolf == LOCATION.RIGHT
            and self.sheep == LOCATION.RIGHT
            and self.vegetable == LOCATION.RIGHT
        )


def is_state_valid(current_state: ItemState):
    if (
        current_state.wolf == current_state.sheep
        and not current_state.sheep == current_state.farmer
    ) or (
        current_state.vegetable == current_state.sheep
        and not current_state.sheep == current_state.farmer
    ):
        return False

    return True


def process_farmer_travel_alone(state: ItemState):
    if state.farmer != LOCATION.LEFT:
        return False

    state.farmer = LOCATION.RIGHT
    state.action = ACTION.TRAVEL_BY_SELF.value

    return is_state_valid(state)


def process_farmer_travel_with_wolf(state: ItemState):
    if state.farmer != LOCATION.LEFT or state.wolf != LOCATION.LEFT:
        return False

    state.farmer = LOCATION.RIGHT
    state.wolf = LOCATION.RIGHT
    state.action = ACTION.TRAVEL_WITH_WOLF.value

    return is_state_valid(state)


def process_farmer_travel_with_sheep(state: ItemState):
    if state.farmer != LOCATION.LEFT or state.sheep != LOCATION.LEFT:
        return False

    state.farmer = LOCATION.RIGHT
    state.sheep = LOCATION.RIGHT
    state.action = ACTION.TRAVEL_WITH_SHEEP.value

    return is_state_valid(state)


def process_farmer_travel_with_vegetable(state: ItemState):
    if state.farmer != LOCATION.LEFT or state.vegetable != LOCATION.LEFT:
        return False

    state.farmer = LOCATION.RIGHT
    state.vegetable = LOCATION.RIGHT
    state.action = ACTION.TRAVEL_WITH_VEGE.value

    return is_state_valid(state)


def process_farmer_come_back_alone(state: ItemState):
    if state.farmer != LOCATION.RIGHT:
        return False

    state.farmer = LOCATION.LEFT
    state.action = ACTION.COME_BACK_BY_SELF.value

    return is_state_valid(state)


def process_farmer_come_back_with_wolf(state: ItemState):
    if state.farmer != LOCATION.RIGHT or state.wolf != LOCATION.RIGHT:
        return False

    state.farmer = LOCATION.LEFT
    state.wolf = LOCATION.LEFT
    state.action = ACTION.COME_BACK_WITH_WOLF.value

    return is_state_valid(state)


def process_farmer_come_back_with_sheep(state: ItemState):
    if state.farmer != LOCATION.RIGHT or state.sheep != LOCATION.RIGHT:
        return False

    state.farmer = LOCATION.LEFT
    state.sheep = LOCATION.LEFT
    state.action = ACTION.COME_BACK_WITH_SHEEP.value

    return is_state_valid(state)


def process_farmer_come_back_with_vegetable(state: ItemState):
    if state.farmer != LOCATION.RIGHT or state.vegetable != LOCATION.RIGHT:
        return False

    state.farmer = LOCATION.LEFT
    state.vegetable = LOCATION.LEFT
    state.action = ACTION.COME_BACK_WITH_VEGE.value

    return is_state_valid(state)


def is_processed_state(states: [deque], current_state: deque):
    for previous_state in states:
        if previous_state == current_state:
            return True

    return False


def explore_ways_to_cross_river():
    yield process_farmer_come_back_alone
    yield process_farmer_come_back_with_vegetable
    yield process_farmer_come_back_with_sheep
    yield process_farmer_come_back_with_wolf
    yield process_farmer_travel_alone
    yield process_farmer_travel_with_vegetable
    yield process_farmer_travel_with_sheep
    yield process_farmer_travel_with_wolf


def explore_solution(states: deque):
    current_state = states[-1]
    if current_state.is_final_state():
        print("\n --- Solutions ---")
        for state in states:
            print(state.action)
        return

    for can_cross_river in explore_ways_to_cross_river():
        next_state = deepcopy(current_state)
        if can_cross_river(next_state):

            # make sure we never visited the node before
            # not for prevent self-loop as it does not exist in binary tree
            # mainly for speed up process to prevent re-exploring path explored already
            if not is_processed_state(states, next_state):
                # append the next state and move forward
                states.append(next_state)
                # DFS method
                explore_solution(states)
                # pop off all the previous state, so that it resume explore other branch
                states.pop()


if __name__ == "__main__":
    states = deque()
    init_state = ItemState()

    states.append(init_state)
    explore_solution(states)

    assert len(states) == 1
