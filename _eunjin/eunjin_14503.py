N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def allCleaned(y, x):  # (y,x) 좌표 주변 4칸 중 빈 칸이 있는지 여부 반환
    global N, M, matrix
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny >= 0 and ny < N and nx >= 0 and nx < M:
            if matrix[ny][nx] == 0:
                return False

    return True


def backward(y, x, d):  # (y,x) 좌표와 방향 기준 한 칸 후진 가능한지 여부 반환
    ny = y+dy[d]
    nx = x+dx[d]
    if ny < 0 or ny >= N or nx < 0 or nx >= M:
        return False
    if matrix[ny][nx] == 1:
        return False
    return True


def solve(y, x, d):
    global matrix
    # print("solve called:", y, x, d)

    if not matrix[y][x]:  # 현재 칸 청소
        matrix[y][x] = -1
        # print("cleaned y:", y, ", x:", x)

    if allCleaned(y, x):  # 주변에 빈 칸 없는 경우
        if backward(y, x, d):  # 한 칸 후진 가능한 경우
            ny = y+dy[d]
            nx = x+dx[d]

            solve(ny, nx, d)
        else:  # 한 칸 후진 불가한 경우
            return
    else:  # 주변에 빈 칸 있는 경우
        for i in range(1, 5):
            nd = (d-i) % 4
            ny, nx = y, x
            if nd == 0:
                ny += dy[2]
                nx += dx[2]
            elif nd == 1:
                ny += dy[3]
                nx += dx[3]
            elif nd == 2:
                ny += dy[0]
                nx += dx[0]
            elif nd == 3:
                ny += dy[1]
                nx += dx[1]

            if ny >= 0 and ny < N and nx >= 0 and nx < M:
                if matrix[ny][nx] == 0:
                    solve(ny, nx, nd)
                    return


solve(r, c, d)

result = 0
for row in matrix:
    for col in row:
        if col == -1:
            result += 1


print(result)
