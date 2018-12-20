def lift(p, used):
    if p == 0:
        return 1
    N = 6
    n = min(N + 1, p + 1)
    cnt = 0
    for i in range(1, n):
        if p - i in used:
            cnt += used[p - i]
            continue
        cnt += lift(p - i, used)
        used[p - i] = cnt
    return cnt


def main():
    P = 32
    print(lift(P, {}))


if __name__ == '__main__':
    main()
