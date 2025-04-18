import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
MIN = -1e12
# dp[x]: x번째까지 고려했을 때 최대 연속합
dp = [MIN] * N
dp[0] = max(dp[0], arr[0])
for i in range(1, N):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])
print(max(dp))
