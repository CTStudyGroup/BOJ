from collections import deque

# 입력 받기
M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque()
visited = [[False] * M for _ in range(N)]
visit_cnt = 0
for y in range(N):
    for x in range(M):
        if (matrix[y][x] == 1):
            q.append((0, y, x))
            visited[y][x] = True
            visit_cnt += 1
        elif(matrix[y][x] == -1):
            visited[y][x] = True
            visit_cnt += 1


def all_visited():
    global visited
    for row in visited:
        for elem in row:
            if(elem == False):
                return False

    return True


while q:
    dist, y, x = q.popleft()

    if (visit_cnt == M*N):
        if(len(q) > 0):
            print(q.pop()[0])
        else:
            print(dist)
        # print(visited)
        exit()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if(0 <= ny < N and 0 <= nx < M) and not visited[ny][nx] and matrix[ny][nx] == 0:
            q.append((dist+1, ny, nx))
            visited[ny][nx] = True
            visit_cnt += 1
    # print(q)

if not all_visited():
    print(-1)
