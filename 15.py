def main():
    M = 3000
    n = 2500
    pre = 0
    now = 1
    while n > 1:
        if pre * 2 == now or pre * 2 + 1 == now:
            if M >= now * 2:
                pre = now
                now *= 2
                n -= 1
            else:
                pre = now
                now //= 2
        elif pre % 2 == 0:
            if M >= now * 2 + 1:
                pre = now
                now = now * 2 + 1
                n -= 1
            else:
                pre = now
                now //= 2
        else:
            pre = now
            now //= 2

    print(now)


if __name__ == '__main__':
    main()
