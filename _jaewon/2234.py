import sys
input = sys.stdin.readline

M, N = map(int, input().split(" "))
visited = [[0 for _ in range(M)] for _ in range(N)]
matrix = []

for row in range(N):
    matrix.append(list(map(int, input().split())))

wall = {} # 벽의 위치를 4자리수로 표현 [하, 우, 상, 좌]
for i in range(16):
    binary = bin(i)
    wall[i] = '0' * (4-len(binary[2:])) + binary[2:]


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def dfs(currentX, currentY, group_num):
    visited[currentY][currentX] = group_num # visited에 group_num을 사용해서 메모리 효율 up
    wall_number = matrix[currentY][currentX]
    count = 1

    for dir in range(4):
        Wall4Bit = wall[wall_number]
        # 벽이 있으면 continue
        if(Wall4Bit[dir] == '1'):
            continue

        nx = currentX + dx[dir]
        ny = currentY + dy[dir]

        if((0<=nx<M) and (0<=ny<N) and visited[ny][nx] == 0):
            count += dfs(nx, ny, group_num)
    
    return count


index = 1
spaces = []
for row in range(N):
    for col in range(M):
        if(visited[row][col] == 0):
            spaces.append(dfs(col, row, index))
            index += 1

rooms = index-1
print(rooms) # 방의 개수
print(max(spaces)) # 가장 넓은 방의 넓이


# visited 배열에는, 해당 원소의 방 번호가 들어가 있음.
adj = [[0 for _ in range(rooms)] for _ in range(rooms)]

maximum = 0
for row in range(N):
    for col in range(M):
        for dir in range(4):
            nx = col + dx[dir]
            ny = row + dy[dir]

            if(not((0<=nx<M) and (0<=ny<N))):
                continue
            
            current_room = visited[row][col]
            adj_room = visited[ny][nx]

            # 이미 탐색한 방
            if(adj[current_room-1][adj_room-1] != 0):
                continue

            if(current_room == adj_room):
                adj[current_room-1][adj_room-1] = spaces[current_room-1]
                maximum = max(maximum,spaces[current_room-1])
            else:
                adj[current_room-1][adj_room-1] = spaces[current_room-1] + spaces[adj_room-1]
                adj[adj_room-1][current_room-1] = spaces[current_room-1] + spaces[adj_room-1]
                maximum = max(maximum,spaces[current_room-1] + spaces[adj_room-1])

print(maximum)
