def print_parenthesis(str, n):
    if n > 0:
        _print_parenthesis(str, 0, n, 0, 0)
    return


def _print_parenthesis(strs, pos, n,
                       open, close):
    if close == n:
        for i in strs:
            print(i, end="")
        print()
        return
    else:
        if open > close:
            strs[pos] = '}';
            _print_parenthesis(strs, pos + 1, n, open, close + 1)
        if open < n:
            strs[pos] = '{'
            _print_parenthesis(strs, pos + 1, n, open + 1, close)


if __name__ == "__main__":
    n = 3
    strs = [""] * 2 * n
    print_parenthesis(strs, n)
