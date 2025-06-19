import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e6)

banned = [False] * (N + 1)
for _ in range(M):
    banned[int(input().strip())] = True

# dp
# 2차원 풀이
# X를 N으로 설정하니까 메모리 초과
# 어차피 한번에 갈 수 있는 최대 칸은 N보다 훨씬 작음
X = 150
dp = [[INF] * X for _ in range(N + 1)]
dp[2][1] = 1  # 제일 처음엔 한 칸 점프만 가능

for y in range(3, N + 1):
    if banned[y]:  # 금지된 돌
        continue
    for x in range(1, X):  # 1칸 이상 점프해야함함
        if y - x <= 0:  # 0 ~ 음수 칸에서 시작 불가
            continue
        if banned[y - x]:  # 이전 칸이 밴인 경우 불가
            continue

        val = INF

        if x - 1 > 0 and x - 1 < X:
            val = min(val, dp[y - x][x - 1])
        if x > 0:
            val = min(val, dp[y - x][x])
        if x + 1 > 0 and x + 1 < X:
            val = min(val, dp[y - x][x + 1])

        if val < INF:
            dp[y][x] = val + 1

answer = -1
if min(dp[N]) < INF:
    answer = min(dp[N])

print(answer)
