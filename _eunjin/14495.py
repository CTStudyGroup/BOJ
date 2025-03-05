N = int(input())

if N in [1, 2, 3]:
    print(1)
    exit()

dp = [0] * (N + 1)

dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, N + 1):
    dp[i] = dp[i - 1] + dp[i - 3]

print(dp[N])
