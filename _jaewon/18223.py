# 최단 경로 탐색
# 최단 경로 중, 민준이(P)가 포함된 경로가 있으면 반드시 그 경로 선택
import sys
import collections
import heapq
input = sys.stdin.readline

V, E, P = map(int, input().split())

linked_list = collections.defaultdict(list)
for _ in range(E):
    from_node, to_node, distance = map(int, input().split())
    linked_list[from_node].append((to_node, distance))
    linked_list[to_node].append((from_node, distance))

INF = 10**18

def dijkstra(start):
    # 변수명 최대한 유지: distances 사용
    distances = [INF] * (V + 1)
    distances[start] = 0

    pq = [(0, start)]  # (현재까지의 거리, 노드)
    while pq:
        dist_u, u = heapq.heappop(pq)
        if dist_u > distances[u]:
            continue
        for v, w in linked_list[u]:
            nd = dist_u + w
            if nd < distances[v]:
                distances[v] = nd
                heapq.heappush(pq, (nd, v))
    return distances

dist_from_1 = dijkstra(1)
dist_from_P = dijkstra(P)

# P를 경유한 최단거리와 전체 최단거리 비교
if dist_from_1[V] == dist_from_1[P] + dist_from_P[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")