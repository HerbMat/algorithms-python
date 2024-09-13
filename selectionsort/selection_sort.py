from typing import List


def selection_sort(arr: List):
    size = len(arr)
    min_index = 0
    for i in range(0, size - 1):
        for j in range(i, size):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp


if __name__ == '__main__':
    arr = [31, 41, 59, 26, 41, 58]
    selection_sort(arr)
    print(*arr, sep=", ")
