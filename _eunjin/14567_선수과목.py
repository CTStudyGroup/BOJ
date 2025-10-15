from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)


def bfs(start):
    q = deque()
    q.append((start, 1))  # node, depth

    while q:
        node, depth = q.popleft()

        answer[node] = max(answer[node], depth)

        for adj_node in adj_list[node]:
            q.append((adj_node, depth + 1))

answer = [0] * (N + 1)

for i in range(1, N + 1):
    bfs(i)

print(' '.join(map(str, answer[1:])))
