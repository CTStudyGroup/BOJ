from collections import deque

N = int(input())
y1, x1, y2, x2 = map(int, input().split())


dy = [-2, -2, 0, 0, 2, 2]
dx = [-1, 1, -2, 2, -1, 1]


q = deque()
visited = [[False] * N for _ in range(N)]
visited[y1][x1] = True
q.append((y1, x1, 0))

while q:
    cy, cx, dist = q.popleft()

    if cy == y2 and cx == x2:
        print(dist)
        exit()


    for i in range(6):
        ny, nx = cy + dy[i], cx + dx[i]

        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            q.append((ny, nx, dist + 1))
            visited[ny][nx] = True

print(-1)
