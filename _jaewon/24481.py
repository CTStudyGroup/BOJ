import sys
sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
depths = [-1] * (N+1)

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

# 인접 리스트 정렬 (작은 번호부터 탐색)
for i in range(1, N+1):
    adj[i].sort()

def dfs(node, depth):
    visited[node] = True
    depths[node] = depth
    
    for nxt in adj[node]:
        if not visited[nxt]:
            dfs(nxt, depth + 1)

dfs(R, 0)

for i in range(1, N+1):
    print(depths[i])
