"""
There are 3 buckets available for user to measure water with, 3 L, 5 L, and 8 L.
None of them has any indicater / marks to tell current level of water inside the bucket.

We had filled up 8 L bucket with waters and would like split it equally between 2 people
"""

from dataclasses import dataclass
from collections import deque


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
    poll_from: int
    add_to: int
    amount_of_water: int

    def __repr__(self):
        return f"poll from: {self.poll_from}L, add to: {self.add_to}L, water amount: {self.amount_of_water}"


class BucketState:
    def __init__(self, actions: [Action] = []):
        self.three_L_bucket = Bucket(capacity=3)
        self.five_L_bucket = Bucket(capacity=5)
        self.eight_L_bucket = Bucket(capacity=8, water=8)
        self.actions = actions

    def __iter__(self):
        yield self.eight_L_bucket
        yield self.five_L_bucket
        yield self.three_L_bucket

    def get_bucket_from_size(self, size):
        if size == 3:
            return self.three_L_bucket
        elif size == 5:
            return self.five_L_bucket
        else:
            return self.eight_L_bucket

    def get_current_state(self):
        return (
            self.eight_L_bucket.water,
            self.five_L_bucket.water,
            self.three_L_bucket.water,
        )

    def resume_state(self):
        for current_action in self.actions:
            poll_from = self.get_bucket_from_size(current_action.poll_from)
            add_to = self.get_bucket_from_size(current_action.add_to)

            poll_from.dump_water(current_action.amount_of_water)
            add_to.add_water(current_action.amount_of_water)

    def is_final_state(self):
        return (
            self.eight_L_bucket.water == 4
            and self.five_L_bucket.water == 4
            and self.three_L_bucket.water == 0
        )

    def set_action(self, poll_from, add_to, amount_of_water):
        self.actions.append(Action(poll_from, add_to, amount_of_water))

    def take_action(self, poll_from_bucket_capacity: int, add_to_bucket_capacity: int):
        poll_from = self.get_bucket_from_size(poll_from_bucket_capacity)
        add_to = self.get_bucket_from_size(add_to_bucket_capacity)

        if poll_from.has_water() and not add_to.is_full():
            dump_water = (
                add_to.remain_capacity()
                if poll_from.water > add_to.remain_capacity()
                else poll_from.water
            )
            add_to.add_water(dump_water)
            poll_from.dump_water(dump_water)
            self.set_action(
                poll_from_bucket_capacity, add_to_bucket_capacity, dump_water
            )


def explore_next_move(current_state: BucketState):
    for poll_from_bucket in current_state:
        for add_to_bucket in current_state:
            if (
                not poll_from_bucket == add_to_bucket
                and poll_from_bucket.has_water()
                and not add_to_bucket.is_full()
            ):
                new_bucket_state = BucketState(list(current_state.actions))
                new_bucket_state.resume_state()

                new_bucket_state.take_action(
                    poll_from_bucket.capacity, add_to_bucket.capacity
                )

                yield new_bucket_state


def search_solution(bucket_state: BucketState):
    visited_status = set()
    queue = deque()
    queue.append(bucket_state)

    # trying to use BFS to find the shortest solution to handle this problem
    while queue:
        current_state = queue.popleft()
        latest_status = current_state.get_current_state()

        if latest_status not in visited_status:
            for next_move in explore_next_move(current_state):
                queue.append(next_move)

                if next_move.is_final_state():
                    return next_move

            visited_status.add(latest_status)


def get_water_quality_for_visual_validation(buckets, action):
    def get_index_by_capacity(capacity):
        switcher = {8: 0, 5: 1, 3: 2}
        return switcher.get(capacity, "Invalid capacity")

    poll_from = get_index_by_capacity(action.poll_from)
    add_to = get_index_by_capacity(action.add_to)

    buckets[poll_from] -= action.amount_of_water
    buckets[add_to] += action.amount_of_water


if __name__ == "__main__":
    bucket_state = BucketState()
    solution = search_solution(bucket_state)

    if solution:
        visual_validation_bucket = [8, 0, 0]
        print(f"water start with 8L, 5L, 3L -> '{visual_validation_bucket}'")
        for action in solution.actions:
            get_water_quality_for_visual_validation(visual_validation_bucket, action)
            print(
                f"poll {action.amount_of_water}L of water from '{action.poll_from}L bucket' to '{action.add_to}L bucket' -> {visual_validation_bucket}"
            )
