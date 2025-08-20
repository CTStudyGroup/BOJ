N = int(input())

dp = [[0] * (N+1) for _ in range(3)]

dp[2][1] = 1

for j in range(2, N+1):
    dp[0][j] = (dp[1][j-1] + dp[2][j-1]) % 1000000007
    dp[1][j] = (dp[0][j-1] + dp[2][j-1]) % 1000000007
    dp[2][j] = (dp[0][j-1] + dp[1][j-1]) % 1000000007

print(dp[0][N])