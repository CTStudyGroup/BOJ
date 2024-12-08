import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())


matrix = [[0 for _ in range(N+1)]]
for _ in range(N):
    row = [0]
    arr = list(map(int, input().split()))
    matrix.append(row + arr)

# print(matrix)

# dp[y][x]: (1,1)부터 (y,x)까지의 합
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for y in range(1, N+1):
    for x in range(1, N+1):
        dp[y][x] = dp[y][x-1] + dp[y-1][x] - dp[y-1][x-1] + matrix[y][x]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2]-(dp[x2][y1-1]+dp[x1-1][y2]-dp[x1-1][y1-1]))

# print("=== matrix ===")
# for row in matrix:
#     for col in row:
#         print(col, end=" ")
#     print()


# print("=== dp ===")
# for row in dp:
#     for col in row:
#         print(col, end=" ")
#     print()
