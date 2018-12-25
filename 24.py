N = 12


def arrange(d, t, memo):
    if (d, t) in memo:
        return memo[(d, t)]
    if d > N or t > N:
        return 0
    cnt = 0
    # 2 列も 3 列も空いている
    if d == t:
        # 1 人が 2 カ所を使うとき
        # 2 人グループが並ぶとき
        cnt += 2 * arrange(d + 1, t, memo)
        cnt += arrange(d + 1, t + 1, memo)
        cnt += arrange(d + 2, t, memo)
    # 3 列シートは空いている
    elif d > t:
        cnt += arrange(d, t + 2, memo)
        # 1 人が 3 カ所を使うとき
        # 1 人がどちらかの端に座って、残りを 2 人グループが使うとき
        # 3 人グループが並ぶとき
        cnt += 4 * arrange(d, t + 1, memo)
    # 2 列シートは空いている
    else:
        cnt += 2 * arrange(d + 1, t, memo)
        cnt += arrange(d + 2, t, memo)
    return cnt


def main():
    print(arrange(0, 0, {(N, N): 1}))


if __name__ == '__main__':
    main()
