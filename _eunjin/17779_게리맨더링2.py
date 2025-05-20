import copy
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def print_matrix(matrix):
    print("---")
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()

def get_value(x, y, d1, d2, matrix):
    n1, n2, n3, n4, n5 = 0, 0, 0, 0, 0

    # 1번 구역
    tx = x
    ty = y - 1
    while ty >= 0:
        for c in range(tx + 1):
            n1 += matrix[ty][c]
            matrix[ty][c] = 0
        if tx < x + d1:
            tx += 1
        ty -= 1

    # 2번 구역
    tx = x + d1 + d2 + 1
    ty = y - d1 + d2
    while ty >= 0:
        for c in range(tx, N):
            n2 += matrix[ty][c]
            matrix[ty][c] = 0
        if tx > x + d1 + 1:
            tx -= 1
        ty -= 1

    # 3번 구역
    tx = x - 1
    ty = y
    while ty < N:
        for c in range(tx + 1):
            n3 += matrix[ty][c]
            matrix[ty][c] = 0
        if tx < x + d2 - 1:
            tx += 1
        ty += 1

    # 4번 구역
    tx = x + d1 + d2
    ty = y - d1 + d2 + 1
    while ty < N:
        for c in range(tx, N):
            n4 += matrix[ty][c]
            matrix[ty][c] = 0
        if tx > x + d2:
            tx -= 1
        ty += 1

    for r in range(N):
        for c in range(N):
            n5 += matrix[r][c]

    cnt = [n1, n2, n3, n4, n5]

    return max(cnt) - min(cnt)

# 가능한 y,x,d1,d2 조합 생성
comb = []
for x in range(1, N + 1):
    for y in range(1, N + 1):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):
                if x + d1 + d2 <= N and y - d1 >= 1 and y + d2 <= N:
                    comb.append((x - 1, y - 1, d1, d2))

# 각 조합에 대해 인구 값 구하기
answer = 1e12
for x, y, d1, d2 in comb:
    mat = copy.deepcopy(matrix)
    val = get_value(x, y, d1, d2, mat)
    answer = min(answer, val)

print(answer)
