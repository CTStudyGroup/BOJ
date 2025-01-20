# 백준 5567 결혼식
# keypoint : bfs

from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

graph=[[] for i in range(n+1)]
visited=[False]*(n+1)

def bfs(start):
    queue=deque()
    queue.append(start)
    visited[start]=True
    depth=0
    cnt=0

    while queue:
        depth+=1
        for i in range(len(queue)):
            friend=queue.popleft()
            for j in graph[friend]:
                if not visited[j]:
                    visited[j]=True
                    queue.append(j)
                    cnt+=1

        if depth==2:
            break
    return cnt

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))