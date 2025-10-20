import heapq
import sys
from collections import deque

input = sys.stdin.readline

def paint(x1, y1, x2, y2, num) :
    if x1 <= x2 and y1 <= y2 :
        for x in range(x1, x2 + 1) :
            for y in range(y1, y2 + 1) :
                grid[y][x] = num
    elif x1 > x2 and y1 <= y2 :
        for x in range(x1, x2- 1, -1) :
            for y in range(y1, y2 + 1) :
                grid[y][x] = num
    elif x1 > x2 and y1 > y2 :
        for x in range(x1, x2- 1, -1) :
            for y in range(y1, y2 -1 , -1) :
                grid[y][x] = num
    elif x1 <= x2 and y1 > y2 :
        for x in range(x1, x2 + 1) :
            for y in range(y1, y2 -1, -1) :
                grid[y][x] = num

grid = [[0]*501 for _ in range(501)]
visited = [[float('inf')]*501 for _ in range(501)]
N = int(input())
for _ in range(N) :
    x1, y1, x2, y2 = map(int, input().split())
    paint(x1, y1, x2, y2, 1)

M = int(input())
for _ in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    paint(x1, y1, x2, y2, 2)

dq = deque()
dq.append((0, 0))
visited[0][0] = 0

dirs = [(0,1), (0,-1), (1,0), (-1,0)]

while dq:
    y, x = dq.popleft()
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny <= 500 and 0 <= nx <= 500:
            if grid[ny][nx] == 2: 
                continue
            cost = visited[y][x] + grid[ny][nx]
            if cost < visited[ny][nx]:
                visited[ny][nx] = cost
              # 위험 구역이면 최대한 나중에 탐색하기 위해서 뒤에 추가
                if grid[ny][nx] == 1:
                    dq.append((ny, nx)) 
                # 안전 구역이면 먼저 탐색하기 위해서 앞에 추가
                else:
                    dq.appendleft((ny, nx)) 


print(visited[500][500] if visited[500][500] != float('inf') else -1)
