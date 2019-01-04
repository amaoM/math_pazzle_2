N = 12
nums = [(0, 0), (1, 1), (2, 2), (5, 5), (6, 9), (8, 8), (9, 6)]


def check(l, r, n):
    if r > l:
        return len(nums) ** n
    if l > r or n == 0:
        return 0
    cnt = 0
    if r == l:
        for li, lr in nums:
            for ri, rr in nums:
                cnt += check(lr, rr, n - 2)
    return cnt


def main():
    cnt = 0
    for li, lr in nums:
        for ri, rr in nums:
            cnt += check(lr, rr, N - 2)
    print(cnt)


if __name__ == '__main__':
    main()
