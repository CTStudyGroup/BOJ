N = int(input())
arr = list(float(input()) for _ in range(N))

# dp[x]: x까지의 곱
dp = [0]*N

dp[0] = arr[0]

# dp[x] = max(dp[x-1]*arr[x],arr[x])
for i in range(1, N):
    dp[i] = max(dp[i-1]*arr[i], arr[i])

# print(dp)
print('%0.3f' % max(dp))
