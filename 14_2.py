def combinations(l, i, r):
    if i == 0:
        return [r]
    ll = l[::]
    res = []
    for k in range(len(l)):
        rr = r[::]
        rr.append(l[k])
        ll.remove(l[k])
        res.extend(combinations(ll, i - 1, rr))
    return res


def main():
    M = 45678
    cnt = M
    money_list = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    for i in range(len(money_list), 0, -1):
        combs = combinations(money_list, i, [])
        for ml in combs:
            rest = M
            for money in ml:
                rest -= money
            if 0 > rest:
                continue
            c = len(ml)
            for money in ml:
                r = rest // money
                c += r
                rest -= r * money
            cnt = min(cnt, c)
        if cnt < M:
            break
    print(cnt)


if __name__ in '__main__':
    main()
