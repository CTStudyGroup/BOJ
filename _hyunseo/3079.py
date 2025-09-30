import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
q=[]
station = []
for _ in range(N) :
  a = int(input())
  heapq.heappush(q, (a, a))
  station.append(a)
station.sort()

print(station)

end_time = 0

for _ in range(M) :
  cur, cost = heapq.heappop(q)
  print(cur, cost)
  end_time = cur
  heapq.heappush(q, (cur+cost, cost))
  
  
print(end_time)




