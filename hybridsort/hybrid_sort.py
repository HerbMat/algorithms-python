from typing import List

import insertionsort
from insertionsort import insertion_sort_binary_search


def partition(arr: List[int], p: int, r: int) -> int:
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


def quicksort(arr: List[int], p: int, r: int):
    if (p < r) and abs(p - r) > 3:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


def hybrid_sort(arr: List[int], p: int, r: int):
    quicksort(arr, p, r)
    insertion_sort_binary_search(arr)


if __name__ == "__main__":
    arr = [31, 15, 22, 41, 45, 59, 26, 41, 58, 64, 52]
    hybrid_sort(arr, 0, len(arr) - 1)
    print(*arr, sep=",")
