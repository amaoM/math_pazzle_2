def main():
    N = 16
    cnt = 0
    memo = {}
    for i in range(1, (1 << N) - 1):
        if i not in memo:
            c = 0
            while i > 0:
                # この法則が謎
                ri = ~i
                mi = (ri << 1) + 1
                i = (i & (~mi)) | ((i >> 1) & ri)
                c += 1
            memo[i] = c
        cnt += memo[i]
    print(cnt)


if __name__ == '__main__':
    main()
