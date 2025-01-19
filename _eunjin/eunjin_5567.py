import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
M = int(input())

adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

q = deque()
q.append([1, 0])  # node, depth
visited[1] = True


while q:
    node, depth = q.popleft()

    for adj_node in adj_list[node]:
        if visited[adj_node]:
            continue
        if depth < 2:
            q.append([adj_node, depth+1])
            visited[adj_node] = True

print(sum(visited)-1)
