# 고슴도치 탈출 문제 (BFS)
# 물과 고슴도치가 동시에 움직이며 BFS로 처리

from collections import deque

# 방향 벡터 (상하좌우)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 입력 처리
R, C = map(int, input().split(" "))
matrix = []  # 지도
start = tuple()  # 고슴도치 시작 위치
target = tuple()  # 비버 굴 위치
queue = deque()  # BFS 큐

# 지도 입력 및 초기 설정
for row in range(R):
    new_row = input()
    seperate = []
    for col in range(C):
        seperate.append(new_row[col])
        if(new_row[col] == 'D'):
            target = (col, row)
        elif(new_row[col] == 'S'):
            start = (col, row)
        elif(new_row[col] == '*'):
            queue.append((col, row, 0, 0))  # 물 위치를 먼저 큐에 삽입 (type 0)
    matrix.append(seperate)

# 고슴도치 방문 여부 체크 배열
visited = [[0 for _ in range(C)] for _ in range(R)]
visited[start[1]][start[0]] = 1

# 고슴도치 시작 위치 큐에 삽입 (type 1)
queue.append((start[0], start[1], 1, 0))

# type 0: 물 이동
# type 1: 고슴도치 이동
# queue 항목: (x좌표, y좌표, type, depth)

def bfs():
    while queue:
        currentX, currentY, type, depth = queue.popleft()

        # 고슴도치가 목적지에 도달한 경우
        if(type == 1 and currentX == target[0] and currentY == target[1]):
            return depth

        for dir in range(4):
            nx = currentX + dx[dir]
            ny = currentY + dy[dir]

            if 0 <= nx < C and 0 <= ny < R:
                if type == 0:
                    # 물은 비버굴(D), 돌(X), 물(*)을 제외하고 퍼짐
                    if matrix[ny][nx] == '.' or matrix[ny][nx] == 'S':
                        matrix[ny][nx] = '*'
                        queue.append((nx, ny, 0, depth + 1))
                elif type == 1:
                    # 고슴도치는 아직 방문하지 않았고, 빈칸(.) 또는 목적지(D)만 이동 가능
                    if visited[ny][nx] == 0 and (matrix[ny][nx] == '.' or matrix[ny][nx] == 'D'):
                        visited[ny][nx] = 1
                        queue.append((nx, ny, 1, depth + 1))

    # 도달 불가능한 경우
    return 0

# BFS 실행
result = bfs()
if result:
    print(result)
else:
    print("KAKTUS")
