def vote(n):
    if 2 >= n:
        return 1
    cnt = 1
    cnt += vote(n - 1)
    for i in range(2, n):
        cnt += vote(i) * vote(n - 1)
    return cnt


def main():
    N = 7
    print(vote(N))


if __name__ == '__main__':
    main()
