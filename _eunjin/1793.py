numbers = []

try:
    while True:
        n = input().strip()
        if n:  # 빈 줄이 아닐 경우
            numbers.append(int(n))
except EOFError:
    pass

# dp[x]: 2*x 타일 채우는 방법의 수
dp = [0] * 251
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, 251):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

for n in numbers:
    print(dp[n])
