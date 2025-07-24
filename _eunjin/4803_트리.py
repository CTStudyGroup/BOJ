import sys
from collections import deque
input = sys.stdin.readline

# bfs탐색하면서 기존에 방문했던 노드 다시 방문하게 되면 그건 트리가 아님
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    node_cnt = 0
    edge_cnt = 0

    while q:
        node = q.popleft()
        node_cnt += 1


        for adj_node in adj_list[node]:
            edge_cnt += 1
            if not visited[adj_node]:
                q.append(adj_node)
                visited[adj_node] = True

    edge_cnt = edge_cnt // 2

    return True if edge_cnt == node_cnt - 1 else False

T = 1
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    adj_list = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    answer = 0

    for node in range(1, N + 1):
        if not visited[node]:
            isTree = bfs(node)

            if isTree:
                answer += 1

    if answer == 0:
        print(f"Case {T}: No trees.")
    elif answer == 1:
        print(f"Case {T}: There is one tree.")
    else:
        print(f"Case {T}: A forest of {answer} trees.")

    T += 1

