string1 = input()
string2 = input()

# DP LCS 문제
# dp[i][j]: i번째, j번째 문자까지 봤을 때 가장 긴 부분 문자열의 길이
dp = [[0] * len(string2) for _ in range(len(string1))]

# 행 초기화
for i in range(len(string2)):
    if string2[i] == string1[0]:
        dp[0][i] = 1

# 열 초기화
for i in range(len(string1)):
    if string1[i] == string2[0]:
        dp[i][0] = 1

answer = 0

for i in range(1, len(string1)):
    for j in range(1, len(string2)):
        if string1[i] == string2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(answer, dp[i][j])


print(answer)
