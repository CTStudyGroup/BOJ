dp = [[0 for _ in range(3)] for _ in range(1516)]
dp[1][1] = 1
for i in range(2, 1516):
    dp[i][0] = dp[i-1][1] + dp[i-1][2]
    dp[i][1] = dp[i-1][0] + dp[i-1][2]
    dp[i][2] = dp[i-1][0] + dp[i-1][1]
    for j in range(3):
        dp[i][j] %= 1000000007
print(dp[int(input())][0])
