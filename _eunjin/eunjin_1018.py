# 입력 받기
N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]

# m1, m2와 matrix를 비교해 최소 diff 값을 리턴


def count_min_diff(mat):
    global m1, m2

    diff_m1 = 0
    diff_m2 = 0
    for y in range(8):
        for x in range(8):
            if mat[y][x] != m1[y][x]:
                diff_m1 += 1
            if mat[y][x] != m2[y][x]:
                diff_m2 += 1

    return min(diff_m1, diff_m2)


# 체스판 matrix 2가지 생성
m1 = [[] for _ in range(8)]
m2 = [[] for _ in range(8)]

for i in range(8):
    if i % 2 == 0:
        m1[i] = list("WBWBWBWB")
        m2[i] = list("BWBWBWBW")
    else:
        m1[i] = list("BWBWBWBW")
        m2[i] = list("WBWBWBWB")

result = 1e12

for y in range(N-7):
    for x in range(M-7):

        curr_matrix = []
        for i in range(y, y+8):
            curr_matrix.append(matrix[i][x: x+8])

        result = min(result, count_min_diff(curr_matrix))

print(result)
