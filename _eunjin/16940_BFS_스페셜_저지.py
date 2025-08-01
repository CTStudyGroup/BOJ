from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

orders = list(map(int, input().split()))

# 방문하지 않은 정점 큐에 넣을 때 순서 고려하지 않음
# bfs 방문 경로가 여러개가 나온다.
# 직전에 어떤 노드를 먼저 큐에 넣었냐에 따라 다음 노드가 달라짐
# adj_list에서 다음 노드 뽑을 때 주어진 노드가 있으면 그 노드를 큐의 제일 앞에 넣기?

q = deque()
visited = [False] * (N + 1)

q.append((1, 0))  # node, depth
visited[1] = True

visited_depth = []

while q:
    node, depth = q.popleft()
    # print("curr node:", node, depth)
    visited_depth.append(depth)

    for adj_node in adj_list[node]:
        if not visited[adj_node]:
            if adj_node == orders[depth + 1]:
                q.appendleft((adj_node, depth + 1))
            else:
                q.append((adj_node, depth + 1))

            visited[adj_node] = True


# print(visited_depth)

for i in range(1, len(visited_depth)):
    if visited_depth[i - 1] > visited_depth[i]:
        print(0)
        exit()
print(1)
