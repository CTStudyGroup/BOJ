from collections import deque

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

start_y, start_x = -1, -1

for r in range(N):
    for c in range(M):
        if matrix[r][c] == "I":
            start_y, start_x = r, c

visited = [[False]*M for _ in range(N)]
q = deque()
cnt = 0
q.append((start_y, start_x))  # y,x
visited[start_y][start_x] = True

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]

        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if visited[ny][nx]:
            continue

        if matrix[ny][nx] == "O":
            q.append((ny, nx))
            visited[ny][nx] = True
        if matrix[ny][nx] == "P":
            q.append((ny, nx))
            visited[ny][nx] = True
            cnt += 1

print(cnt if cnt else "TT")
