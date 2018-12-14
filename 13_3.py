M = 5
N = 3


def search(seq, used, n):
    if n == 0:
        result = 1
        cnt = seq.count(0)
        for i in range(1, cnt + 1):
            result *= i
        return result
    cnt = 0
    for i in range(1, M):
        new_seq = seq[0:i+1]
        new_seq.reverse()
        new_seq.extend(seq[i+1:])
        print(i, seq, bin(used), bin(1 << i))
        # ビット演算の意味が理解できない
        if seq[i] == 0 and used & (1 << i) == 0:
            new_seq[0] = i + 1
            cnt += search(new_seq, used | (1 << i), n - 1)
        elif seq[i] == i + 1:
            cnt += search(new_seq, used, n - 1)
    return cnt


def main():
    seq = [0 for _ in range(M)]
    seq[0] = 1
    print(search(seq, 1, N))


if __name__ == '__main__':
    main()
