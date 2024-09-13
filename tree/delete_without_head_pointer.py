from tree import Node


def delete_without_head_pointer(node: Node):
    if node is None:
        return
    elif node.next_element is None:
        return
    node.value = node.next_element.value
    node.next_element = node.next_element.next_element


if __name__ == '__main__':
    tail = Node(30, None)
    prevNode = Node(4, tail)
    nodeToFind = Node(20, prevNode)
    head = Node(10, nodeToFind)
    delete_without_head_pointer(nodeToFind)
    print("End")
