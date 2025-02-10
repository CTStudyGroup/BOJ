from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)

visited = [False]*(N+1)

q = deque()
q.append((X, 0))
visited[X] = True

ans_list = []

while q:
    x, d = q.popleft()

    if d == K:
        ans_list.append(x)
        continue

    for adj_node in adj_list[x]:
        if not visited[adj_node]:
            q.append((adj_node, d+1))
            visited[adj_node] = True

# print(ans_list)

if not ans_list:
    print(-1)
else:
    ans_list.sort()
    for elem in ans_list:
        print(elem)
