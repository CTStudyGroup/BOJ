from collections import deque

def isValid(x, y):
    global N, M
    return 0<=x<N and 0<=y<M

def bfs(start, farm):
    global visited
    queue = deque([start])
    height = farm[start[0]][start[1]]
    isPeak = True

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = x+dx, y+dy
            if isValid(nx, ny):
                if farm[nx][ny] == height and not visited[nx][ny]:
                    queue.append((nx, ny))
                elif farm[nx][ny] > height:
                    isPeak = False

    if isPeak: return 1
    return 0

N, M = list(map(int, input().split()))
farm = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
           ans += bfs((i, j), farm)
print(ans)