def div(n, vertical, side, memo):
    if (n, vertical, side) in memo:
        return memo[(n, vertical, side)]
    if n == 1:
        return 1
    cnt = 0
    for v in range(vertical - 1, 0, -1):
        cnt += div(n - 1, v, side, memo)
    for s in range(side - 1, 0, -1):
        cnt += div(n - 1, vertical, s, memo)
    memo[(n, vertical, side)] = cnt
    return cnt


def main():
    N = 10
    V = 20
    S = 20
    print(div(N, V, S, {}))


if __name__ == '__main__':
    main()
