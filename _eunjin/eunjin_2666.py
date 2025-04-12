N = int(input())
a, b = map(int, input().split())
M = int(input())
order = []
for _ in range(M):
    order.append(int(input()))

# # dp??
# # 빈 공간을 어디로 이동할거냐
# # 각 순서마다 어떤 빈 공간을 선택할거냐의 문제

dp = [[[0 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]


def go(x, door1, door2):
    if x == M:
        return 0

    val = order[x]
    dp[val][door1][door2] = min(abs(val - door1) + go(x + 1, val, door2), abs(val - door2) + go(x + 1, door1, val))

    return dp[val][door1][door2]

print(go(0, a, b))
