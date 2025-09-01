import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
pq = list(map(int, input().split()))

# 우선순위큐에 카드 모두 넣고 가장 작은 카드 2개씩 뽑기
heapq.heapify(pq)

for _ in range(M):
    n1 = heapq.heappop(pq)
    n2 = heapq.heappop(pq)
    heapq.heappush(pq, n1 + n2)
    heapq.heappush(pq, n1 + n2)

print(sum(pq))
