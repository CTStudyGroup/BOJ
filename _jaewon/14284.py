# from_node부터 to_node의 최단거리를 구하라.
from collections import defaultdict
import sys
import heapq
n, m = map(int, sys.stdin.readline().strip().split())

graph = defaultdict(list)
for _ in range(m):
    from_node, to_node, cost = map(int,sys.stdin.readline().strip().split())

    graph[from_node].append((cost, to_node))
    graph[to_node].append((cost, from_node))

from_vertex, to_vertex = map(int, sys.stdin.readline().strip().split())

distances = [10**9] * (n+1)
distances[from_vertex] = 0

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, from_vertex)) # (distance, vertex)

    while queue:
        distance, now = heapq.heappop(queue)

        if(distances[now] < distance):
            continue

        for cost, next in graph[now]:
            new_dist = distance + cost

            if(new_dist < distances[next]):
                distances[next] = new_dist
                heapq.heappush(queue, (new_dist, next))

dijkstra()
print(distances[to_vertex])