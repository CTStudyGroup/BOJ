T = int(input())

# dp
# dp[x]: x를 1,2,3의 합으로 나타내는 방법의 수
dp = [1] * 10001
for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(T):
    N = int(input())

    print(dp[N])
