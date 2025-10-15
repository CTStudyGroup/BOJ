N = int(input())
customers = list(map(int, input().split()))
M = int(input())

# 이게 뭔 문제지..
psum = [0] * N
psum[0] = customers[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + customers[i]


# 틀린 풀이
# dp[x]: x번째 객차까지 고려했을 때의 최대 운송 손님 수
# x번째 객차가 기관차 범위에 포함 되는 경우: x-M+1 ~ x번째 객차를 기관차로 끈다.
# x번째 객차가 기관차 범위에 포함 안되는 경우
# dp = [0] * N

# dp[M - 1] = psum[M - 1]

# for i in range(M, N):
#     dp[i] = max(dp[i], dp[i - M] + psum[i] - psum[i - M], dp[i - 1])

# print(dp[-1])


# 기관차 3번 이용이라는 조건도 고려해야함
# dp[x][y]: x번째 객차까지 고려했을 때의 최대 운송 손님 수, 지금까지 기관차 횟수는 y번
# x번째 객차가 기관차 범위에 포함 되는 경우: x-M+1 ~ x번째 객차를 기관차로 끈다.
# x번째 객차가 기관차 범위에 포함 안되는 경우
dp = [[0] * 4 for _ in range(N)]
dp[M - 1][1] = psum[M - 1]
# print(dp)

for i in range(M, N):
    for j in range(1, 4):
        dp[i][j] = max(dp[i - 1][j], dp[i - M][j - 1] + psum[i] - psum[i - M])


print(dp[-1][3])
