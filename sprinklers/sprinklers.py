from typing import List


def find_best_sprinkler(gallery: List[int], marked_rooms: List[bool]) -> int:
    n = len(gallery)
    sprinklers_max_rooms = 0
    sprinkler_index = -1
    for i in range(n):
        if not marked_rooms[i]:
            sprinkler_range = gallery[i]
            left_range = 0 if sprinkler_range == -1 else sprinkler_range if i - sprinkler_range >= 0 else i
            right_range = 0 if sprinkler_range == -1 else sprinkler_range if i + sprinkler_range < n else n - sprinkler_range
            sprinkled_rooms = left_range + right_range
            sprinkled_rooms = sprinkled_rooms + 1 if sprinkler_range >= 0 else sprinkled_rooms
            if sprinkled_rooms > sprinklers_max_rooms:
                sprinklers_max_rooms = sprinkled_rooms
                sprinkler_index = i
    return sprinkler_index


def mark_rooms(marked_rooms: List[bool], sprinkler_range: int, index: int):
    n = len(marked_rooms)
    left_marked = index - sprinkler_range if index - sprinkler_range >= 0 else 0
    right_marked = index + sprinkler_range + 1 if index + sprinkler_range < n - 1 else n
    marked_rooms[index] = True
    for i in range(left_marked, right_marked):
        marked_rooms[i] = True


def min_sprinklers(gallery: List[int]) -> int:
    sprinklers = 0
    marked_rooms = [False for i in range(len(gallery))]

    while True:
        sprinkler_index = find_best_sprinkler(gallery, marked_rooms)
        if sprinkler_index < 0:
            break
        mark_rooms(marked_rooms, gallery[sprinkler_index], sprinkler_index)
        sprinklers += 1
    for i in range(len(marked_rooms)):
        if not marked_rooms[i]:
            return -1
    return sprinklers


if __name__ == "__main__":
    print(min_sprinklers([-1, 2, 2, -1, 0, 0]))
    print(min_sprinklers([2, 3, 4, -1, 2, 0, 0, -1, 0]))
    print(min_sprinklers([2, 3, 4, -1, 0, 0, 0, 0, 0]))
