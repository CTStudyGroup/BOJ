import copy
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

commands = []
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    commands.append((a, b, c, d, e))

# command 0:상 1:우 2:하 3:좌


def move_up(board):
    global combined
    for y in range(1, N):
        for x in range(N):
            if board[y][x]:
                num = board[y][x]
                ny = y
                while(True):  # 블록을 만날 때까지 이동
                    if ny-1 < 0:
                        break
                    if board[ny-1][x] == 0 or (board[ny-1][x] == num and not combined[ny-1][x]):
                        ny -= 1
                    else:
                        break

                if ny == y:  # 블록 이동 불가한 경우
                    continue

                if board[ny][x] == 0:  # 해당 자리에 블록이 없는 경우
                    board[ny][x] = num
                    board[y][x] = 0
                elif board[ny][x] == num:  # 두 블록의 숫자가 같은 경우
                    board[ny][x] = 2*board[ny][x]
                    board[y][x] = 0
                    combined[ny][x] = True
                else:  # 해당 자리에 블록이 있고, 숫자가 다른 경우
                    ny += 1
                    board[y][x] = 0
                    board[ny][x] = num


def move_down(board):
    global combined
    for y in range(N-2, -1, -1):
        for x in range(N):
            if board[y][x]:
                num = board[y][x]
                ny = y
                while(True):  # 블록을 만날 때까지 이동
                    if ny+1 >= N:
                        break
                    if board[ny+1][x] == 0 or (board[ny+1][x] == num and not combined[ny+1][x]):
                        ny += 1
                    else:
                        break

                if ny == y:  # 블록 이동 불가한 경우
                    continue

                if board[ny][x] == 0:  # 해당 자리에 블록이 없는 경우
                    board[ny][x] = num
                    board[y][x] = 0
                elif board[ny][x] == num:  # 두 블록의 숫자가 같은 경우
                    board[ny][x] = 2*board[ny][x]
                    board[y][x] = 0
                    combined[ny][x] = True
                else:  # 해당 자리에 블록이 있고, 숫자가 다른 경우
                    ny += 1
                    board[y][x] = 0
                    board[ny][x] = num


def move_right(board):
    global combined
    for x in range(N-2, -1, -1):
        for y in range(N):
            if board[y][x]:
                num = board[y][x]
                nx = x
                while(True):  # 블록을 만날 때까지 이동
                    if nx+1 >= N:
                        break
                    if board[y][nx+1] == 0 or (board[y][nx+1] == num and not combined[y][nx+1]):
                        nx += 1
                    else:
                        break

                if nx == x:  # 블록 이동 불가한 경우
                    continue

                if board[y][nx] == 0:  # 해당 자리에 블록이 없는 경우
                    board[y][nx] = num
                    board[y][x] = 0
                elif board[y][nx] == num:  # 두 블록의 숫자가 같은 경우
                    board[y][nx] = 2*board[y][nx]
                    board[y][x] = 0
                    combined[y][nx] = True
                else:  # 해당 자리에 블록이 있고, 숫자가 다른 경우
                    nx += 1
                    board[y][x] = 0
                    board[y][nx] = num


def move_left(board):
    global combined
    for x in range(1, N):
        for y in range(N):
            if board[y][x]:
                num = board[y][x]
                nx = x
                while(True):  # 블록을 만날 때까지 이동
                    if nx-1 < 0:
                        break
                    if board[y][nx-1] == 0 or (board[y][nx-1] == num and not combined[y][nx-1]):
                        nx -= 1
                    else:
                        break

                if nx == x:  # 블록 이동 불가한 경우
                    continue

                if board[y][nx] == 0:  # 해당 자리에 블록이 없는 경우
                    board[y][nx] = num
                    board[y][x] = 0
                elif board[y][nx] == num:  # 두 블록의 숫자가 같은 경우
                    board[y][nx] = 2*board[y][nx]
                    board[y][x] = 0
                    combined[y][nx] = True
                else:  # 해당 자리에 블록이 있고, 숫자가 다른 경우
                    nx += 1
                    board[y][x] = 0
                    board[y][nx] = num


max_value = 0

for command in commands:
    b = copy.deepcopy(board)
    for i in range(5):
        combined = [[False for _ in range(N)] for _ in range(N)]
        if command[i] == 0:
            move_up(b)
        if command[i] == 1:
            move_right(b)
        if command[i] == 2:
            move_down(b)
        if command[i] == 3:
            move_left(b)
    max_value = max(max_value, max(map(max, b)))
    # print("command:", command)
    # for row in b:
    #     for col in row:
    #         print(col, end=" ")
    #     print()


print(max_value)
