def check(n, t, memo):
    if (n, t) in memo:
        return memo[(n, t)]
    if 0 > t:
        return 0
    if n == 0:
        return 1
    cnt = check(n - 1, t + 3, memo)
    if t >= 2:
        cnt += check(n - 1, t - 2, memo)
    memo[(n, t)] = cnt
    return cnt


def main():
    N = 32
    print(check(N, 0, {}))


if __name__ == '__main__':
    main()
