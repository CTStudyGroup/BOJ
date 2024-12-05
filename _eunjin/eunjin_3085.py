import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())

matrix = [list(input()) for _ in range(N)]

# print(matrix)

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def countMax(Y, NY, X, NX):
    global matrix, N

    max_y_cnt = 0
    max_ny_cnt = 0
    max_x_cnt = 0
    max_nx_cnt = 0

    # 행 탐색
    y_cnt = 0
    ny_cnt = 0
    y_color = matrix[Y][0]
    ny_color = matrix[NY][0]
    for x in range(N):
        y_curr = matrix[Y][x]
        ny_curr = matrix[NY][x]
        if y_color == y_curr:
            y_cnt += 1
        else:
            y_color = y_curr
            max_y_cnt = max(max_y_cnt, y_cnt)
            y_cnt = 1
        max_y_cnt = max(max_y_cnt, y_cnt)

        if ny_color == ny_curr:
            ny_cnt += 1
        else:
            ny_color = ny_curr
            max_ny_cnt = max(max_ny_cnt, ny_cnt)
            ny_cnt = 1
        max_ny_cnt = max(max_ny_cnt, ny_cnt)

    # 열 탐색
    x_cnt = 0
    nx_cnt = 0
    x_color = matrix[0][X]
    nx_color = matrix[0][NX]
    for y in range(N):
        x_curr = matrix[y][X]
        nx_curr = matrix[y][NX]
        if x_color == x_curr:
            x_cnt += 1
        else:
            x_color = x_curr
            max_x_cnt = max(max_x_cnt, x_cnt)
            x_cnt = 1
        max_x_cnt = max(max_x_cnt, x_cnt)

        if nx_color == nx_curr:
            nx_cnt += 1
        else:
            nx_color = nx_curr
            max_nx_cnt = max(max_nx_cnt, nx_cnt)
            nx_cnt = 1
        max_nx_cnt = max(max_nx_cnt, nx_cnt)

    return max(max_y_cnt, max_ny_cnt, max_x_cnt, max_nx_cnt)


# 모든 요소 돌면서 자리 바꾸기
max_cnt = 0
for y in range(N):
    for x in range(N):
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if matrix[y][x] != matrix[ny][nx]:
                    # 사탕 교환
                    temp = matrix[y][x]
                    matrix[y][x] = matrix[ny][nx]
                    matrix[ny][nx] = temp

                    # 사탕 최대 개수 구하기
                    cnt = countMax(y, ny, x, nx)
                    max_cnt = max(max_cnt, cnt)
                    # print("(", y, ",", x, ") -> (", ny, ",", nx, "):", max_cnt)

                    # 사탕 원상 복귀
                    matrix[ny][nx] = matrix[y][x]
                    matrix[y][x] = temp
            max_cnt = max(max_cnt, countMax(y, y, x, x))

print(max_cnt)
