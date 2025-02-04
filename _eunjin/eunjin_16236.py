from collections import deque
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

shark = ()  # 상어의 좌표
shark_size = 2  # 상어의 크기

for r in range(N):
    for c in range(N):
        if matrix[r][c] == 9:
            shark = (r, c)


def get_nearest(shark_pos):  # 가장 가까운 먹을 수 있는 물고기 좌표 리스트, 최단 거리 구하기
    s_y, s_x = shark_pos  # 상어의 좌표
    fish_list = []
    visited = [[False]*N for _ in range(N)]

    q = deque()
    q.append((s_y, s_x, 0))  # y,x,dist
    visited[s_y][s_x] = True

    min_d = N**2

    while(q):
        curr_y, curr_x, curr_d = q.popleft()

        if fish_list and curr_d > min_d:  # 먹을 수 있는 물고기 좌표의 최소 거리보다 멀어진 경우
            break

        if matrix[curr_y][curr_x] in [1, 2, 3, 4, 5, 6] and matrix[curr_y][curr_x] < shark_size:  # 먹을 수 있는 물고기인 경우
            if curr_d <= min_d:
                min_d = curr_d
                fish_list.append((curr_y, curr_x))  # 물고기 좌표 리스트에 추가
                continue

        # 다음 칸 탐색
        for i in range(4):
            ny = curr_y+dy[i]
            nx = curr_x+dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:  # matrix 범위를 벗어난 경우
                continue
            if matrix[ny][nx] > shark_size:  # 상어 크기보다 큰 물고기가 있는 경우
                continue
            if visited[ny][nx]:  # 이미 방문한 칸인 경우
                continue

            q.append((ny, nx, curr_d+1))
            visited[ny][nx] = True
    # print("min_d:", min_d)
    return fish_list, min_d


def get_fin_fish(fish_list):  # 거리가 같은 물고기 여러 마리 중 최종적으로 먹을 물고기 1마리 좌표 구하기
    ret = sorted(fish_list, key=lambda x: (x[0], x[1]))
    return ret[0]


def eat_fish(fish_pos):  # 해당 좌표의 물고기 먹기
    global eat_cnt, shark_size, matrix
    y, x = fish_pos
    if eat_cnt+1 == shark_size:  # 상어 크기 키우기
        shark_size += 1
        eat_cnt = 0
    else:
        eat_cnt += 1


T = 0
eat_cnt = 0
while(True):
    near_fishes, dist = get_nearest(shark)
    # print("near_fishes:", near_fishes, ", dist:", dist)
    if(len(near_fishes)) == 0:
        print(T)
        break

    fish_pos = get_fin_fish(near_fishes)  # 먹을 물고기 결정
    eat_fish(fish_pos)  # 물고기 먹기
    matrix[shark[0]][shark[1]] = 0
    shark = fish_pos  # 상어 좌표 업데이트
    matrix[shark[0]][shark[1]] = 9
    # print("eat fish:", fish_pos, ", now shark pos:", shark, ", shark_size:", shark_size)
    T += dist
