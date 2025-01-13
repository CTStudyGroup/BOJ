import sys
input = sys.stdin.readline

M, N = map(int, input().split())

matrix = [[1 for _ in range(M)] for _ in range(M)]

# 제일 왼쪽 열과 위쪽 행의 최종 크기를 먼저 계산하고
# 나머지는 각 행마다 왼쪽->오른쪽으로 가면서 dp 처럼 계산

# 제일 왼쪽 열과 위쪽 행의 숫자 list
# Python3, PyPy3 시간 초과 풀이
# arr = [1 for _ in range(2*M-1)]

# for _ in range(N):
#     input_arr = list(map(int, input().split()))

#     n = 0
#     idx = 0
#     for num in input_arr:
#         if num:
#             for i in range(idx, idx+num):
#                 arr[i] += n
#             idx += num
#         n += 1

# PyPy3 성공 풀이
arr = [1 for _ in range(2*M-1)]

for _ in range(N):
    zero, one, two = list(map(int, input().split()))

    for i in range(zero, zero+one):
        arr[i] += 1

    for i in range(zero+one, zero+one+two):
        arr[i] += 2

# matrix 채우기
# 왼쪽 열부터 채우기
x = 0
y = M-1
for i in range(M-1):
    matrix[y][x] = arr[i]
    y -= 1

# 위쪽 행 채우기
x = 0
y = 0
for i in range(M-1, 2*M-1):
    matrix[y][x] = arr[i]
    x += 1

# 나머지 matrix dp 채우기
for y in range(1, M):
    for x in range(1, M):
        matrix[y][x] = max(matrix[y-1][x-1], matrix[y-1][x])

for row in matrix:
    for elem in row:
        print(elem, end=" ")
    print()
