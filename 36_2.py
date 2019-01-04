N = 12
M = 7


def check(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    cnt = 0
    for i in range(M):
        cnt += check(n - 2, memo) + i * (M ** (n - 2))
    memo[n] = cnt
    return cnt


def main():
    print(check(N, {}))


if __name__ == '__main__':
    main()
