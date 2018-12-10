def main():
    N = 100
    c = 0
    for goo in range(N + 1):
        for choki in range(N - goo + 1):
            paa = N - goo - choki
            m = max(goo, choki, paa)
            if [goo, choki, paa].count(m) == 1:
                c += 1
    print(c)


if __name__ == '__main__':
    main()
