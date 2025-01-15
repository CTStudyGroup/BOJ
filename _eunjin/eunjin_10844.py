N = int(input())

# dp[y][x]: 길이가 y이고 마지막 자리 숫자가 x일 때 계단 수의 개수
dp = list([0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(N+1))


dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 0으로 시작하는 수는 계단수가 아님
# 중간에 0이 들어갈 수는 있음
# 01 불가, 10 가능

# dp[2][1] = dp[1][0]+dp[1][2]
# dp[2][2] = dp[1][1]+dp[1][3]
# dp[2][9] = dp[1][8]

for y in range(2, N+1):
    for x in range(0, 10):
        if x == 9:
            dp[y][x] = dp[y-1][x-1]
        elif x == 0:
            dp[y][x] = dp[y-1][x+1]
        else:
            dp[y][x] = dp[y-1][x-1]+dp[y-1][x+1]

# print(dp)

print(sum(dp[N]) % 1000000000)
