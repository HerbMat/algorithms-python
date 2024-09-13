import math
import sys
from typing import Tuple

from bst.Node import Node


def largest_bst(node: Node) -> Tuple[int, int, bool, int]:
    result_left = largest_bst(node.left) if node.left is not None else (node.value, -math.inf, True, 0)
    result_right = largest_bst(node.right) if node.right is not None else (math.inf, node.value, True, 0)
    if is_left_valid(node, result_left) and is_right_valid(node, result_right):
        return result_left[0], result_right[1], True, result_right[-1] + result_left[-1] + 1
    bst_size = result_left[-1] if result_left[-1] >= result_right[-1] else result_right[-1]
    if bst_size == 0:
        bst_size = 1
    return 0, 0, False, bst_size


def is_left_valid(node: Node, left_result: Tuple[int, int, bool, int]) -> bool:
    return node.value > left_result[1] and left_result[2]


def is_right_valid(node: Node, right_result: Tuple[int, int, bool, int]) -> bool:
    return node.value < right_result[0] and right_result[2]


def print_result(result: Tuple[int, int, bool, int]) -> None:
    print(f"{result[0]}, {result[1]}, {result[2]}, {result[3]}")


if __name__ == "__main__":
    root_1 = Node(2, Node(1), Node(3, None, Node(4)))
    result_1 = largest_bst(root_1)
    print_result(result_1)
    root_2 = Node(2, None, Node(7, None, Node(6, None, Node(9))))
    result_2 = largest_bst(root_2)
    print_result(result_2)
    root_3 = Node(2, Node(5), Node(20, Node(9), Node(25)))
    result_3 = largest_bst(root_3)
    print_result(result_3)
    root_4 = Node(7, Node(4, Node(3), Node(5)), Node(15, Node(10, Node(9), Node(12)), Node(20, Node(16), Node(21))))
    result_4 = largest_bst(root_4)
    print_result(result_4)
    root_5 = Node(1, Node(4, Node(6), Node(8)), Node(4))
    result_5 = largest_bst(root_5)
    print_result(result_5)
    root_6 = Node(6, Node(6, None, Node(2)), Node(2, Node(1), Node(3)))
    result_6 = largest_bst(root_6)
    print_result(result_6)
