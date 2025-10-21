N = int(input())
dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    val = 0
    for j in range(i):
        val += dp[j] * dp[i - 1 - j]
    dp[i] = val

print(dp[N])
