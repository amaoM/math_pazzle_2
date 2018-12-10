def conversion(n, a, b, c):
    roma = ''
    if n == 9:
        roma += a + c
    elif 9 > n > 4:
        roma += b + (a * int(n % 5))
    elif n == 4:
        roma += a + b
    else:
        roma += a * n
    return roma


def main():
    cnt = 0
    for n in range(1, 4000):
        roma = ''
        m, n = divmod(n, 1000)
        roma += 'M' * m
        c, n = divmod(n, 100)
        x, n = divmod(n, 10)
        roma += conversion(c, 'C', 'D', 'M')
        roma += conversion(x, 'X', 'L', 'C')
        roma += conversion(n, 'I', 'V', 'X')
        if (len(roma) == 12):
            print(roma)
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
