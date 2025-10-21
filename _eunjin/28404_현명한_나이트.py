from collections import deque

N, M = map(int, input().split())
Y, X = map(int, input().split())
Y -= 1
X -= 1

matrix = [[-1] * N for _ in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = m

# bfs로 탐색하면서 해당 좌표에 말 있으면 현재까지의 이동 거리 = 최단 거리
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
dx = [-2, -2, -1, -1, 1, 1, 2, 2]

orders = [-1] * M

q = deque()
visited = [[False] * N for _ in range(N)]
visited[Y][X] = True
q.append((Y, X, 0))  # y, x, depth

while q:
    cy, cx, depth = q.popleft()

    if matrix[cy][cx] >= 0:
        orders[matrix[cy][cx]] = depth

    for i in range(8):
        ny, nx = cy + dy[i], cx + dx[i]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            visited[ny][nx] = True
            q.append((ny, nx, depth + 1))

print(*orders)
