from random import randrange
from typing import List

from hybridsort import partition


def randomized_partition(arr: List[int], p: int, r: int) -> int:
    i = randrange(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)


def randomized_select(arr: List[int], p, r, i) -> int:
    if p == r:
        return arr[p]
    q = randomized_partition(arr, p, r)
    k = q - p + 1
    if i == k:
        return arr[q]
    elif i < k:
        return randomized_select(arr, p, q - 1, i)
    return randomized_select(arr, q + 1, r, i - k)


def randomized_select_iter(arr: List[int], p, r, i) -> int:
    last = r
    first = p
    el_pos = i
    while True:
        if first == last:
            return arr[first]
        q = randomized_partition(arr, first, last)
        k = q - first + 1
        if el_pos == k:
            return arr[q]
        elif el_pos < k:
            last = q - 1
        else:
            first = q + 1
            el_pos = i - k


if __name__ == "__main__":
    arr = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]

    print(f"{randomized_select(arr, 0, len(arr) - 1, 6)}")
    print(f"{randomized_select_iter(arr, 0, len(arr) - 1, 6)}")
