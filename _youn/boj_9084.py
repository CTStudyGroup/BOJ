from collections import defaultdict

def solve(coins, M):
    dp = defaultdict(int)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i-coin]
    return dp[M]

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    print(solve(coins, M))