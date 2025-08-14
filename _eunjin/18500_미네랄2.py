from collections import deque
import sys
input = sys.stdin.readline
R, C = map(int, input().split())

matrix = [list(input().strip()) for _ in range(R)]

N = int(input())
height = list(map(int, input().split()))
for i in range(N):
    height[i] = R - height[i]  # y좌표 기준으로 변환

def print_matrix(mat):
    print('\n'.join(''.join(map(str, row)) for row in mat))

# 막대가 날아가다 미네랄 만나면 해당 칸 미네랄 파괴, 막대 이동 종료
# 미네랄 파괴 후 남은 클러스터가 분리되는 경우 가능함
# 클러스터 분리된 경우: 중력 작용, 다른 클러스터나 땅을 만날때까지 떨어짐

# 막대기 날리기, 행 h에서 방향 d로. 미네랄 만난 경우 해당 좌표 반환
dd = [1, -1]  # 왼쪽, 오른쪽
def throw(h, d):
    y = h
    if d == 0:  # 왼쪽 -> 오른쪽
        x = 0
        while x < C:
            if matrix[y][x] == '.':
                x += 1
            else:
                return y, x
    else:  # 오른쪽 -> 왼쪽
        x = C - 1
        while x >= 0:
            if matrix[y][x] == '.':
                x -= 1
            else:
                return y, x

    return -1, -1  # 미네랄 만나지 않은 경우


# 해당 좌표부터 bfs탐색하며 떠있는 클러스터인지 판단하고 노드 좌표 리스트 반환
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
def bfs(y, x):
    q = deque()
    valid = True
    ret = []

    q.append((y, x))
    visited[y][x] = 1

    while q:
        y, x = q.popleft()
        if y == R - 1:  # 바닥에 닿아있는 클러스터로, 분리 대상 아님
            valid = False

        ret.append([y, x])

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue

            if not visited[ny][nx] and matrix[ny][nx] == "x":
                visited[ny][nx] = 1
                q.append((ny, nx))

    return valid, ret


# 해당 클러스터를 몇칸까지 아래 이동 가능한지 반환
def down_cnt(cluster):
    cnt = 0
    flag = True
    while flag:
        for y, x in cluster:
            ny = y + cnt + 1
            if ny >= R or (ny < R and matrix[ny][x] == "x"):
                flag = False
                break
        if flag:
            cnt += 1

    return cnt


# 해당 클러스터 중력 작용
def drop(cluster):
    cnt = down_cnt(cluster)  # 아래로 내릴 칸 수
    for y, x in cluster:
        matrix[y + cnt][x] = "x"


for i in range(N):
    my, mx = throw(height[i], i % 2)
    if my == mx == -1:  # 미네랄 만나지 않음
        continue

    matrix[my][mx] = '.'  # 미네랄 파괴

    cluster_cnt = 0
    cluster = []
    visited = [[0] * C for _ in range(R)]

    # 행 방향 클러스터 탐색
    if i % 2 == 0:  # 왼쪽 -> 오른쪽
        if mx + 1 < C and matrix[my][mx + 1] == "x":
            valid, cluster_row = bfs(my, mx + 1)  # 한 칸 오른쪽에서 bfs 시작
            if valid:
                cluster_cnt += 1
                cluster = cluster_row
    else:  # 오른쪽 -> 왼쪽
        if mx - 1 >= 0 and matrix[my][mx - 1] == "x":
            valid, cluster_row = bfs(my, mx - 1)  # 한 칸 왼쪽에서 bfs 시작
            if valid:
                cluster_cnt += 1
                cluster = cluster_row

    # 위 방향 클러스터 탐색
    if my - 1 >= 0 and matrix[my - 1][mx] == "x" and not visited[my - 1][mx]:
        valid, cluster_up = bfs(my - 1, mx)  # 바로 윗칸 시작
        if valid:
            cluster_cnt += 1
            cluster = cluster_up

    # 아래 방향 클러스터 탐색
    if my + 1 < R and matrix[my + 1][mx] == "x" and not visited[my + 1][mx]:
        valid, cluster_down = bfs(my + 1, mx)  # 바로 아래칸 시작
        if valid:
            cluster_cnt += 1
            cluster = cluster_down

    if cluster_cnt >= 2:
        matrix[my][mx] = 'x'  # 미네랄 파괴 취소
        continue

    # 모든 방향 탐색했는데도 분리 대상 클러스터 없는 경우
    if not cluster:
        continue

    # 클러스터 중력 작용을 위해 현재 클러스터 임시 삭제
    for cy, cx in cluster:
        matrix[cy][cx] = "."

    # 클러스터 중력 작용
    drop(cluster)

print_matrix(matrix)
