import sys
from math import ceil


def heap_minimum(tab: list[int]) -> int:
    return tab[0]


def parent(i: int) -> int:
    return ceil(i/2) - 1


def left(i: int) -> int:
    return 2*i + 1


def right(i: int) -> int:
    return 2*i + 2


def min_heapify(tab: list[int], pos: int):
    left_child = left(pos)
    right_child = right(pos)
    lowest = pos
    if left_child <= len(tab)-1 and tab[left_child] < tab[pos]:
        lowest = left_child
    if right_child <= len(tab)-1 and tab[right_child] < tab[pos]:
        lowest = right_child
    if lowest != pos:
        new_lowest = tab[pos]
        tab[pos] = tab[lowest]
        tab[lowest] = new_lowest
        min_heapify(tab, lowest)


def heap_extract_min(tab: list[int]) -> int:
    tab_length = len(tab)
    if tab_length < 1:
        raise IndexError("Element is empty")
    minimum = tab[0]
    tab[0] = tab[tab_length - 1]
    tab.pop()
    min_heapify(tab, 0)

    return minimum


def heap_delete(tab: list[int], pos: int):
    tab_length = len(tab)
    if tab_length < pos:
        raise IndexError("Element is out of array")
    tab[pos] = tab[tab_length - 1]
    tab.pop()
    min_heapify(tab, pos)


def heap_decrease_key(tab: list[int], i: int, key: int):
    if key > tab[i]:
        raise ValueError("New key is bigger than existing")
    tab[i] = key
    while i > 0 and tab[parent(i)] > tab[i]:
        new_parent = tab[i]
        tab[i] = tab[parent(i)]
        tab[parent(i)] = new_parent
        i = parent(i)


def heap_decrease_key_insert_sort(tab: list[int], i: int, key: int):
    if key > tab[i]:
        raise ValueError("New key is bigger than existing")
    tab[i] = key
    temp = tab[i]
    while i >= 0:
        if i > 0 and tab[parent(i)] > temp:
            tab[i] = tab[parent(i)]
            i = parent(i)
        else:
            tab[i] = temp
            break


def min_heap_insert(tab: list[int], key: int):
    tab.append(sys.maxsize)
    heap_decrease_key(tab, len(tab)-1, key)


if __name__ == '__main__':
    arr = [10, 14, 19, 26, 31, 42, 27, 44, 35, 33]
    print(f"{heap_minimum(arr)}")
    print(f"{heap_extract_min(arr)}")
    arr_two = arr.copy()
    heap_decrease_key_insert_sort(arr_two, 6, 9)
    print(*arr_two, sep=", ")
    heap_decrease_key(arr, 6, 9)
    print(*arr, sep=", ")
    min_heap_insert(arr, 13)
    print(*arr, sep=", ")
    heap_delete(arr, 4)
    print(*arr, sep=", ")
