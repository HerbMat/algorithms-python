from itertools import groupby, count
from typing import List


def find_max_for_freq(freq: int, arr: List[int]) -> int:
    elements = {k: len(list(v)) for k, v in groupby(arr, lambda x: x)}
    result = [key for (key, val) in elements.items() if val == freq]
    return max(result)


if __name__ == "__main__":
    print(find_max_for_freq(1, [2, 2, 5, 50, 1]))
