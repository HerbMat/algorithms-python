from typing import List


def insertion_sort(arr: List):
    size = len(arr)
    for i in range(1, size):
        for j in range(i, 0, -1):
            if arr[j] > arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
            else:
                break


def insertion_sort_binary_search(arr: List):
    size = len(arr)
    for i in range(1, size):
        new_index = binary_search_new_sort_pos(arr, arr[i], 0, i-1)
        temp = arr[i]
        for j in range(i-1, new_index-1, -1):
            arr[j+1] = arr[j]
        arr[new_index] = temp


def binary_search_new_sort_pos(arr: List, el: int, begin: int, end: int) -> int:
    middle = begin + (end - begin) // 2
    if begin >= end:
        if arr[begin] <= el:
            return begin + 1
        else:
            return begin
    elif arr[middle] == el:
        return middle
    elif arr[middle] < el:
        return binary_search_new_sort_pos(arr, el, middle+1, end)
    elif arr[middle] > el:
        return binary_search_new_sort_pos(arr, el, begin, middle-1)


if __name__ == '__main__':
    arr = [31, 41, 59, 26, 41, 58]
    insertion_sort_binary_search(arr)
    print(*arr, sep=", ")
