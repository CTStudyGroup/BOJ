import sys
import copy
input = sys.stdin.readline

# 원판 T번 회전 후
# 원판에 있는 수 중 인접하면서 수가 같은 것 모두 찾아서 지우기
# 원판에 남아있는 수의 평균 구하기
# 원판에 남아있는 수들 마다 평균보다 크면 -1, 작으면 +1
# 원판에 남아있는 수의 합 구하기

N, M, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def print_matrix(mat):
    for row in mat:
        for elem in row:
            print(elem, end=" ")
        print()
    print("----------")

# (x의 배수)번 원판을 d방향으로 k칸 회전
def rotate(X, D, K):
    global matrix
    for x in range(X, N + 1, X):
        temp = [0] * M

        if d == 0:  # 시계 방향
            for i in range(M):
                temp[(i + K) % M] = matrix[x - 1][i]
        else:  # 반시계 방향
            for i in range(M):
                temp[(i - K) % M] = matrix[x - 1][i]

        matrix[x - 1] = temp

# 인접하면서 같은 수 모두 지우기
# 인접하면서 같은 수 있으면 True, 없으면 False 리턴
dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]
def remove():
    global matrix
    temp_matrix = copy.deepcopy(matrix)
    ret = False

    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 0:
                continue

            # 인접 수 중 자신과 같은 수 있으면 temp_matrix의 자신을 0으로 변경
            adj_nodes = []
            if y == 0:
                for i in range(3):
                    ny, nx = (y + dy[i]) % N, (x + dx[i]) % M
                    adj_nodes.append((ny, nx))
            elif y == N - 1:  # 인접 방향 3개
                for i in range(1, 4):
                    ny, nx = (y + dy[i]) % N, (x + dx[i]) % M
                    adj_nodes.append((ny, nx))
            else:  # 인접 방향 4개
                for i in range(4):
                    ny, nx = (y + dy[i]) % N, (x + dx[i]) % M
                    adj_nodes.append((ny, nx))

            for ny, nx in adj_nodes:
                if matrix[ny][nx] == matrix[y][x]:
                    temp_matrix[y][x] = 0
                    ret = True
                    break

    matrix = temp_matrix
    return ret

# 원판에 남아있는 수들 마다 평균보다 크면 -1, 작으면 +1
def update():
    cnt = 0
    total = 0
    for y in range(N):
        for x in range(M):
            if matrix[y][x] > 0:
                total += matrix[y][x]
                cnt += 1
    if cnt == 0:
        avg = 0
    else:
        avg = total / cnt

    for y in range(N):
        for x in range(M):
            if matrix[y][x] <= 0:
                continue

            if matrix[y][x] > avg:
                matrix[y][x] -= 1
            elif matrix[y][x] < avg:
                matrix[y][x] += 1

# 원판에 남아있는 수의 합 구하기
def get_sum():
    ret = 0
    for row in matrix:
        ret += sum(row)
    return ret

for _ in range(T):
    x, d, k = map(int, input().split())

    rotate(x, d, k)
    removed = remove()

    if not removed:
        update()

print(get_sum())
