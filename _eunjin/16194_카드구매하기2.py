import sys
input = sys.stdin.readline

N = int(input())
costs = [0] + list(map(int, input().split()))
INF = sys.maxsize

# dp 배낭 문제
# dp[x]: 카드를 x개 사기위한 최소 금액
dp = [INF] * (N + 1)
dp[1] = costs[1]

# dp[x] = min(costs[x],dp[x-j]+dp[j])
for x in range(2, N + 1):
    dp[x] = costs[x]
    for j in range(1, x):
        dp[x] = min(dp[x], dp[x - j] + dp[j])

print(dp[N])
