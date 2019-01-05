def rotation(digit, now, total, dire, memo):
    if (digit, now, total, dire) in memo:
        return memo[(digit, now, total, dire)]
    if 0 > total:
        return 0
    if digit == 0:
        if total == 0:
            return 1
        else:
            return 0
    cnt = 0
    for d in range(1, 10):
        if dire is True:
            now += d
        else:
            now -= d
        cnt += rotation(digit - 1, now, total - d, dire is False, memo)
    memo[(digit, now, total, dire)] = cnt
    return cnt


def main():
    D = 10
    N = 50
    print(rotation(D, 0, N, True, {}))


if __name__ == '__main__':
    main()
