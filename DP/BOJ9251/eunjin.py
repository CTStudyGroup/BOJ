# 입력 받기
S1 = input()
S2 = input()
S1 = "0"+S1
S2 = "0"+S2

# dp 테이블: dp[y][x]: S2의 y번째 인덱스와 S1의 x번째 인덱스까지의 최장 공통 부분 수열
dp = [[0]*len(S1) for _ in range(len(S2))]

# for y in range(1, len(S2)):
#     for x in range(1, len(S1)):
#         dp[y][x] = max(dp[y][x-1], dp[y-1][x], dp[y-1][x-1])
#         if(S2[y] == S1[x]):
#             if(dp[y][x] < y and dp[y][x] < x):
#                 dp[y][x] += 1

for y in range(1, len(S2)):
    for x in range(1, len(S1)):
        if S2[y] == S1[x]:
            dp[y][x] = dp[y-1][x-1] + 1
        else:
            dp[y][x] = max(dp[y-1][x], dp[y][x-1])

# print(dp)
print(dp[len(S2)-1][len(S1)-1])
