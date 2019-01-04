N = 12
M = 7


def check(n):
    if n == 0:
        return 0
    return M * check(n - 2) + 21 * (M ** (n - 2))


def main():
    print(check(N))


if __name__ == '__main__':
    main()
