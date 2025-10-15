from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, 1, -1, -1, 0, 1]


def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = 1
    checked[y][x] = True
    while q:
        cy, cx = q.popleft()
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if visited[ny][nx]:
                continue
            if matrix[cy][cx] < matrix[ny][nx]:  # 인접 노드가 더 높으면
                return 0
            if matrix[cy][cx] == matrix[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx))
                checked[ny][nx] = True

    return 1

answer = 0
checked = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not checked[i][j]:
            visited = [[0] * M for _ in range(N)]
            answer += bfs(i, j)
print(answer)
