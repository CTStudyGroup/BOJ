import sys
from collections import deque

input = sys.stdin.readline

d = [[-2,-1], [-2,1], [-1,-2], [-1,2], [1,-2], [1,2], [2,-1], [2,1]]

N, M = map(int, input().split())
grid = [[0]*N for _ in range(N)]
X, Y = map(int, input().split())
X, Y = X-1, Y-1
answer = []
horses = []
for _ in range(M) :
    A, B = map(int, input().split())
    A, B = A-1, B-1
    horses.append([A,B])

q= deque([[X, Y, 0]])
visited = [[sys.maxsize]*N for _ in range(N)]
while q :
    x, y, cnt = q.popleft()
    
    for dx, dy in d :
        nx, ny = dx + x, dy + y
        if 0<= nx < N and 0 <= ny < N  :
            if visited[ny][nx] > cnt + 1 :
                visited[ny][nx] = min(visited[ny][nx],  cnt + 1 )
                q.append([nx, ny, cnt + 1])

for A, B in horses:
    answer.append(visited[B][A])
print(*answer)
