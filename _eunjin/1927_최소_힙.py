import heapq
import sys
input = sys.stdin.readline

N = int(input())

q = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, x)

