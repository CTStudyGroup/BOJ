import copy

# 시작은 (0,0)에서, 방향은 (0,0)에 있던 물고기 방향

# 물고기 이동
# 번호가 작은 물고기부터 한칸 이동 (모든 물고기 동시에 이동하는거 아님)
# 빈 칸 or 다른 물고기 있는 칸으로 이동 가능
# 이동 가능한 칸 만날 때까지 반시계 회전
# 이동할 수 없으면 이동X
# 기존 물고기가 있는 칸으로 이동 시 서로의 위치가 맞바뀜

# 상어 이동
# 한번에 여러칸 이동 가능
# 물고기 있는 칸으로 이동 시, 물고기를 먹고 그 물고기의 방향으로 바뀜
# 이동 중 지나가는 칸에 있는 물고기는 먹지 않음
# 물고기 있는 칸으로만 이동 가능
# 이동 가능한 칸 없으면 종료

# 상어가 먹을 수 있는 물고기 번호의 합의 최대 구하기 = 백트래킹

matrix = [[0] * 4 for _ in range(4)]
fish_list = [[] for _ in range(17)]  # [좌표,방향], 값이 0이면 해당 물고기는 보드에 없음

def print_matrix(mat):
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()

def print_fish():
    for i in range(1, 17):
        if fish_list[i] == 0:
            print(i, "번 물고기: 보드에 없음")
        else:
            print(i, "번 물고기:", fish_list[i][0], ", 방향:", fish_list[i][1])

def print_fish_dirr():
    for i in range(1, 17):
        if fish_list[i] == 0:
            print(-1, end=" ")
        else:
            print(fish_list[i][1], end=" ")
    print()

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dd = [0, 2, 3, 4, 5, 6, 7, 8, 1]

# (y,x) 좌표에서 이동 가능한 방향 찾기
def get_dirr(y, x, d):
    ret = -1
    t = 0
    cd = d
    while t < 8:  # 횟수
        t += 1

        ny, nx = y + dy[cd], x + dx[cd]
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:  # 범위 벗어난 경우
            cd = dd[cd]  # 다음 방향 탐색
            continue

        if matrix[ny][nx] == -1:  # 상어가 있는 경우
            cd = dd[cd]
            continue

        ret = cd
        break

    return ret


# n번 물고기 이동
def move_fish(n):
    cy, cx, cd = fish_list[n][0][0], fish_list[n][0][1], fish_list[n][1]
    nd = get_dirr(cy, cx, cd)
    if nd == -1:  # 이동 불가인 경우
        return
    ny, nx = cy + dy[nd], cx + dx[nd]  # 이동할 좌표

    if matrix[ny][nx] == 0:  # 빈칸으로 이동하는 경우
        matrix[ny][nx] = n
        matrix[cy][cx] = 0
        fish_list[n] = [(ny, nx), nd]
    else:  # 물고기 있는 칸으로 이동하는 경우
        temp_n = matrix[ny][nx]
        temp_d = fish_list[temp_n][1]

        matrix[ny][nx] = n
        fish_list[n] = [(ny, nx), nd]

        matrix[cy][cx] = temp_n
        fish_list[temp_n] = [(cy, cx), temp_d]

# 모든 물고기 이동
def all_fish_move():
    for i in range(1, 17):
        if fish_list[i] != 0:
            move_fish(i)

# 상어가 이동 가능한 다음 좌표 리스트 구하기, 이동 가능한 좌표 없으면 빈 리스트 리턴
def get_shark_next(cy, cx, cd):
    ret = []
    for i in range(1, 4):  # 1~3칸까지 이동 가능
        ny, nx = cy + dy[cd] * i, cx + dx[cd] * i

        if 0 <= ny < 4 and 0 <= nx < 4:
            if matrix[ny][nx] > 0:  # 물고기가 있는 칸으로만 이동 가능
                ret.append((ny, nx))
    return ret

# 입력 처리
for y in range(4):
    inp = list(map(int, input().split()))
    for x in range(0, 7, 2):
        fish = inp[x]
        dirr = inp[x + 1]
        matrix[y][x // 2] = fish
        fish_list[fish] = [(y, x // 2), dirr]


def backtracking(sy, sx, sd, depth):
    global matrix, fish_list, point, answer

    all_fish_move()
    shark_next = get_shark_next(sy, sx, sd)

    if not shark_next:
        answer = max(point, answer)
        return

    for ny, nx in shark_next:
        temp_fish_n = matrix[ny][nx]
        temp_fish = copy.deepcopy(fish_list[temp_fish_n])  # [(좌표),방향]
        temp_matrix = copy.deepcopy(matrix)
        temp_fish_list = copy.deepcopy(fish_list)

        # 상어 이동
        matrix[sy][sx] = 0
        matrix[ny][nx] = -1
        point += temp_fish_n
        fish_list[temp_fish_n] = 0
        backtracking(ny, nx, temp_fish[1], depth + 1)

        # 상어 이동 복구
        point -= temp_fish_n
        matrix[ny][nx] = temp_fish_n
        matrix[sy][sx] = -1
        matrix = temp_matrix
        fish_list = temp_fish_list

# 시작
point = matrix[0][0]  # 점수
answer = 0
start_d = fish_list[matrix[0][0]][1]
fish_list[matrix[0][0]] = 0
matrix[0][0] = -1

backtracking(0, 0, start_d, 0)

print(answer)
