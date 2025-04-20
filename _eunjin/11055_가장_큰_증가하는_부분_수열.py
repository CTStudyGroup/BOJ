N = int(input())
A = list(map(int, input().split()))

# dp
# dp[x]: x를 포함하는 증가하는 부분 수열의 합
dp = [x for x in A]
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

# print(dp)
print(max(dp))
