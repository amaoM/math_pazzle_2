P = 180
D = 14


def read(p, d, memo):
    if (p, d) in memo:
        return memo[(p, d)]

    if d == 1:
        return 1

    cnt = 0

    for i in range(1, (p - d * (d - 1) // 2) // d + 1):
        cnt += read(p - i * d, d - 1, memo)
    memo[(p, d)] = cnt
    return cnt


def main():
    cnt = 0
    for i in range(1, D + 1):
        cnt += read(P, i, {})
    print(cnt)


if __name__ == '__main__':
    main()
