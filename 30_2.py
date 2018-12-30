def main():
    C = 32
    L = 10
    memo = {}
    for i in range(C + 1):
        for j in range(C + 1):
            memo[(i, j, 0)] = 0
            memo[(i, j, 1)] = 0
    memo[(0, 0, 0)] = 1
    for i in range(1, C + 1):
        for j in range(1, i + 1):
            for k in range(1, min(L, i) + 1):
                memo[(i, j, 0)] += memo[(i - k, i - j, 1)]
                memo[(i, j, 1)] += memo[(i - k, i - j, 0)]
    cnt = 0
    for i in range(C, C // 2, -1):
        cnt += memo[(C, i, 1)]
    print(cnt)


if __name__ == '__main__':
    main()
