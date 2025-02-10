r1, c1, r2, c2 = map(int, input().split())

N = max(abs(r1), abs(r2), abs(c1), abs(c2)) * 2 + 1

rows = r2 - r1 + 1
cols = c2 - c1 + 1
matrix = [[0] * cols for _ in range(rows)]

# d 0:상, 1:좌, 2:하, 3:우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

r, c = N // 2, N // 2
d = 3
num = 1
cnt = 1
curr_cnt = 0

while num <= (N * N):
    # 좌표가 범위 내에 있을 경우에만 저장
    if r1 <= r - (N // 2) <= r2 and c1 <= c - (N // 2) <= c2:
        matrix[r - (N // 2) - r1][c - (N // 2) - c1] = num

    num += 1
    curr_cnt += 1
    r, c = r + dr[d], c + dc[d]
    # print("r:", r, ",c:", c, ",curr_cnt:", curr_cnt, ", cnt:", cnt, ",d:", d)

    # 방향 전환
    if curr_cnt == cnt:
        d = (d + 1) % 4
        curr_cnt = 0
        if d == 1 or d == 3:
            cnt += 1

    if r < 0 or r >= N or c < 0 or c >= N:
        break


max_len = max(len(str(matrix[i][j])) for i in range(rows) for j in range(cols))

# 결과 출력
for row in matrix:
    print(" ".join(str(x).rjust(max_len) for x in row))
