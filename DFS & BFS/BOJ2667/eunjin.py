# 입력 받기
N = int(input())

matrix = [[] for _ in range(N)]

for i in range(N):
    string = input()
    for elem in string:
        matrix[i].append(elem)

# print(matrix)

visited = [[False]*N for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cnt_list = []
cnt = 0


def dfs(y, x):
    global matrix, cnt
    if(visited[y][x]):
        return

    cnt += 1
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if(0 <= ny < N and 0 <= nx < N) and matrix[ny][nx] == '1':
            dfs(ny, nx)


# dfs로 탐색
# matrix 전체를 돌면서, 값이 '1'이면서 visited False인 지점을 시작으로 탐색
for y in range(N):
    for x in range(N):
        if(matrix[y][x] == '1' and not visited[y][x]):
            cnt = 0
            dfs(y, x)
            #print("y:", y, ", x:", x, ", cnt:", cnt)
            cnt_list.append(cnt)

# 총 단지수
print(len(cnt_list))
cnt_list.sort()
for elem in cnt_list:
    print(elem)
