from collections import deque
import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    n,m=map(int,input().split())
    importance=list(map(int,input().split()))
    q=deque()

    for j in range(n):
        q.append([importance[j],j])

    cnt=0
    while q:
        imax=max(importance)
        if q[0][0]==imax:
            cnt+=1
            if q[0][1]==m:
                break
            q.popleft()
            importance.remove(imax)
        else:
            q.rotate(-1)

    print(cnt)