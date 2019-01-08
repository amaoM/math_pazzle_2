N = 16


def move(left, right, wl, island, cnt):
    if left == right:
        return cnt

    if 0 <= left <= N and 0 <= right <= N:
        island[left] = wl + 1
        island[right] = wl + 1
        a = move(left + 1, right - 1, wl + 1, island[::], cnt + 2)

        if wl > 0:
            island[left] = wl - 1
            island[right] = wl - 1
            b = move(left + 1, right - 1, wl - 1, island[::], cnt + 2)

            island[left] = wl - 1
            c = move(left + 1, right + 1, wl - 1, island[::], cnt + 2)

            island[right] = wl - 1
            d = move(left - 1, right - 1, wl - 1, island[::], cnt + 2)

            return max(a, b, c, d)
        return a
    return 0


def main():
    print(move(1, N - 1, 0, [0 for _ in range(N + 1)], 2))


if __name__ == '__main__':
    main()
