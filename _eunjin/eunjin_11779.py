import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    dist[start] = 0

    while q:
        curr_dist, curr_node = heapq.heappop(q)
        # print("curr_node:", curr_node, ", curr_dist:", curr_dist)

        if dist[curr_node] < curr_dist:
            continue

        route[curr_node].append(curr_node)
        for adj_dist, adj_node in adj_list[curr_node]:
            temp_dist = curr_dist+adj_dist
            if temp_dist < dist[adj_node]:
                dist[adj_node] = temp_dist
                # print("dist[", adj_node, "]:", temp_dist)
                heapq.heappush(q, (temp_dist, adj_node))
                route[adj_node] = route[curr_node][:]


N = int(input())
M = int(input())
adj_list = [[] for _ in range(N+1)]
INF = int(1e12)
dist = [INF]*(N+1)
route = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, d = map(int, input().split())
    adj_list[s].append((d, e))  # dist,next node

start, end = map(int, input().split())

dijkstra(start)

print(dist[end])
print(len(route[end]))
print(*route[end])
