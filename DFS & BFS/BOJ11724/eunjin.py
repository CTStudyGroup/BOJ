import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())

matrix = [[] for _ in range(N+1)]

for _ in range(M):
    y, x = map(int, input().split())
    matrix[y].append(x)
    matrix[x].append(y)

# print(matrix)


visited = [False]*(N+1)


def dfs(x):
    global visited, matrix
    visited[x] = True

    for i in matrix[x]:
        if not visited[i]:
            dfs(i)


cnt = 0
for x in range(1, N+1):
    if not visited[x]:
        dfs(x)
        cnt += 1


print(cnt)
