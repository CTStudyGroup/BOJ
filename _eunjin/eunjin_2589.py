from collections import deque

N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def bfs(start_y, start_x, cnt):
    q = deque()

    q.append((start_y, start_x, cnt))
    visited[start_y][start_x] = True

    while q:
        y, x, n = q.popleft()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if matrix[ny][nx] == 'L' and not visited[ny][nx]:
                q.append((ny, nx, n+1))
                visited[ny][nx] = True

    return n


result = []

# 각 L마다 depth를 구하기
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'L':
            visited = [[False]*M for _ in range(N)]
            result.append(bfs(i, j, 0))

# print(result)
print(max(result))
