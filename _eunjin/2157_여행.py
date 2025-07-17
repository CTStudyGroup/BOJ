import heapq
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# dp? 그래프탐색?
# 도시 번호가 증가하는 순서대로만 이동한다


# 시간 초과 풀이
# 근데 그냥 다익스트라로 촤장경로로 하면 안되는지..
# 안된다... M개를 고르는, depth까지 같이 고려해서 dist를 2차원으로 두었어야 함
# 지금은 depth 고려 안하고 dist[node]에 덮어써버림
# 2차원으로 바꿔도 불가능.. 시간초과

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start, 1))  # dist, node, depth
#     dist[start][1] = 0

#     while q:
#         d, node, depth = heapq.heappop(q)  # d는 힙에 음수로 바꿔서 저장됨
#         curr_d = -d

#         if depth >= M:
#             continue

#         if dist[node][depth] != -1 and curr_d < dist[node][depth]:
#             continue

#         for adj_node, adj_dist in adj_list[node]:
#             td = curr_d + adj_dist
#             if td > dist[adj_node][depth + 1]:
#                 dist[adj_node][depth + 1] = td
#                 heapq.heappush(q, (-td, adj_node, depth + 1))  # dist는 음수로 바꿔서 힙에 저장

# adj_list = [[] for _ in range((N + 1))]
# for _ in range(K):
#     a, b, c = map(int, input().split())
#     if a < b:
#         adj_list[a].append((b, c))

# dist = [[-1] * (M + 1) for _ in range(N + 1)]

# dijkstra(1)
# print(max(dist[N]))


# 그냥 dp로 다시 풀기

adj_list = [[] for _ in range((N + 1))]
for _ in range(K):
    a, b, c = map(int, input().split())
    if a < b:
        adj_list[a].append((b, c))

# dp[i][j]: i번 도시에 도착했고 그동안 j개를 골라서 방문했을 때의 최대 만족도
dp = [[-1] * (M + 1) for _ in range(N + 1)]
dp[1][1] = 0

for i in range(1, N + 1):
    for j in range(1, M):
        if dp[i][j] == -1:  # 해당 도시 방문하지 않은 경우
            continue

        for nxt, cost in adj_list[i]:
            dp[nxt][j + 1] = max(dp[nxt][j + 1], dp[i][j] + cost)

print(max(dp[N][2:]))
