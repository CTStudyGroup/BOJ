import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

start, end = map(int, input().split())
INF = int(1e9)

# 그냥 다익스트라로 두 노드 최단거리 찾는 문제

dist = [INF] * (N + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # dist, start
    dist[start] = 0

    while q:
        curr_dist, curr_node = heapq.heappop(q)

        if dist[curr_node] < curr_dist:
            continue

        for adj_node, adj_dist in adj_list[curr_node]:
            temp_dist = curr_dist + adj_dist
            if temp_dist < dist[adj_node]:
                dist[adj_node] = temp_dist
                heapq.heappush(q, (temp_dist, adj_node))

    return dist[end]

print(dijkstra(start))
