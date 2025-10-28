import sys
input = sys.stdin.readline

MAX_N = 32768
# 가능한 제곱수 리스트
squares = [i * i for i in range(1, 182)]  # 181^2 = 32761

# dp[k][n] = n을 정확히 k개의 제곱수로 표현하는 경우의 수
dp = [[0] * (MAX_N + 1) for _ in range(5)]
dp[0][0] = 1  # 0을 0개의 제곱수로 표현하는 방법 1가지

# 동전 조합 방식
for s in squares:
    for k in range(1, 5):
        for n in range(s, MAX_N + 1):
            dp[k][n] += dp[k - 1][n - s]

# 미리 1~4개를 합쳐서 답 저장
ans = [0] * (MAX_N + 1)
for n in range(MAX_N + 1):
    ans[n] = dp[1][n] + dp[2][n] + dp[3][n] + dp[4][n]

# 입력 처리
for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    print(ans[n])
