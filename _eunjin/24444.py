from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for nodes in adj_list:
    nodes.sort()

t = 1

def bfs(start):
    global t
    visited = [0] * (N + 1)

    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        node = q.popleft()

        for adj_node in adj_list[node]:
            if not visited[adj_node]:
                t += 1
                visited[adj_node] = t
                q.append(adj_node)

    return visited

answer = bfs(R)

for i in range(1, N + 1):
    print(answer[i])
