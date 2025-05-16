import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(int(input()) for _ in range(N))

# dp
dp = [100001 for _ in range(K + 1)]
dp[0] = 0

for coin in arr:
    for i in range(coin, K + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(-1) if dp[K] == 100001 else print(dp[K])
