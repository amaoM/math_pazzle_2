def sort(line):
    for i in range(5):
        if line[0] == '1':
            return 0
        n = int(line[0])
        _line = line[n:]
        for num in line[:n]:
            _line = num + _line
        line = _line
    if line[0] == '1':
        return 1
    return 0


def deal(line, cards, cnt):
    if len(cards) == 0:
        cnt += sort(line)

    for i, c in enumerate(cards):
        cards.remove(c)
        cnt = deal(line + str(c), cards, cnt)
        cards.insert(i, c)

    return cnt


def main():
    cnt = deal('', [c for c in range(1, 10)], 0)
    print(cnt)


if __name__ == '__main__':
    main()
