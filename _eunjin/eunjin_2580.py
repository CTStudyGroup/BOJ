def is_possible(y, x, n):
    global matrix

    for c in range(9):
        if matrix[y][c] == n:
            return False
    for r in range(9):
        if matrix[r][x] == n:
            return False
    for r in range(3):
        for c in range(3):
            if matrix[3 * (y // 3) + r][3 * (x // 3) + c] == n:
                return False

    return True


def search(lev):
    global matrix, pos

    # base case
    if lev == len(pos):  # 스도쿠 완성
        for i in range(9):
            for j in range(9):
                print(matrix[i][j], end=' ')
            print()
        exit(0)
        return

    y, x = pos[lev]

    # recursive case
    for n in range(1, 10):
        if is_possible(y, x, n):
            matrix[y][x] = n
            search(lev + 1)
            matrix[y][x] = 0


# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
pos = []
for i in range(9):
    for j in range(9):
        cur = matrix[i][j]
        if cur == 0:
            pos.append((i, j))

search(0)
