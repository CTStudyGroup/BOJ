# R, C, Q = map(int, input().split())

# matrix = [list(map(int, input().split())) for _ in range(R)]

# for _ in range(Q):
#     r1, c1, r2, c2 = map(int, input().split())

#     sm = 0

#     for r in range(r1 - 1, r2):
#         for c in range(c1 - 1, c2):
#             sm += matrix[r][c]

#     answer = sm // ((r2 - r1 + 1) * (c2 - c1 + 1))
#     print(answer)

# 위 풀이는 시간 초과
# 누적합으로 풀어야 한다

R, C, Q = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(R)]

# dp[r2][c2]-dp[r2][c1-1]-dp[r1-1][c2]+dp[r1-1][c1-1]
# dp[r][c]: (0,0)부터 (r,c)까지의 누적합
dp = [[0] * (C + 1) for _ in range(R + 1)]
# 1열 초기화
for c in range(1, C + 1):
    dp[1][c] = dp[1][c - 1] + matrix[0][c - 1]

# 1행 초기화
for r in range(1, R + 1):
    dp[r][1] = dp[r - 1][1] + matrix[r - 1][0]

for r in range(2, R + 1):
    for c in range(2, C + 1):
        dp[r][c] = matrix[r - 1][c - 1] + dp[r][c - 1] + dp[r - 1][c] - dp[r - 1][c - 1]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())

    sm = dp[r2][c2] - dp[r2][c1 - 1] - dp[r1 - 1][c2] + dp[r1 - 1][c1 - 1]

    answer = sm // ((r2 - r1 + 1) * (c2 - c1 + 1))
    print(answer)
