# DP[i]: i원을 지불할 때, 최소 동전 개수
# DP[i] = min(DP[i-1] + 1, DP[i-2] + 1, DP[i-5] + 1, DP[i-7] + 1)

N = int(input())
DP = [10**6 for _ in range(N+1)]
DP[0] = 0
coins = [1,2,5,7]
for coin in coins:
    if(N >= coin):
        DP[coin] = 1

for i in range(N+1):
    minimum = DP[i]
    for coin in coins:
        if(i > coin):
            minimum = min(minimum, DP[i-coin] + 1)
    DP[i] = minimum

print(DP[N])

