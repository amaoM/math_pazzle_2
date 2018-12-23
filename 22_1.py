from functools import cmp_to_key


X = [8, 6, 8, 9, 3, 4, 1, 7, 6, 1]
Y = [5, 1, 1, 9, 1, 6, 9, 0, 9, 6]
N = 10


def main():
    board = [[X[x] + Y[y] for y in range(N)] for x in range(N)]
    cost = [[18 * N for _ in range(N)] for _ in range(N)]

    cost[0][0] = board[0][0]
    queue = [[0, 0]]

    while len(queue) > 0:
        sorted(queue, key=cmp_to_key(
            lambda a, b: cost[b[0]][b[1]] > cost[a[0]][a[1]]))
        x, y = queue.pop(0)
        for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = x + d[0]
            ny = y + d[1]
            if nx >= 0 and N > nx and ny >= 0 and N > ny and \
                    cost[nx][ny] > cost[x][y] + board[nx][ny]:
                cost[nx][ny] = cost[x][y] + board[nx][ny]
                queue.append([nx, ny])
    print(cost[N - 1][N - 1])


if __name__ == '__main__':
    main()
