import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

# 예외 케이스
if N == 2:
    print(1, 2)
    exit()

# 두 집단으로 나뉘어짐, 유니온 파인드로도 가능할듯???
# 그냥 bfs로 하자
adj_list = [[] for _ in range(N + 1)]

for _ in range(N - 2):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# 1을 기준으로 bfs 탐색
visited = [False] * (N + 1)
q = deque()
q.append(1)
visited[1] = True

while q:
    node = q.popleft()

    for adj_node in adj_list[node]:
        if not visited[adj_node]:
            q.append(adj_node)
            visited[adj_node] = True

if sum(visited) == 1:  # 1을 기준으로 bfs 돌렸을 때 방문한 노드 총 개수가 1개면 1이 끊어진 노드임
    print(1, 2)
else:
    a, b = 0, 0  # 연결할 두 노드
    for i in range(N, 0, -1):
        if not visited[i]:
            a = i
        else:
            b = i
    print(a, b)
