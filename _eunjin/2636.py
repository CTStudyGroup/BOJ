from collections import deque

R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

# 치즈가 아예 없는 경우 예외 처리
cheese = 0
for row in matrix:
    cheese += sum(row)

if not cheese:
    print(0)
    print(0)
    exit()

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

# bfs (0,0)부터 시작
def bfs(cheese_set):
    visited = [[False] * C for _ in range(R)]

    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if not visited[ny][nx] and matrix[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                if matrix[ny][nx] == 1:
                    cheese_set.add((ny, nx))


# 공기 부분을 bfs해서 다음 노드가 치즈인 경우 set에 담기
T = 0
while True:
    cheese_set = set()

    bfs(cheese_set)
    # print("cheese_set:", cheese_set)

    if not cheese_set:
        print(T)
        print(cheese)
        break

    cheese = 0
    for row in matrix:
        cheese += sum(row)

    for y, x in cheese_set:
        matrix[y][x] = 0

    T += 1
