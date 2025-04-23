from collections import deque

def bfs(Graph, start):
    queue = deque([start])
    visited = [0]*(len(Graph)+1)
    visited[start] = 1
    count = 2

    while queue:
        u = queue.popleft()

        for v in sorted(Graph[u], reverse=True):
            if visited[v]==0:
                visited[v] = count
                queue.append(v)
                count += 1
    return visited[1:]

N, M, R = list(map(int, input().split()))
Graph = {i:[] for i in range(1, N+1)}
for _ in range(M):
    u, v = list(map(int, input().split()))
    Graph[u].append(v)
    Graph[v].append(u)
print(*bfs(Graph, R),sep='\n')