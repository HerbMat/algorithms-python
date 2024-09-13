from typing import List


def linear_search(arr: List, searched_val: int) -> int:
    size = len(arr)
    for i in range(0, size):
        if arr[i] == searched_val:
            return i
    return -1


if __name__ == '__main__':
    arr = [31, 41, 59, 26, 41, 58]
    i = linear_search(arr, 31)
    print(f'{i} \n')
    i = linear_search(arr, 226)
    print(f'{i} \n')
