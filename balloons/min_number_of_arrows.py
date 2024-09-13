from typing import Tuple


def find_min_max(points: list[Tuple[int, int]], bursted: list[bool]) -> set[int]:
    values = set()
    length = len(points)
    for i in range(length):
        if not bursted[i]:
            for j in range(points[i][0], points[i][1] + 1):
                values.add(j)
    return values


def burst_balloons(points: list[Tuple[int, int]], bursted: list[bool], point: int) -> list[bool]:
    length = len(points)
    for i in range(length):
        if points[i][0] <= point <= points[i][1]:
            bursted[i] = True
    return bursted


def find_number_of_bursted_elements(points: list[Tuple[int, int]], bursted: list[bool], point: int) -> int:
    length = len(points)
    num_of_bursted_elements = 0
    for i in range(length):
        if not bursted[i]:
            if points[i][0] <= point <= points[i][1]:
                num_of_bursted_elements += 1
    return num_of_bursted_elements


def shoot_arrow(points: list[Tuple[int, int]], bursted: list[bool]) -> int:
    if not all(bursted):
        points_to_be_bursted = find_min_max(points, bursted)
        highest_num_of_bursted_elements = 0
        point_to_burst = -1
        for i in points_to_be_bursted:
            num_of_bursted_elements = find_number_of_bursted_elements(points, bursted, i)
            if num_of_bursted_elements > highest_num_of_bursted_elements:
                point_to_burst = i
                highest_num_of_bursted_elements = num_of_bursted_elements
        if highest_num_of_bursted_elements > 0:
            bursted = burst_balloons(points, bursted, point_to_burst)
            return shoot_arrow(points, bursted) + 1
    return 0


def min_number_of_arrows(points: list[Tuple[int, int]]) -> int:
    length = len(points)
    if length == 0:
        return 0
    if length == 1:
        return 1

    bursted = [False for i in range(length)]

    return shoot_arrow(points, bursted)


if __name__ == '__main__':
    points = [(10, 16), (2, 8), (1, 6), (7, 12)]
    print(f'result = {min_number_of_arrows(points)}')
    points = [(1, 6)]
    print(f'result = {min_number_of_arrows(points)}')
    points = [(13, 16), (2, 8), (1, 6), (9, 12), (20, 22), (21, 30), (20, 27), (26, 34)]
    print(f'result = {min_number_of_arrows(points)}')

