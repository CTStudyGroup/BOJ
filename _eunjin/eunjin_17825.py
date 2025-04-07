dice = list(map(int, input().split()))
board = [0] * 33

# 파란색 경로
routes = [[5, 22, 23, 24, 30, 31, 32, 20, 21],
          [10, 25, 26, 30, 31, 32, 20, 21],
          [15, 27, 28, 29, 30, 31, 32, 20, 21]]
for i in range(21):
    board[i] = i * 2
board[22], board[23], board[24] = 13, 16, 19
board[25], board[26] = 22, 24
board[27], board[28], board[29], board[30], board[31], board[32] = 28, 27, 26, 25, 30, 35
# board[21]: 도착칸

mal = [0, 0, 0, 0]  # 말의 board idx

answer = 0

def backtracking(depth, mal, score):
    global answer
    if depth == 10:
        answer = max(answer, score)
        return

    for m in range(4):
        temp_mal = mal[m]  # 말의 현재 위치

        if temp_mal == 21:  # 해당 말이 도착한 상태이면 skip
            continue

        if temp_mal == 5 or 22 <= temp_mal <= 24:  # 첫번째 파란 경로
            idx = routes[0].index(temp_mal)
            if idx + dice[depth] <= 8:  # 주사위 칸 수 만큼 이동해도 도착하지 않는 경우
                next = routes[0][dice[depth] + idx]
            else:  # 도착하는 경우
                next = 21
        elif temp_mal == 10 or temp_mal == 25 or temp_mal == 26:  # 두번째 파란 경로
            idx = routes[1].index(temp_mal)
            if idx + dice[depth] <= 7:
                next = routes[1][dice[depth] + idx]
            else:
                next = 21
        elif temp_mal == 15 or 27 <= temp_mal <= 32:
            idx = routes[2].index(temp_mal)
            if idx + dice[depth] <= 8:
                next = routes[2][dice[depth] + idx]
            else:
                next = 21
        else:  # 빨간 경로
            if temp_mal + dice[depth] <= 21:
                next = temp_mal + dice[depth]
            else:
                next = 21

        if next in mal and next != 21:  # 다음 이동할 좌표에 다른 말이 있고, 그게 도착 칸이 아니라면 이동 skip
            continue

        mal[m] = next  # 말 이동
        backtracking(depth + 1, mal, score + board[next])
        mal[m] = temp_mal  # 다시 이전 위치로 복구


backtracking(0, mal, 0)
print(answer)

