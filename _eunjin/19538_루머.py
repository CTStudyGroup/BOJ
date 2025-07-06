import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

adj_list = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    nodes = list(map(int, input().split()))

    for n in nodes:
        if n != 0:
            adj_list[i].append(n)

M = int(input())
start = list(map(int, input().split()))

adj_believed = [0] * (N + 1)  # 루머 믿는 주변인의 수
believed = [-1] * (N + 1)  # i번째 노드가 루머 처음 믿기 시작한 시간

q = deque()
for st in start:
    q.append((st, 0))  # node, d
    believed[st] = 0

while q:
    node, d = q.popleft()

    for adj_node in adj_list[node]:
        if believed[adj_node] >= 0:
            continue

        adj_believed[adj_node] += 1

        if adj_believed[adj_node] * 2 >= len(adj_list[adj_node]):  # 인접 노드의 절반 이상이 루머 믿으면 자신도 믿음
            believed[adj_node] = d + 1
            q.append((adj_node, d + 1))

print(*believed[1:])
