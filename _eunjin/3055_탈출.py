from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
matrix = [list(input().strip()) for _ in range(R)]

start_y, start_x = 0, 0
water = []
for y in range(R):
    for x in range(C):
        if matrix[y][x] == 'S':
            start_y, start_x = y, x
        elif matrix[y][x] == '*':
            water.append((y, x))

# 한번의 bfs에서 물+고슴도치 모두 확장, 물을 먼저 확장시키고 고슴도치 경로 결정하기
q = deque()
visited = [[False] * C for _ in range(R)]
answer = -1
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# 물 시작 노드 추가
for y, x in water:
    q.append((y, x, 0, 0))  # y, x, type(0:물, 1:고슴도치), depth

q.append((start_y, start_x, 1, 0))  # 고슴도치 시작 노드 추가

while q and answer < 0:
    y, x, type, depth = q.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            continue

        if not visited[ny][nx]:
            if type == 0 and matrix[ny][nx] == '.':
                q.append((ny, nx, 0, depth + 1))
                matrix[ny][nx] = "*"
                visited[ny][nx] = True

            if type == 1 and matrix[ny][nx] == '.':
                q.append((ny, nx, 1, depth + 1))
                visited[ny][nx] = True

            if type == 1 and matrix[ny][nx] == 'D':
                answer = depth + 1
                break

print("KAKTUS") if answer < 0 else print(answer)
