from typing import List


def find_new_point(first_point: tuple[int, int], second_point: tuple[int, int], last_point: tuple[int, int]) -> tuple[int, int]:
    new_vector = (first_point[0] - second_point[0], first_point[1] - second_point[1])

    return last_point[0] - new_vector[0], last_point[1] - new_vector[1]


def find_missing_point(points: tuple[tuple[int, int], tuple[int, int], tuple[int, int]]) -> tuple[int, int]:
    results = [find_new_point(points[0], points[1], points[2]), find_new_point(points[1], points[2], points[0]),
               find_new_point(points[2], points[0], points[1])]
    final_result = results[0]

    for i in range(1, 3):
        if abs(final_result[0]) + abs(final_result[1]) > abs(results[i][0]) + abs(results[i][1]):
            final_result = results[i]
    return final_result


if __name__ == '__main__':
    result = find_missing_point(((1, 1), (2, 3), (4, 2)))
    print(f"Point ({result[0]},{result[1]})")
