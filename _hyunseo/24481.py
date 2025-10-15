import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R= map(int, input().split())


def dfs(r, path) :
    if visited[r] != -1 :
        return
    visited[r] = path
    for neighbor in grid[r] :
        if visited[neighbor] == -1:
            dfs(neighbor, path + 1)
    return
            
visited = [-1]*(N+1)
grid = defaultdict(list)
for _ in range(M) :
    a, b = map(int, input().split())
    grid[a].append(b)
    grid[b].append(a)

for i in range(N) :
    grid[i].sort()

dfs(R, 0)

for idx in range(1, N+1) :
    print(visited[idx])
