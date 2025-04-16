import heapq
import sys
input = sys.stdin.readline

N = int(input())

q = []
for _ in range(N):
    n = int(input())
    if n > 0:
        heapq.heappush(q, -n)
    else:
        if q:
            print(-1 * heapq.heappop(q))
        else:
            print(0)
