T, W = map(int, input().split())

# dp[y][x][z]: y초 시점에서 x번 나무 아래에 있고 그 시점까지 z번 이동했을 때 받은 최대 자두 개수
dp = [[[0]*(W+1) for _ in range(2)]for _ in range(T+1)]


drop = [[0, 0]]
for _ in range(T):
    n = int(input())
    if n == 1:
        drop.append([1, 0])
    else:
        drop.append([0, 1])

dp[1][0][0] = drop[1][0]
# 틀린 초기화 부분
# dp[1][1][0] = drop[1][1]
dp[1][1][1] = drop[1][1]

# x가 0인 경우
# dp[y][x][z] = max(dp[y-1][0][z], dp[y-1][1][z-1]) + drop[y][0]
# dp[2][0][0] = dp[1][0][0] + drop[2][0] = 1
# dp[2][0][1] = max(dp[1][0][1],dp[1][1][0]) + drop[2][0] = 2
# dp[2][0][2] = max(dp[1][0][2],dp[1][1][1]) + drop[2][0] = 0

# x가 1인 경우
# dp[y][x][z] = max(dp[y-1][1][z], dp[y-1][0][z-1]) + drop[y][1]
# dp[2][1][0] = dp[1][1][0] + drop[y][1] = 1
# dp[2][1][1] = max(dp[1][1][1],dp[1][0][0]) + drop[y][1] = 0
# dp[2][1][2] = max(dp[1][1][2],dp[1][0][1]) + drop[y][1] = 0

for y in range(2, T+1):
    for x in range(2):
        for z in range(W+1):
            if x == 0:
                if z == 0:
                    dp[y][x][z] = dp[y-1][0][0] + drop[y][0]
                else:
                    dp[y][x][z] = max(dp[y-1][0][z], dp[y-1][1][z-1]) + drop[y][0]

            if x == 1:
                if z == 0:
                    dp[y][x][z] = dp[y-1][1][0] + drop[y][1]
                else:
                    dp[y][x][z] = max(dp[y-1][1][z], dp[y-1][0][z-1]) + drop[y][1]


# for y in range(T+1):
#     print("---------T:", y, "-----------")
#     for x in range(2):
#         for z in range(W+1):
#             print(dp[y][x][z], end=" ")
#         print()

print(max(max(dp[T][0]), max(dp[T][1])))
