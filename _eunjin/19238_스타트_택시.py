from collections import deque
import sys

# . . # . . .
# . . # . . .
# . . 0 . . .
# . . . . . .
# . . 2 . # .
# . . . # 1 .

N, M, curr_fuel = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if matrix[y][x]:
            matrix[y][x] = "#"  # 벽
        else:
            matrix[y][x] = "."  # 빈칸

taxi_y, taxi_x = map(int, input().split())
taxi_y, taxi_x = taxi_y - 1, taxi_x - 1
matrix[taxi_y][taxi_x] = -1

dest = []  # 각 승객별 목적지

for m in range(M):
    y, x, dy, dx = map(int, input().split())
    matrix[y - 1][x - 1] = m
    dest.append((dy - 1, dx - 1))

def print_matrix(mat):
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()

# 현재 택시 위치에서 태울 승객 선택
# 승객 만날 때까지 bfs 탐색, 같은 depth에서 여러 승객 만나면 전부 임시 배열에 넣음
# 임시 배열에서 행 번호, 열 번호 가장 짧은 것 하나 추출
# 승객까지의 거리도 같이 리턴
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def find_rider(curr_y, curr_x):
    q = deque()
    visited = [[False] * N for _ in range(N)]
    q.append((curr_y, curr_x, 0))
    visited[curr_y][curr_x] = True

    temp = []  # 같은 depth의 승객 리스트
    min_d = sys.maxsize

    if matrix[curr_y][curr_x] not in ["#", "."] and matrix[curr_y][curr_x] >= 0:
        temp.append((curr_y, curr_x))
        return temp, 0


    while q:
        cy, cx, cd = q.popleft()

        if cd >= min_d:  # 최단 거리 갖는 승객을 찾았으면 이후 노드는 탐색 안함
            break

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if visited[ny][nx]:
                continue

            if matrix[ny][nx] == "#":  # 다음 노드가 벽이면
                continue

            if matrix[ny][nx] != "." and matrix[ny][nx] >= 0:  # 다음 노드에 승객이 있으면
                temp.append((ny, nx))
                visited[ny][nx] = True
                min_d = min(min_d, cd + 1)
                continue

            # 다음 노드가 일반 공간이면
            if matrix[ny][nx] == ".":
                q.append((ny, nx, cd + 1))
                visited[ny][nx] = True


    temp.sort(key=lambda x: [x[0], x[1]])  # 행번호, 열번호 순 정렬
    # print(temp, min_d)
    return(temp, min_d)

# (curr_y,curr_x) -> k번 승객의 목적지까지 이동
# 이동한 거리가 curr_fuel 이상인데도 아직 dest 못갔으면 종료
# dest 도착 시 (이동 거리)*2만큼 fuel에 추가
# 같은 depth에서 연료 소진 or 목적지 도착이 칸에 따라 결정 날 수 있다
def move_to_dest(curr_y, curr_x, k):
    global curr_fuel
    q = deque()
    visited = [[False] * N for _ in range(N)]

    q.append((curr_y, curr_x, 0))
    visited[curr_y][curr_x] = True

    # print(k, "번 승객의 목적지:", dest[k], " 현재 좌표:", curr_y, ",", curr_x)

    while q:
        cy, cx, cd = q.popleft()
        if cy == dest[k][0] and cx == dest[k][1]:
            # print(k, "번 승객의 목적지까지의 거리:", cd)
            curr_fuel += cd  # cd만큼 소모하고 cd*2만큼 충전되므로
            matrix[curr_y][curr_x] = "."  # 승객이 있던 칸 빈칸으로 바꾸기
            return True

        if cd >= curr_fuel:  # 연료 소진
            # print("연료 소진")
            if not q or q[-1][2] > cd:  # 같은 depth에서 탐색할 칸이 더 안남았으면
                return False

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if not visited[ny][nx] and matrix[ny][nx] != "#":
                q.append((ny, nx, cd + 1))
                visited[ny][nx] = True
    return False

def all_moved():
    for elem in moved:
        if not elem:
            return False
    return True


# print("시작 연료:", curr_fuel)
moved = [False] * M  # 각 승객 이동 여부
# print_matrix(matrix)

# 근데 승객 태워서 이동하는 도중에 연료 떨어지면 승객은 중간에 내리는건가??
# 그건 중요하지 않음이다
while True:
    next_cords, used = find_rider(taxi_y, taxi_x)

    if not next_cords:  # 다음 이동 불가하면
        print(-1)
        exit()

    if used >= curr_fuel:  # 승객까지 가는데에 연료 소진하면
        print(-1)
        exit()

    curr_fuel -= used  # 승객까지 이동하는 동안의 연료 차감
    cy, cx = next_cords[0][0], next_cords[0][1]
    # print(matrix[cy][cx], "번 승객 좌표까지 이동 후 남은 연료:", curr_fuel)

    # 이동시킬 승객
    k = matrix[cy][cx]

    # 택시 이동
    matrix[taxi_y][taxi_x] = "."
    taxi_y, taxi_x = cy, cx
    # matrix[taxi_y][taxi_x] = -1

    success = move_to_dest(cy, cx, k)

    if not success:
        print(-1)
        exit()

    # 택시 좌표 목적지로 이동
    taxi_y, taxi_x = dest[k][0], dest[k][1]
    # matrix[taxi_y][taxi_x] = -1

    # print(k, "번 승객 목적지까지 이동 후 남은 연료:", curr_fuel)
    moved[k] = True

    if all_moved():
        break


print(curr_fuel)


