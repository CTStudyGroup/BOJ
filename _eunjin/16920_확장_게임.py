import sys
from collections import deque
input = sys.stdin.readline

N, M, P = map(int, input().split())
S = list(map(int, input().split()))

matrix = [list(input().strip()) for _ in range(N)]

def print_matrix(mat):
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            print(mat[y][x], end=" ")
        print()

# 1번 유저 -> 9번 유저 순으로 확장 진행
# S[i]칸 만큼 상하좌우 인접 칸으로 확장 (모든 칸에 동시에 확장)
# 다음 유저로 순서 넘어감

# S[i]칸 점프해서 그 칸 하나에다가만 확장하는게 아니라, 그 칸까지 쭉 확장하는거다
# 상하좌우 한 방향으로만 쭉 가는게 아니라, 가다가 꺾을 수도 있다.. 이동 거리가 S[i]칸 이내라면
# => bfs로 거리가 S[i]칸 이내인 좌표 모두 구하기

# 각 유저마다 자신의 visited을 두고 그걸 expand, bfs 전부에서 공유하도록 했더니
# 이전 다른 시작 칸 탐색에서 이미 방문해버려서 다음 시작점에서 탐색할 때 길이 막혀버린다, 12% 시간 초과
# 근데 visited를 bfs 안에서 선언하고 돌리면 1% 시간 초과

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, k):  # (y,x) 좌표 기준 이동 거리가 S[k]이내인 확장 가능한 모든 좌표 리턴
    # global visited
    ret = []
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True

    q = deque()
    q.append((y, x, 0))

    while q:
        cy, cx, cd = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if matrix[ny][nx] == "." and not visited[ny][nx]:
                if cd + 1 <= S[k]:  # 거리가 S[k]이내로만 확장 가능
                    visited[ny][nx] = True
                    q.append((ny, nx, cd + 1))
                    ret.append((ny, nx))
    return ret


def expand(n):  # n번 유저 확장
    cords = []

    for y in range(N):
        for x in range(M):
            if matrix[y][x] != str(n):
                continue  # 본인 성이 없으면 pass
            curr_cord = bfs(y, x, n - 1)

            cords.extend(curr_cord)
    for y, x in cords:
        matrix[y][x] = str(n)

    return True if cords else False  # n번 유저가 확장 가능한 좌표가 있으면 True, 없으면 False 리턴


while True:
    valid_cnt = 0
    for n in range(P):

        valid = expand(n + 1)
        if valid:
            valid_cnt += 1
    # print_matrix(matrix)
    # print("---------------------")

    if valid_cnt == 0:
        break

cnt = [0] * P
for y in range(N):
    for x in range(M):
        if matrix[y][x] != "." and matrix[y][x] != "#":
            cnt[int(matrix[y][x]) - 1] += 1

print(*cnt)
