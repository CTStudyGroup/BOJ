from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

order = list(map(int, input().split()))

# 방문하지 않은 정점 큐에 넣을 때 순서 고려하지 않음
# bfs 방문 경로가 여러개가 나온다.
# 직전에 어떤 노드를 먼저 큐에 넣었냐에 따라 다음 노드가 달라짐

visited = [False] * (N + 1)
position = [0] * (N + 1)

# 순서 배열에서 각 노드의 순서를 기록
for i in range(N):
    position[order[i]] = i

# 각 노드의 인접 리스트를 방문 순서 기준으로 정렬
for i in range(1, N + 1):
    adj_list[i].sort(key=lambda x: position[x])

q = deque()
q.append(1)
visited[1] = True
visit_order = []

while q:
    node = q.popleft()
    visit_order.append(node)

    for adj_node in adj_list[node]:
        if not visited[adj_node]:
            visited[adj_node] = True
            q.append(adj_node)

if visit_order == order:
    print(1)
else:
    print(0)
