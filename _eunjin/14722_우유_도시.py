import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# dp
# 0으로 시작
# 0 -> 1 -> 2 -> 0
# 그전에 무슨 우유 마셨는지 정보 갖고있어야함 = 3차원 dp?

# dp[y][x][z]: (y,x) 까지 왔고 마지막으로 마신 우유가 z인 경우에 마실 수 있는 우유 최대 개수
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dy = [-1, 0]  # 위, 왼쪽
dx = [0, -1]

# 딸기우유 있는 칸은 최소 1
for y in range(N):
    for x in range(N):
        if matrix[y][x] == 0:
            dp[y][x][0] = 1


for y in range(N):
    for x in range(N):
        for d in range(2):
            ny, nx = y + dy[d], x + dx[d]

            if ny < 0 or nx < 0:
                continue

            for curr_milk in range(3):  # 우유 종류
                # 현재 칸의 우유 마시는 경우
                if matrix[y][x] == curr_milk:
                    prev_milk = (curr_milk + 2) % 3  # 이전에 마셔야할 우유
                    prev_val = dp[ny][nx][prev_milk]

                    # 이전에 우유를 최소 1번은 마섰어야 지금 우유도 마실 수 있음
                    dp[y][x][curr_milk] = max(dp[y][x][curr_milk], prev_val + (0 if prev_val == 0 else 1))

                # 현재 우유 안마시는 경우
                dp[y][x][curr_milk] = max(dp[y][x][curr_milk], dp[ny][nx][curr_milk])

print(max(dp[N - 1][N - 1]))
