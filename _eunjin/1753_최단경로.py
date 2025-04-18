import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

adj_list = [[] for _ in range(V + 1)]

INF = sys.maxsize

for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append([v, w])  # node, dist

dist = [INF] * (V + 1)

def dijkstra(start):
    hq = []
    heapq.heappush(hq, [0, start])
    dist[start] = 0

    while hq:
        curr_dist, curr_node = heapq.heappop(hq)

        if dist[curr_node] < curr_dist:
            continue

        for adj_node, adj_dist in adj_list[curr_node]:
            temp = curr_dist + adj_dist
            if temp < dist[adj_node]:
                dist[adj_node] = temp
                heapq.heappush(hq, [temp, adj_node])

dijkstra(K)

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
