import sys

input = sys.stdin.readline

MOD = 1000000009

dp = [0] * 100_001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3
dp[6] = 6

for i in range(7, 100001):
    dp[i] = (dp[i-2] + dp[i-4] + dp[i-6]) % MOD

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])
