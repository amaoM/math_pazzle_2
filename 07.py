def nPr(n, r):
    res = 1
    for i in range(r):
        res *= n - i
    return res


def main():
    cnt = 0
    N = 15
    for i in range(1, N):
        # この先頭の i が謎
        cnt += i * (N - i) * nPr(N, i - 1)
    print(cnt)


if __name__ == '__main__':
    main()
