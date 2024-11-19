import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

# 입력 받기
N = int(input())
M = int(input())

adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))

start, end = map(int, input().split())

# 다익스트라 알고리즘 실행
dist = [INF] * (N+1)


def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, [0, start])
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        if dist[cur_node] < cur_dist:
            continue
        for adj_node, adj_dist in adj_list[cur_node]:
            temp_dist = cur_dist + adj_dist
            if temp_dist < dist[adj_node]:
                dist[adj_node] = temp_dist
                heapq.heappush(q, [temp_dist, adj_node])


dijkstra(start)
print(dist[end])
