def janken(n, a, b, memo):
    if (n, a, b) in memo:
        return memo[(n, a, b)]
    if a == 0 or b == 0:
        return 1
    if n == 0:
        return 0
    cnt = 0
    cnt += janken(n - 1, a + 1, b - 1, memo)
    cnt += janken(n - 1, a - 1, b + 1, memo)
    cnt += janken(n - 1, a, b, memo)
    memo[(n, a, b)] = cnt
    return cnt


def main():
    N = 24
    A = 10
    B = 10
    print(janken(N, A, B, {}))


if __name__ == '__main__':
    main()
