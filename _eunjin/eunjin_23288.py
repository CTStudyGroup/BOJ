from collections import deque

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dice = [1, 2, 3, 4, 5, 6]
dice_x, dice_y = 0, 0
dice_dir = 2

# 북, 동, 남, 서
dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]
dr_reverse = [0, 3, 4, 1, 2]  # 반대 방향
dr_clock = [0, 2, 3, 4, 1]  # 시계 방향
dr_rclock = [0, 4, 1, 2, 3]  # 반시계 방향

# 북, 동, 남, 서 방향으로 굴러갈 때의 주사위 숫자 위치 변화
dd = [[],
      [1, 5, 2, 3, 0, 4],
      [2, 1, 5, 0, 4, 3],
      [4, 0, 2, 3, 5, 1],
      [3, 1, 0, 5, 4, 2]]

# 주사위를 dice_dir 방향으로 회전
# 방향: 북(1), 동(2), 남(3), 서(4)
def rotate_dice():
    global dice

    new_dice = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        new_dice[dd[dice_dir][i]] = dice[i]

    dice = new_dice

# 주사위를 dice_dir 방향으로 한칸 굴리기
# 이동 방향에 칸이 없다면, 반대 방향으로 돌려 한 칸 굴리기
def roll_dice():
    global dice, dice_y, dice_x, dice_dir

    ny = dice_y + dy[dice_dir]
    nx = dice_x + dx[dice_dir]

    if ny < 0 or ny >= N or nx < 0 or nx >= M:  # 범위 초과이면 방향 전환
        dice_dir = dr_reverse[dice_dir]
        ny = dice_y + dy[dice_dir]
        nx = dice_x + dx[dice_dir]

    rotate_dice()  # 주사위 숫자 업데이트
    dice_y = ny  # 주사위 좌표 업데이트
    dice_x = nx

# 주사위가 위치한 칸에 대한 점수 bfs탐색으로 획득
def get_score():
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((dice_y, dice_x))
    visited[dice_y][dice_x] = True

    base_score = matrix[dice_y][dice_x]
    times = 0

    while q:
        y, x = q.popleft()

        times += 1

        for i in range(1, 5):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if matrix[ny][nx] == base_score:  # 출발점의 수와 같으 경우일 떄만
                    q.append((ny, nx))
                    visited[ny][nx] = True

    return base_score * times

# 주사위 다음 이동 방향 결정
def update_direction():
    global dice_dir

    dice_num = dice[-1]
    matrix_num = matrix[dice_y][dice_x]

    if dice_num > matrix_num:
        dice_dir = dr_clock[dice_dir]
    elif dice_num < matrix_num:
        dice_dir = dr_rclock[dice_dir]


total_score = 0
while K > 0:
    roll_dice()
    total_score += get_score()
    update_direction()
    K -= 1
print(total_score)
