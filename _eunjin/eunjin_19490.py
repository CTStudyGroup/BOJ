from collections import deque

# 입력 받기
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

dist = [[-1]*m for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

start_y = -1
start_x = -1

for y in range(n):
    for x in range(m):
        if matrix[y][x] == 2:
            start_y = y
            start_x = x
            dist[y][x] = 0

        if matrix[y][x] == 0:
            dist[y][x] = 0


# bfs 실행
q = deque()
q.append((start_y, start_x, 0))

visited = [[False]*m for _ in range(n)]
visited[start_y][start_x] = True

while q:
    y, x, d = q.popleft()
    # print("y:", y, ",x:", x)

    dist[y][x] = d

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # print("ny:", ny, ', nx:', nx)

        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            if matrix[ny][nx] == 1:
                # print("next visit: ", ny, nx)
                q.append((ny, nx, d+1))
                visited[ny][nx] = True


for row in dist:
    for elem in row:
        print(elem, end=" ")
    print()
