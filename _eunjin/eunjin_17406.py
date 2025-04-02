from itertools import permutations
import copy

N, M, K = map(int, input().split())
origin_matrix = [list(map(int, input().split())) for _ in range(N)]
rotations = [list(map(int, input().split())) for _ in range(K)]

# 회전 연산
def rotate_total(matrix, r, c, s):
    y, x = r, c
    for l in range(2 * s + 1, 1, -2):
        rotate(matrix, y - s - 1, x - s - 1, l)
        y += 1
        x += 1

# (y,x)에서 시작하는 l*l 테두리의 행과 열 회전
# 위, 왼쪽, 아래, 오른쪽 방향으로 업데이트
def rotate(matrix, y, x, l):
    # 시작점을 temp에 저장하고 마지막에 시작점 다음 노드에 덮어써주기
    temp = matrix[y][x]

    # 위쪽 방향 업데이트
    for r in range(y, y + l - 1):
        matrix[r][x] = matrix[r + 1][x]

    # 왼쪽 방향 업데이트
    for c in range(x, x + l - 1):
        matrix[y + l - 1][c] = matrix[y + l - 1][c + 1]

    for r in range(y + l - 1, y - 1, -1):
        matrix[r][x + l - 1] = matrix[r - 1][x + l - 1]

    for c in range(x + l - 1, x, -1):
        matrix[y][c] = matrix[y][c - 1]

    matrix[y][x + 1] = temp


# 각 회전 연산 사용 순열 구하기
# orders에 주어진 순서대로 직접 배열 회전 후 배열의 행 회소 합 구하기
answer = 5000
for order in permutations(range(0, K), K):
    matrix = copy.deepcopy(origin_matrix)
    for i in order:
        cmd = rotations[i]
        rotate_total(matrix, cmd[0], cmd[1], cmd[2])

    for row in matrix:
        answer = min(answer, sum(row))

print(answer)
