import copy
R, C, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

machine = []

for y in range(R):
    for x in range(C):
        if matrix[y][x] == -1:
            machine.append(y)

top = machine[0]
bottom = machine[1]

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

# 미세먼지 확산
def spread():
    global matrix
    tmp_matrix = copy.deepcopy(matrix)

    for y in range(R):
        for x in range(C):
            if matrix[y][x] <= 0:
                continue

            amount = matrix[y][x] // 5  # 확산되는 양
            cnt = 0  # 확산된 방향 개수
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= R or nx >= C:
                    continue
                if matrix[ny][nx] == -1:
                    continue
                cnt += 1  # 확산된 방향 개수 카운트
                tmp_matrix[ny][nx] += amount  # 확산
            tmp_matrix[y][x] -= amount * cnt  # 남은 미세먼지 양
    matrix = tmp_matrix

# 공기청정기
def refresh():
    global matrix
    # 위쪽 공기청정기: 아래쪽, 왼쪽, 위쪽, 오른쪽 순서로 순환
    for y in range(top - 2, -1, -1):
        matrix[y + 1][0] = matrix[y][0]
    for x in range(0, C - 1):
        matrix[0][x] = matrix[0][x + 1]
    for y in range(0, top):
        matrix[y][C - 1] = matrix[y + 1][C - 1]
    for x in range(C - 1, 1, -1):
        matrix[top][x] = matrix[top][x - 1]
    matrix[top][1] = 0

    # 아래쪽 공기청정기: 위쪽, 왼쪽, 아래쪽, 오른쪽 순서로 순환
    for y in range(bottom + 1, R - 1):
        matrix[y][0] = matrix[y + 1][0]
    for x in range(0, C - 1):
        matrix[R - 1][x] = matrix[R - 1][x + 1]
    for y in range(R - 1, bottom, -1):
        matrix[y][C - 1] = matrix[y - 1][C - 1]
    for x in range(C - 1, 1, -1):
        matrix[bottom][x] = matrix[bottom][x - 1]
    matrix[bottom][1] = 0


for _ in range(T):
    spread()  # 미세먼지 확산
    refresh()  # 공기청정기 작동

answer = 0
for row in matrix:
    answer += sum(row)

# for row in matrix:
#     for col in row:
#         print(col, end=" ")
#     print()

print(answer + 2)

