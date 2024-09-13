from queue import PriorityQueue
from typing import List, Tuple


def insert(queue: PriorityQueue, k: int) -> PriorityQueue:
    queue.put(k)
    return queue


def find(queue: PriorityQueue, k: int) -> bool:
    temp_stack = []
    return_value = False
    while not queue.empty():
        el = queue.get()
        temp_stack.append(el)
        if el == k:
            return_value = True
    for el in temp_stack:
        insert(queue, el)
    return return_value


def delete(queue: PriorityQueue) -> PriorityQueue:
    value = queue.get()
    print(f"deleted {value} \n")
    return queue


def find_and_delete_max(queue: PriorityQueue, k: int) -> PriorityQueue:
    if find(queue, k):
        print("1 \n")
        delete(queue)
    else:
        print("-1 \n")
    return queue


def find_elements_in_priority_queue(elements: List[int], elements_to_find: List[int]):
    queue = PriorityQueue()
    for el in elements:
        insert(queue, el)
    for el in elements_to_find:
        find_and_delete_max(queue, el)


if __name__ == '__main__':
    elements = [-1, -2, -3, -4, -5, -2, -3, -1]
    elements_to_find = [-1, -3, -2, -9, -10]
    find_elements_in_priority_queue(elements, elements_to_find)
