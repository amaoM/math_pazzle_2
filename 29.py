def cut(m, n, s, b, memo):
    W = 10
    if b - s > W:
        return 0
    if (m, n, s, b) in memo:
        return memo[(m, n, s, b)]
    if m == 0:
        if n == 0:
            return 1
        else:
            return 0
    cnt = 0
    for i in range(n + 1):
        cnt += cut(m - 1, n - i, min(i, s), max(i, b), memo)
    memo[(m, n, s, b)] = cnt
    return cnt


def main():
    M = 20
    N = 40
    print(cut(M, N, N, 0, {}))


if __name__ == '__main__':
    main()
