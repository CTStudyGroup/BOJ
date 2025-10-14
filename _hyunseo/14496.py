import sys
from collections import defaultdict, deque

input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())

dic = defaultdict(list)

for _ in range(M) :
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
    if a == A and b == B :
        print(1)
        sys.exit()
    if b == A and a == B:
        print(1)
        sys.exit()

answer = sys.maxsize
q = deque()
q.append([A,  0])
visited = [False]*(N+1)
while q :
    num, cnt = q.popleft()
    if num == B :
        print(cnt)
        sys.exit()
        
    for neighbor in dic[num] :
        if visited[neighbor] == False :
            visited[neighbor] = True
            q.append([neighbor, cnt + 1])
            
print(-1)
