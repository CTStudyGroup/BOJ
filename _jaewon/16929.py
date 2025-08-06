# 사이클이 존재하는지 판단하라.
# 사이클을 판단하는 방법은? 

(N,M) = map(int,input().split(' '))
matrix = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    row = input()
    for j in range(M):
        matrix[i][j] = row[j]

visited = [[False for _ in range(M)] for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(currentY, currentX, parentY, parentX, char):
    visited[currentY][currentX] = True

    for dir in range(4):
        ny = currentY + dy[dir]
        nx = currentX + dx[dir]

        if 0 <= ny < N and 0 <= nx < M:
            if matrix[ny][nx] != char:
                continue
            if not visited[ny][nx]:
                if dfs(ny, nx, currentY, currentX, char):
                    return True
            elif ny != parentY or nx != parentX:
                # 부모가 아닌데 방문한 곳이면 사이클
                return True

    return False

flag = False
for y in range(N):
    for x in range(M):
        if not visited[y][x]:
            if dfs(y, x, -1, -1, matrix[y][x]):
                flag = True
                break
    if flag:
        break

print("Yes" if flag else "No")
