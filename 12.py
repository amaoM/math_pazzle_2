def main():
    P = 314159265358
    N = 11
    i = 1
    while True:
        if ((P + 1) * i) // 10**N != (P * i) // 10**N:
            print(i)
            return
        i += 1


if __name__ == '__main__':
    main()
