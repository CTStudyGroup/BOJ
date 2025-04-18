from collections import deque

def bfs(start, numbers):
    global values
    queue = deque([(start[0], start[1], numbers[start[0]][start[1]])])

    while queue:
        x, y, val = queue.popleft()

        if len(val)==6:
            values.add(val)
            continue
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<5 and 0<=ny<5:
                queue.append((nx, ny, val+numbers[nx][ny]))

def dfs(start, numbers):
    stack = [(start[0], start[1], numbers[start[0]][start[1]])]

    while stack:
        x, y, val = stack.pop()

        if len(val)==6:
            values.add(val)
            continue
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<5 and 0<=ny<5:
                stack.append((nx, ny, val+numbers[nx][ny]))

numbers = [list(input().split()) for _ in range(5)]
values = set()

for i in range(5):
    for j in range(5):
        # bfs((i,j),numbers)
        dfs((i, j), numbers)
print(len(values))