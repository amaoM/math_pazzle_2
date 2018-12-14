def sort(combination_box):
    for i in range(5):
        lines = []
        for line in combination_box[i]:
            for ii in range(1, 9):
                if int(line[ii]) != ii + 1:
                    continue
                _line = line[ii + 1:]
                for num in line[:ii + 1]:
                    _line = num + _line
                lines.append(_line)
        combination_box.append(lines)
    return len(combination_box[i + 1])


def deal(line, cards):
    if len(cards) == 0:
        return [line]

    combinations = []
    for i, c in enumerate(cards):
        cards.remove(c)
        combinations.extend(deal(line + str(c), cards))
        cards.insert(i, c)
    return combinations


def main():
    combinations = deal('1', [c for c in range(2, 10)])
    print(sort([combinations]))


if __name__ == '__main__':
    main()
