from typing import Sequence


def run_rearrange() -> None:
    array = [1, 2, 3, 4, 5, 6]
    result = rearrange_array(array)
    print(f"result {result}")
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = rearrange_array(array)
    print(f"result {result}")


def rearrange_array(array: Sequence[int]) -> Sequence[int]:
    copy_array = []
    array_length = len(array)
    half_array_length = array_length // 2
    for i in range(0, half_array_length):
        copy_array.append(array[array_length - i - 1])
        copy_array.append(array[i])
    if array_length % 2 == 1:
        copy_array.append(array[half_array_length])
    return copy_array
