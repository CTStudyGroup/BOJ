import sys
import heapq
input = sys.stdin.readline

T = int(input())
INF = sys.maxsize

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

for _ in range(T):
    N, D, start = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]

    for _ in range(D):
        a, b, s = map(int, input().split())
        adj_list[b].append([a, s])  # node, dist

    dist = [INF] * (N + 1)
    dijkstra(start)

    cnt = 0
    mx = 0
    for i in range(1, N + 1):
        if dist[i] != INF:
            mx = max(mx, dist[i])
            cnt += 1
    print(cnt, mx)
