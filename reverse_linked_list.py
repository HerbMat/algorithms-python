from tree import Node


def reverse_linked_list(head: Node) -> Node:
    element = head
    new_next = None
    while element is not None:
        old_next = element.next_element
        element.next_element = new_next
        new_next = element
        element = old_next
    return new_next


if __name__ == '__main__':
    last_element = Node(4, None)
    prev_element = Node(3, last_element)
    prev_element_first = Node(2, prev_element)
    head = Node(1, prev_element_first)
    result = reverse_linked_list(head)
    printElement = result
    while printElement is not None:
        print(f"\n {printElement.value}")
        printElement = printElement.next_elementojek
