from collections import deque
import sys
input=sys.stdin.readline

def bfs(x,y):
    queue=deque([(x,y)])
    visited[x][y]=1
    while queue:
        x,y=queue.popleft()
        dx=[0,1,0,-1]   # 동,남,서,북
        dy=[1,0,-1,0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[x][y]==graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=1
                queue.append([nx,ny])

n=int(input())

graph=[list(input().rstrip()) for i in range(n)]

visited=[[False]*n for i in range(n)]
answer=[0,0]

# 정상인
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            answer[0]+=1

# 적록색맹 (초록색->빨간색 임의 변경)
for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
            graph[i][j]='R'

visited=[[False]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            answer[1]+=1

print(*answer)