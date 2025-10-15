import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
matrix = []
visited = [[0 for _ in range(C)] for _ in range(R)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(R):
    matrix.append(input())

def dfs(currentX, currentY, depth):
    visited[currentY][currentX] = 1

    if(depth == K and currentX == C-1 and currentY == 0):
        return 1

    count = 0
    for dir in range(4):
        nx = currentX + dx[dir]
        ny = currentY + dy[dir]

        if((0<=nx<C) and (0<=ny<R) and visited[ny][nx] == 0):
            if(matrix[ny][nx] == '.'):
                count += dfs(nx, ny, depth + 1)
                # 핵심 코드: 상, 하, 좌, 우 중에서 한 곳을 갔다온 다음, 다시 이 분기점으로 돌아올 수 있게 visited = 0으로 만들어줘야 함.
                visited[ny][nx] = 0 

    return count

total = 0
total = dfs(0, R-1, 1)

print(total)