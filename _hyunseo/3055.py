from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

# 물과 고슴도치 위치 미리 큐에 넣기
water_q = deque()
hedgehog_q = deque()
visited = [[False]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            water_q.append((i, j))
        elif board[i][j] == 'S':
            hedgehog_q.append((i, j, 0))  # y, x, depth
            visited[i][j] = True

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while hedgehog_q:
    # 1. 먼저 물부터 확장
    for _ in range(len(water_q)):
        wy, wx = water_q.popleft()
        for d in range(4):
            nwy, nwx = wy + dy[d], wx + dx[d]
            if 0 <= nwy < R and 0 <= nwx < C and board[nwy][nwx] == '.':
                board[nwy][nwx] = '*'
                water_q.append((nwy, nwx))

    # 2. 고슴도치 이동
    for _ in range(len(hedgehog_q)):
        y, x, depth = hedgehog_q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < R and 0 <= nx < C:
                if board[ny][nx] == 'D':
                    print(depth + 1)
                    sys.exit()
                if board[ny][nx] == '.' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    hedgehog_q.append((ny, nx, depth + 1))

print("KAKTUS")
