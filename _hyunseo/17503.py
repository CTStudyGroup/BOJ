import heapq
import sys

input = sys.stdin.readline
#축제 열리는 기간 N, 선호도의 합 M, 마실 수 있는 맥주 종류 K
N, M, K = map(int, input().split())
arr = []
for _ in range(K) :
    v, c = map(int, input().split())
    arr.append([v,c])
arr.sort(key =lambda x : (x[1], x[0]))

liked = 0
q = []

for i in arr :
    liked += i[0]
    heapq.heappush(q, i[0])
    
    if len(q) == N :
        if liked >= M :
            print(i[1])
            exit()
        else :
            liked -= heapq.heappop(q)
else :
    print(-1)
    exit()

