import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

small_adj_list = [[] for _ in range(N + 1)]  # list[a] = b 이면 a < b
big_adj_list = [[] for _ in range(N + 1)]  # list[a] = b 이면 a > b

for _ in range(M):
    a, b = map(int, input().split())  # a > b
    small_adj_list[b].append(a)
    big_adj_list[a].append(b)


def bfs(start, adj_list):
    q = deque()
    visited = [False] * (N + 1)

    visited[start] = True
    q.append(start)

    while q:
        node = q.popleft()

        for adj_node in adj_list[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                q.append(adj_node)

    return visited[1:]

# 각 물건을 시작으로 bfs 탐색 2번(작은 방향, 큰 방향)
for i in range(1, N + 1):
    cnt = 0
    small = bfs(i, small_adj_list)
    big = bfs(i, big_adj_list)

    for j in range(N):
        if not small[j] and not big[j]:
            cnt += 1

    print(cnt)
