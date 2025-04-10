# 한 칸에는 학생 한 명만 가능
# 인접한 칸: 상하좌우

# 학생의 자리 정하기
# 비어있는 칸 중에서, 좋아하는 학생이 인접한 칸에 가장 많이 있는 그 칸으로
# 좋아하는 학생이 있는 인접 칸의 개수가 같은 칸이 여러 개이면, (=좋아하는 학생 인접 횟수가 최대치인 칸이 여러개이면), 인접 칸 중 비어있는 칸이 가장 많은 칸으로
# 그 인접 칸 중 비어있는 칸도 여러개이면, 행의 번호가 가장 작은 칸으로
# 그러한 칸도 여러개이면 열의 번호가 가장 작은 칸으로

N = int(input())

def print_board():
    for row in board:
        for elem in row:
            print(elem, end=" ")
        print()


students = [[] for _ in range(N ** 2 + 1)]  # students[x]: x번 학생이 좋아하는 학생 배열
order = []  # 주어진 학생 순서
for _ in range(N**2):
    i, a, b, c, d = map(int, input().split())
    students[i] = [a, b, c, d]
    order.append(i)

board = [[0] * N for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# sn번 학생의 자리 정하기
def get_seat(sn):
    # 비어있는 칸들 중 좋아하는 학생이 인접한 칸에 가장 많은 칸 리스트 구하기
    max_near_like = []
    mxcnt = -1
    for y in range(N):
        for x in range(N):
            if board[y][x] != 0:
                continue

            # 좋아하는 학생이 있는 인접 칸의 개수 세기
            cnt = 0
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if board[ny][nx] in students[sn]:
                        cnt += 1

            if cnt > mxcnt:  # 최댓값 및 리스트 갱신
                mxcnt = cnt
                max_near_like = [(y, x)]
            elif cnt == mxcnt:
                max_near_like.append((y, x))

    # print(sn, "번 학생의 1번 조건 만족하는 좌표:", max_near_like)

    if len(max_near_like) == 1:
        return max_near_like[0][0], max_near_like[0][1]  # y,x

    # 인접한 칸 중 비어있는 칸이 가장 많은 칸 리스트 구하기
    max_near_empty = []
    mxcnt = -1
    for y, x in max_near_like:
        # 인접 칸 중 비어있는 칸의 개수 세기
        cnt = 0
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] == 0:
                    cnt += 1

        if cnt > mxcnt:  # 최댓값 및 리스트 갱신
            mxcnt = cnt
            max_near_empty = [(y, x)]
        elif cnt == mxcnt:
            max_near_empty.append((y, x))

    # print(sn, "번 학생의 2번 조건 만족하는 좌표:", max_near_empty)

    if len(max_near_empty) == 1:
        return max_near_empty[0][0], max_near_empty[0][1]  # y,x

    # 행 번호가 가장 작은 칸 리스트 구하기
    min_row_num = []
    mnrow = N
    for y, x in max_near_empty:
        if y < mnrow:
            mnrow = y
            min_row_num = [(y, x)]
        elif y == mnrow:
            min_row_num.append((y, x))
        else:
            break

    # print(sn, "번 학생의 3번 조건 만족하는 좌표:", min_row_num)
    return min_row_num[0][0], min_row_num[0][1]


# 모든 학생 자리에 앉히기
for st in order:
    y, x = get_seat(st)
    board[y][x] = st

# 만족도 구하기
answer = 0
for y in range(N):
    for x in range(N):
        st = board[y][x]
        cnt = 0  # 인접 좋아하는 학생 수

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] in students[st]:
                    cnt += 1

        if cnt == 1:
            answer += 1
        elif cnt == 2:
            answer += 10
        elif cnt == 3:
            answer += 100
        elif cnt == 4:
            answer += 1000

print(answer)


