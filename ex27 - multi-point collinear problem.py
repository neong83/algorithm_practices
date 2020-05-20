"""
一个几何平面上有 N 个点，根据欧氏（欧几里得）几何原理，每两个点可以连成一条直线，
N 个点可以连成很多条直线。当然，也会有多个点共线的情况出现，现在我们的问题是，在
这 N 个点中，找出哪两个点组成的直线上包含最多的点，也就是找出含有最多点的那条直线。

There are N points on a geometric plane. According to Euclidean (Euclidean) geometry,
every two points can be connected into a straight line, and N points can be connected
into many straight lines. Of course, there will also be multiple points collinear,
and now our problem is to find out which of the N points contains the most points
on the line formed by the two points, that is, to find the the straight line with the
most points.

Answer:
(x: 30.0, y: 43.0), (x: 12.0, y: 13.0), (x: 57.0, y: 88.0), (x: 48.0, y: 73.0), (x: 39.0, y: 58.0), (x: 3.0, y: -2.0), (x: -912.0, y: -1741.0)

Visual validation: https://www.desmos.com/calculator/mhq4hsncnh
"""

from dataclasses import dataclass
from math import isclose

EPSILON = 1 * 10 ** (-8)


@dataclass
class Point:
    x: float
    y: float

    def __str__(self):
        return f"(x: {self.x}, y: {self.y})"


@dataclass
class Slope:
    k: float
    point_index: int

    def __str__(self):
        return f"{self.k}(index={self.point_index})"

    def __repr__(self):
        return self.__str__()


def partition(slopes: [Slope], low: int, high: int):
    pivot = slopes[high].k
    i = low

    for j in range(low, high):
        if slopes[j].k < pivot:
            slopes[i], slopes[j] = slopes[j], slopes[i]
            i += 1

    slopes[i], slopes[high] = slopes[high], slopes[i]
    return i


def quick_sort(slops: [Slope], low: int, high: int):
    if low < high:
        mid = partition(slops, low, high)
        quick_sort(slops, low, mid - 1)
        quick_sort(slops, mid + 1, high)


def calculate_slope(p0: Point, p1: Point):
    if isclose(p0.x, p1.x, abs_tol=EPSILON):
        return float("inf")  # infinite

    return (p1.y - p0.y) / (p1.x - p0.x)


def get_max_point_list(slopes: [Slope]):
    max_length, start_position, current_length = 0, 0, 1

    for i in range(len(slopes)):
        if not isclose(slopes[i].k, slopes[i - 1].k, abs_tol=EPSILON):
            if current_length > max_length:
                max_length = current_length
                start_position = i

                current_length = 1
        else:
            current_length += 1

    return max_length, start_position - max_length


def get_straight_lines_from_points(points: Point):
    max_points = 0
    point_indexes = []

    number_of_points_in_graph = len(points)

    for i in range(number_of_points_in_graph):
        slopes: [Slope] = []
        for j in range(number_of_points_in_graph):
            if i == j:
                continue

            k = calculate_slope(points[i], points[j])
            slopes.append(Slope(k, j))

        # arrange / sort slope with the same value
        quick_sort(slopes, 0, len(slopes) - 1)
        # sorted(slopes, key=lambda slope: slope.k)

        max_length, start_point = get_max_point_list(slopes)

        if max_length > max_points:
            max_points = max_length

            # get the index of those points from slope for final result
            point_indexes.clear()
            for k in range(start_point, start_point + max_length + 1):
                point_indexes.append(slopes[k].point_index)

    return point_indexes


if __name__ == "__main__":
    test_points: [Point] = [
        Point(1301.0, 1256.0),  # 0
        Point(21.0, 28.0),
        Point(6222.0, 52.0),
        Point(-7071.0, -6264.0),
        Point(-6406.0, -1183.0),
        Point(-2358.0, -129.0),  # 5
        Point(-912.0, -1741.0),
        Point(39.0, 58.0),
        Point(3.0, -2.0),
        Point(57.0, 88.0),
        Point(1502.0, -7726.0),  # 10
        Point(30.0, 43.0),
        Point(-6932.0, 363.0),
        Point(-4422.0, -5669.0),
        Point(12.0, 13.0),
        Point(5874.0, -9005.0),  # 15
        Point(48.0, 73.0),
        Point(-2358.0, 129.0),
        Point(7703.0, 1806.0),
        Point(-3559.0, -1078.0),
        Point(-4808.0, -2166.0),  # 20
    ]

    point_indexes_in_test_points = get_straight_lines_from_points(test_points)

    point_output_list = []
    for index in point_indexes_in_test_points:
        point_output_list.append(str(test_points[index]))

    print(f"There are {len(point_indexes_in_test_points)} points on the same line")
    print(", ".join(point_output_list))
