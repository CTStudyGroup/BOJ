# 빨간 보드 출발: 초록, 파랑으로 다른 블록을 만나거나 보드 끝까지 이동
# 초록 보드: 한 행에 전부 블록이 있으면 해당 행의 타일 모두 삭제, 점수 +1
# 파란 보드: 한 열에 전부 블록이 있으면 해당 열의 타일 모두 삭제, 점수 +1
# 초록 특별 칸: 0번, 1번 행에 블록이 있으면 블록 있는 행의 개수만큼 제일 아래 행의 타일 삭제, 한칸씩 전부 밑으로 이동
# 파란 특별 칸: 0번, 1번 열에 블록이 있으면 블록 있는 열의 개수만큼 제일 오른쪽 행의 타일 삭제, 한칸씩 전부 오른쪽으로 이동

# 특정 행/열이 전부 블록 있는 경우와 특별칸에 블록 있는 경우가 동시 발생하면
# 행/열이 블록으로 가득 찬 경우가 없을 때까지 점수 얻는 과정 먼저 하고, 그러고 나서도 특별칸에 블록이 남아있으면 특별 진행

N = int(input())
info = []
for _ in range(N):
    t, y, x = map(int, input().split())
    info.append([t, (y, x)])


dt1 = [[0, 0]]
dt2 = [[0, 0], [0, 1]]  # (y,x), (y,x+1) => 1*2
dt3 = [[0, 0], [1, 0]]  # (y,x), (y+1,x) => 2*1
dt = [[], dt1, dt2, dt3]

matrix = [[0] * 10 for _ in range(10)]
# (0,0) ~ (3,3): red
# (4,0) ~ (5,3): green special
# (4,0) ~ (9,3): green
# (0,4) ~ (3,5): blue special
# (0,4) ~ (3,9): blue

def print_matrix():
    print("-------- matrix ---------")
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()

dy = [1, 0]  # green, blue
dx = [0, 1]

# (y,x) 자리에 type t 블록 놓을 수 있는지 여부
def valid(t, y, x):
    for dty, dtx in dt[t]:
        ny, nx = y + dty, x + dtx
        if ny < 0 or ny >= 10 or nx < 0 or nx >= 10:  # 범위 초과
            return False
        if matrix[ny][nx]:  # 다른 블록 있음
            return False
    return True

# (y,x)에서 시작하는 type t짜리 블록을 이동
def move_block(t, start_y, start_x):
    # 초록색으로 이동
    ny, nx = start_y, start_x
    while valid(t, ny, nx):
        ny, nx = ny + dy[0], nx + dx[0]
    fy, fx = ny - dy[0], nx - dx[0]  # 마지막 valid한 시점으로 설정
    for dty, dtx in dt[t]:  # 해당 위치에 블록 추가
        matrix[fy + dty][fx + dtx] = 1

    # 파란색으로 이동
    ny, nx = start_y, start_x
    while valid(t, ny, nx):
        ny, nx = ny + dy[1], nx + dx[1]
    fy, fx = ny - dy[1], nx - dx[1]  # 마지막 valid한 시점으로 설정
    for dty, dtx in dt[t]:  # 해당 위치에 블록 추가
        matrix[fy + dty][fx + dtx] = 1


# green, blue 행/열이 블록으로 가득 차있는지 여부 확인
# 어차피 특별 영역에서 모든 행/열이 블록으로 가득 찰 수는 없음, 일반 영역만 보면 된다
def check_full():
    global score
    ret = [[], []]  # row, col
    # 초록 영역
    for y in range(6, 10):
        flag = True
        for x in range(0, 4):
            if matrix[y][x] == 0:
                flag = False
                break

        if flag:
            ret[0].append(y)
            score += 1

    # 파란 영역
    for x in range(6, 10):
        flag = True
        for y in range(0, 4):
            if matrix[y][x] == 0:
                flag = False
                break

        if flag:
            ret[1].append(x)
            score += 1

    return ret


# 지워야할 행을 전부 0으로 만들기
def delete_row(R):
    # print(R, "번째 행 삭제")
    for x in range(0, 4):
        matrix[R][x] = 0

# 지워야할 열을 전부 0으로 만들기
def delete_col(C):
    # print(C, "번째 열 삭제")
    for y in range(0, 4):
        matrix[y][C] = 0

# 지워진 행 위의 행을 한칸씩 내리기
def move_row(R):
    for y in range(R - 1, 3, -1):
        for x in range(0, 4):
            matrix[y + 1][x] = matrix[y][x]

# 지워진 열 왼쪽의 열을 한칸씩 오른쪽으로 이동
def move_col(C):
    for x in range(C - 1, 3, -1):
        for y in range(0, 4):
            matrix[y][x + 1] = matrix[y][x]

# 주어진 행/열 모두 삭제
# arr[0]: 삭제할 열, arr[1]: 삭제할 행
def delete_all_row_col(arr):
    arr[0].sort()  # 위에서부터 진행해야 덮어쓰기 문제 안생김
    arr[1].sort()
    for r in arr[0]:
        delete_row(r)
        move_row(r)

    for c in arr[1]:
        delete_col(c)
        move_col(c)

# 특별 영역에 블록 있는지 확인해서 특별 연산
def check_special():
    # 초록색 영역
    for y in range(4, 6):
        for x in range(0, 4):
            if matrix[y][x]:  # 블록 있으면
                move_row(9)
                delete_row(y)

    # 파란색 영역
    for x in range(4, 6):
        for y in range(0, 4):
            if matrix[y][x]:
                move_col(9)
                delete_col(x)

def count():
    ret = 0
    for row in matrix:
        ret += sum(row)
    return ret

score = 0

for t, cord in info:
    move_block(t, cord[0], cord[1])
    delete_all_row_col(check_full())
    check_special()
    # print_matrix()

print(score)
print(count())


