N = int(input())
A = list(map(int, input().split()))

# dp[x]: x까지 고려했을 때 LIS 길이
dp = [1] * N

for i in range(1, N):
    for j in range(i, -1, -1):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

