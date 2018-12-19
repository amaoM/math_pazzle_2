def euclidean(a, b):
    if a % b == 0:
        return b
    return euclidean(b, a % b)


def main():
    N = 1234567
    n = N
    cnt = 0
    for i in range(1, N // 2 + 1):
        if euclidean(n - i, i) == 1:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
