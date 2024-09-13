import math
from typing import List


def number_to_binary(num: int) -> List[int]:
    arr = []
    biggest_divisor = 2
    while biggest_divisor < num:
        biggest_divisor = biggest_divisor * 2
    if biggest_divisor > num:
        biggest_divisor = math.ceil(biggest_divisor / 2)
    while biggest_divisor > 1:
        if biggest_divisor == num:
            arr.append(1)
            num = num - biggest_divisor
        elif biggest_divisor < num:
            num = num - biggest_divisor
            arr.append(1)
        elif biggest_divisor > num:
            arr.append(0)
        biggest_divisor = math.ceil(biggest_divisor / 2)
    arr.append(num)

    return arr


def print_all_numbers_in_binary(n: int):
    arr = []
    for i in range(n):
        append = True
        for j in range(len(arr)-1, 0, -1):
            if arr[j] == 1:
                arr[j] = 0
                append = True
            elif arr[j] == 0:
                arr[j] = 1
                append = False
                break
        if append:
            arr = [0 for i in arr]
            arr.insert(0, 1)
        print(*arr, sep="")


def generate_print_binary(n):
    from queue import Queue
    q = Queue()

    q.put("1")

    while n > 0:
        n -= 1
        s1 = q.get()
        print(s1)

        s2 = s1

        q.put(s1 + "0")
        q.put(s2 + "1")


if __name__ == '__main__':
    print_all_numbers_in_binary(16)
    print("echo\n")
    generate_print_binary(16)
    print("done\n")
    arr = number_to_binary(27)
    print(*arr, sep="")
