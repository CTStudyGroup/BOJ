R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
commands = list(input())

dy = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dx = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

# 내 아두이노, 미친아두이노의 좌표 저장
arduino = [-1, -1]
mad_arduinos = []
for r in range(R):
    for c in range(C):
        if board[r][c] == 'I':
            arduino = [r, c]
        elif board[r][c] == 'R':
            mad_arduinos.append([r, c])

# c 방향으로 아두이노 이동, 미친아두이노 만나면 False 리턴
def move_arduino(c):
    global arduino
    c = int(c)
    board[arduino[0]][arduino[1]] = '.'
    arduino[0] = arduino[0] + dy[c]
    arduino[1] = arduino[1] + dx[c]


    if board[arduino[0]][arduino[1]] == 'R':  # 미친아두이노 만나면 false
        return False
    else:
        board[arduino[0]][arduino[1]] = 'I'
    return True

# 8방향중 아두이노와 가장 가까워지는 이동 후 좌표 리턴
def get_nearest(y, x):
    ret_y, ret_x = -1, -1
    min_dist = 201

    for i in range(1, 10):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= R or nx < 0 or nx >= C:  # 보드 넘어서는 좌표
            continue

        dist = abs(arduino[0] - ny) + abs(arduino[1] - nx)

        if dist < min_dist:  # 이게 최소 거리이면
            ret_y, ret_x = ny, nx
            min_dist = dist

    return ret_y, ret_x


# 미친아두이노 모두 이동
# 미친아두이노가 아두이노를 만나면 False 리턴
# 한 칸에 2개 이상의 미친아두이노가 있게 되면 그 칸의 미친아두이노 모두 삭제
def move_mad_arduinos():
    temp_board = [['.' for _ in range(C)] for _ in range(R)]  # 이동을 마친 미친아두이노를 담아둘 보드

    for r in range(R):
        for c in range(C):
            if board[r][c] == 'R':
                ny, nx = get_nearest(r, c)  # 이동할 좌표 구하기

                if board[ny][nx] == 'I':  # 아두이노를 만나면
                    return False
                else:
                    temp_board[ny][nx] += 'R'

    # temp_board 한 칸의 길이가 3이상(.RR)이면 그 칸은 .으로 변경
    for r in range(R):
        for c in range(C):
            if len(temp_board[r][c]) > 2:
                temp_board[r][c] = '.'

    # temp_board -> board로 반영
    for r in range(R):
        for c in range(C):
            board[r][c] = temp_board[r][c][-1]
    board[arduino[0]][arduino[1]] = 'I'

    return True


for i in range(len(commands)):
    valid = move_arduino(commands[i])  # 아두이노 이동
    if not valid:  # 미친아두이노 만나면 패배
        print("kraj", i + 1)
        exit()

    valid = move_mad_arduinos()  # 미친아두이노 이동
    if not valid:
        print("kraj", i + 1)
        exit()

for row in board:
    for elem in row:
        print(elem, end='')
    print()
