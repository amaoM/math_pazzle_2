W = 10
H = 10


def search(frame, memo):
    if min(frame) == H:
        return 1

    if ''.join(list(map(str, frame))) in memo:
        return memo[''.join(list(map(str, frame)))]

    tiles = [(1, 1), (2, 2), (4, 2), (4, 4)]
    pos = frame.index(min(frame))
    cnt = 0
    for xx, yy in tiles:
        check = True
        for x in range(xx):
            if pos + x >= W or frame[pos + x] + yy > H:
                check = False
            elif frame[pos + x] != frame[pos]:
                check = False
        if check is False:
            continue
        for x in range(xx):
            frame[pos + x] += yy
        cnt += search(frame[::], memo)
        for x in range(xx):
            frame[pos + x] -= yy
    memo[''.join(list(map(str, frame)))] = cnt
    return cnt


def main():
    frame = [0 for _ in range(W)]
    print(search(frame, {}))


if __name__ == '__main__':
    main()
