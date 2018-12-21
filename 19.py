def nCr(n, r, memo):
    if (n, r) in memo:
        return memo[(n, r)]
    if r == 0 or n == r:
        return 1
    memo[(n, r)] = nCr(n - 1, r - 1, memo) + nCr(n - 1, r, memo)
    return memo[(n, r)]


def main():
    R = 50
    H = 35
    print(nCr(H - 1, R - H, {}))


if __name__ == '__main__':
    main()
