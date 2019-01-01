def nCr(n, r, memo):
    if (n, r) in memo:
        return memo[(n, r)]
    if r == 0 or n == r:
        return 1
    cnt = 0
    cnt += nCr(n - 1, r, memo) + nCr(n - 1, r - 1, memo)
    memo[(n, r)] = cnt
    return cnt


def main():
    N = 14
    cnt = 0
    for i in range(2, N - 1):
        cnt += nCr(N - 1, i, {}) * (N - i - 1) * (i - 1)
    print(cnt)


if __name__ == '__main__':
    main()
