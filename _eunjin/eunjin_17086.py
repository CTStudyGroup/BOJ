from collections import deque

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

# bfs로 1이 나올 때까지 거리 재가면서 탐색
dy = [1, 0, -1, 0, -1, -1, 1, 1]
dx = [0, 1, 0, -1, -1, 1, -1, 1]

answer = 0

def bfs(y, x):
    global answer

    q = deque()
    visited = [[False] * M for _ in range(N)]

    q.append((y, x, 0))
    visited[y][x] = True

    while q:
        y, x, d = q.popleft()
        if matrix[y][x] == 1:
            answer = max(answer, d)
            return

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue

            if visited[ny][nx]:
                continue

            q.append((ny, nx, d + 1))
            visited[ny][nx] = True


for i in range(N):
    for j in range(M):
        bfs(i, j)
        # print("(", i, ",", j, "): ", answer)

print(answer)
