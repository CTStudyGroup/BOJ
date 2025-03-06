# import sys
# input = sys.stdin.readline

# string = input().strip()
# Q = int(input())

# 문자열의 0 ~ x번째 인덱스 까지에서 각 알파벳의 등장 개수 세기
# l, r 입력에 대해 r까지의 개수 - l-1까지의 개수

# alphabet = [[0] * len(string) for _ in range(26)]

# for i in range(len(string)):
#     alphabet[ord(string[i]) - 97][i] += 1

# for _ in range(Q):
#     char, l, r = input().split()
#     l, r = int(l), int(r)
#     n = ord(char) - 97
#     if l == 0:
#         print(sum(alphabet[n][:r + 1]))
#     else:
#         print(sum(alphabet[n][:r + 1]) - sum(alphabet[n][:l]))

# 위 풀이로는 시간 초과
# sum을 dp로 풀어야 한다

import sys
input = sys.stdin.readline

string = input().strip()
Q = int(input())

# dp[x][y]: x번째 인덱스까지 y알파벳의 등장 횟수
dp = [[0] * 26 for _ in range(len(string))]
n = ord(string[0]) - 97
dp[0][n] += 1

# dp[x] = dp[x-1] 복사하고 x번째 문자의 개수만 +1
for i in range(1, len(string)):
    dp[i] = dp[i - 1][:]

    n = ord(string[i]) - 97
    dp[i][n] += 1

for _ in range(Q):
    char, l, r = input().split()
    l, r = int(l), int(r)
    n = ord(char) - 97
    if l == 0:
        print(dp[r][n])
    else:
        print(dp[r][n] - dp[l - 1][n])
