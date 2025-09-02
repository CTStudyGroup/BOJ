import sys

input = sys.stdin.readline
import heapq

# 카드 개수 n
n, m = map(int,input().split())

# 맨 처음 카드 상태
cards = list(map(int,input().split()))
heapq.heapify(cards)
# 카드 놀이
for i in range(m) :
    t1 = heapq.heappop(cards)
    t2 = heapq.heappop(cards)
    heapq.heappush(cards, t1+t2)
    heapq.heappush(cards, t1+t2)
print(sum(cards))
