from linkedlist.Node import Node


def add_number_to_list(head: Node, num: int) -> Node:
    node = head
    stack = []
    if node is not None:
        stack.append(node)
        while node.right is not None:
            stack.append(node.right)
            node = node.right
    addition = num
    while len(stack) > 0:
        el = stack.pop()
        result = el.value + addition
        if result < 10:
            el.value = result
            addition = 0
            break
        else:
            addition = 1
            el.value = result - 10
    if addition > 0:
        new_head = Node(addition, head)
        return new_head
    return head


def create_first_case() -> Node:
    tail = Node(6)
    medium = Node(5, tail)
    head = Node(4, medium)

    return head


def create_second_case() -> Node:
    tail = Node(3)
    medium = Node(2, tail)
    head = Node(1, medium)

    return head


def create_third_case() -> Node:
    tail = Node(9)
    medium = Node(9, tail)
    head = Node(9, medium)

    return head


def create_fourth_case() -> Node:
    tail = Node(9)
    medium = Node(3, tail)
    head = Node(2, medium)

    return head


def create_fifth_case() -> Node:
    head = Node(9)

    return head


def create_sixth_case() -> Node:
    head = Node(2)

    return head


def print_nodes(head: Node):
    while head is not None:
        print(head.value)
        head = head.right


if __name__ == "__main__":

    print(print_nodes(add_number_to_list(create_first_case(), 1)))
    print(print_nodes(add_number_to_list(create_second_case(), 1)))
    print(print_nodes(add_number_to_list(create_third_case(), 1)))
    print(print_nodes(add_number_to_list(create_fourth_case(), 1)))
    print(print_nodes(add_number_to_list(create_fifth_case(), 1)))
    print(print_nodes(add_number_to_list(create_sixth_case(), 1)))
