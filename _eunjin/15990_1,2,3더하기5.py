import sys
input = sys.stdin.readline
T = int(input())
MOD = 1000000009

# dp
# 같은 수 두번 이상 연속 사용 불가
dp = [[0] * 3 for _ in range(100001)]  # 마지막 숫자가 1,2,3
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    dp[i][0] += (dp[i - 1][1] + dp[i - 1][2]) % MOD
    dp[i][1] += (dp[i - 2][0] + dp[i - 2][2]) % MOD
    dp[i][2] += (dp[i - 3][0] + dp[i - 3][1]) % MOD

for _ in range(T):
    n = int(input())
    print(sum(dp[n]) % MOD)

