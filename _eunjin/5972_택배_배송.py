import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

INF = sys.maxsize

dist = [INF] * (N + 1)

def dijkstra(start):
    hq = []
    heapq.heappush(hq, [0, start])
    dist[start] = 0

    while hq:
        curr_dist, curr_node = heapq.heappop(hq)

        if dist[curr_node] < curr_dist:
            continue

        for adj_node, adj_dist in adj_list[curr_node]:
            temp = adj_dist + curr_dist
            if temp < dist[adj_node]:
                dist[adj_node] = temp
                heapq.heappush(hq, [temp, adj_node])

dijkstra(1)
print(dist[N])
