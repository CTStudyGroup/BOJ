N, M = map(int, input().split())
MOD = 1000000007

if N < M:
    print(1)
    exit()

# dp
dp = [0] * (N + 1)

for i in range(1, M):  # A스킬만 쓰는 경우의 수 초기화
    dp[i] = 1

dp[M] = 2

for i in range(M + 1, N + 1):
    dp[i] = (dp[i - 1] + dp[i - M]) % MOD

print(dp[N])
