P = 180
D = 14


def read(p, r, d, memo):
    if (p, r, d) in memo:
        return memo[(p, r, d)]

    if p == 0:
        return 1

    if d == 0 or 0 > p:
        return 0

    cnt = 0
    for i in range(r):
        cnt += read(p - i, i, d - 1, memo)
    memo[(p, r, d)] = cnt
    return cnt


def main():
    print(read(P, P + 1, D, {}))


if __name__ == '__main__':
    main()
