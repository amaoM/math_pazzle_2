def take(c, t, f, a, memo):
    L = 10
    if (c, t, f, a) in memo:
        return memo[(c, t, f, a)]
    if c == 0:
        if t is False:
            if f > a:
                return 1
            else:
                return 0
    cnt = 0
    for i in range(1, min(c, L) + 1):
        if t is True:
            cnt += take(c - i, not(t), f + i, a, memo)
        else:
            cnt += take(c - i, not(t), f, a + i, memo)
    memo[(c, t, f, a)] = cnt
    return cnt


def main():
    C = 32
    print(take(C, True, 0, 0, {}))


if __name__ == '__main__':
    main()
