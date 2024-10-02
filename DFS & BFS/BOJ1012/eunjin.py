import sys
sys.setrecursionlimit(100000)

# 입력 받기
T = int(input())


def dfs(y, x):
    global visited, matrix
    if(visited[y][x]):
        return

    visited[y][x] = True

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if(0 <= ny < N and 0 <= nx < M) and matrix[ny][nx] == 1:
            dfs(ny, nx)


t = 0
while(t < T):
    t += 1

    M, N, K = map(int, input().split())

    matrix = [[0]*M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1

    visited = [[False]*M for _ in range(N)]
    cnt = 0

    for y in range(N):
        for x in range(M):
            if(matrix[y][x] == 1 and not visited[y][x]):
                cnt += 1
                dfs(y, x)
    print(cnt)
