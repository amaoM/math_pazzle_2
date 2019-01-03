N = 12


def move(b, f, memo):
    if (b, f) in memo:
        return memo[(b, f)]
    if b == 0 and f == 0:
        return 1
    if f == 0:
        return 0
    cnt = 0
    for i in range(1, f + 1):
        cnt += move(f - i, b + i - 1, memo)
    memo[(b, f)] = cnt
    return cnt


def main():
    print(move(0, N - 2, {}))


if __name__ == '__main__':
    main()
