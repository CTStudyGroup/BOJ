import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

dic = defaultdict(list)

n, m = map(int, input().split())
for _ in range(m):
    a, b, c = map(int, input().split())
    dic[a].append((b, c))
    dic[b].append((a, c))

s, t = map(int, input().split())

def solve(dic, s, t):
    INF = sys.maxsize
    dist = [INF] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]  # (누적비용, 노드)

    while pq:
        cost, u = heapq.heappop(pq)
        if cost > dist[u]:
            continue
        if u == t:
            return cost
        for v, w in dic[u]:
            nc = cost + w
            if nc < dist[v]:
                dist[v] = nc
                heapq.heappush(pq, (nc, v))
    return -1  # (이 문제에선 거의 안 나옴)

print(solve(dic, s, t))
