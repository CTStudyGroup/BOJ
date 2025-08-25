import sys
import heapq
input = sys.stdin.readline

V, E, P = map(int, input().split())
adj_list = [[] for _ in range(V + 1)]
INF = int(1e9)

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))


def dijkstra(start):
    dist = [INF] * (V + 1)
    q = []
    dist[start] = 0
    heapq.heappush(q, [0, start])  # dist, start

    while q:
        curr_dist, curr_node = heapq.heappop(q)

        if dist[curr_node] < curr_dist:
            continue

        for adj_node, adj_dist in adj_list[curr_node]:
            temp_dist = curr_dist + adj_dist
            if temp_dist < dist[adj_node]:
                dist[adj_node] = temp_dist
                heapq.heappush(q, [temp_dist, adj_node])

    return dist

dist_arr = dijkstra(1)  # 1에서 시작한 최단 거리

dist_v = dist_arr[V]  # 1 -> V까지의 거리
dist_p = dist_arr[P]  # 1 -> P 까지의 거리

dist_pv = dijkstra(P)[V]  # P -> V까지의 거리

if dist_p + dist_pv == dist_v:  # 1->P + P->V = 1->V
    print("SAVE HIM")
else:
    print("GOOD BYE")
