import sys

input = sys.stdin.readline

D, K = map(int, input().split())
dp=[1]
dp.append(1)
for i in range(2, D) :
    dp.append(dp[i-1] + dp[i-2])
for a in range(1, K//D) :
    for b in range(a, K + 1) :
        if K == a*dp[D-3] + b*dp[D-2] :
            
            print(a)
            print(b)
            
            sys.exit()
