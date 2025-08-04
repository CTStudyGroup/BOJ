from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
adj_list = [[] for _ in range(N)]
for _ in range(M):
    v, w = map(int, input().split())
    adj_list[v - 1].append(w - 1)
    adj_list[w - 1].append(v - 1)


# 모든 친구와 연결되는 최소 비용 찾기
# 각 연결요소를 구하고, 각 연결 요소마다 최소 A 값 구하기

def bfs(start):
    q = deque()
    q.append(start)
    mn = 10001
    visited[start] = True

    while q:
        node = q.popleft()
        mn = min(mn, A[node])  # 최소 친구비 갱신

        for adj_node in adj_list[node]:
            if not visited[adj_node]:
                q.append(adj_node)
                visited[adj_node] = True

    return mn

visited = [False] * N
answer = 0

for i in range(N):
    if not visited[i]:
        answer += bfs(i)

if answer > K:
    print("Oh no")
else:
    print(answer)
