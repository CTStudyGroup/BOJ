R, C, W = map(int, input().strip().split())

dp = [[0] * 31 for _ in range(31)]
dp[0][0] = 1

for i in range(1, 31):
    dp[i][0] = 1
    dp[i][i] = 1

for i in range(2, 31):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

answer = 0
for w in range(W):
    for i in range(w + 1):
        answer += dp[w + R - 1][i + C - 1]
print(answer)
