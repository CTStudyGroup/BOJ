def row_check(r, num):  # 행에 숫자 가능 여부
    for x in range(9):
        if num == matrix[r][x]:
            return False
    return True


def col_check(c, num):  # 열에 숫자 가능 여부
    for y in range(9):
        if num == matrix[y][c]:
            return False
    return True


def div_check(r, c, num):  # 3*3 영역에 숫자 가능 여부
    nr = (r//3) * 3
    nc = (c//3) * 3
    for y in range(3):
        for x in range(3):
            if num == matrix[nr+y][nc+x]:
                return False
    return True


def dfs(depth):
    if depth >= len(zeros):  # 0의 개수만큼을 전부 탐색한 경우
        for r in range(9):
            print(''.join(map(str, matrix[r])))
        exit()

    nr, nc = zeros[depth]  # 다음 0의 좌표 꺼내기

    for num in range(1, 10):  # 각 좌표마다 1~9의 숫자에 대해 탐색
        if row_check(nr, num) and col_check(nc, num) and div_check(nr, nc, num):
            matrix[nr][nc] = num  # 해당 좌표에 숫자 일단 넣어보고 다음 단계로
            dfs(depth+1)
            matrix[nr][nc] = 0  # 해당 좌표에 해당 숫자 불가, 0으로 원상복구


matrix = []
zeros = []

for r in range(9):
    temp = list(map(int, input()))
    for c in range(9):
        if temp[c] == 0:
            zeros.append((r, c))
    matrix.append(temp)

dfs(0)
