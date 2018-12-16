def combination(l, i, r):
    if i == 0:
        print(r)
    ll = l[::]
    for k in range(len(l)):
        rr = r[::]
        rr.append(l[k])
        ll.remove(l[k])
        combination(ll, i - 1, rr)


def main():
    print(combination([1, 2, 3, 4, 5], 3, []))


if __name__ in '__main__':
    main()
