from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

# 시간 초과 풀이
adj_list = [[] for _ in range(N)]  # adj_list[0]=1 : 0->1, 0이 상사

for i in range(1, N):
    adj_list[arr[i] - 1].append(i)

# print(adj_list)

def bfs(start, w):
    q = deque()
    q.append(start)
    score[start] += w
    visited = [False] * N
    visited[start] = True

    while q:
        node = q.popleft()
        next_node = adj_list[node]

        for next_node in adj_list[node]:
            if not visited[next_node]:
                score[next_node] += w
                q.append(next_node)
                visited[next_node] = True

score = [0] * N
for _ in range(M):
    i, w = map(int, input().split())
    bfs(i - 1, w)


print(*score)
