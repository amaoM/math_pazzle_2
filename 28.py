def course(h, p, memo):
    if (h, p) in memo:
        return memo[(h, p)]
    if 0 >= h or 0 >= p:
        return 0
    if h == 1 and 5 >= p:
        return 1
    cnt = 0
    for i in range(1, 6):
        cnt += course(h - 1, p - i, memo)
    memo[(h, p)] = cnt
    return cnt


def main():
    H = 18
    P = 72
    print(course(H, P, {}))


if __name__ == '__main__':
    main()
