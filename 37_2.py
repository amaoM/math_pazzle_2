def rotation(digit, total, dire, memo):
    if (digit, total, dire) in memo:
        return memo[(digit, total, dire)]
    if 0 > total:
        return 0
    if digit == 0:
        if total == 0:
            return 1
        else:
            return 0
    cnt = 0
    for d in range(1, 10):
        cnt += rotation(digit - 1, total - d, dire is False, memo)
    memo[(digit, total, dire)] = cnt
    return cnt


def main():
    D = 10
    N = 50
    print(rotation(D, N, True, {}))


if __name__ == '__main__':
    main()
