from collections import deque

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
mal_board = [[[] for _ in range(N)] for _ in range(N)]
mal_dirr = [0]  # 1234, 우좌상하
mal_cords = [[]]  # 말들의 좌표

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]
dd = [0, 2, 1, 4, 3]


def print_matrix(mat):
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()

# n번 말을 (y,x) 좌표로 이동
def move_to_white(n, target_y, target_x):
    curr_y, curr_x = mal_cords[n]  # 현재 n번 말의 좌표

    temp = []  # n번 말과 함께 이동해야할 말
    while mal_board[curr_y][curr_x] and mal_board[curr_y][curr_x][-1] != n:
        # n번 말이 나올 때까지 뒤에서부터 뽑음
        temp.append(mal_board[curr_y][curr_x].pop())
    temp.append(mal_board[curr_y][curr_x].pop())

    while temp:  # temp의 말 모두 목표 좌표로 이동
        k = temp.pop()
        mal_cords[k][0], mal_cords[k][1] = target_y, target_x
        mal_board[target_y][target_x].append(k)

# n번 말을 (y,x) 좌표로 이동
def move_to_red(n, target_y, target_x):
    curr_y, curr_x = mal_cords[n]

    temp = deque()
    while mal_board[curr_y][curr_x] and mal_board[curr_y][curr_x][-1] != n:
        temp.append(mal_board[curr_y][curr_x].pop())

    temp.append(mal_board[curr_y][curr_x].pop())

    while temp:
        k = temp.popleft()
        mal_cords[k][0], mal_cords[k][1] = target_y, target_x
        mal_board[target_y][target_x].append(k)

# n번말 이동
def move(n):
    curr_y, curr_x = mal_cords[n]

    ny, nx = curr_y + dy[mal_dirr[n]], curr_x + dx[mal_dirr[n]]

    if ny < 0 or ny >= N or nx < 0 or nx >= N:
        mal_dirr[n] = dd[mal_dirr[n]]
    elif board[ny][nx] == 2:
        mal_dirr[n] = dd[mal_dirr[n]]

    curr_dir = mal_dirr[n]
    ny, nx = curr_y + dy[mal_dirr[n]], curr_x + dx[mal_dirr[n]]


    if 0 <= ny < N and 0 <= nx < N:
        if board[ny][nx] == 0:
            move_to_white(n, ny, nx)
        elif board[ny][nx] == 1:
            move_to_red(n, ny, nx)

def check_end():
    for row in mal_board:
        for mals in row:
            if len(mals) >= 4:
                return False
    return True


for i in range(1, K + 1):
    y, x, d = map(int, input().split())
    mal_board[y - 1][x - 1].append(i)
    mal_dirr.append(d)
    mal_cords.append([y - 1, x - 1])

T = 1
while T <= 1000:
    for i in range(1, K + 1):
        move(i)

        if not check_end():
            print(T)
            exit()

    T += 1

print(-1)
