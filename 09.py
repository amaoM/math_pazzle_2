def main():
    N = 8
    i = 8
    cnt = 0
    max_n = 1

    while True:
        if N**(max_n - 1) > max_n * (N - 1)**max_n:
            break
        max_n += 1

    while True:
        oct_str = str(oct(i))[2:]
        n = len(oct_str)
        if n > max_n:
            print('No other')
            return
        ten_int = int(''.join(oct_str), N)
        oct_sum = sum([int(s)**n for s in oct_str])
        if ten_int == oct_sum:
            print(oct_str)
            cnt += 1
        if cnt == 8:
            return
        i += 1


if __name__ == '__main__':
    '''
    補足
    8 進数に変換した数字の各桁の桁数乗和を求め
    それが 10 進数に変換した数字と同じであれば
    ナルシシスト数になる
    '''
    main()
