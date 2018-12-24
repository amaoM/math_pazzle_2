def div(x, y, memo):
    if (x, y) in memo:
        return memo[(x, y)]
    if x == 0:
        return 1
    if 0 > x:
        return 0
    cnt = 0
    if 5 >= x >= 2:
        cnt += 1
    for xx in range(2, 6):
        cnt += div(x - xx * 2, y, memo)
    memo[(x, y)] = cnt
    return cnt


def main():
    N = 100
    cnt = 0

    for x in range(2, N // 2 + 1):
        if N % x != 0:
            continue
        y = N // x

        cnt += div(x, y, {})

    print(cnt)


if __name__ == '__main__':
    main()
