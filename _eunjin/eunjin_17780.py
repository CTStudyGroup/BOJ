N, K = map(int, input().split())

opp_dir = [0, 2, 1, 4, 3]
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

# 체스판 색상 정보
matrix = [list(map(int, input().split())) for _ in range(N)]

# 체스판 위 말 정보
position = [[[]for _ in range(N)] for _ in range(N)]

# 한 좌표에 쌓인 말의 최대 개수
max_pos = 1

chess = []

for i in range(K):
    y, x, d = map(int, input().split())
    chess.append([y-1, x-1, d])
    position[y-1][x-1].append(i)


def isExceeds(i):  # i번째 말이 다음 칸으로 이동할 때 체스판을 벗어나는지 여부 반환
    global chess, dy, dx
    y, x, d = chess[i]
    ny = y+dy[d]
    nx = x+dx[d]
    if nx >= N or nx < 0 or ny >= N or ny < 0:
        return True
    return False


def nextIsBlue(i):  # i번째 말의 다음 칸이 파란색인지 여부 반환
    global matrix, chess, dy, dx
    y, x, d = chess[i]
    ny = y+dy[d]
    nx = x+dx[d]
    return True if matrix[ny][nx] == 2 else False


def goNext(i, ny, nx):  # i번째 말을 (ny,nx) 좌표로 이동
    global matrix, chess, position, max_pos
    if nx >= N or nx < 0 or ny >= N or ny < 0:
        return

    y, x = chess[i][0], chess[i][1]
    mals = position[y][x]  # 현재 좌표에 있는 모든 말 찾기

    if matrix[ny][nx] == 1:  # 다음 칸이 빨간색인 경우
        mals = mals[::-1]  # 이동할 말 역순으로 뒤집기

    position[ny][nx].extend(mals)  # 다음 칸으로 말 모두 이동
    for mal in mals:  # 각 말의 (y,x) 좌표 업데이트
        chess[mal][0] = ny
        chess[mal][1] = nx

    position[y][x] = []  # 원래 있던 칸의 말 초기화
    max_pos = max(max_pos, len(position[ny][nx]))  # 말 최대 개수 업데이트


t = 0
for t in range(1, 1001):
    for i in range(K):
        # 말의 y좌표, x좌표, 방향
        y, x, d = chess[i]

        # 해당 말이 가장 밑에 있는 말이 아닌 경우
        if position[y][x][0] != i:
            continue

        # 다음 칸으로 이동 시 체스판을 벗어나는 경우 방향 반대로
        if isExceeds(i):
            d = opp_dir[d]
            chess[i] = [y, x, d]

        # 다음 칸이 파란색인 경우 방향 반대로
        if nextIsBlue(i):
            d = opp_dir[d]
            chess[i] = [y, x, d]

        ny = y+dy[d]
        nx = x+dx[d]

        # 방향을 반대로 바꾼 후에 다음 칸이 체스판을 벗어나는 경우
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue

        # 다음 칸이 파란색이 아닐 때에만 이동
        if matrix[ny][nx] != 2:
            goNext(i, ny, nx)

    # print("-------------position, i:", i+1, "-------------")
    # for y in range(N):
    #     for x in range(N):
    #         print(position[y][x], end=" ")
    #     print()
    if max_pos >= 4:
        print(t)
        exit()

print(-1)
