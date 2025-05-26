def dfs(start, G):
    visited = [0]*(N+1)
    stack = [start]
    cnt = 1

    while stack:
        u = stack.pop()
        if visited[u]!=0: continue
        visited[u] = cnt
        cnt+=1

        for v in G[u]:
            if visited[v]==0:
                stack.append(v)
    return visited[1:]

N, M, R = map(int, input().split())
G = {i:[] for i in range(N+1)}
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1,N+1):
    G[i].sort(reverse=True)

print(*dfs(R ,G),sep='\n')