S = 4


def move(t, seats):
    if t == 0:
        return 1
    cnt = 0
    for s in [i for i in range(0, S * S)]:
        x, y = divmod(s, S)
        tx, ty = divmod(t, S)
        if x != tx and y != ty:
            if seats[s] is False:
                seats[s] = True
                cnt += move(t - 1, seats[::])
                seats[s] = False
    return cnt


def main():
    seats = [False for _ in range(0, S * S)]
    print(move(S * S - 1, seats))


if __name__ == '__main__':
    main()
