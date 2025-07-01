import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

# 의견 전달 경로가 여러개이면 최단 경로로 전달, 이 떄의 거리 = 의사전달시간
# 연결된 노드끼리는 같은 위원회

# bfs로 먼저 연결요소 개수, 연결요소별 노드 번호 구하고
# 각 노드에 대해서 bfs로 연결요소 안의 다른 노드간의 거리 구함

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

def bfs1(start):
    q = deque()
    q.append(start)
    visited[start] = True
    ret = [start]

    while q:
        node = q.popleft()

        for adj_node in adj_list[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                q.append(adj_node)
                ret.append(adj_node)

    return ret

def bfs2(start):
    q = deque()
    q.append((start, 0))
    visited = [False] * (N + 1)
    visited[start] = True
    mx_dist = 0

    while q:
        node, dist = q.popleft()
        mx_dist = max(mx_dist, dist)

        for adj_node in adj_list[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                q.append((adj_node, dist + 1))

    return mx_dist


# 연결 요소 개수, 연결요소별 노드 번호 구함
connected_cnt = 0  # 연결요소의 개수
connected = []  # 각 연결요소별 노드 번호
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if not visited[i]:
        connected.append(bfs1(i))
        connected_cnt += 1
print(connected_cnt)


# 각 연결요소마다 대표자 뽑기
answer_arr = []
for nodes in connected:
    min_dist = sys.maxsize
    answer = 0
    for node in nodes:
        dist = bfs2(node)
        # print("node:", node, ", dist:", dist)

        if dist < min_dist:
            answer = node
            min_dist = dist
    answer_arr.append(answer)

for ans in sorted(answer_arr):
    print(ans)
