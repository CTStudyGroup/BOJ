import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# dp다
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = matrix[0][0]

for i in range(1, M):
    dp[0][i] = dp[0][i - 1] + matrix[0][i]

for j in range(1, N):
    dp[j][0] = dp[j - 1][0] + matrix[j][0]

for r in range(1, N):
    for c in range(1, M):
        dp[r][c] = max(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + matrix[r][c]

print(dp[N - 1][M - 1])
