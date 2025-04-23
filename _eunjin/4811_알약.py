import sys
input = sys.stdin.readline


# W N개, H N개
# 2~60일 중, 1~30일의 W를 고르기
# 완탐으로 하나하나 다 보기
# 이거 못한다 시간초과

# dp??
# dp[i][j]: W i개와 H j개로 만들 수 있는 문자열의 개수
# dp[i][j] = dp[i-1][j] + dp[i][j-1] (뒤에 W를 붙이는 경우, 뒤에 H를 붙이는 경우)

dp = [[0] * 31 for _ in range(31)]
for i in range(1, 31):
    dp[i][0] = 1


for i in range(1, 31):
    for j in range(1, i + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

while True:
    N = int(input())
    if N == 0:
        break
    print(dp[N][N])
