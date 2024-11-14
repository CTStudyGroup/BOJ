# 입력 받기
N = int(input())

dp = [0] * 31
dp[0] = 1

for n in range(2, 31, 2):
    dp[n] = dp[n - 2] * 3
    for i in range(n - 4, -1, -2):
        dp[n] += dp[i] * 2

print(dp[N])
