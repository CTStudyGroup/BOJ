import sys
input = sys.stdin.readline

def valid(x, y):
    while y > 0:
        x, y = y, x % y
    return x

dp = [0] * 1001
dp[1] = 3

for x in range(2, 1001):
    n = 0
    for y in range(1, x + 1):  # 아래 절반만 확인, 0은 확인할 필요 없음
        if valid(x, y) == 1:
            n += 2  # 절반 *2해서 위쪽 절반에서 나올 수 있는 것도 반영
    dp[x] = dp[x - 1] + n

C = int(input())

for _ in range(C):
    N = int(input())
    print(dp[N])
