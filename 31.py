def deal(cards, line):
    if len(cards) == 0:
        return [line]
    lines = []
    for i, c in enumerate(cards):
        line.append(c)
        cards.pop(i)
        lines.extend(deal(cards, line[::]))
        line.pop(-1)
        cards.insert(i, c)
    return lines


def main():
    N = 8
    S = [i for i in range(1, N + 1)]
    lines = deal(S, [])
    cnt = 0
    for line in lines:
        for i, n in enumerate(line):
            line[i] = line[n - 1]
            line[n - 1] = n
        if line != S:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
