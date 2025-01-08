import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

graph = [[] for i in range(n+1)]


def dfs(x, y):
    for i in graph[x]:
        a, b = i
        if dist[a] == -1:
            dist[a] = b+y
            dfs(a, b+y)


for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [-1 for _ in range(n+1)]
dist[1] = 0
dfs(1, 0)

start = dist.index(max(dist))

dist = [-1 for _ in range(n+1)]
dist[start] = 0
dfs(start, 0)

print(max(dist))
