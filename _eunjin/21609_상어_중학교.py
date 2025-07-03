from collections import deque

# 인접칸: 상하좌우

# 블록 그룹(연결요소)
# 연결 요소에는 일반 블록 최소 1개 필요
# 연결 요소 내 모든 일반 블록의 색 같아야 함
# 검은 블록은 포함되면 안됨
# 무지개 블록은 제한 없이 포함 가능
# 연결된 노드 개수는 2 이상이어야 함
# 기준 블록: 무지개 블록 아닌 것들 중에서 행번호,열번호가 가장 작은 블록

# 아래 1~5번을 블록 그룹이 존재하는 동안 반복
# 1.크기가 가장 큰 블록 그룹찾기
# 크기 같은 블록 여러개이면 무지개가 더 많은 그룹, 기준 블록의 행이 큰 것, 기준 블록의 열이 큰 것 찾음
# 2. 1에서 찾은 블록 그룹의 모든 블록 제거, (블록 수)**2점 획득
# 3. 중력 작용
# 4. 보드가 90도 반시계 회전
# 5. 중력 작용

# 중력 작용
# 검은색을 제외한 모든 블록을 아래 칸으로 계속 이동(다른 블록을 만날때까지)


# 진짜 지랄났다.........


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def print_matrix(mat):
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()
    print("--------------")

# 해당 시작 좌표의 연결 요소 모든 노드 배열 리턴
def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    visited = [[False] * N for _ in range(N)]
    visited[start_y][start_x] = True

    color = matrix[start_y][start_x]  # 일반 블록 색깔
    connected_nodes = []  # 해당 연결 요소에 속한 모든 노드

    while q:
        cy, cx = q.popleft()

        if (matrix[cy][cx] > 0) and (matrix[cy][cx] != color):  # 기준 색과 다르면
            continue

        connected_nodes.append((cy, cx))

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if visited[ny][nx]:
                continue

            if matrix[ny][nx] >= 0:
                q.append((ny, nx))
                visited[ny][nx] = True

    return connected_nodes

# 해당 연결요소의 모든 노드 중 기준 노드의 좌표 리턴
def get_one_node(connected_nodes):
    connected_nodes.sort(key=lambda x: [x[0], x[1]])
    for node in connected_nodes:
        if matrix[node[0]][node[1]] > 0:
            return node

def get_rainbow_cnt(connected_nodes):
    ret = 0
    for (y, x) in connected_nodes:
        if matrix[y][x] == 0:
            ret += 1
    return ret


# 모든 좌표에 대해 bfs 호출해서 모든 블록 그룹 구하고, 그중 기준에 맞는 그룹 하나 리턴
# 검은색, 무지개색 노드에 대해서는 bfs 호출X: 일반 노드 최소 1개 있어야 하므로
def find_block_group():
    visited = [[False] * N for _ in range(N)]
    max_groups = []  # 크기 가장 큰 블록 그룹 리스트
    max_len = 0

    for y in range(N):
        for x in range(N):
            if not visited[y][x] and matrix[y][x] > 0:
                connected_nodes = bfs(y, x)
                if connected_nodes:
                    if len(connected_nodes) < 2:  # 블록 개수 최소 2개여야 함
                        continue
                    if len(connected_nodes) > max_len:
                        max_groups = [connected_nodes]
                        max_len = len(connected_nodes)
                    elif len(connected_nodes) == max_len:
                        max_groups.append(connected_nodes)

                    for node in connected_nodes:
                        visited[node[0]][node[1]] = True

    # print("max_groups:", max_groups)

    if not max_groups:  # 블록 그룹 없으면 False 리턴
        return False

    if len(max_groups) == 1:  # 크기가 최다인 그룹 하나뿐이면
        return max_groups[0]

    # 무지개 블록 개수 기준
    max_rainbows = []
    mx_cnt = 0
    for i in range(len(max_groups)):
        cnt = get_rainbow_cnt(max_groups[i])
        if cnt > mx_cnt:
            max_rainbows = [max_groups[i]]
            mx_cnt = cnt
        elif cnt == mx_cnt:
            max_rainbows.append(max_groups[i])

    # print("max_rainbows:", max_rainbows)

    if len(max_rainbows) == 1:
        return max_rainbows[0]

    # 기준 블록 기준
    one_block = []  # ((y,x),i) : (기준불록 좌표, 인덱스)로 구성
    for i in range(len(max_rainbows)):
        one_block.append((get_one_node(max_rainbows[i]), i))

    one_block.sort(key=lambda x: [-x[0][0], -x[0][1]])
    # print("sorted one_block:", one_block)

    return max_rainbows[one_block[0][1]]  # 기준블록 가장 우위인 연결요소 인덱스


# 해당 블록 그룹 제거, 빈칸은 -2로 나타냄
def delete_block_group(target_group):
    global score
    for (y, x) in target_group:
        matrix[y][x] = -2
    score += len(target_group)**2

# (y,x) 좌표에 있는 블록을 가능한만큼 아래로 이동
def move_down(y, x):
    sy = y
    while sy < N - 1:
        sy += 1
        if matrix[sy][x] >= -1:  # 다른 블록을 만나면
            if sy - 1 != y:
                matrix[sy - 1][x] = matrix[y][x]
                matrix[y][x] = -2
            # print_matrix(matrix)
            return

    matrix[sy][x] = matrix[y][x]
    matrix[y][x] = -2
    # print_matrix(matrix)
    return

# 중력 작용
# 검은색을 제외한 모든 블록을 아래 칸으로 계속 이동(다른 블록을 만날때까지)
def matrix_down():
    # 아래 좌표에서부터 시작해서 내리면서 올라와야 함
    for x in range(N):  # 특정 열 기준으로 한줄 쭉 내리기
        for y in range(N - 2, -1, -1):
            if matrix[y][x] >= 0:
                move_down(y, x)


def rotate():
    global matrix
    temp_matrix = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            temp_matrix[y][x] = matrix[x][N - y - 1]

    matrix = temp_matrix

score = 0

while True:
    target_group = find_block_group()
    if not target_group:
        break

    delete_block_group(target_group)
    matrix_down()
    rotate()
    matrix_down()

print(score)
