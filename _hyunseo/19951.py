import sys

input = sys.stdin.readline
N, M = map(int, input().split())

height = list(map(int, input().split()))

dp = [0] * N
for _ in range(M) :
    a, b, k = map(int, input().split())
    dp[a-1] += k
    if b == N : continue
    dp[b] -=k
sum = 0
for idx, val in enumerate(dp) :
    sum  += val
    height[idx] += sum
print(*height)
