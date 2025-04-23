import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for i in range(1, N + 1):
    adj_list[i].sort(reverse=True)

def bfs(start):
    global n
    q = deque()
    q.append(start)
    visited[start] = n

    while q:
        node = q.popleft()

        for adj_node in adj_list[node]:
            if not visited[adj_node]:
                n += 1
                visited[adj_node] = n
                q.append(adj_node)


n = 1
visited = [0] * (N + 1)
bfs(R)

for i in range(1, N + 1):
    print(visited[i])
