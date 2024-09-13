import math
import sys
from typing import Tuple

from bst.Node import Node


def check_bst(node: Node) -> Tuple[int, int, bool]:
    result_left = check_bst(node.left) if node.left is not None else (node.value, -math.inf, True)
    result_right = check_bst(node.right) if node.right is not None else (math.inf, node.value, True)
    if is_left_valid(node, result_left) and is_right_valid(node, result_right):
        return result_left[0], result_right[1], True
    return 0, 0, False


def is_left_valid(node: Node, left_result: Tuple[int, int, bool]) -> bool:
    return node.value > left_result[1] and left_result[2]


def is_right_valid(node: Node, right_result: Tuple[int, int, bool]) -> bool:
    return node.value < right_result[0] and right_result[2]


if __name__ == "__main__":
    root_1 = Node(2, Node(1), Node(3, None, Node(4)))
    result = check_bst(root_1)
    print(f"{result[0]}, {result[1]}, {result[2]}")
    root_2 = Node(2, None, Node(7, None, Node(6, None, Node(9))))
    result_2 = check_bst(root_2)
    print(f"{result_2[0]}, {result_2[1]}, {result_2[2]}")
    root_3 = Node(2, Node(5), Node(20, Node(9), Node(25)))
    result_3 = check_bst(root_3)
    print(f"{result_3[0]}, {result_3[1]}, {result_3[2]}")
    root_4 = Node(7, Node(4, Node(3), Node(5)), Node(15, Node(10, Node(9), Node(12)), Node(20, Node(16), Node(21))))
    result_4 = check_bst(root_4)
    print(f"{result_4[0]}, {result_4[1]}, {result_4[2]}")
