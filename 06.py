def main():
    S = 1000
    N = 20
    cnt = 0
    for long in range(S, 0, -1):
        for short in range(1, long + 1):
            t_long = long
            t_short = short
            c = 0
            while True:
                c += 1
                if t_long - t_short == 0:
                    break
                t_short, t_long = sorted([t_long - t_short, t_short])
            if c == N:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
