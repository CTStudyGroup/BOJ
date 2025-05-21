import sys
input = sys.stdin.readline

def print_matrix(mat):
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()

def cmd1():  # 상하 반전
    global matrix
    temp_matrix = [[0] * M for _ in range(N)]
    for x in range(M):
        for y in range(N):
            temp_matrix[N - y - 1][x] = matrix[y][x]
    matrix = temp_matrix

def cmd2():  # 좌우 반전
    global matrix
    temp_matrix = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            temp_matrix[y][M - x - 1] = matrix[y][x]
    matrix = temp_matrix

def cmd3():  # 오른쪽 회전
    global matrix, M, N
    temp_matrix = [[0] * N for _ in range(M)]
    for y in range(N):
        for x in range(M):
            temp_matrix[x][N - y - 1] = matrix[y][x]
    matrix = temp_matrix
    N, M = M, N

def cmd4():  # 왼쪽 회전
    global matrix, M, N
    temp_matrix = [[0] * N for _ in range(M)]
    for y in range(N):
        for x in range(M):
            temp_matrix[M - x - 1][y] = matrix[y][x]
    matrix = temp_matrix
    N, M = M, N

def cmd5():
    global matrix
    temp_matrix = [[0] * M for _ in range(N)]
    HN = N // 2
    HM = M // 2

    # 2번 그룹
    for y in range(HN):
        for x in range(HM):
            temp_matrix[y][x + HM] = matrix[y][x]

    # 3번 그룹
    for y in range(HN):
        for x in range(HM, M):
            temp_matrix[y + HN][x] = matrix[y][x]

    # 4번 그룹
    for y in range(HN, N):
        for x in range(HM, M):
            temp_matrix[y][x - HM] = matrix[y][x]

    # 1번 그룹
    for y in range(HN, N):
        for x in range(HM):
            temp_matrix[y - HN][x] = matrix[y][x]

    matrix = temp_matrix

def cmd6():
    global matrix
    temp_matrix = [[0] * M for _ in range(N)]
    HN = N // 2
    HM = M // 2

    # 4번 그룹
    for y in range(HN):
        for x in range(HM):
            temp_matrix[y + HN][x] = matrix[y][x]

    # 3번 그룹
    for y in range(HN, N):
        for x in range(HM):
            temp_matrix[y][x + HM] = matrix[y][x]

    # 2번 그룹
    for y in range(HN, N):
        for x in range(HM, M):
            temp_matrix[y - HN][x] = matrix[y][x]

    # 1번 그룹
    for y in range(HN):
        for x in range(HM, M):
            temp_matrix[y][x - HM] = matrix[y][x]

    matrix = temp_matrix

N, M, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))

for c in cmd:
    if c == 1:
        cmd1()
    elif c == 2:
        cmd2()
    elif c == 3:
        cmd3()
    elif c == 4:
        cmd4()
    elif c == 5:
        cmd5()
    else:
        cmd6()

print_matrix(matrix)
