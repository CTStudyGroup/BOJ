# 250728 : [BOJ 10422] 괄호

T = int(input())
num =[int(input()) for _ in range(T)]
max_num = max(num)//2
dp=[1]

for number in range(1, max_num + 1) :
  tmp = 0
  for i in range(number ) :
    tmp += dp[i]*dp[number - i - 1]
    tmp %= 1000000007
  dp.append(tmp)
for n in num:
    if n % 2 == 1:
        print(0)
    else:
        print(dp[n//2] % 1000000007)
