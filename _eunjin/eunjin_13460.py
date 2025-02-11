from collections import deque

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
visited = []

ry, rx, by, bx = 0, 0, 0, 0

for n in range(N):
    for m in range(M):
        if board[n][m] == "R":
            ry, rx = n, m
        if board[n][m] == "B":
            by, bx = n, m


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def move(y, x, i, j):  # 벽 또는 구멍을 만날 때까지 이동 후 좌표와 이동한 칸 수 반환
    cnt = 0
    while board[y+i][x+j] != "#" and board[y][x] != "O":
        y += i
        x += j
        cnt += 1
    return y, x, cnt


q = deque()
q.append((ry, rx, by, bx, 1))  # ry, rx, by, bx, n
visited.append((ry, rx, by, bx))

ans = -1

while q:
    ry, rx, by, bx, n = q.popleft()

    if n > 10:
        break

    for i in range(4):
        nry, nrx, rCnt = move(ry, rx, dy[i], dx[i])
        nby, nbx, bCnt = move(by, bx, dy[i], dx[i])

        if board[nby][nbx] == "O":  # 파란 구슬이 빠질 수 있는 경우, 이 케이스는 안되는 것
            continue

        if board[nry][nrx] == "O":  # 빨간 구슬이 빠질 수 있는 경우, 횟수를 출력하고 종료
            print(n)
            exit()

        if nry == nby and nrx == nbx:  # 두 구슬 좌표가 겹치는 경우
            if rCnt > bCnt:  # 빨간 구슬이 늦게 도달한 경우
                nry -= dy[i]
                nrx -= dx[i]
            else:
                nby -= dy[i]
                nbx -= dx[i]

        if (nry, nrx, nby, nbx) not in visited:
            visited.append((nry, nrx, nby, nbx))
            q.append((nry, nrx, nby, nbx, n+1))

print(-1)
