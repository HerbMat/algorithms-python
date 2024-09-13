from typing import List


def binary_search(arr: List, el: int, begin: int, end: int) -> int:
    middle = begin + (end - begin) // 2
    if begin >= end:
        return -1
    elif arr[middle] == el:
        return middle
    elif arr[middle] < el:
        return binary_search(arr, el, middle+1, end)
    elif arr[middle] > el:
        return binary_search(arr, el, begin, middle-1)


if __name__ == '__main__':
    arr = [26, 31, 41, 41, 58, 59]
    result = binary_search(arr, 1, 0, len(arr)-1)
    print(f' {result}')
