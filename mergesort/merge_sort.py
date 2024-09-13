from typing import List


def merge_sort(arr: List):
    if len(arr) > 1:
        size = len(arr)
        middle = size//2
        left = arr[:middle]
        right = arr[middle:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            elif j < size:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [31, 41, 59, 26, 41, 58]
    merge_sort(arr)
    print(*arr, sep=", ")
