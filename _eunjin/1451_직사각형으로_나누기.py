N, M = map(int, input().split())
matrix = [[0 for _ in range(M + 1)]]

for _ in range(N):
    inp = [0] + list(map(int, list(input())))
    matrix.append(inp)

# 누적합 계산
psum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for r in range(1, N + 1):
    for c in range(1, M + 1):
        psum[r][c] = matrix[r][c] + psum[r - 1][c] + psum[r][c - 1] - psum[r - 1][c - 1]

def calc(x1, y1, x2, y2):
    return psum[x2][y2] - psum[x2][y1 - 1] - psum[x1 - 1][y2] + psum[x1 - 1][y1 - 1]

answer = 0

# 3개의 직사각형으로 나누는 방법 6가지
for i in range(1, M - 1):
    for j in range(i + 1, M):
        r1 = calc(1, 1, N, i)
        r2 = calc(1, i + 1, N, j)
        r3 = calc(1, j + 1, N, M)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

for i in range(1, N - 1):
    for j in range(i + 1, N):
        r1 = calc(1, 1, i, M)
        r2 = calc(i + 1, 1, j, M)
        r3 = calc(j + 1, 1, N, M)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

for i in range(1, M):
    for j in range(1, N):
        r1 = calc(1, 1, N, i)
        r2 = calc(1, i + 1, j, M)
        r3 = calc(j + 1, i + 1, N, M)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

for i in range(1, N):
    for j in range(1, M):
        r1 = calc(1, 1, i, j)
        r2 = calc(i + 1, 1, N, j)
        r3 = calc(1, j + 1, N, M)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

for i in range(1, N):
    for j in range(1, M):
        r1 = calc(1, 1, i, M)
        r2 = calc(i + 1, 1, N, j)
        r3 = calc(i + 1, j + 1, N, M)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

for i in range(1, N):
    for j in range(1, M):
        r1 = calc(1, 1, i, j)
        r2 = calc(i, j + 1, i, M)
        r3 = calc(i + 1, 1, N, M)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

print(answer)
