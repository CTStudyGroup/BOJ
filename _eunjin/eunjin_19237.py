# 번호가 1인 상어는 나머지 모두를 쫓아낼 수 있다.
# 맨 처음에는 모든 상어가 자기 칸에 자신의 냄새를 뿌린다.
# 1초마다 모든 상어가 상하좌우 인접 칸으로 이동하고, 자신의 냄새를 이동한 칸에 뿌린다.
# 이때 상어는 동시에 이동한다. 다른 상어의 이동이 그 다음 상어의 이동에 영향 주지 않음
# 냄새는 상어가 k번 이동하고 나면 사라진다.

# 상어의 이동방향 결정: 인접 칸 중 냄새가 없는 칸으로 방향 전환
# 모든 칸에 냄새가 있으면 자신의 냄새가 있는 칸의 방향으로 전환
# 냄새가 없는 칸이 여러개면 특정 우선순위를 따라서 방향 전환
# 우선순위는 상어 마다, 상어가 보고있는 방향마다 다 다르다.

# 모든 상어가 이동한 후, 한 칸에 여러 마리 상어가 있으면 가장 작은 번호 가진 상어 하나만 살아남는다.

N, M, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
for y in range(N):
    for x in range(N):
        board[y][x] -= 1

# 각 좌표의 냄새 정보, smell_board[y][x]: (y,x)좌표의 냄새 [shark num, k]
smell_board = [[[] for _ in range(N)] for _ in range(N)]

# 0번 ~ M-1번 상어의 좌표
sharks = [[-1, -1] for _ in range(M)]
for y in range(N):
    for x in range(N):
        if board[y][x] >= 0:
            sharks[board[y][x]] = [y, x]

# 0번 ~ M-1번 상어의 방향 정보
shark_dirr = list(map(int, input().split()))
for i in range(M):
    shark_dirr[i] -= 1

# 0번 ~ M-1번 상어마다 방향 우선순위
dirr_priority = []  # dirr_priority[x][y][z]: x번 상어의 방향이 y일 때, 우선순위 z번의 방향
for _ in range(M):
    p = [list(map(int, input().split())) for _ in range(4)]
    for y in range(4):
        for x in range(4):
            p[y][x] -= 1

    dirr_priority.append(p)

def print_board():
    print("--- board ---")
    for row in board:
        for elem in row:
            print(elem, end=" ")
        print()

def print_smell_board():
    print("--- smell board ---")
    for row in smell_board:
        for elem in row:
            print(elem, end=" ")
        print()

def print_priority():
    print("--- dirr priority ---")
    for i in range(M):
        print("priority i:", i)
        for row in dirr_priority[i]:
            for elem in row:
                print(elem, end=" ")
            print()

# 모든 상어의 좌표에 냄새 뿌리기
def create_smell():
    global smell_board
    for i in range(M):
        if sharks[i]:
            y, x = sharks[i][0], sharks[i][1]
            smell_board[y][x] = [i, K]


# sn번 상어의 다음 이동 방향 결정
dy = [-1, 1, 0, 0]  # 상,하,좌,우
dx = [0, 0, -1, 1]
def get_shark_dirr(sn):
    ret = -1
    shark_y, shark_x = sharks[sn]  # 현재 sn번 상어의 좌표
    curr_dirr = shark_dirr[sn]  # 현재 sn번 상어가 보고있는 방향
    # 냄새가 없는 모든 칸, 내 냄새가 있는 모든 칸의 이동 방향 구하기
    my_smell = []  # 인접 칸 중 내 냄새가 있는 칸에 대한 이동방향
    no_smell = []  # 인접 칸 중 냄새가 없는 칸에 대한 이동방향
    for i in range(4):
        ny = shark_y + dy[i]
        nx = shark_x + dx[i]

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if not smell_board[ny][nx]:
            no_smell.append(i)
        else:
            if smell_board[ny][nx][0] == sn:  # 내 냄새인 경우
                my_smell.append(i)

    if len(no_smell) == 1:  # 냄새 없는 칸이 딱 한칸이면, 그 칸으로 이동
        # print(sn, "번 상어의 냄새 없는 칸은 하나뿐이고, 이동 방향:", no_smell[0])
        ret = no_smell[0]
    elif len(no_smell) == 0:  # 냄새 없는 칸이 없다면, 내 냄새로 가는 칸 중 우선순위에 따라 이동
        priority = dirr_priority[sn][curr_dirr]
        for i in priority:
            if i in my_smell:
                # print(sn, "번 상어의 우선순위에 의한 내 냄새 있는 칸, 이동 방향:", i)
                ret = i
                break
    else:  # 냄새 없는 칸이 여러 개인 경우
        priority = dirr_priority[sn][curr_dirr]
        for i in priority:
            if i in no_smell:
                # print(sn, "번 상어의 우선순위에 의한 냄새 없는 칸, 이동 방향:", i)
                ret = i
                break
    return ret

# 모든 상어의 이동 방향 업데이트
def update_all_shark_dirr():
    global shark_dirr
    for i in range(M):
        if sharks[i]:  # 삭제되지 않은 상어에 대해서만
            shark_dirr[i] = get_shark_dirr(i)

# 모든 상어를 각자의 이동방향에 따라 한 칸 이동
def move_shark():
    for i in range(M):
        if not sharks[i]:  # 이미 삭제된 상어는 skip
            continue
        by, bx = sharks[i][0], sharks[i][1]  # 기존 상어 좌표
        dirr = shark_dirr[i]  # 상어의 이동 방향
        board[by][bx] = -1  # 기존 자리 비우고

        ny, nx = by + dy[dirr], bx + dx[dirr]  # 새로운 좌표
        if board[ny][nx] >= 0:  # 해당 좌표에 다른 상어가 있으면, 현재 상어는 쫓겨나야함
            sharks[i] = []  # 상어 좌표 배열 비우기
        else:
            board[ny][nx] = i
            sharks[i][0], sharks[i][1] = ny, nx


# 모든 냄새의 k값 업데이트
def reduce_smell():
    for y in range(N):
        for x in range(N):
            if smell_board[y][x]:
                # if sharks[smell_board[y][x][0]]:
                smell_board[y][x][1] -= 1  # 냄새 1 줄이기
                if smell_board[y][x][1] == 0:  # 냄새 아예 없어지면 초기화
                    smell_board[y][x] = []

# 1번 상어만 격자에 남았는지 여부를 리턴
def check_end():
    for y in range(N):
        for x in range(N):
            if board[y][x] > 0:
                return False
    return True

create_smell()
for T in range(1, 1001):
    # print(T, "번째 이동")
    update_all_shark_dirr()
    # print("updated shark dirr:", shark_dirr)

    move_shark()
    # print_board()

    reduce_smell()
    # print_smell_board()

    create_smell()
    # print_smell_board()

    if check_end():
        print(T)
        exit()
print(-1)
