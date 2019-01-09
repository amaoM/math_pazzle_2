W = 10
H = 10


def search(pos, frame, memo):
    if pos == W * H:
        return 1

    if frame[pos] == 1:
        return search(pos + 1, frame[::], memo)

    if (pos, ''.join(list(map(str, frame)))) in memo:
        return memo[(pos, ''.join(list(map(str, frame))))]

    tiles = [(1, 1), (2, 2), (4, 2), (4, 4)]
    cnt = 0
    for xx, yy in tiles:
        check = True
        for x in range(xx):
            for y in range(yy):
                if pos % W >= W - x or pos // W >= H - y:
                    check = False
                elif frame[pos + x + y * H] == 1:
                    check = False
        if check is False:
            continue
        for x in range(xx):
            for y in range(yy):
                frame[pos + x + y * H] = 1
        cnt += search(pos + 1, frame[::], memo)
        for x in range(xx):
            for y in range(yy):
                frame[pos + x + y * H] = 0
    memo[(pos, ''.join(list(map(str, frame))))] = cnt
    return cnt


def main():
    pos = 0
    frame = [0 for _ in range(H * W)]
    print(search(pos, frame, {}))


if __name__ == '__main__':
    main()
