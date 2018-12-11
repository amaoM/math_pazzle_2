def main():
    N = 29
    start = 1
    goal = 17
    step = abs(start - goal)
    print((1 << (step - 1)) + (1 << (N - step - 1)) - 1)


if __name__ == '__main__':
    '''
    補足
    - 途中の駅でスタンプを押さない場合は、降りてないと考えればよい。
    '''
    main()
