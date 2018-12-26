def catalan(n, memo):
    if n in memo:
        return memo[n]
    cnt = 0
    for i in range(n):
        cnt += catalan(i, memo) * catalan(n - 1 - i, memo)
    memo[n] = cnt
    return cnt


def main():
    N = 39
    print(catalan((N - 1) // 2, {0: 1}))


if __name__ == '__main__':
    main()
