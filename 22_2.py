X = [8, 6, 8, 9, 3, 4, 1, 7, 6, 1]
Y = [5, 1, 1, 9, 1, 6, 9, 0, 9, 6]
N = 10


def move(x, y, z, m, memo):
    z += X[x] + Y[y]

    if z >= m:
        return m
    if x == N - 1 and y == N - 1:
        return min(m, z)

    memo.append((x, y))
    for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if N > x + d[0] and x >= 0 and \
                N > y + d[1] and y >= 0 and \
                (x + d[0], y + d[1]) not in memo:
            m = move(x + d[0], y + d[1], z, m, memo[::])
    return m


def main():
    print(move(0, 0, 0, 18 * N, []))


if __name__ == '__main__':
    main()
