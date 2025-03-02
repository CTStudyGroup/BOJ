C, N = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

# knapsack
# dp[x]: 비용이 x일 때 최대 고객수
MAX_COST = 100 * 1000
dp = [0] * (MAX_COST + 1)

for cost, customers in city:
    for j in range(cost, MAX_COST + 1):
        dp[j] = max(dp[j], dp[j - cost] + customers)

for i in range(MAX_COST + 1):
    if dp[i] >= C:
        print(i)
        break
