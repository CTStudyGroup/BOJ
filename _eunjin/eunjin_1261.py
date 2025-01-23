from collections import deque
import sys
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

INF = 100000


def bfs(y, x):
    q = deque()
    q.append((y, x, 0))

    while q:
        y, x, d = q.popleft()

        if dist[y][x] < d:
            continue

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                temp_d = d
                if matrix[ny][nx] == 1:
                    temp_d += 1
                if temp_d < dist[ny][nx]:
                    dist[ny][nx] = temp_d
                    q.append((ny, nx, temp_d))


M, N = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(N)]
dist = [[INF]*M for _ in range(N)]

dist[0][0] = 0

bfs(0, 0)

print(dist[N-1][M-1])
