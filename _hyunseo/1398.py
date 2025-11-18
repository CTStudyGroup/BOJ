# 251112 : [BOJ 1398] 동전 문제

import sys

input = sys.stdin.readline


dp = [sys.maxsize]*(101)
dp[0] = 0
dp[1] = 1
for num in range(101) :
    for i in range(2) :
        if num - 10 ** i < 0 : break
        dp[num] = min(dp[num], dp[num-10**i] + 1)
    for i in range(2) :
        if num - (10**i)*25 < 0 : break
        dp[num] = min(dp[num], dp[num - (10**i)*25] + 1)

print(dp)
T = int(input())

for _ in range(T) :
    N = int(input())
    answer = 0
    while N > 0 :
        tmp = N % 100
        answer += dp[tmp]
        N //= 100
    print(answer)
