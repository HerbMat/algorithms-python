
def divide_groups_incrementally(n: int, k: int) -> int:
    comparison_result = n - k
    if comparison_result < 0:
        return 0
    if comparison_result == 1:
        return 1
    arr = [0 for i in range(k)]
    arr[0] = comparison_result

    return 1 + find_groups(arr)


def find_groups(arr: list[int]) -> int:
    if should_finish(arr):
        return 0
    new_found_group = make_new_group(arr)
    return 1 + find_groups(new_found_group)


def should_finish(arr: list[int]) -> bool:
    return arr[0] <= arr[-1] + 1


def make_new_group(arr: list[int]) -> list[int]:
    new_group = arr.copy()
    length = len(new_group)
    index_giver = 0
    index_receiver = 0
    for i in range(1, length):
        if new_group[i] == new_group[index_giver]:
            index_giver = i
        elif new_group[i] + 1 <= new_group[index_giver] - 1:
            index_receiver = i
            break

    if index_receiver > 0:
        new_group[index_giver] = new_group[index_giver] - 1
        new_group[index_receiver] = new_group[index_receiver] + 1
    return new_group


if __name__ == "__main__":
    # print(f'Result: {divide_groups_incrementally(8,4)}')
    # print(f'Result: {divide_groups_incrementally(4,3)}')
    print(f'Result: {divide_groups_incrementally(15,6)}')
