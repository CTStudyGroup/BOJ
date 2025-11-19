import sys
from collections import defaultdict, deque

input = sys.stdin.readline
N = int(input())
dic = defaultdict(set)
for _ in range(N-1) :
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

lst = list(map(int, input().split()))
# 입력 문제
if lst[0] != 1 :
    print(0)
    sys.exit()
    
    
    
visited = [False] * (N+1)
visited[0], visited[1]  = True, True
q = [1]
idx = 1 
while True :
    if idx == N  :
        print(1)
        break
    if not q :
        print(0)
        break
    if lst[idx] in dic[q[-1]] :
        visited[lst[idx]] = True
        q.append(lst[idx])
        idx += 1
        
    else :
        q.pop()
        
