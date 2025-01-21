import sys
sys.setrecursionlimit(100000)

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def dfs(y, x):
    global node_set

    # base case
    if matrix[y][x] == -1:
        return

    # recursive case
    matrix[y][x] = -1
    node_set.add((y, x))

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]

        if ny >= 0 and ny < M and nx >= 0 and nx < N:
            if matrix[ny][nx] == 0:
                dfs(ny, nx)


M, N, K = map(int, input().split())

matrix = [[0]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            matrix[y][x] = 1
cnt = 0
size_arr = []

for y in range(M):
    for x in range(N):
        if matrix[y][x] == 0:
            node_set = set()
            dfs(y, x)
            cnt += 1
            size_arr.append(len(node_set))

print(cnt)
print(*sorted(size_arr))
