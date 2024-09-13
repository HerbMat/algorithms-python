import math
from typing import List


def find_max_subarray(arr: List, low: int, high: int) -> tuple[int, int, int]:
    if low >= high:
        return low, high, arr[low]
    mid = (low + high) // 2
    left_low, left_high, left_sum = find_max_subarray(arr, low, mid)
    right_low, right_high, right_sum = find_max_subarray(arr, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def find_max_crossing_subarray(tab: List, low: int, mid: int, high: int) -> tuple[int, int, int]:
    left_sum = right_sum = - math.inf
    sub_arr_sum = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        sub_arr_sum += tab[i]
        if sub_arr_sum > left_sum:
            left_sum = sub_arr_sum
            max_left = i
    max_right = low
    sub_arr_sum = 0
    for i in range(mid + 1, high + 1):
        sub_arr_sum += tab[i]
        if sub_arr_sum > right_sum:
            right_sum = sub_arr_sum
            max_right = i
    return max_left, max_right, left_sum + right_sum


if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3, 5]
    low, high, sum_res = find_max_subarray(arr, 0, len(arr)-1)
    result = arr[low:high+1]
    print(*result, sep=", ")
    print(f"\n {sum_res}")
