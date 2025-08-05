from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# 틀린 풀이
# def bfs(sy, sx):
#     q = deque()
#     q.append((sy, sx, 0))  # y,x,depth
#     visited[sy][sx] = True

#     while q:
#         cy, cx, depth = q.popleft()
#         print(cy, cx, depth)

#         for i in range(4):
#             ny, nx = cy + dy[i], cx + dx[i]
#             print("ny,nx:", ny, nx)

#             if ny < 0 or ny >= N or nx < 0 or nx >= M:
#                 continue

#             if not visited[ny][nx] and matrix[ny][nx] == matrix[sy][sx]:
#                 q.append((ny, nx, depth + 1))
#                 visited[ny][nx] = True

#             if ny == sy and nx == sx:
#                 print("ny,nx:", ny, ",", nx, ", depth+1:", depth + 1)
#                 # return True

#     return False


def dfs(y, x, depth):
    global cycle
    if visited[y][x]:
        if y == start_y and x == start_x and depth >= 4:
            cycle = True
        return

    visited[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < N and 0 <= nx < M:
            if matrix[ny][nx] == matrix[y][x]:
                dfs(ny, nx, depth + 1)

cycle = False

for y in range(N):
    for x in range(M):
        visited = [[False] * M for _ in range(N)]
        start_y, start_x = y, x
        dfs(start_y, start_x, 0)

        if cycle:
            print("Yes")
            exit()

print("No")
