from collections import deque


n, m = map(int, input().split()) 
castle = [list(map(int, input().split())) for _ in range(m)]

dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
wall_bits = [1, 2, 4, 8]  

visited = [[0] * n for _ in range(m)]
room_sizes = [0]  
room_count = 0
max_room_size = 0

def bfs(sx, sy, room_id):
    q = deque([(sx, sy)])
    visited[sx][sy] = room_id
    size = 1

    while q:
        x, y = q.popleft()
        walls = castle[x][y]
        for d in range(4):
            nx, ny = x + dirs[d][0], y + dirs[d][1]
            if not (walls & wall_bits[d]):  # 해당 방향에 벽이 없으면
                if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
                    visited[nx][ny] = room_id
                    q.append((nx, ny))
                    size += 1
    return size

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            room_count += 1
            size = bfs(i, j, room_count)
            room_sizes.append(size)
            max_room_size = max(max_room_size, size)

max_after_remove = 0
for i in range(m):
    for j in range(n):
        for dx, dy in [(0, 1), (1, 0)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n:
                a, b = visited[i][j], visited[ni][nj]
                if a != b:
                    max_after_remove = max(max_after_remove, room_sizes[a] + room_sizes[b])

print(room_count)
print(max_room_size)
print(max_after_remove)
