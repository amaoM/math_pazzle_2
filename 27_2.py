def nCr(n, r, memo):
    if (n, r) in memo:
        return memo[(n, r)]
    if r == 0 or n == r:
        return 1
    cnt = nCr(n - 1, r, memo) + nCr(n - 1, r - 1, memo)
    memo[(n, r)] = cnt
    return cnt


def main():
    N = 10
    V = 20
    S = 20
    cnt = 0
    for x in range(N):
        y = N - 1 - x
        cnt += nCr(V - 1, x, {}) * nCr(S - 1, y, {}) * nCr(N - 1, x, {})
    print(cnt)


if __name__ == '__main__':
    main()
