# 입력 받기
N = int(input())

# dp[x]: x년 말에 존재하는 벌레의 수
dp = [0 for _ in range(21)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

# new_worms[x]: x년 초에 새로 생성된 벌레의 수
new_worms = [0 for _ in range(21)]
new_worms[1] = 1
new_worms[2] = 1
new_worms[3] = 2

for i in range(4, 21):
    dp[i] = dp[i-1]*2
    if (i-3) % 2 == 1:
        dp[i] -= new_worms[i-3]
        new_worms[i-3] = 0
    if (i-4) % 2 == 0:
        dp[i] -= new_worms[i-4]
        new_worms[i-4] = 0
    new_worms[i] = dp[i-1]


print(dp[N])

# print(dp)
