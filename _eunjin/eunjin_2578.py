# 입력 받기
board = [list(map(int, input().split())) for _ in range(5)]
number = [list(map(int, input().split())) for _ in range(5)]

bingo = [False for _ in range(26)]

# print(board)
# print(number)
# print(bingo)


def isBingo():
    global board, bingo
    cnt = 0

    # 세로 방향 빙고 찾기
    for x in range(5):
        answer = True
        for y in range(5):
            n = board[y][x]
            if not bingo[n]:
                answer = False
                break
        if answer:
            cnt += 1

    # 가로 방향 빙고 찾기
    for y in range(5):
        answer = True
        for x in range(5):
            n = board[y][x]
            if not bingo[n]:
                answer = False
                break
        if answer:
            cnt += 1

    # 대각선 방향 빙고 찾기
    answer = True
    for i in range(5):
        n = board[i][i]
        if not bingo[n]:
            answer = False
            break
    if answer:
        cnt += 1

    answer = True
    for i in range(4, -1, -1):
        n = board[i][4-i]
        if not bingo[n]:
            answer = False
            break
    if answer:
        cnt += 1

    return cnt >= 3


N = 1

for y in range(5):
    for x in range(5):
        n = number[y][x]
        bingo[n] = True
        # print(isBingo())
        if isBingo():
            print(N)
            exit()

        N += 1
