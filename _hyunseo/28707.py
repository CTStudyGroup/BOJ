import sys

input = sys.stdin.readline
# A의 길이 
N = int(input())
A = list(map(int, input().split()))

#조작 개수
M = int(input())
L, R, C = [], [], []
# L은 왼쪽 교체, R은 오른쪽 교체, C는 드는 비용
for _ in range(M) :
    a, b, c = map(int, input().split())
    L.append(a-1)
    R.append(b-1)
    C.append(c)

#비용 최솟값을 구하는 식, N < 10이니 bruteforce



import heapq
from collections import defaultdict

q = []
q.append([0, A])
answer = sys.maxsize
visited = set()
flag = True

visited = {}
visited[tuple(A)] = 0
while q :
    cost, cur= heapq.heappop(q)
    if sorted(cur) == cur :
        print(cost)
        sys.exit()
        
    cur_tuple = tuple(cur)
    if cur_tuple in visited and visited[cur_tuple] < cost:
        continue
    
    for i in range(M) :
            cur[L[i]], cur[R[i]]= cur[R[i]],cur[L[i]]
            nxt_cost = cost + C[i]
            
            nxt_cur = tuple(cur)
            if nxt_cur not in visited or nxt_cost < visited[nxt_cur] :
                visited[nxt_cur] = nxt_cost
                heapq.heappush(q, [nxt_cost, cur[:]])

            cur[L[i]], cur[R[i]]= cur[R[i]],cur[L[i]]

print(-1)
