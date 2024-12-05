# 입력 받기
N = int(input())

if N == 1:
    print(0)
    exit()
if N == 2:
    print(1)
    exit()
if N == 3:
    print(1)
    exit()

dp = [0 for _ in range(N+1)]

# dp[x]: x -> 1을 만들기 위한 연산 최소 횟수
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N+1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i//3], dp[i//2], dp[i-1])+1
    elif i % 3 == 0:
        dp[i] = min(dp[i//3], dp[i-1])+1
    elif i % 2 == 0:
        dp[i] = min(dp[i//2], dp[i-1])+1
    else:
        dp[i] = dp[i-1]+1


print(dp[N])
