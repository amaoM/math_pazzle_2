memo = [0 for _ in range(60)]
lights = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def count(t):
    if memo[t] == 0:
        if 10 > t:
            memo[t] = lights[0] + lights[t]
        else:
            l, r = divmod(t, 10)
            memo[t] = lights[l] + lights[r]
    return memo[t]


def main():
    cnt = 0
    for h in range(24):
        for m in range(60):
            for s in range(60):
                light_sum = count(h) + count(m) + count(s)
                if light_sum == 30:
                    cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
