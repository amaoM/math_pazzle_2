def main():
    M = 45678
    money_list = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    used = [0 for _ in range(len(money_list))]
    rest = M
    for i, money in enumerate(money_list):
        if rest > money:
            used[i] = 1
            rest -= money
    for i, money in enumerate(money_list):
        used[i] += rest // money
        rest %= money
    for i in range(len(money_list) - 1):
        if used[i] == 0 and money_list[i + 1] * used[i + 1] >= money_list[i]:
            used[i] = 1
            used[i + 1] -= money_list[i] // money_list[i + 1]


if __name__ == '__main__':
    main()
