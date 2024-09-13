def reverse_k_elements_in_queue(queue: list, k: int):
    temp_stack = []
    for i in range(0, k):
        temp_stack.append(queue.pop(0))
    first_element = temp_stack[-1]
    while len(temp_stack) > 0:
        queue.append(temp_stack.pop())
    while queue[0] != first_element:
        queue.append(queue.pop(0))


if __name__ == '__main__':
    queue = [1, 2, 3, 4, 5]
    reverse_k_elements_in_queue(queue, 3)
    print(*queue, sep=", ")
