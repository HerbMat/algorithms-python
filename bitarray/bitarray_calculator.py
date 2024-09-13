from typing import List


def add(first: List, second: List) -> List:
    rest = 0
    sum_bit = []
    for a, b in zip(reversed(first), reversed(second)):
        result = a + b + rest
        if result >= 2:
            rest = 1
        else:
            rest = 0
        sum_bit.insert(0, result % 2)
    sum_bit.insert(0, rest)
    return sum_bit


if __name__ == '__main__':
    first = [1, 0, 1, 0, 0, 1]
    second = [1, 1, 1, 0, 0, 0]
    arr = add(first, second)
    print(*arr, sep=", ")
