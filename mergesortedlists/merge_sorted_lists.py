from math import ceil


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def min_heapify(tab: list[list[int]], pos: int):
    left_child = left(pos)
    right_child = right(pos)
    lowest = pos
    if left_child <= len(tab) - 1 and tab[left_child][0] < tab[pos][0]:
        lowest = left_child
    if right_child <= len(tab) - 1 and tab[right_child][0] < tab[pos][0]:
        lowest = right_child
    if lowest != pos:
        new_lowest = tab[pos]
        tab[pos] = tab[lowest]
        tab[lowest] = new_lowest
        min_heapify(tab, lowest)


def build_min_heap(tab: list[list[int]]):
    heap_size = len(tab)
    for i in range(ceil((heap_size-1))//2, -1, -1):
        min_heapify(tab, i)


def heap_extract_min(tab: list[list[int]]) -> int:
    tab_length = len(tab)
    if tab_length < 1:
        raise IndexError("Element is empty")
    minimum = tab[0].pop(0)
    if len(tab[0]) == 0:
        tab[0] = tab[tab_length - 1]
        tab.pop()
    min_heapify(tab, 0)

    return minimum


def merge_sorted_list(sorted_lists: list[list[int]]) -> list[int]:
    build_min_heap(sorted_lists)
    result = []
    while len(sorted_lists) > 0:
        result.append(heap_extract_min(sorted_lists))
    return result


if __name__ == '__main__':
    lists = [
        [1, 3, 6, 7],
        [2, 4, 6, 8],
        [0, 9, 10, 11]
    ]
    result = merge_sorted_list(lists)
    print(*result, sep=", ")
