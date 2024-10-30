from queue import PriorityQueue
# 입력 받기
N, E = map(int, input().split())

INF = int(1e12)


def dijkstra(start_node):
    global N, adj_list

    dist = [INF]*(N+1)

    pq = PriorityQueue()
    dist[start_node] = 0
    pq.put([0, start_node])

    while not pq.empty():
        cur_dist, cur_node = pq.get()
        for adj_dist, adj_node in adj_list[cur_node]:
            temp_dist = cur_dist + adj_dist
            if temp_dist < dist[adj_node]:
                dist[adj_node] = temp_dist
                pq.put([temp_dist, adj_node])

    return dist


adj_list = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append([c, b])  # dist, node
    adj_list[b].append([c, a])  # 양방향이므로


v1, v2 = map(int, input().split())


dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

case1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
case2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]

result = min(case1, case2)

print(result if result < INF else -1)
