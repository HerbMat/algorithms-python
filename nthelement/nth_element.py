from tree import Node


def find_nth_element(head: Node, n: int) -> int:
    if n == 0:
        return -1
    last_element_index = 0
    node = head
    while node.next_element is not None:
        node = node.next_element
        last_element_index += 1
    if n == 1:
        return node.value
    if last_element_index < n:
        return -1
    if last_element_index == 0:
        return head.value
    nth_from_last_index = last_element_index - n
    nth_node = head
    for i in range(nth_from_last_index):
        nth_node = nth_node.next_element
    return nth_node.next_element.value


if __name__ == '__main__':
    last_element = Node(4, None)
    prev_element = Node(3, last_element)
    prev_element_first = Node(2, prev_element)
    head = Node(1, prev_element_first)
    print(f"{find_nth_element(head, 1)}")
    print(f"{find_nth_element(head, 2)}")
    print(f"{find_nth_element(head, 3)}")
