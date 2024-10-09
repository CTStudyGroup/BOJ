import sys
sys.setrecursionlimit(100000)

# 입력 받기
N, M = map(int, input().split())

matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    y, x = map(int, input().split())
    matrix[y][x] = 1

print(matrix)

for col in matrix:
    for row in col:
        print(row, end=" ")
    print()

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

visited = [[False]*(N+1)for _ in range(N+1)]


def dfs(y, x):
    if visited[y][x]:
        return

    visited[y][x] = True

    for i in range(4):
        ny = y+dy[i]
        nx = x + dx[i]
        if(1 <= ny <= N and 1 <= nx <= N) and not visited[ny][nx]:
            dfs(ny, nx)


cnt = 0
for y in range(1, N+1):
    for x in range(1, N+1):
        if not visited[y][x] and matrix[y][x] == 1:
            cnt += 1
            dfs(y, x)

print(cnt)
