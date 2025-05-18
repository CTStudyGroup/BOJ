import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

# bfs 탐색하면서 최대 연결 노드 개수 구하기
matrix = [['.' for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = "#"

answer = 0

visited = [[False] * M for _ in range(N)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for y in range(N):
    for x in range(M):
        if matrix[y][x] == "#" and not visited[y][x]:
            n = 1
            q = deque()
            q.append((y, x))
            visited[y][x] = True

            while q:
                cy, cx = q.popleft()

                for i in range(4):
                    ny, nx = cy + dy[i], cx + dx[i]

                    if 0 <= ny < N and 0 <= nx < M:
                        if not visited[ny][nx] and matrix[ny][nx] == "#":
                            q.append((ny, nx))
                            visited[ny][nx] = True
                            n += 1

            answer = max(answer, n)

print(answer)
