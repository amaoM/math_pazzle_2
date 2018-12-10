def main():
    N = 46
    triangle = [1]
    for n in range(1, N):
        us = triangle[-n:]
        triangle.append(1)
        for m in range(n - 1):
            triangle.append(us[m] + us[m + 1])
        triangle.append(1)

    money = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    cnt = 0
    for n in triangle[-N:]:
        for m in money:
            c, n = divmod(n, m)
            cnt += c
    print(cnt)


if __name__ == '__main__':
    main()
