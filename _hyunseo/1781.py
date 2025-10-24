import heapq
import sys

input = sys.stdin.readline
N = int(input())

q = []
for _ in range(N)  :
    d, r = map(int, input().split())
    q.append((d, r))
q.sort()
heap = []

for d, r in q :
    heapq.heappush(heap,r)
    if len(heap) > d: 
        heapq.heappop(heap)
print(sum(heap))
