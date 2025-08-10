import sys
from collections import deque

input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

R, C = map(int, input().split())
forest = [list(input().strip()) for _ in range(R)]

water_time = [[-1] * C for _ in range(R)]
hedgehog_time = [[-1] * C for _ in range(R)]

water_queue = deque()
hedgehog_queue = deque()
start = end = None

for i in range(R):
    for j in range(C):
        cell = forest[i][j]
        if cell == 'S':
            start = (i, j)
            hedgehog_time[i][j] = 0
            forest[i][j] = '.'  
        elif cell == 'D':
            end = (i, j)
        elif cell == '*':
            water_queue.append((i, j))
            water_time[i][j] = 0

while water_queue:
    x, y = water_queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if forest[nx][ny] == '.' and water_time[nx][ny] == -1:
                water_time[nx][ny] = water_time[x][y] + 1
                water_queue.append((nx, ny))

hedgehog_queue.append(start)
while hedgehog_queue:
    x, y = hedgehog_queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if forest[nx][ny] in ('.', 'D') and hedgehog_time[nx][ny] == -1:
                next_time = hedgehog_time[x][y] + 1
                # Only move if water arrives later or never
                if water_time[nx][ny] == -1 or next_time < water_time[nx][ny]:
                    hedgehog_time[nx][ny] = next_time
                    hedgehog_queue.append((nx, ny))

ex, ey = end
if hedgehog_time[ex][ey] == -1:
    print("KAKTUS")
else:
    print(hedgehog_time[ex][ey])
