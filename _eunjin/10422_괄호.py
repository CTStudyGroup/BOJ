T = int(input())
MOD = 1000000007

# dp로 1~5000까지 답 다 구해놓고 출력하기
# 각 숫자를 2의 배수들의 합으로 나타낼 수 있는 경우의 수
dp = [0] * 5001
dp[0] = 1

for i in range(2, 5001, 2):
    for j in range(0, i, 2):
        dp[i] = (dp[i] + dp[j] * dp[i - j - 2]) % MOD

for _ in range(T):
    L = int(input())
    print(dp[L])
