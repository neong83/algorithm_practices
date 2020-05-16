"""
Given m numbers (in order to facilitate peopel's mental or oral calculations, they are
generally less than 10), use add, subtract, multiply, and divide those numbers in various
combinations to see if the result can be equal to 24?

1 <= m <= 4
"""

from dataclasses import dataclass


@dataclass
class Number:
    num: float
    num_string: str


def add(left: Number, right: Number) -> Number:
    return Number(left.num + right.num, f"({left.num_string} + {right.num_string})")


def subtract(left: Number, right: Number) -> Number:
    return Number(left.num - right.num, f"({left.num_string} - {right.num_string})")


def multiply(left: Number, right: Number) -> Number:
    return Number(left.num * right.num, f"({left.num_string} * {right.num_string})")


def divide(left: Number, right: Number) -> Number:
    if right.num == 0:
        return None
    return Number(left.num / right.num, f"({left.num_string} / {right.num_string})")


def find_equation_equals_to_24(numbers: [Number], operations):
    size = len(numbers)

    if size == 1:
        if int(numbers[0].num) == 24:
            print(f"{numbers[0].num_string} = {numbers[0].num}")
        return

    for i in range(size):
        for j in range(size):
            if i == j:
                continue

            for operation in operations:
                result = operation(numbers[i], numbers[j])

                if result:
                    sub_numbers = [result]

                    for k in range(size):
                        if not k == i and not k == j:
                            sub_numbers.append(numbers[k])

                    find_equation_equals_to_24(sub_numbers, operations)


if __name__ == "__main__":
    set_one = [Number(3, "3"), Number(3, "3"), Number(7, "7"), Number(7, "7")]
    set_two = [Number(1, "1"), Number(5, "5"), Number(4, "4"), Number(7, "7")]
    set_three = [Number(2, "2"), Number(5, "5"), Number(6, "6"), Number(9, "9")]
    set_four = [Number(1, "1"), Number(3, "3"), Number(5, "5"), Number(7, "7")]

    operations = [add, subtract, multiply, divide]

    for numbers in [set_one, set_two, set_three, set_four]:

        question_title = "\n-----------------\nFind solution for"
        for num in numbers:
            question_title += f"  {num.num_string}  "
        question_title += "  =    24 \n"
        print(question_title)

        find_equation_equals_to_24(numbers, operations)
