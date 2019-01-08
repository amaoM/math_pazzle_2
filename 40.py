N = 16


def check(island):
    pos = (0, N)
    q = [pos]
    log = {}
    log[pos] = 0
    while len(q) > 0:
        left, right = q.pop(0)
        for lt in range(left - 1, left + 2, 2):
            for rt in range(right - 1, right + 2, 2):
                if lt == rt:
                    return log[(left, right)] + 2
                if lt >= 0 and N >= rt and island[lt] == island[rt]:
                    if rt > lt and (lt, rt) not in log:
                        q.append((lt, rt))
                        log[(lt, rt)] = log[(left, right)] + 2
    return -1


def search(island, left, level):
    island[left] = level
    if left == N:
        return check(island)
    m = -1
    if level > 0:
        m = max(m, search(island, left + 1, level - 1))
    if N > left + level:
        m = max(m, search(island, left + 1, level + 1))
    return m


def main():
    print(search([-1 for _ in range(N + 1)], 0, 0))


if __name__ == '__main__':
    main()
