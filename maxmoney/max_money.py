import math


def max_money(n: int, k: int) -> int:
    return (math.ceil(n / 2)) * k


if __name__ == "__main__":
    print(f'max money {max_money(5, 10)}$')
    print(f'max money {max_money(2, 12)}$')
