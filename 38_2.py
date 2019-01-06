S = 4


def move(t, seats, memo):
    if (t, seats) in memo:
        return memo[(t, seats)]
    if 0 > t:
        return 1
    cnt = 0
    for s in [i for i in range(0, S * S)]:
        x, y = divmod(s, S)
        tx, ty = divmod(t, S)
        if x != tx and y != ty:
            if seats & (1 << s) == 0:
                cnt += move(t - 1, seats | (1 << s), memo)
    memo[(t, seats)] = cnt
    return cnt


def main():
    print(move(S * S - 1, 0, {}))


if __name__ == '__main__':
    main()
