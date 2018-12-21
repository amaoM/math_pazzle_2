N = 15
S = 3
E = 10
memo = {}


def search(passed, d):
    cnt = 0
    key = ''.join(map(str, passed))
    if (key, d) in memo:
        return memo[(key, d)]
    if passed[-1] == E:
        memo[(key, d)] = 1
        return 1
    if d > 0:
        for i in range(N - E + 1):
            p = passed[::]
            if E + i in p:
                continue
            p.append(E + i)
            cnt += search(p, -1)
    else:
        for i in range(E):
            p = passed[::]
            if E - i in p:
                continue
            p.append(E - i)
            cnt += search(p, 1)
    return cnt


def main():
    print(search([S], 1))


if __name__ == '__main__':
    main()
