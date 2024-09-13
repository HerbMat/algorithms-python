from typing import List
from binarysearch import binary_search


def find_if_exists_sum_equal_x(arr: List, x: int) -> int:
    for i in range(0, len(arr)):
        value_to_check = x - arr[i]
        search_array = [val for j, val in enumerate(arr) if j != i]
        index = binary_search(search_array, value_to_check, 0, len(search_array))
        if index >= 0:
            return index
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    result = find_if_exists_sum_equal_x(arr, 3)
    print(f' {result}')
