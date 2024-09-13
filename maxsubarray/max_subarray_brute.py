import sys
from typing import List


def find_max_subarray(arr: List) -> List:
    size = len(arr)
    max_sum = arr[0]
    start = 0
    end = 0
    for i in range(1, size+1):
        for j in range(i, size+1):
            possible_max_sum = sum(arr[i:j])
            if possible_max_sum > max_sum:
                max_sum = possible_max_sum
                start = i
                end = j
    return arr[start:end]


if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3, 5]
    result = find_max_subarray(arr)
    print(*result, sep=", ")
