N = 12


def move(now, d, path):
    if path[now - 1] == '1':
        return 0
    path[now - 1] = '1'
    if now == N:
        if path == ['1' for _ in range(N)]:
            return 1
        else:
            return 0
    cnt = 0
    for i in range(1, N):
        nxt = now
        nxt += i * d
        if 1 > nxt or nxt > N:
            continue
        cnt += move(nxt, -1 * d, path[::])
    return cnt


def main():
    print(move(1, 1, ['0' for _ in range(N)]))


if __name__ == '__main__':
    main()
