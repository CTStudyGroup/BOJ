import heapq

def solve(Beers, N, M, K):
    Jeon = []
    curr_M = 0
    for _ in range(K):
        c, m = heapq.heappop(Beers)
        curr_M += m
        heapq.heappush(Jeon, m)

        if len(Jeon) == N:
            if curr_M >= M: return c
            else:
                curr_M -= heapq.heappop(Jeon)
    return -1

N, M, K = map(int, input().split())
Beers = []
for _ in range(K):
    v, c = map(int, input().split())
    heapq.heappush(Beers, (c, v))
print(solve(Beers, N, M, K))