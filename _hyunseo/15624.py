import sys

n = int(input())

dp=[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610, 987,1597]

while len(dp) <= n + 1 :
  dp.append((dp[-1] + dp[-2])%1000000007)
print(dp[n])
