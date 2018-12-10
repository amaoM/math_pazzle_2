def main():
    N = 29
    start = 1
    goal = 17
    step = abs(start - goal)
    print((1 << (step - 1)) + (1 << (N - step - 1)) - 1)


if __name__ == '__main__':
    main()
