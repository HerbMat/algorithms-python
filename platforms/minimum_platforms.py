from typing import List


def binary_search_greater(arr: List, el: int, begin: int, end: int) -> int:
    middle = begin + (end - begin) // 2
    if begin >= end:
        return -1
    elif arr[middle] <= el:
        return middle
    elif arr[middle] > el:
        return binary_search_greater(arr, el, begin, middle - 1)


def find_minimum_platforms(arrivals: List[int], departures: List[int]) -> int:
    departures_to_check = [departures[0]]
    max_platforms = 1
    for i in range(1, len(arrivals)):
        required_platforms = len(departures_to_check) - (1 + binary_search_greater(departures_to_check, arrivals[i], 0, i - 1))
        max_platforms = max_platforms if (max_platforms >= required_platforms) else required_platforms
        departures_to_check.append(departures[i])
        departures_to_check.sort()
    return max_platforms


if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(f'{find_minimum_platforms(arr, dep)}')
    arr = [900, 1100, 1235]
    dep = [1000, 1200, 1240]
    print(f'{find_minimum_platforms(arr, dep)}')
