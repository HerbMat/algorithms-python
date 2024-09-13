from typing import List


def calculate_num_of_zero_sub_arrays(arr: List) -> int:
    length = len(arr)
    i = 0
    num_of_possible_sub_arrays = 0
    while i < length:
        if arr[i] == 0:
            begin = i
            while i < length and arr[i] == 0:
                i += 1
            num_of_possible_sub_arrays += calculate_all_possible_sub_arrays_of_zeros(begin, i)
        else:
            i += 1
    return num_of_possible_sub_arrays


def calculate_all_possible_sub_arrays_of_zeros(begin: int, end: int) -> int:
    if end - begin == 0:
        return 0
    if end - begin == 1:
        return 1
    return 2 * calculate_all_possible_sub_arrays_of_zeros(begin, end - 1) + 1


if __name__ == "__main__":
    print(f"Result {calculate_num_of_zero_sub_arrays([0,0,1,0])}")
    print(f"Result {calculate_num_of_zero_sub_arrays([0,0,1,0,0,0,1,0 ])}")
    print(f"Result {calculate_num_of_zero_sub_arrays([0,0,0,0,0,0 ])}")
    print(f"Result {calculate_num_of_zero_sub_arrays([1,1,1,1 ])}")
    print(f"Result {calculate_num_of_zero_sub_arrays([1,0,0,0,0,0,1 ])}")
