"""
There are 3 buckets available for user to measure water with, 3 L, 5 L, and 8 L.
None of them has any indicater / marks to tell current level of water inside the bucket.

We had filled up 8 L bucket with waters and would like split it equally between 2 people
"""

from dataclasses import dataclass
from collections import deque
from copy import deepcopy
from enum import Enum


class CAPACITY(Enum):
    THREE_L = 3
    FIVE_L = 5
    EIGHT_L = 8


class Bucket:
    def __init__(self, capacity, water=0):
        self.capacity = capacity
        self.water = water

    def __str__(self):
        return f"{self.capacity}L bucket with {self.water} water"

    def __eq__(self, other):
        return self.capacity == other.capacity and self.water == other.water

    def is_full(self):
        return self.capacity == self.water

    def has_water(self):
        return self.water > 0

    def remain_capacity(self):
        return self.capacity - self.water

    def add_water(self, water):
        available_space = self.remain_capacity()
        if available_space > 0:
            self.water += water if available_space > water else available_space

    def dump_water(self, water):
        if self.water >= water:
            self.water -= water
        else:
            self.water = 0


@dataclass
class Action:
    poll_from: CAPACITY
    add_to: CAPACITY
    amount_of_water: int

    def __repr__(self):
        return f"poll from: {self.poll_from.value}L, add to: {self.add_to.value}L, water amount: {self.amount_of_water}"


class BucketState:
    def __init__(self):
        self.three_L_bucket = Bucket(capacity=CAPACITY.THREE_L.value)
        self.five_L_bucket = Bucket(capacity=CAPACITY.FIVE_L.value)
        self.eight_L_bucket = Bucket(
            capacity=CAPACITY.EIGHT_L.value, water=CAPACITY.EIGHT_L.value
        )
        self.action = None

    def __eq__(self, other):
        return (
            self.three_L_bucket.water == other.three_L_bucket.water
            and self.five_L_bucket.water == other.five_L_bucket.water
            and self.eight_L_bucket.water == other.eight_L_bucket.water
        )

    def get_bucket_by_capacity(self, bucket_capacity: CAPACITY):
        switcher = {
            CAPACITY.EIGHT_L: self.eight_L_bucket,
            CAPACITY.FIVE_L: self.five_L_bucket,
            CAPACITY.THREE_L: self.three_L_bucket,
        }
        return switcher.get(bucket_capacity, "Unknow capacity")

    def get_current_state(self):
        return (
            self.eight_L_bucket.water,
            self.five_L_bucket.water,
            self.three_L_bucket.water,
        )

    def is_final_state(self):
        return (
            self.eight_L_bucket.water == 4
            and self.five_L_bucket.water == 4
            and self.three_L_bucket.water == 0
        )

    def is_water_can_move_between(
        self, poll_from_bucket_capacity: CAPACITY, add_to_bucket_capacity: CAPACITY
    ):
        poll_from = self.get_bucket_by_capacity(poll_from_bucket_capacity)
        add_to = self.get_bucket_by_capacity(add_to_bucket_capacity)

        return (
            not poll_from == add_to and poll_from.has_water() and not add_to.is_full()
        )

    def set_action(self, poll_from, add_to, amount_of_water):
        self.action = Action(poll_from, add_to, amount_of_water)

    def take_action(
        self, poll_from_bucket_capacity: CAPACITY, add_to_bucket_capcity: CAPACITY
    ):
        poll_from = self.get_bucket_by_capacity(poll_from_bucket_capacity)
        add_to = self.get_bucket_by_capacity(add_to_bucket_capcity)

        if poll_from.has_water() and not add_to.is_full():
            dump_water = (
                add_to.remain_capacity()
                if poll_from.water > add_to.remain_capacity()
                else poll_from.water
            )
            add_to.add_water(dump_water)
            poll_from.dump_water(dump_water)
            self.set_action(
                poll_from_bucket_capacity, add_to_bucket_capcity, dump_water
            )


def get_water_quality_for_visual_validation(buckets, action):
    def get_index_by_capacity(capacity):
        switcher = {CAPACITY.EIGHT_L: 0, CAPACITY.FIVE_L: 1, CAPACITY.THREE_L: 2}
        return switcher.get(capacity, "Invalid capacity")

    poll_from = get_index_by_capacity(action.poll_from)
    add_to = get_index_by_capacity(action.add_to)

    buckets[poll_from] -= action.amount_of_water
    buckets[add_to] += action.amount_of_water


def is_processed_state(states: [deque], current_state: deque):
    for previous_state in states:
        if previous_state == current_state:
            return True

    return False


def way_to_move_waters():
    for bucket_one in CAPACITY:
        for bucket_two in CAPACITY:
            yield bucket_one, bucket_two


def explore_next_move(current_state: BucketState):
    for poll_from_bucket, add_to_bucket in way_to_move_waters():
        if current_state.is_water_can_move_between(poll_from_bucket, add_to_bucket):
            new_bucket_state = deepcopy(current_state)
            new_bucket_state.take_action(poll_from_bucket, add_to_bucket)
            yield new_bucket_state


def search_solution(states: deque):
    current_state = states[-1]

    if current_state.is_final_state():
        print(" --- Solutions ---")
        visual_validation_bucket = [8, 0, 0]

        for state in states:
            action = state.action

            if action:
                get_water_quality_for_visual_validation(
                    visual_validation_bucket, action
                )
                print(
                    f"poll {action.amount_of_water}L of water from '{action.poll_from}L bucket' to '{action.add_to}L bucket' -> {visual_validation_bucket}"
                )
            else:
                print(f"water start with 8L, 5L, 3L -> '{visual_validation_bucket}'")

    # trying to use BFS to find the shortest solution to handle this problem
    for next_move in explore_next_move(current_state):
        if not is_processed_state(states, next_move):
            states.append(next_move)
            search_solution(states)
            states.pop()


if __name__ == "__main__":
    init_state = BucketState()
    states = deque()

    states.append(init_state)

    search_solution(states)
