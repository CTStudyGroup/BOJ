from queue import PriorityQueue

# 입력 받기
N, M, X = map(int, input().split())

adj_list = [[] for _ in range(M+1)]
adj_list_reverse = [[] for _ in range(M+1)]
for _ in range(M):
    start, end, t = map(int, input().split())
    adj_list[start].append([end, t])  # node, dist
    adj_list_reverse[end].append([start, t])  # node, dist


INF = int(1e12)


def dijkstra(adj_list, start_node):
    global N

    dist = [INF] * (N+1)

    pq = PriorityQueue()
    pq.put([0, start_node])
    dist[start_node] = 0

    while not pq.empty():
        cur_dist, cur_node = pq.get()
        for adj_node, adj_dist in adj_list[cur_node]:
            temp_dist = cur_dist + adj_dist
            if(temp_dist < dist[adj_node]):
                dist[adj_node] = temp_dist
                pq.put([temp_dist, adj_node])

    return dist


dist = dijkstra(adj_list, X)
dist_reverse = dijkstra(adj_list_reverse, X)

result = -1
for i in range(1, N+1):
    result = max(result, dist[i]+dist_reverse[i])

print(result)
