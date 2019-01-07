def check(unused, once, neighbor, memo):
    if (unused, once, neighbor) in memo:
        return memo[(unused, once, neighbor)]
    cnt = 0
    if unused > 0:
        cnt += check(unused - 1, once + neighbor, 1, memo)
    if once > 0:
        cnt += once * check(unused, once - 1 + neighbor, 0, memo)
    memo[(unused, once, neighbor)] = cnt
    return cnt


def main():
    N = 11
    print(check(N, 0, 0, {(0, 0, 0): 1}))


if __name__ == '__main__':
    main()
