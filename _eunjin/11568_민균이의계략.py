# 가장 긴 증가하는 부분 수열 문제 = dp LIS
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# dp[x]: arr[x]를 마지막 원소로 하는 LIS 길이
dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
