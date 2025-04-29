N = int(input())
r = 2**N - 1
c = 2 * r - 1
board = [[' '] * c for _ in range(r)]


def recursion(x, y, n):
    if n == 1:
        board[x][y] = '*'
        return

    R = 2 ** n - 1  # 행의 개수
    C = 2 * R - 1  # 열의 개수

    if n % 2 == 1:
        for i in range(R - 1, -1, -1):
            board[x + R - i - 1][y + i] = "*"
            board[x + R - i - 1][y + C - 1 - i] = "*"
        for j in range(1, C - 1):
            board[x + R - 1][y + j] = "*"

        recursion(x + 2**(n - 1) - 1, y + 2**(n - 1), n - 1)
    else:
        for i in range(R):
            board[x + i][y + i] = "*"
            board[x + i][y + C - 1 - i] = "*"
        for j in range(1, C - 1):
            board[x][y + j] = "*"

        recursion(x + 1, y + 2**(n - 1), n - 1)


recursion(0, 0, N)

for row in board:
    print(''.join(row).rstrip())


