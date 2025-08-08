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

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(currentX, currentY, group_num):
    visited[currentY][currentX] = group_num # visited에 group_num을 사용해서 메모리 효율 up
    count = 1
    print(f"{currentX},{currentY} 방문")

    wall_number = matrix[currentY][currentX]
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
            space = dfs(row, col, index, 0)
            print(space)
            index += 1
